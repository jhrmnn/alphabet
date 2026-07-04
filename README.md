# Alphabet transmission matrix → A4 PDF

`make_alphabet_matrix.py` builds an HTML table of the alphabet's descent
(Phoenician → Greek → Etruscan → Classical Latin → Later Latin, plus Modern
Greek and the Greek-only letters) and renders it to a two-page A4-landscape PDF
with [WeasyPrint](https://weasyprint.org/).

All the data lives in the `rows` list near the top of the script — one tuple per
letter — so editing content is just editing that list. Styling is the `CSS`
string; layout is plain HTML `<table>`.

## Requirements

- **Python 3.9+**
- **WeasyPrint**: `pip install weasyprint`
  - WeasyPrint needs the system libraries **Pango, HarfBuzz, fontconfig, cairo/GDK-Pixbuf**.
    - Debian/Ubuntu: `sudo apt install libpango-1.0-0 libpangocairo-1.0-0 libharfbuzz0b libffi-dev`
    - macOS (Homebrew): `brew install pango`
    - See the [WeasyPrint install docs](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html) if it complains.
- **Fonts** (seven OFL families): Cardo, Cinzel, Spectral, IBM Plex Mono,
  Frank Ruhl Libre, Noto Sans Phoenician, Noto Sans Old Italic.
  The exotic scripts (Phoenician `𐤀`, Old Italic/Etruscan `𐌀`, archaic Greek
  digamma/koppa/san `Ϝ Ϙ Ϻ`, Hebrew with niqqud) will render as tofu boxes
  without these.
- **Brill Epichoric** — used for the archaic **Greek** column, whose
  epichoric letterforms are historically truer to ~800 BCE than the classical
  Cardo shapes. It is **not** OFL: Brill offers it free under a *non-commercial*
  EULA ([brill.com/page/510272](https://brill.com/page/510272)), so
  `install_fonts.sh` downloads Brill's own package and extracts the `.otf`. If
  it is missing, the Greek column falls back to Cardo. The right-most Modern
  Greek column stays on Cardo either way.

## Run

```bash
# 1. install the fonts (Linux; writes to ~/.fonts and refreshes fontconfig)
bash install_fonts.sh

# 2. install WeasyPrint
pip install weasyprint

# 3. generate
python3 make_alphabet_matrix.py     # → alphabet-transmission-matrix-A4.pdf
```

The output filename is the `out = ...` line at the very bottom of the script.

## Notes

- On macOS, `install_fonts.sh` downloads the .ttf files but can't refresh the
  cache; drop them into `~/Library/Fonts` (or double-click each) instead.
- Fonts are fetched from the `google/fonts` GitHub repo; Cinzel and Frank Ruhl
  Libre are variable fonts, which recent WeasyPrint handles fine.
- Prefer a browser engine instead? The script builds a self-contained HTML
  string in the `DOC` variable — you can `print(DOC)` and save it as `.html`,
  then print to PDF from Chrome (use the same `@page` size). Fonts still need to
  be installed (or swap the `@font-face`/`font-family` names for webfont links).
