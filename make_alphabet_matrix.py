# -*- coding: utf-8 -*-
from weasyprint import HTML
import html as _h

E = ("", "", "", "", "empty")
def P(g,s,t,f=None): return (g,"phoen",s,t,f)
def G(g,s,t,f=None): return (g,"greek",s,t,f)
def T(g,s,t,f=None): return (g,"etrus",s,t,f)
def L(g,s,t,f=None): return (g,"latin",s,t,f)
def NY(note): return ("—","latin",note,"same","notyet")
def S(ps, heb, tr, gl, ghost=False): return dict(ps=ps, heb=heb, tr=tr, gl=gl, ghost=ghost)
def MG(g,s,nm,tone,ghost=False): return dict(g=g,s=s,nm=nm,tone=tone,ghost=ghost)
def DROP(note): return dict(drop=True, note=note)
def LL(g, phon): return dict(g=g, phon=phon)     # later-Latin: black letter + European sound note
D2 = dict(dash=True)

# row: (source, Phoen, Greek, Etrus, ClassicalLatin(~0 AD), LaterLatin, note, ModernGreek)
rows = [
 (S("ʔalp · ox","אֶלֶף","elef","thousand"),
   P("𐤀","/ʔ/","orig"),G("Α","/a/","chg"),T("𐌀","/a/","same"),L("A","/a/","same"),LL("A","Eng. name /eɪ/ (GVS)"),
   "Consonant → vowel: Greek reheard the glottal stop as /a/. (Ox sense survives in <i>aluf</i>, ‘chief'.)",
   MG("Α α","/a/","álfa","same")),
 (S("bayt · house","בַּיִת","bayit","house"),
   P("𐤁","/b/","orig"),G("Β","/b/","same"),T("𐌁","—","same","unused"),L("B","/b/","same"),LL("B","W. Rom. b→/v/; Sp. b=v"),
   "Etruscan carried B in its abecedarium but never used it (no /b/); Latin reactivated it.",
   MG("Β β","/v/","víta","chg")),
 (S("gaml · camel","גָּמָל","gamal","camel"),
   P("𐤂","/g/","orig"),G("Γ","/g/","same"),T("𐌂","/k/","chg"),L("C","/k/","same"),LL("C","palat.: It./tʃ/·Fr./s/·Sp./θ/"),
   "Voicing lost at Etruscan (/g/→/k/); early C also spelled /g/ — that job passed to G.",
   MG("Γ γ","/ɣ/","gámma","chg")),
 (S("dalt · door","דֶּלֶת","delet","door"),
   P("𐤃","/d/","orig"),G("Δ","/d/","same"),T("𐌃","—","same","unused"),L("D","/d/","same"),LL("D","Sp. intervoc. →[ð]"),
   "Carried but unused in Etruscan (no /d/); reactivated in Latin.",
   MG("Δ δ","/ð/","délta","chg")),
 (S("— uncertain","הֵא","he","name only"),
   P("𐤄","/h/","orig"),G("Ε","/e/","chg"),T("𐌄","/e/","same"),L("E","/e/","same"),LL("E","Eng.→/iː/ (GVS)"),
   "Consonant → vowel at Greek (/h/ → /e/). The name <i>he</i> is no living noun; its picture is unknown.",
   MG("Ε ε","/e/","épsilon","same")),
 (S("waw · hook","וָו","vav","hook"),
   P("𐤅","/w/","orig"),G("Ϝ","/w/","same"),T("𐌅","/w/","same"),L("F","/f/","chg"),LL("F","Sp. f-→h- (hijo)"),
   "Digamma kept waw's /w/; Etruscan wrote /f/ as 𐌅𐌇. <b>Latin reassigned</b> the shape to /f/ once V (← upsilon) took /w/.",
   DROP("digamma dropped · numeral ϛ = 6")),
 (S("zayin · weapon","זַיִן","zayin","weapon"),
   P("𐤆","/z/","orig"),G("Ζ","/zd/","chg"),T("𐌆","/ts/","chg"),NY("dropped ~312 BCE"),D2,
   "<b>Latin's two Z's</b>: at slot 7 in the Phoenician–Greek order. Dropped from Latin ~3rd c. BCE (rhotacism /z/→/r/); G took its seat; re-imported to the end 1st c. BCE (row below).",
   MG("Ζ ζ","/z/","zíta","chg")),
 (S("gaml · camel","גָּמָל","gamal","(via C)",ghost=True),
   P("𐤂","/g/","orig","ghost"),G("Γ","/g/","same","ghost"),T("𐌂","/k/","same","ghost"),L("G","/g/","same"),LL("G","palat.: It./dʒ/·Fr./ʒ/·Sp./x/"),
   "<b>New sign, c. 230 BCE</b>: a bar added to C to restore the /g/ Etruscan had erased — into the 7th seat Z vacated.",
   MG("Γ γ","/ɣ/","gámma","chg",ghost=True)),
 (S("ḥet · fence?","חֵית","ḥet","name only"),
   P("𐤇","/ħ/","orig"),G("Η","/h/ · /ɛː/","chg"),T("𐌇","/h/","same"),L("H","/h/","same"),LL("H","silent across Romance"),
   "Phoenician ḥet merges /ħ/+/χ/. Greek <b>forks</b>: Western heta /h/ vs Ionic eta /ɛː/; Latin took the Western /h/ branch.",
   MG("Η η","/i/","íta","chg")),
 (S("ṭet · wheel?","ט","ṭet","name only"),
   P("𐤈","/tˤ/","orig"),G("Θ","/tʰ/","chg"),T("𐌈","/tʰ/","same"),NY("→ TH"),D2,
   "Phoenician emphatic <b>ṭet</b> → Greek aspirate theta /tʰ/. Latin had no letter and wrote Greek θ as the digraph <b>TH</b>. Modern Greek fricativized it to /θ/.",
   MG("Θ θ","/θ/","thíta","chg")),
 (S("yad · hand","יָד","yad","hand"),
   P("𐤉","/j/","orig"),G("Ι","/i/","chg"),T("𐌉","/i/","same"),L("I","/i/","same"),LL("I","Eng.→/aɪ/ (GVS); cons.→J"),
   "Consonant → vowel at Greek (/j/ → /i/); Latin used it for both /i/ and /j/ — the /j/ half later split off as J.",
   MG("Ι ι","/i/","ióta","same")),
 (S("yad · hand","יָד","yad","(via I)",ghost=True),
   E,E,E,NY("= I"),LL("J","/dʒ/·/ʒ/·/x/·/j/"),
   "<b>Youngest letter</b>: a 16th-c. swash split from I to carry the consonant /j/ → /dʒ/. Absent at 0 AD.",
   MG("Ι ι","/i/","ióta","same",ghost=True)),
 (S("kap · palm","כַּף","kaf","palm"),
   P("𐤊","/k/","orig"),G("Κ","/k/","same"),T("𐌊","/k/","same"),L("K","/k/","same"),LL("K","stable /k/"),
   "Etruscan used K before /a/ — part of a three-way C / K / Q split by following vowel that Latin inherited.",
   MG("Κ κ","/k/","káppa","same")),
 (S("lamd · goad","לָמֶד","lamed","‘to learn'"),
   P("𐤋","/l/","orig"),G("Λ","/l/","same"),T("𐌋","/l/","same"),L("L","/l/","same"),LL("L","Sp. -ll-→/ʎ/→/ʝ/"),
   "<i>Stable throughout.</i>",
   MG("Λ λ","/l/","lámda","same")),
 (S("maym · water","מַיִם","mayim","water"),
   P("𐤌","/m/","orig"),G("Μ","/m/","same"),T("𐌌","/m/","same"),L("M","/m/","same"),LL("M","stable"),
   "<i>Stable throughout.</i>",
   MG("Μ μ","/m/","mi","same")),
 (S("nun · fish","נוּן","nun","fish = dag"),
   P("𐤍","/n/","orig"),G("Ν","/n/","same"),T("𐌍","/n/","same"),L("N","/n/","same"),LL("N","-gn-→/ɲ/ (ñ)"),
   "<i>Stable throughout.</i> (‘Fish' is the Aramaic sense; Hebrew for fish is <i>dag</i>.)",
   MG("Ν ν","/n/","ni","same")),
 (S("samek · prop","ס","samekh","support"),
   P("𐤎","/s/","orig"),G("Ξ","/ks/","chg"),E,NY("→ X"),D2,
   "Samekh took the 14th slot, repurposed by Greek for /ks/. Latin got /ks/ from Western <b>chi → X</b>, so xi itself left no Latin heir.",
   MG("Ξ ξ","/ks/","ksi","same")),
 (S("ʕayn · eye","עַיִן","ayin","eye"),
   P("𐤏","/ʕ/","orig"),G("Ο","/o/","chg"),T("𐌏","—","same","unused"),L("O","/o/","same"),LL("O","Eng.→/oʊ/ (GVS)"),
   "Phoenician ayin merges /ʕ/ + /ɣ/. Consonant → vowel at Greek. Etruscan had no /o/ (unused); Latin reactivated it.",
   MG("Ο ο","/o/","ómikron","same")),
 (S("pe · mouth","פֶּה","pe","mouth"),
   P("𐤐","/p/","orig"),G("Π","/p/","same"),T("𐌐","/p/","same"),L("P","/p/","same"),LL("P","W. Rom. p→b→v"),
   "<i>Stable throughout.</i>",
   MG("Π π","/p/","pi","same")),
 (S("ṣade · fish-hook?","צ","tsade","name only"),
   P("𐤑","/sˤ/","orig"),G("Ϻ","/s/","chg"),E,NY("→ S"),D2,
   "Phoenician emphatic <b>ṣade</b> → Greek <b>san</b> (Ϻ). Sigma won; san died before the classical age. No Latin heir — /s/ reached Latin via sigma → S. Afterlife: numeral <b>ϡ</b> (sampi, 900), debated.",
   DROP("obsolete · sampi ϡ = 900?")),
 (S("— uncertain","קוֹף","qof","monkey (mod.)"),
   P("𐤒","/q/","orig"),G("Ϙ","/k/","chg"),T("𐌒","/k/","same"),L("Q","/k/","same"),LL("Q","/kw/→/k/ (que)"),
   "Qoppa, before back vowels; dropped from classical Greek (numeral 90). Latin keeps Q only in QV.",
   DROP("koppa dropped · numeral ϟ = 90")),
 (S("raʾš · head","רֹאשׁ","rosh","head"),
   P("𐤓","/r/","orig"),G("Ρ","/r/","same"),T("𐌓","/r/","same"),L("R","/r/","same"),LL("R","Fr.→ uvular /ʁ/"),
   "Sound stable; Latin added the diagonal leg to tell R apart from P.",
   MG("Ρ ρ","/r/","ro","same")),
 (S("šin · tooth","שֵׁן","shen","tooth"),
   P("𐤔","/ʃ/","orig"),G("Σ","/s/","chg"),T("𐌔","/s/","same"),L("S","/s/","same"),LL("S","Fr. drops pre-cons.; Sp. e-"),
   "Sibilant shuffle: shin's /ʃ/ became sigma's /s/ (and swapped names with samek).",
   MG("Σ σ/ς","/s/","sígma","same")),
 (S("taw · mark","תָּו","tav","mark, sign"),
   P("𐤕","/t/","orig"),G("Τ","/t/","same"),T("𐌕","/t/","same"),L("T","/t/","same"),LL("T","-ti-→/ts/→/s/ (nation)"),
   "<i>Stable throughout.</i>",
   MG("Τ τ","/t/","taf","same")),
 # ---- Greek appendix (post-tau) ----
 (S("waw · hook","וָו","vav","(via Υ)",ghost=True),
   P("𐤅","/w/","orig","ghost"),G("Υ","/u/","chg"),T("𐌖","/u/","same"),NY("= V"),LL("U","Eng.→/juː/"),
   "Upsilon — waw's second child, appended at the Greek alphabet's end as vowel /u/. U split from V in the late Middle Ages. Absent at 0 AD.",
   MG("Υ υ","/i/","ípsilon","chg",ghost=True)),
 (S("waw · hook","וָו","vav","(via Υ)",ghost=True),
   P("𐤅","/w/","orig","ghost"),G("Υ","/u/","chg"),T("𐌖","/u, w/","same"),L("V","/w, u/","same"),LL("V","Lat./w/→/v/; Sp. v=b"),
   "Same upsilon line; in Latin, V served both /w/ and /u/. The whole U · V · W · Y clan descends from this one sign.",
   MG("Υ υ","/i/","ípsilon","chg",ghost=True)),
 (S("waw · hook","וָו","vav","(via V)",ghost=True),
   E,E,E,NY("= V"),LL("W","Eng./w/ · Ger./v/"),
   "<b>Doubled V</b> — a medieval invention for a Germanic /w/ that Latin had no letter for. Absent at 0 AD.",
   MG("Υ υ","/i/","ípsilon","chg",ghost=True)),
 (S("— Greek invention","","",""),
   E,G("Φ","/pʰ/","orig"),T("𐌘","/pʰ/","same"),NY("→ PH"),D2,
   "A <b>Greek invention</b> (with Ψ, Χ) for aspirated /pʰ/ — no Phoenician parent. Latin wrote it <b>PH</b>; Modern Greek turned it into /f/.",
   MG("Φ φ","/f/","fi","chg")),
 (S("samek · prop","סָמֶך","samekh","(via Χ)",ghost=True),
   E,G("Χ","/ks/","orig"),T("𐌗","/ks/","same"),L("X","/ks/","same"),LL("X","Sp.→/x/~/s/ (México)"),
   "A Greek supplemental with no Phoenician parent. Latin took the <b>Western</b> value /ks/; Eastern Greek used Χ for /kʰ/. Ends the classical alphabet before Y, Z.",
   MG("Χ χ","/x/","chi · /ks/ = Ξ","chg")),
 (S("waw · hook","וָו","vav","(via Υ)",ghost=True),
   P("𐤅","/w/","orig","ghost"),G("Υ","/y/","chg","ghost"),E,L("Y","/y/","same"),LL("Y","Gk /y/ (ü) → /i/"),
   "Re-borrowed straight from Greek upsilon in the 1st c. BCE for Greek loanwords — bypassing Etruscan; the ‘Greek i'. (Upsilon faded — already solid at U/V.)",
   MG("Υ υ","/i/","ípsilon","chg",ghost=True)),
 (S("— Greek invention","","",""),
   E,G("Ψ","/ps/","orig"),E,NY("→ PS"),D2,
   "A <b>Greek invention</b> for /ps/ (Eastern value; Western Greek used the shape for /kʰ/). No Latin letter — written <b>PS</b>. Stable today.",
   MG("Ψ ψ","/ps/","psi","same")),
 (S("— Ionian, ‹ O","","",""),
   E,G("Ω","/ɔː/","orig"),E,NY("→ O"),D2,
   "The last Greek letter — an <b>Ionian addition</b> (~7th–6th c. BCE), a long-/ɔː/ twin of omicron. Latin used <b>O</b>. Modern Greek merged it back to plain /o/.",
   MG("Ω ω","/o/","oméga","chg")),
 # ---- Z re-imported to the end (present by 0 AD) ----
 (S("‹ zayin (row 7)","","",""),
   E,G("Ζ","/z/","same","ghost"),E,L("Z","/z/","same"),LL("Z","It./ts/ · Sp./θ/ (zapato)"),
   "Latin's re-import of Z (1st c. BCE) sits at the alphabet's <b>end</b> — its ancestral 7th seat had gone to G. Its Phoenician–Greek ancestry is in the slot-7 row above.",
   DROP("")),
]

