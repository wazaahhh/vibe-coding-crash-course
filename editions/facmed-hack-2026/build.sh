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
# assets/quiz_qr.svg (needs the Python package segno).
quiz_url="$(tr -d '[:space:]' < quiz_url.txt)"
python3 -c "import segno, sys; segno.make(sys.argv[1], error='m').save('assets/quiz_qr.svg', scale=8, border=2, dark='#11233F')" "$quiz_url"
sed -i '' "s#{{QUIZ_URL}}#${quiz_url#https://}#g" "$out"
echo "Quiz: $quiz_url"

if [ "${1:-}" = "--html" ] || [ "${1:-}" = "--pdf" ]; then
  npx -y @marp-team/marp-cli@4.1.2 "$out" --html --allow-local-files -o slides.html
fi
if [ "${1:-}" = "--pdf" ]; then
  # Marp's own --pdf can hang on puppeteer; Chrome prints the HTML cleanly.
  chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  "$chrome" --headless=new --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PWD/slides.pdf" "file://$PWD/slides.html" 2>/dev/null
  echo "Wrote slides.pdf"
fi
