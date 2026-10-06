# PDF hebdomadaires pour Google Classroom (et pour faire cours sans réseau).
# Usage : python3 pdf.py <site_construit> <dossier_pdf> [dossier_polices] [semaines...]
#   sN-presentation.pdf     : une diapositive par page (16:9)
#   sN-textes.pdf           : dossier de textes de la semaine (A4) : extraits, questions, citations, lectures
#   sN-guide-enseignant.pdf : le guide imprimable de l'enseignant (A4)
# dossier_polices : node_modules contenant @fontsource-variable/playfair-display, @fontsource-variable/source-sans-3, @fontsource/caveat
import asyncio, html, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from playwright.async_api import async_playwright
from content_a import W as WA
from content_b import W as WB
from articles import ARTICLES
from notes_a import NOTES as NA
from notes_b import NOTES as NB
from biblio import BIB_WEEK

SITE, OUT = os.path.abspath(sys.argv[1]), sys.argv[2]
FONTS = sys.argv[3] if len(sys.argv) > 3 else ""
ONLY = [int(x) for x in sys.argv[4:]]
os.makedirs(OUT, exist_ok=True)
WEEKS = WA + WB
NOTES = {**NA, **NB}
CLASSROOM = "https://classroom.google.com/c/ODg5MzMzMTU4ODc4?cjc=rxdffgje"
SITEURL = "https://gkhndnr.github.io/catania-litterature-2026/"

def font_css():
    if not FONTS: return ""
    f = lambda pkg, name: f"file://{os.path.abspath(FONTS)}/{pkg}/files/{name}"
    pf, ss, cv = "@fontsource-variable/playfair-display", "@fontsource-variable/source-sans-3", "@fontsource/caveat"
    out = ""
    for sub in ["latin", "latin-ext"]:
        out += f"@font-face{{font-family:'Playfair Display';font-style:normal;font-weight:400 900;src:url({f(pf, f'playfair-display-{sub}-wght-normal.woff2')})}}"
        out += f"@font-face{{font-family:'Playfair Display';font-style:italic;font-weight:400 900;src:url({f(pf, f'playfair-display-{sub}-wght-italic.woff2')})}}"
        out += f"@font-face{{font-family:'Source Sans 3';font-style:normal;font-weight:200 900;src:url({f(ss, f'source-sans-3-{sub}-wght-normal.woff2')})}}"
        out += f"@font-face{{font-family:'Source Sans 3';font-style:italic;font-weight:200 900;src:url({f(ss, f'source-sans-3-{sub}-wght-italic.woff2')})}}"
        for wt in (500, 700):
            out += f"@font-face{{font-family:'Caveat';font-weight:{wt};src:url({f(cv, f'caveat-{sub}-{wt}-normal.woff2')})}}"
    return out

def e(s):
    t = html.escape(s, quote=False)
    t = re.sub(r" ([?!;:»])", " \\1", t).replace("« ", "« ")
    return t.replace("&lt;i&gt;", "<i>").replace("&lt;/i&gt;", "</i>")

def deck_html(n):
    h = open(os.path.join(SITE, f"s{n}.html"), encoding="utf-8").read()
    secs = re.findall(r'<section class="slide".*?</section>', h, re.S)
    css = open(os.path.join(SITE, "site.css"), encoding="utf-8").read()
    return (f"<!doctype html><html lang=fr><head><meta charset=utf-8><style>{font_css()}{css}"
            "@page{size:1920px 1080px;margin:0}html,body{margin:0;padding:0;background:#fff}"
            ".slide{break-after:page;page-break-after:always}</style></head><body>" + "".join(secs) + "</body></html>"), len(secs)

def cits_from_notes(n):
    seen, out = set(), []
    for txt in NOTES[n].values():
        m = re.search(r"CITATIONS D'APPUI · (.*?)(?:\n\n|$)", txt, re.S)
        if not m: continue
        for line in m.group(1).split("\n"):
            mm = re.match(r"« (.*) » \((.*)\)$", line.strip())
            if mm and mm.group(1) not in seen:
                seen.add(mm.group(1)); out.append((mm.group(1), mm.group(2)))
    return out