tone_cls = {"orig":"s-orig","chg":"s-chg","same":"s-same"}
heads = [("Phoenician","~1050 BCE"),("Greek","~800 BCE"),("Etruscan","~700 BCE"),("Classical Latin","~ AD 1")]

def src_cell(s):
    ghost = " ghost" if s["ghost"] else ""
    if s["heb"]:
        hebline = ('<span class="heb">%s</span> <span class="tr">%s</span> <i class="gl">%s</i>'
                   % (s["heb"], _h.escape(s["tr"]), _h.escape(s["gl"])))
    else:
        hebline = ""
    return ('<td class="src%s"><span class="ps">%s</span><span class="hb">%s</span></td>'
            % (ghost, _h.escape(s["ps"]), hebline))

def cell(c):
    g,script,s,tone,flag = c
    if flag=="empty":
        return '<td class="stage"><span class="empty">—</span></td>'
    if flag=="notyet":
        return ('<td class="stage"><span class="glyph g-latin ny">—</span>'
                '<span class="nynote">%s</span></td>') % _h.escape(s)
    ghost = " ghost" if flag=="ghost" else ""
    tag = '<span class="utag">unused</span>' if flag=="unused" else ""
    return ('<td class="stage%s"><span class="glyph g-%s">%s</span>'
            '<span class="sound %s">%s</span>%s</td>') % (ghost, script, g, tone_cls[tone], _h.escape(s), tag)

