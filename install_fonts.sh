#!/usr/bin/env bash
# Fetch the fonts the generator needs into ~/.fonts (Linux) and refresh the cache.
# All are OFL-licensed and pulled from the google/fonts repo.
set -euo pipefail
DEST="${1:-$HOME/.fonts}"
mkdir -p "$DEST"
BASE="https://raw.githubusercontent.com/google/fonts/main"

fetch () { curl -fsSL -o "$DEST/$2" "$BASE/$1" && echo "  $2"; }

echo "Downloading fonts to $DEST ..."
fetch ofl/cardo/Cardo-Regular.ttf                       Cardo-Regular.ttf
fetch ofl/cardo/Cardo-Bold.ttf                          Cardo-Bold.ttf
fetch ofl/cardo/Cardo-Italic.ttf                        Cardo-Italic.ttf
fetch "ofl/cinzel/Cinzel%5Bwght%5D.ttf"                 Cinzel.ttf
fetch ofl/spectral/Spectral-Regular.ttf                 Spectral-Regular.ttf
fetch ofl/spectral/Spectral-Medium.ttf                  Spectral-Medium.ttf
fetch ofl/spectral/Spectral-Italic.ttf                  Spectral-Italic.ttf
fetch ofl/ibmplexmono/IBMPlexMono-Regular.ttf           IBMPlexMono-Regular.ttf
fetch ofl/ibmplexmono/IBMPlexMono-Medium.ttf            IBMPlexMono-Medium.ttf
fetch "ofl/frankruhllibre/FrankRuhlLibre%5Bwght%5D.ttf" FrankRuhlLibre.ttf
fetch ofl/notosansphoenician/NotoSansPhoenician-Regular.ttf NotoSansPhoenician-Regular.ttf
fetch ofl/notosansolditalic/NotoSansOldItalic-Regular.ttf   NotoSansOldItalic-Regular.ttf

if command -v fc-cache >/dev/null 2>&1; then
  fc-cache -f "$DEST" >/dev/null 2>&1 || true
  echo "Font cache refreshed."
else
  echo "Note: fontconfig (fc-cache) not found — on macOS just double-click the .ttf files, or drop them in ~/Library/Fonts."
fi
echo "Done."
