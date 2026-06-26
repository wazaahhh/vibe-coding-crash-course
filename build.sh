#!/usr/bin/env bash
# Build slides.md from the per-module files in modules/.
# Edit the module files — NOT slides.md (it is generated).
#
# Usage: ./build.sh   then   marp slides.md
set -euo pipefail
cd "$(dirname "$0")"

out="slides.md"
cat modules/_header.md > "$out"

first=1
for f in $(ls modules/[0-9][0-9]-*.md | sort); do
  if [ "$first" = 1 ]; then
    cat "$f" >> "$out"
    first=0
  else
    printf '\n\n---\n\n' >> "$out"
    cat "$f" >> "$out"
  fi
done

echo "Built $out from $(ls modules/[0-9][0-9]-*.md | wc -l | tr -d ' ') module files."