def later_cell(x):
    if x.get("dash"):
        return '<td class="llx"><span class="llg2 dsh">—</span></td>'
    return ('<td class="llx"><span class="llg2">%s</span><span class="llnote">%s</span></td>'
            % (x["g"], _h.escape(x["phon"])))

def mg_cell(m):
    if m.get("drop"):
        return '<td class="mg"><span class="mgg drop">—</span><span class="mgn">%s</span></td>' % _h.escape(m["note"])
    ghost = " ghost" if m.get("ghost") else ""
    return ('<td class="mg%s"><span class="mgg">%s</span>'
            '<span class="sound %s">%s</span><span class="mgn">%s</span></td>'
            % (ghost, m["g"], tone_cls[m["tone"]], _h.escape(m["s"]), _h.escape(m["nm"])))

trs = []
for src, ph, gr, et, classical, later, note, mg in rows:
    stcells = cell(ph)+cell(gr)+cell(et)+cell(classical)
    trs.append('<tr>%s%s%s<td class="note">%s</td>%s</tr>'
               % (src_cell(src), stcells, later_cell(later), note, mg_cell(mg)))
tbody = "\n".join(trs)
thead = ('<tr>'
         '<th class="src">Source word<span class="yr">Proto-Sinaitic · Hebrew · ~1800 BCE</span></th>'
         + "".join('<th>%s<span class="yr">%s</span></th>' % (h,y) for h,y in heads)
         + '<th class="llx">Later Latin<span class="yr">modern letter · sound in Europe</span></th>'
         + '<th class="note">Shifts &amp; notes</th>'
         + '<th class="mg">Modern Greek<span class="yr">today · vs ancient</span></th></tr>')

