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

# Brill Epichoric — archaic/epichoric Greek letterforms for the Greek column.
# Not on google/fonts; it ships as a zip from Brill under a *non-commercial* EULA
# (https://brill.com/page/510272). We pull the package and extract just the .otf.
if [ -f "$DEST/BrillEpichoric.otf" ]; then
  echo "  BrillEpichoric.otf (already present)"
elif ! command -v unzip >/dev/null 2>&1; then
  echo "  ! 'unzip' not found — skipping Brill Epichoric; the Greek column falls back to Cardo."
else
  echo "Fetching Brill Epichoric (non-commercial EULA — see brill.com/page/510272) ..."
  TMPZIP="$(mktemp -t epichoric.XXXXXX.zip)"
  if curl -fsSL -o "$TMPZIP" "https://brill.com/fileasset/downloads_static/static_epichoric_fontpackage.zip"; then
    OTF="$(unzip -Z1 "$TMPZIP" | grep -m1 '\.otf$')"
    unzip -p "$TMPZIP" "$OTF" > "$DEST/BrillEpichoric.otf" && echo "  BrillEpichoric.otf"
  else
    echo "  ! could not download Brill Epichoric; the Greek column falls back to Cardo."
  fi
  rm -f "$TMPZIP"
fi

# Aegean (George Douros, public domain) — Old Italic letterforms that follow
# actual Etruscan inscriptions (e.g. tau as T, not the cross Noto Sans Old
# Italic draws). Not on google/fonts; it ships in the Debian/Ubuntu
# 'fonts-ancient-scripts' package, so on apt systems we pull that package and
# extract just the one .ttf. Without it the Etruscan column falls back to Noto.
if [ -f "$DEST/Aegean.ttf" ]; then
  echo "  Aegean.ttf (already present)"
elif command -v apt-get >/dev/null 2>&1 && command -v dpkg-deb >/dev/null 2>&1; then
  echo "Fetching Aegean via the fonts-ancient-scripts package ..."
  TMPD="$(mktemp -d)"
  if ( cd "$TMPD" && apt-get download fonts-ancient-scripts ) >/dev/null 2>&1 \
     && dpkg-deb -x "$TMPD"/fonts-ancient-scripts_*.deb "$TMPD/x" 2>/dev/null; then
    AEG="$(find "$TMPD/x" -iname 'Aegean*.ttf' | head -n1)"
    [ -n "$AEG" ] && cp "$AEG" "$DEST/Aegean.ttf" && echo "  Aegean.ttf"
  else
    echo "  ! could not fetch Aegean; the Etruscan column falls back to Noto Sans Old Italic."
  fi
  rm -rf "$TMPD"
else
  echo "  ! 'apt-get'/'dpkg-deb' not found — install the UFAS 'Aegean' font by hand"
  echo "    (https://dn-works.com/ufas/); the Etruscan column falls back to Noto Sans Old Italic."
fi

if command -v fc-cache >/dev/null 2>&1; then
  fc-cache -f "$DEST" >/dev/null 2>&1 || true
  echo "Font cache refreshed."
else
  echo "Note: fontconfig (fc-cache) not found — on macOS just double-click the .ttf files, or drop them in ~/Library/Fonts."
fi
echo "Done."
