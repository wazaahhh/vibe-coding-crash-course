#!/usr/bin/env bash
# Build slides.md for the FacMed Hack edition from its numbered module files.
# Edit the module files — NOT slides.md (it is generated).
#
# Usage: ./build.sh            -> slides.md
#        ./build.sh --html     -> + slides.html (Marp)
#        ./build.sh --pdf      -> + slides.html + slides.pdf (Chrome headless)
set -euo pipefail
cd "$(dirname "$0")"

out="slides.md"
cat _header.md > "$out"

first=1
for f in $(ls [0-9][0-9]-*.md | sort); do
  if [ "$first" = 1 ]; then
    cat "$f" >> "$out"
    first=0
  else
    printf '\n\n---\n\n' >> "$out"
    cat "$f" >> "$out"
  fi
done
echo "Built $out from $(ls [0-9][0-9]-*.md | wc -l | tr -d ' ') module files."

# Live quiz: the URL in quiz_url.txt goes into every {{QUIZ_URL}}, and its QR code into
# assets/quiz_qr.svg (needs the Python package segno). The PIN is set on the quiz's admin
# page and never committed: pass it at build time (QUIZ_PIN=1234 ./build.sh --pdf) and the
# slides show it and the QR code carries it; without it they say it is in the Zoom chat.
quiz_url="$(tr -d '[:space:]' < quiz_url.txt)"
quiz_qr="$quiz_url"
if [ -n "${QUIZ_PIN:-}" ]; then
  quiz_qr="${quiz_url%/}/?pin=${QUIZ_PIN}"
  pin_label="PIN ${QUIZ_PIN}"
else
  pin_label="PIN in the Zoom chat"
fi
python3 -c "import segno, sys; segno.make(sys.argv[1], error='m').save('assets/quiz_qr.svg', scale=8, border=2, dark='#11233F')" "$quiz_qr"
sed -i '' -e "s#{{QUIZ_URL}}#${quiz_url#https://}#g" -e "s#{{QUIZ_PIN_LABEL}}#${pin_label}#g" "$out"
# Live results panels on poll slides (HTML only): the quiz's /embed page for each question.
# The admin token is never written to tracked files: slides.md/slides.html carry a placeholder
# (read-only panels); QUIZ_ADMIN_KEY=… ./build.sh --html also writes slides-live.html (gitignored)
# with presenter controls (Open · timer · Show results · Close) in each panel.
sed -i '' -e "s#{{QUIZ_EMBED}}#${quiz_url%/}/embed?pin=${QUIZ_PIN:-}\&key=__QUIZ_KEY__\&q=#g" "$out"
echo "Quiz: $quiz_qr"

if [ "${1:-}" = "--html" ] || [ "${1:-}" = "--pdf" ]; then
  npx -y @marp-team/marp-cli@4.1.2 "$out" --html --allow-local-files -o slides.html
  if [ -n "${QUIZ_ADMIN_KEY:-}" ]; then
    sed "s#__QUIZ_KEY__#${QUIZ_ADMIN_KEY}#g" slides.html > slides-live.html
    echo "Wrote slides-live.html (live quiz controls; contains the admin token: do not share or commit)"
  fi
fi
if [ "${1:-}" = "--pdf" ]; then
  # Marp's own --pdf can hang on puppeteer; Chrome prints the HTML cleanly.
  chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  "$chrome" --headless=new --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PWD/slides.pdf" "file://$PWD/slides.html" 2>/dev/null
  echo "Wrote slides.pdf"
fi