CSS = """
@page {
  size: A4 landscape; margin: 6mm 8mm 6mm 8mm;
  @bottom-left { content: "Rows in transmission order — each column reads in its own alphabet's order"; font-family:"IBM Plex Mono",monospace; font-size:6.4pt; color:#9a927f; }
  @bottom-right { content: "p. " counter(page) " / " counter(pages); font-family:"IBM Plex Mono",monospace; font-size:6.4pt; color:#9a927f; }
}
* { box-sizing: border-box; }
body { margin:0; color:#23201A; font-family:"Spectral",serif; font-size:9pt; line-height:1.4; }
.title { font-family:"Cinzel",serif; font-weight:600; font-size:12.5pt; margin:0 0 1.2mm; }
.sub { font-size:7.4pt; color:#4a4437; margin:0 0 1.6mm; max-width:280mm; }
.legend { font-family:"IBM Plex Mono",monospace; font-size:6.5pt; color:#6b6656; margin:0 0 1.6mm; display:flex; gap:6mm; flex-wrap:wrap; }
.k-chg{color:#A6472E;font-weight:600;} .k-same{color:#8A8474;} .k-ghost{opacity:.42;}

table { border-collapse:collapse; width:100%; }
thead { display:table-header-group; }
tr { break-inside:avoid; }
th,td { border:0.4pt solid #C7C2B0; padding:0.35mm 1.2mm; text-align:center; vertical-align:middle; }
thead th { background:#EDEAE0; color:#2E7D74; font-family:"IBM Plex Mono",monospace; font-size:6.4pt; letter-spacing:.03em; text-transform:uppercase; border-bottom:1pt solid #23201A; }
thead th .yr { display:block; color:#9a927f; font-size:5.5pt; margin-top:.4mm; font-weight:normal; letter-spacing:.02em; }
tbody tr:nth-child(even) td { background:#F5F3EC; }

.src { width:24mm; text-align:left; }
.src .ps { display:block; font-style:italic; font-size:7pt; color:#3a352b; }
.src .hb { display:block; margin-top:.4mm; unicode-bidi:isolate; }
.src .heb { font-family:"Frank Ruhl Libre",serif; font-size:9pt; direction:rtl; unicode-bidi:isolate; }
.src .tr { font-family:"IBM Plex Mono",monospace; font-size:6.4pt; color:#23201A; }
.src .gl { font-size:6.8pt; color:#8A8474; }
.src.ghost { opacity:.5; }

.stage { width:13.5mm; }
.glyph { display:block; height:3.7mm; line-height:3.7mm; font-size:10.5pt; }
.g-phoen{font-family:"Noto Sans Phoenician";direction:ltr;}
.g-greek{font-family:"Cardo",serif;}
.g-etrus{font-family:"Noto Sans Old Italic";direction:ltr;}
.g-latin{font-family:"Cinzel",serif;font-weight:600;font-size:10pt;}
.g-latin.ny{color:#b7b1a1;font-weight:400;}
.ghost .glyph{opacity:.36;} .ghost .sound{opacity:.55;}
.sound { display:block; margin-top:.2mm; font-family:"IBM Plex Mono",monospace; font-size:6.4pt; }
.s-orig{color:#23201A;} .s-chg{color:#A6472E;font-weight:500;} .s-same{color:#8A8474;}
.utag{display:block;font-family:"IBM Plex Mono",monospace;font-size:5.6pt;color:#9a927f;margin-top:.25mm;}
.nynote{display:block;font-family:"IBM Plex Mono",monospace;font-size:5.6pt;color:#9a927f;margin-top:.25mm;}
.empty{color:#b7b1a1;font-family:"IBM Plex Mono",monospace;}

/* Later Latin: plain black alphabet column + European sound note, no separator */
.llx { width:38mm; }
.llg2 { display:block; font-family:"Cinzel",serif; font-weight:600; font-size:11pt; color:#23201A; line-height:1; }
.llg2.dsh { color:#b7b1a1; font-weight:400; }
.llnote { display:block; font-family:"IBM Plex Mono",monospace; font-size:5.9pt; color:#7c7666; margin-top:.5mm; line-height:1.16; }

.note { text-align:left; font-size:6.8pt; line-height:1.08; color:#3a352b; width:70mm; border-left:0.8pt solid #23201A; }
.note b{color:#A6472E;font-weight:600;} .note i{color:#8A8474;}

.mg { width:20mm; border-left:0.8pt solid #23201A; }
.mg .mgg { display:block; font-family:"Cardo",serif; font-size:10pt; line-height:0.98; }
.mg .mgn { display:block; font-family:"IBM Plex Mono",monospace; font-size:5.3pt; color:#8A8474; margin-top:.15mm; line-height:1.05; }
.mg .drop { color:#b7b1a1; }
.mg.ghost { opacity:.5; }

.foot { margin-top:1.2mm; font-size:6.2pt; line-height:1.26; color:#8A8474; }
.foot b{color:#5f5a4c;font-weight:600;}
"""

