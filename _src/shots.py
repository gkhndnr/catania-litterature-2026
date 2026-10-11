# Captures d'écran annotées pour la page Mode d'emploi.
# Usage : python3 shots.py <site_construit> <dossier_img> [dossier_polices] ; écrit shots.json à côté de ce fichier.
# Chaque capture : page, largeur, zone (sélecteurs haut/bas), repères (sélecteurs, dans l'ordre de la légende).
import asyncio, json, os, sys
from playwright.async_api import async_playwright

SITE, IMG = sys.argv[1], sys.argv[2]
FONTS = sys.argv[3] if len(sys.argv) > 3 else ""  # facultatif : node_modules avec les polices @fontsource (comme pdf.py)

def font_css():
    if not FONTS: return ""
    f = lambda pkg, name: f"file://{os.path.abspath(FONTS)}/{pkg}/files/{name}"
    pf, ss, cv = "@fontsource-variable/playfair-display", "@fontsource-variable/source-sans-3", "@fontsource/caveat"
    out = ""
    for sub in ["latin", "latin-ext"]:
        out += f"@font-face{{font-family:'Playfair Display';font-style:normal;font-weight:400 900;src:url({f(pf, f'playfair-display-{sub}-wght-normal.woff2')})}}"
        out += f"@font-face{{font-family:'Playfair Display';font-style:italic;font-weight:400 900;src:url({f(pf, f'playfair-display-{sub}-wght-italic.woff2')})}}"
        out += f"@font-face{{font-family:'Source Sans 3';font-style:normal;font-weight:200 900;src:url({f(ss, f'source-sans-3-{sub}-wght-normal.woff2')})}}"
        for wt in (500, 700):
            out += f"@font-face{{font-family:'Caveat';font-weight:{wt};src:url({f(cv, f'caveat-{sub}-{wt}-normal.woff2')})}}"
    return out
os.makedirs(IMG, exist_ok=True)

SPECS = {
 "accueil": dict(page="index.html", width=1280, top="body", bottom=".weeks .wk:nth-child(4)",
   pins=[(".bar nav a[href='s1.html']","below"), (".bar nav a[href='guide.html']","below"), (".bar nav a[href='biblio.html']","below"),
         (".bar nav a[href='carnet.html']","below"), (".bar nav a[href*='classroom']","below"), (".bar nav a[href*='claude.ai']","below"), (".weeks .wk:first-child","tr")]),
 "semaine": dict(page="s1.html", width=1280, top=".weektabs", bottom=".audio",
   pins=[(".weektabs a:last-child","right"), (".deckhead h1","right"), (".essentiel h2","right"), (".t-ess .tierh","right"),
         (".t-cls .tierh","right"), (".t-ryt .tierh","right"), (".audio .eyebrow","right")]),
 "presentation": dict(page="s1.html", width=1280, top="h2.deckt", bottom="#notes", notes=True, cut=420,
   pins=[("#stage","tr"), ("#prev","below"), ("#count","below"), ("#next","below"), ("label.tog","below"), ("a.btn","below"), ("#fs","below"), ("#notes h4","right")]),
 "mobile": dict(page="s1.html", width=390, top="body", bottom=".essentiel",
   pins=[(".bar nav","tr"), (".weektabs a:last-child","right"), (".essentiel h2","right")]),
 "prof": dict(page="prof-s1.html", width=1280, top="main", bottom="ol.ess",
   pins=[("main button.btn","right"), (".callout","tr"), ("main h2","right")]),
}

JS = """([top,bottom,pins])=>{
 const T=document.querySelector(top).getBoundingClientRect().top+scrollY;
 const B=document.querySelector(bottom).getBoundingClientRect().bottom+scrollY;
 const P=pins.map(([s,m])=>{const el=document.querySelector(s);const r=el.getBoundingClientRect();let x,y;
   if(m==='below'){x=r.left+r.width/2;y=r.bottom+16}
   else if(m==='tr'){x=r.right-18;y=r.top+18}
   else if(m==='tl'){x=r.left+14;y=r.top+14}
   else {const g=document.createRange();g.selectNodeContents(el);const rs=[...g.getClientRects()];const first=rs[0]||r;const right=Math.max(...rs.filter(q=>Math.abs(q.top-first.top)<4).map(q=>q.right));x=right+20;y=first.top+first.height/2}
   return [x+scrollX,y+scrollY]});
 return {T,B,P,W:document.documentElement.clientWidth}}"""

async def main():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for key, sp in SPECS.items():
            mobile = sp["width"] < 500
            pg = await b.new_page(viewport={"width": sp["width"], "height": 900}, device_scale_factor=2 if mobile else 1)
            await pg.goto(f"file://{os.path.abspath(SITE)}/{sp['page']}")
            await pg.wait_for_timeout(500)
            await pg.add_style_tag(content=font_css() + ".bar{position:static!important}")
            await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            if sp.get("notes"):
                await pg.check("#shownotes"); await pg.evaluate("show(6)"); await pg.wait_for_timeout(200)
            d = await pg.evaluate(JS, [sp["top"], sp["bottom"], sp["pins"]])
            top = max(0, d["T"] - 12); bottom = d["B"] + 12
            if sp.get("cut"): bottom = min(bottom, d["P"][-1][1] + sp["cut"])
            h = bottom - top
            clip = {"x": 0, "y": top, "width": d["W"], "height": h}
            path = os.path.join(IMG, f"guide-{key}.jpg")
            await pg.screenshot(path=path, clip=clip, full_page=True, type="jpeg", quality=80)
            pins = []
            for (x, y) in d["P"]:
                px = min(max(x, 14), d["W"] - 14); py = min(max(y - top, 14), h - 14)
                pins.append([round(px / d["W"] * 100, 2), round(py / h * 100, 2)])
            out[key] = {"w": int(d["W"]), "h": int(h), "pins": pins}
            await pg.close()
        await b.close()
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "shots.json"), "w"), indent=1)
    print(out)

asyncio.run(main())