def textes_html(w):
    n = w["n"]
    qb = lambda q, src: f'<blockquote><p>«\u00a0{e(q)}\u00a0»</p><cite>{e(src)}</cite></blockquote>'
    txt = ""
    for k, t in enumerate(w["textes"], 1):
        quotes = "".join(qb(" / ".join(l), s) for l, s in t["quotes"])
        qs = "".join(f"<li><b>{e(a)}</b> {e(b)}</li>" for a, b in t["questions"])
        txt += f'<section class="t"><h3>Texte {k} · {e(t["title"])}</h3>{quotes}<p class="lab">Pour lire le texte</p><ul>{qs}</ul></section>'
    nv = w["nouvelle"]
    nvq = qb(" / ".join(nv["quote"][0]), nv["quote"][1]) if nv["quote"] else ""
    nvp = "".join(f"<li><b>{e(a)}</b> {e(b)}</li>" for a, b in nv["points"])
    crit = ""
    for ar in ARTICLES.get(n, []):
        ids = "".join(f"<li><b>{e(a)}</b> {e(b)}</li>" for a, b in ar["idees"])
        cq = "".join(qb(c, s) for c, s in ar["citations"])
        crit += f'<section class="t"><h3>Lecture critique · {e(ar["auteur"])} : {e(ar["titre"])}</h3><ul>{ids}</ul>{cq}<p class="deb">À discuter : {e(ar["debat"])}</p><p class="ref">{e(ar["ref"])}</p></section>'
    cits = "".join(qb(c, s) for c, s in cits_from_notes(n))
    prog = "".join(f"<li><b>{e(a)}</b> {e(b)}</li>" for a, b in w["prog"])
    obj = "".join(f"<li>{e(o)}</li>" for o in w["objectifs"])
    av = "".join(f"<li>{e(x)}</li>" for x in w["avant"])
    an = "".join(f"<li>{e(x)}</li>" for x in w["anthologie"])
    refs = "".join(f"<li>{e(x)}</li>" for x in BIB_WEEK.get(n, []))
    css = """@page{size:A4;margin:16mm 16mm 18mm}
body{font:10.5pt/1.5 'Source Sans 3',Arial,sans-serif;color:#1F1A24;margin:0}
h1{font:700 26pt/1.1 'Playfair Display',Georgia,serif;margin:2mm 0 1mm}
h2{font:700 15pt 'Playfair Display',Georgia,serif;margin:7mm 0 2mm;padding-top:2mm;border-top:1.5pt solid #1F1A24}
h3{font:700 12pt 'Playfair Display',Georgia,serif;margin:4mm 0 1.5mm;color:#A1343C}
.eb{font:700 8pt 'Source Sans 3';letter-spacing:2pt;text-transform:uppercase;color:#A1343C;margin:0}
.sub{color:#4A4453;margin:0 0 3mm;font-style:italic}
blockquote{margin:2mm 0 2mm;padding:1.5mm 0 1.5mm 4mm;border-left:2.5pt solid #A1343C;break-inside:avoid}
blockquote p{margin:0;font:italic 11.5pt/1.4 'Playfair Display',Georgia,serif}
cite{display:block;font:normal 8.5pt 'Source Sans 3';color:#7A7282;margin-top:1mm}
ul{margin:1mm 0 2mm;padding-left:5mm}li{margin:.7mm 0}
.lab{font:700 8pt 'Source Sans 3';letter-spacing:1.5pt;text-transform:uppercase;color:#2E6A8E;margin:2mm 0 0}
.deb{color:#A1343C;font-weight:700;margin:1mm 0}.ref{font-size:8.5pt;color:#7A7282;margin:0}
.box{border:1pt solid #E2D8C6;background:#FBF8F2;padding:3mm 4mm;margin:3mm 0;break-inside:avoid}
.t{break-inside:auto}.small{font-size:8.5pt;color:#7A7282}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:6mm}
.head .qr{flex:none;text-align:center;font-size:7pt;color:#7A7282}"""
    import qrcode, qrcode.image.svg
    def qrsvg(url):
        q = qrcode.QRCode(border=1, image_factory=qrcode.image.svg.SvgPathImage); q.add_data(url); q.make(fit=True)
        s = q.make_image().to_string(encoding="unicode")
        return re.sub(r'width="[^"]+" height="[^"]+"', 'width="70" height="70"', s, count=1)
    return f"""<!doctype html><html lang=fr><head><meta charset=utf-8><style>{font_css()}{css}</style></head><body>
<div class="head"><div><p class="eb">Dossier de textes · Semaine {n} · {e(w['dates_long'])} · Université de Catane</p>
<h1>{e(w['title'])}</h1><p class="sub">{e(w['sub'])} ({e(w['period'])})</p></div>
<div class="qr">{qrsvg(SITEURL + f's{n}.html')}<br>page de la semaine</div></div>
<div class="box"><b>À la fin de la semaine, je peux…</b><ul>{obj}</ul><b>Dans la fiche du cours</b><ul>{prog}</ul></div>
<h2>Textes à la loupe</h2>{txt}
<h2>{e(nv['label'])} · {e(nv['title'])}</h2>{nvq}<ul>{nvp}</ul><p class="small">{e(nv['bas'])}</p>
<h2>Citations de la semaine</h2><p class="small">Citations utilisées en classe (œuvres, préfaces, critique), avec leur source.</p>{cits}
{('<h2>Lecture critique</h2>' + crit) if crit else ''}
<h2>Travail personnel</h2><div class="box"><b>À lire</b><ul>{av}</ul><b>Ma production</b> (à déposer sur Google Classroom) : {e(w['production'])}<br><br><b>Pour mon anthologie (A.2)</b><ul>{an}</ul></div>
<h2>Références de la semaine</h2><ul class="small">{refs}</ul>
<p class="small">Textes intégraux du domaine public : fr.wikisource.org et gallica.bnf.fr. Site du cours : {SITEURL} · Classroom : code rxdffgje.</p>
</body></html>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        for w in WEEKS:
            n = w["n"]
            if ONLY and n not in ONLY: continue
            dh, cnt = deck_html(n)
            tmp = os.path.join(OUT, f"_deck{n}.html"); open(tmp, "w", encoding="utf-8").write(dh)
            await pg.goto("file://" + os.path.abspath(tmp)); await pg.wait_for_timeout(600)
            await pg.pdf(path=os.path.join(OUT, f"s{n}-presentation.pdf"), width="1920px", height="1080px", print_background=True, prefer_css_page_size=True)
            os.remove(tmp)
            th = os.path.join(OUT, f"_textes{n}.html"); open(th, "w", encoding="utf-8").write(textes_html(w))
            await pg.goto("file://" + os.path.abspath(th)); await pg.wait_for_timeout(400)
            await pg.pdf(path=os.path.join(OUT, f"s{n}-textes.pdf"), format="A4", print_background=True, prefer_css_page_size=True,
                         display_header_footer=True, header_template="<span></span>",
                         footer_template=f'<div style="font-size:7pt;color:#7A7282;width:100%;text-align:center">Semaine {n} · {html.escape(w["title"])} · page <span class="pageNumber"></span>/<span class="totalPages"></span></div>')
            os.remove(th)
            await pg.goto(f"file://{SITE}/prof-s{n}.html"); await pg.wait_for_timeout(400)
            await pg.add_style_tag(content=font_css() + "@page{size:A4;margin:14mm} .callout{break-inside:avoid}")
            await pg.wait_for_timeout(300)
            await pg.pdf(path=os.path.join(OUT, f"s{n}-guide-enseignant.pdf"), format="A4", print_background=True,
                         display_header_footer=True, header_template="<span></span>",
                         footer_template=f'<div style="font-size:7pt;color:#7A7282;width:100%;text-align:center">Guide de l\'enseignant · semaine {n} · page <span class="pageNumber"></span>/<span class="totalPages"></span></div>')
            print("ok", n, cnt, "diapositives")
        await b.close()

asyncio.run(main())