DOC = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><style>%s</style></head>
<body>
<div class="title">The alphabet, hand to hand</div>
<div class="sub">Rows run in the <b>transmission order</b> (the shared abgad sequence + Greek post-tau additions), so each column reads top-to-bottom in its own alphabet's order. <b>Classical Latin</b> shows the alphabet at the turn of the millennium: the original slot-7 Z is gone (dropped ~3rd c. BCE), <b>G</b> holds that seat, and re-imported <b>Y</b> and <b>Z</b> sit at the end. <b>Later Latin</b> gives the modern letter with its main sound-developments across Europe (Romance + English). Greek-only letters (Θ Ξ Ϻ Φ Ψ Ω) drop into their Greek positions; faded cells mark ancestors or re-imports that don't count for the ordering.</div>
<div class="legend">
  <span><b class="k-chg">/a/</b> sound changed</span>
  <span><b class="k-same">/a/</b> held</span>
  <span><span class="k-ghost">𐌂</span> faded = doesn't count for order</span>
  <span style="color:#2E7D74">Ξ</span> Greek-only, no Latin heir
</div>
<table><thead>%s</thead><tbody>%s</tbody></table>
<div class="foot"><b>On the glyphs.</b> Unicode's canonical reference forms, not the variable shapes actually inscribed; Etruscan ran right-to-left, and Classical Latin had no lowercase (I and V each did double duty until J, U, W split off in the Middle Ages). The Later-Latin column is a headline sketch — Romance outcomes vary by language and position. Source words and several values are reconstructed and debated (E, H, Q, ṭet, ṣade). Digamma (F), koppa (Q) and san (Ϻ) survive in Greek only as numerals or not at all.</div>
</body></html>""" % (CSS, thead, tbody)

out = "alphabet-transmission-matrix-A4.pdf"
HTML(string=DOC).write_pdf(out)
print("wrote", out)
