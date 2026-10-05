import html, json, re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_a import W as WA
from content_b import W as WB
from articles import ARTICLES
from notes_a import NOTES as NA
from notes_b import NOTES as NB
NOTES = {**NA, **NB}
WEEKS = WA + WB
OLD = sys.argv[1]   # old site dir (for raw slides)
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)

INK, PAPER, PAPER2, CARD, LINE = "#1F1A24", "#F5EFE3", "#EDE4D3", "#FBF8F2", "#E2D8C6"
WINE, BLUE, GOLD, SOFT, MUTE = "#A1343C", "#2E6A8E", "#D9A441", "#4A4453", "#7A7282"
SERIF = "'Playfair Display', Georgia, serif"
SANS = "'Source Sans 3', Arial, sans-serif"
HAND = "'Caveat', 'Brush Script MT', cursive"
APP = "https://claude.ai/artifact/CFbd252hSjfJVZJkZSWaEU"
SITE = "https://gkhndnr.github.io/catania-litterature-2026/"
COURSE = "Letteratura francese dal Preromanticismo a Les années folles"

def e(s):
    t = html.escape(s, quote=False)
    return t.replace("&lt;i&gt;", "<i>").replace("&lt;/i&gt;", "</i>")
def a(s): return html.escape(s, quote=True)

# ------------------------------------------------------------------ slide parts
def slide(sid, bg, color, inner, pad="128px 128px 160px", extra="gap:44px", foot=None):
    f = f'<p style="position:absolute; left:128px; bottom:60px; width:1664px; font-size:24px; color:{MUTE if bg in (PAPER,PAPER2,CARD) else "#BDB3C4"}">{e(foot)}</p>' if foot else ""
    return (f'<section class="slide" id="{sid}" style="background:{bg}; color:{color}; font-family:{SANS}; '
            f'padding:{pad}; display:flex; flex-direction:column; {extra}">\n{inner}\n{f}\n</section>')

def head(eyebrow, title, col=WINE, size=68):
    return (f'<div style="display:flex; flex-direction:column; gap:12px">'
            f'<p style="font-size:24px; letter-spacing:4px; text-transform:uppercase; font-weight:700; color:{col}">{e(eyebrow)}</p>'
            f'<h2 style="font-family:{SERIF}; font-size:{size}px; font-weight:700; line-height:1.1">{e(title)}</h2></div>')

def card(inner, top=WINE, pad="32px 36px", flex="flex:1"):
    return (f'<div style="{flex}; display:flex; flex-direction:column; gap:14px; background:{CARD}; padding:{pad}; '
            f'border-top:8px solid {top}; border-radius:12px">{inner}</div>')

def footer(w): return f"Semaine {w['n']} · {w['title']} · UniCT 2026"

def s_cover(w):
    inner = (f'<div style="position:absolute; left:1392px; top:0; width:528px; height:1080px; background:linear-gradient(160deg, {WINE} 0%, #5E1F2B 100%)"></div>'
      f'<p style="position:absolute; left:1430px; top:740px; width:440px; font-family:{HAND}; font-size:56px; line-height:1.1; color:{PAPER}; transform:rotate(-4deg)">{e(w["hand"])}</p>'
      f'<div style="display:flex; flex-direction:column; gap:24px; width:1180px">'
      f'<p style="font-size:24px; letter-spacing:4px; text-transform:uppercase; font-weight:700; color:{GOLD}">Semaine {w["n"]} · {e(w["dates_long"])}</p>'
      f'<h1 style="font-family:{SERIF}; font-size:{110 if len(w["title"])<26 else 92}px; font-weight:700; line-height:1.05">{e(w["title"])}</h1>'
      f'<p style="font-family:{SERIF}; font-style:italic; font-size:40px; line-height:1.25; color:#E8DFCF">{e(w["sub"])} ({e(w["period"])})</p></div>'
      f'<div style="display:flex; flex-direction:column; gap:8px; width:1180px">'
      f'<p style="font-size:30px; font-weight:600">{e(COURSE)}</p>'
      f'<p style="font-size:24px; color:#BDB3C4">Gökhan Dinar · Visiting Professor · DISUM, Università di Catania</p></div>')
    return slide("cover", INK, PAPER, inner, pad="128px", extra="justify-content:space-between")

def s_objectifs(w):
    lis = "".join(f'<li style="display:flex; gap:20px; align-items:flex-start"><span style="flex:none; width:40px; height:40px; border:4px solid {WINE}; border-radius:8px; margin-top:4px"></span><span>{e(o)}</span></li>' for o in w["objectifs"])
    tags = "".join(f'<div style="display:flex; flex-direction:column; gap:4px; padding:14px 0; border-bottom:1px solid {LINE}"><p style="font-size:20px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:{BLUE}">{e(t)}</p><p style="font-size:24px; line-height:1.3">{e(x)}</p></div>' for t,x in w["prog"])
    inner = head("Objectifs de la semaine", "À la fin de la semaine, je peux…") + (
      f'<div style="display:flex; gap:56px; flex:1">'
      f'<ul style="flex:1.35; list-style:none; padding:0; display:flex; flex-direction:column; gap:28px; font-size:32px; line-height:1.35">{lis}</ul>'
      f'<div style="flex:1; background:{CARD}; border-radius:12px; padding:28px 32px; border-left:8px solid {BLUE}"><p style="font-size:24px; font-weight:700; color:{BLUE}; margin-bottom:6px">Dans la fiche du cours</p>{tags}</div></div>')
    return slide("objectifs", PAPER, INK, inner, foot=footer(w))

def s_seances(w):
    cols = [WINE, BLUE, INK]
    cards = "".join(card(f'<p style="font-size:24px; font-weight:700; color:{c}">SÉANCE {k} · 2 h</p><h3 style="font-family:{SERIF}; font-size:44px; line-height:1.15">{e(t)}</h3><p style="font-size:30px; line-height:1.4; color:{SOFT}">{e(x)}</p>', top=c, pad="40px")
                    for (t,x),c,k in zip(w["seances"], cols, "ABC"))
    inner = head("La semaine en trois séances", "Contexte, texte, expérience") + f'<div style="display:flex; gap:32px; flex:1">{cards}</div>'
    return slide("seances", PAPER, INK, inner, foot=footer(w))

def s_enigme(w):
    q, ctx, h = w["enigme"]
    inner = (f'<p style="font-size:24px; letter-spacing:4px; text-transform:uppercase; font-weight:700; color:#F2D9A8">L\'énigme de la semaine</p>'
      f'<h2 style="font-family:{SERIF}; font-size:84px; font-weight:700; line-height:1.1; width:1560px">{e(q)}</h2>'
      f'<p style="font-size:34px; line-height:1.4; width:1400px">{e(ctx)}</p>'
      f'<p style="font-family:{HAND}; font-size:56px; color:#F2D9A8">{e(h)}</p>')
    return slide("enigme", WINE, PAPER, inner, pad="128px", extra="justify-content:center; gap:40px")

def s_frise(w):
    items = w["frise"]
    cells = "".join(f'<div style="flex:1; display:flex; flex-direction:column; gap:10px; padding-right:18px"><p style="font-family:{SERIF}; font-size:44px; font-weight:700; color:{BLUE if b else WINE}">{e(y)}</p><p style="font-size:26px; line-height:1.3">{e(t)}</p></div>' for y,t,b in items)
    inner = head("Frise", w["frise_titre"]) + (
      f'<div style="display:flex; border-top:6px solid {INK}; padding-top:32px">{cells}</div>'
      f'<p style="font-size:28px; color:{SOFT}"><span style="color:{WINE}; font-weight:700">Rouge</span> : œuvres · <span style="color:{BLUE}; font-weight:700">Bleu</span> : événements qui changent le champ littéraire</p>')
    return slide("frise", PAPER, INK, inner, foot=footer(w))

def s_auteurs(w):
    cards = "".join(card(f'<h3 style="font-family:{SERIF}; font-size:40px; line-height:1.1">{e(n)}</h3><p style="font-size:24px; font-weight:700; color:{WINE}">{e(d)}</p><p style="font-size:28px; line-height:1.4; color:{SOFT}">{e(t)}</p>', top=INK, pad="32px")
                     for n,d,t in w["auteurs"])
    inner = head("Les voix de la semaine", "Qui écrit, d'où, contre qui ?") + f'<div style="display:grid; grid-template-columns:1fr 1fr; gap:28px; flex:1">{cards}</div>'
    return slide("auteurs", PAPER2, INK, inner, extra="gap:36px", foot=footer(w))

def s_outil(w):
    nom, auteur, pts, ex = w["outil"]
    rows = "".join(f'<div style="display:flex; gap:28px; align-items:baseline; padding:18px 0; border-bottom:1px solid rgba(245,239,227,.2)"><p style="flex:none; width:330px; font-family:{SERIF}; font-size:38px; font-weight:700; color:{GOLD}">{e(k)}</p><p style="font-size:32px; line-height:1.35">{e(v)}</p></div>' for k,v in pts)
    inner = (head(f"Boîte à outils · {auteur}", nom, col=GOLD) + f'<div>{rows}</div>'
             f'<p style="font-family:{HAND}; font-size:44px; line-height:1.2; color:#F2D9A8; width:1600px">{e(ex)}</p>')
    return slide("outil", BLUE, PAPER, inner, extra="gap:36px", foot=footer(w))

def quote_block(lines, src, size):
    l = "<br>".join(e(x) for x in lines)
    return (f'<div style="display:flex; flex-direction:column; gap:14px; border-left:8px solid {WINE}; padding-left:36px">'
            f'<p style="font-family:{SERIF}; font-size:{size}px; line-height:1.3; font-style:italic">« {l} »</p>'
            f'<p style="font-size:24px; color:{MUTE}">{e(src)}</p></div>')

def s_texte(w, k):
    t = w["textes"][k]
    nchar = sum(len(" ".join(l)) for l,_ in t["quotes"])
    size = 52 if nchar < 90 else 44 if nchar < 170 else 38
    qs = "".join(quote_block(l, s, size) for l, s in t["quotes"])
    ques = "".join(f'<div style="display:flex; flex-direction:column; gap:6px"><p style="font-size:24px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:{BLUE}">{e(a_)}</p><p style="font-size:28px; line-height:1.35">{e(b_)}</p></div>' for a_,b_ in t["questions"])
    inner = head(f"Texte à la loupe · {k+1}", t["title"]) + (
      f'<div style="display:flex; gap:56px; flex:1; align-items:flex-start">'
      f'<div style="flex:1.5; display:flex; flex-direction:column; gap:36px">{qs}</div>'
      f'<div style="flex:1; display:flex; flex-direction:column; gap:22px; background:{CARD}; border-radius:12px; padding:32px">{ques}</div></div>')
    return slide(f"texte{k+1}", PAPER, INK, inner, extra="gap:40px", foot=footer(w))

def s_methode(w):
    n, titre, pts, ex = w["methode"]
    steps = "".join(f'<li style="display:flex; gap:24px; align-items:baseline"><span style="flex:none; font-family:{SERIF}; font-size:48px; font-weight:700; color:{WINE}; width:48px">{i}</span><span>{e(p)}</span></li>' for i,p in enumerate(pts,1))
    track = "".join(f'<span style="width:72px; height:12px; border-radius:6px; background:{WINE if i<=n else LINE}"></span>' for i in range(1,9))
    inner = head(f"Méthode du commentaire · étape {n} sur 8", titre) + (
      f'<div style="display:flex; gap:8px">{track}</div>'
      f'<div style="display:flex; gap:56px; flex:1">'
      f'<ol style="flex:1.3; list-style:none; padding:0; display:flex; flex-direction:column; gap:28px; font-size:34px; line-height:1.35">{steps}</ol>'
      + card(f'<p style="font-size:24px; font-weight:700; color:{BLUE}">EXERCICE</p><p style="font-size:32px; line-height:1.4">{e(ex)}</p>', top=BLUE, pad="36px") + '</div>')
    return slide("methode", PAPER2, INK, inner, extra="gap:36px", foot=footer(w))

def s_nouvelle(w):
    nv = w["nouvelle"]
    q = quote_block(nv["quote"][0], nv["quote"][1], 42) if nv["quote"] else ""
    pts = "".join(card(f'<p style="font-size:24px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:{WINE}">{e(k)}</p><p style="font-size:29px; line-height:1.38">{e(v)}</p>', top=WINE, pad="28px 32px") for k,v in nv["points"])
    inner = head(nv["label"], nv["title"], size=60 if len(nv["title"])<48 else 50) + q + (
      f'<div style="display:flex; gap:28px">{pts}</div>'
      f'<p style="font-size:28px; color:{BLUE}; font-weight:600">{e(nv["bas"])}</p>')
    return slide("nouvelle", PAPER, INK, inner, extra="gap:36px", foot=footer(w))

def s_labo(w):
    lb = w["labo"]
    cols = [GOLD, "#F2D9A8", PAPER]
    steps = "".join(f'<div style="flex:1; display:flex; flex-direction:column; gap:14px; padding:32px; border:2px solid rgba(245,239,227,.35); border-radius:12px"><p style="font-family:{SERIF}; font-size:44px; font-weight:700; color:{c}">{i}. {e(k)}</p><p style="font-size:30px; line-height:1.4">{e(v)}</p></div>' for i,((k,v),c) in enumerate(zip(lb["steps"],cols),1))
    inner = head("Labo IA · l'Atelier du siècle", lb["title"], col=GOLD) + (
      f'<div style="display:flex; gap:28px">{steps}</div>'
      f'<p style="font-size:30px; line-height:1.4"><span style="color:{GOLD}; font-weight:700">À déposer :</span> {e(lb["produit"])}</p>'
      f'<p style="font-family:{HAND}; font-size:44px; color:#F2D9A8">L\'IA propose, le lecteur vérifie, l\'auteur, c\'est vous.</p>')
    return slide("labo", INK, PAPER, inner, extra="gap:40px", foot=footer(w))

def s_italia(w):
    rows = "".join(f'<div style="display:flex; gap:36px; align-items:baseline; padding:26px 0; border-bottom:1px solid {LINE}"><p style="flex:none; width:300px; font-family:{SERIF}; font-size:44px; font-weight:700; color:{BLUE}">{e(k)}</p><p style="font-size:32px; line-height:1.4">{e(v)}</p></div>' for k,v in w["italia"])
    inner = head("Ponte con l'Italia", "La même époque, de l'autre côté des Alpes", col=BLUE) + f'<div>{rows}</div>'
    return slide("italia", PAPER2, INK, inner, foot=footer(w))

def s_bilan(w):
    av = "".join(f'<li>{e(x)}</li>' for x in w["avant"])
    an = "".join(f'<li>{e(x)}</li>' for x in w["anthologie"])
    nxt = "Et après le cours" if w["n"] == 8 else f"Pour la semaine {w['n']+1}"
    inner = head("Bilan et suite", nxt, col=GOLD) + (
      f'<div style="display:flex; gap:32px; flex:1">'
      f'<div style="flex:1; display:flex; flex-direction:column; gap:16px"><p style="font-size:24px; font-weight:700; color:{GOLD}">À LIRE</p><ul style="font-size:30px; line-height:1.4; display:flex; flex-direction:column; gap:14px">{av}</ul>'
      f'<p style="font-size:24px; font-weight:700; color:{GOLD}; margin-top:18px">MA PRODUCTION</p><p style="font-size:30px; line-height:1.4">{e(w["production"])}</p></div>'
      f'<div style="flex:1; display:flex; flex-direction:column; gap:16px; padding:32px; border:2px solid rgba(245,239,227,.35); border-radius:12px"><p style="font-size:24px; font-weight:700; color:{GOLD}">POUR MON ANTHOLOGIE (A.2)</p><ul style="font-size:28px; line-height:1.4; display:flex; flex-direction:column; gap:12px">{an}</ul>'
      f'<p style="font-size:24px; color:#BDB3C4; margin-top:auto">Rappel de la fiche : la liste A.2 ne reprend pas les œuvres A.1 ni les nouvelles de la partie B.</p></div></div>')
    return slide("bilan", INK, PAPER, inner, extra="gap:36px", foot=footer(w))

# ------------------------------------------------------------------ raw slides from old site
def old_slides(n):
    h = open(os.path.join(OLD, f"s{n}.html"), encoding="utf-8").read()
    notes = json.loads(re.search(r"const NOTES=(\[.*?\]);", h, re.S).group(1))
    secs = re.findall(r'(<section class="slide" id="([^"]+)".*?</section>)', h, re.S)
    return {sid: (sec, notes[i]) for i, (sec, sid) in enumerate(secs)}

def s_critique(w, ar):
    ids = "".join(f'<div style="display:flex; gap:24px; align-items:baseline; padding:14px 0; border-bottom:1px solid {LINE}"><p style="flex:none; width:200px; font-size:24px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:{BLUE}">{e(k)}</p><p style="font-size:28px; line-height:1.38">{e(v)}</p></div>' for k,v in ar["idees"])
    cits = "".join(f'<div style="display:flex; flex-direction:column; gap:8px"><p style="font-family:{SERIF}; font-style:italic; font-size:34px; line-height:1.3">« {e(c)} »</p><p style="font-size:22px; color:{MUTE}">{e(ar["auteur"])}, {e(p)}</p></div>' for c,p in ar["citations"])
    inner = head(f"Lecture critique · {ar['auteur']}", ar["titre"]) + (
      f'<div style="display:flex; gap:48px; flex:1">'
      f'<div style="flex:1.25">{ids}</div>'
      f'<div style="flex:1; display:flex; flex-direction:column; gap:28px; background:{CARD}; border-left:8px solid {WINE}; border-radius:12px; padding:32px">{cits}'
      f'<p style="margin-top:auto; font-size:26px; line-height:1.35; color:{WINE}; font-weight:600">À discuter : {e(ar["debat"])}</p></div></div>'
      f'<p style="font-size:20px; color:{MUTE}">{e(ar["ref"])}</p>')
    return slide(f"critique-{ar['id']}", PAPER, INK, inner, extra="gap:30px", foot=footer(w))

def s_critique_frise(w, ar):
    cells = "".join(f'<div style="flex:1; display:flex; flex-direction:column; gap:10px; padding-right:18px"><p style="font-family:{SERIF}; font-size:40px; font-weight:700; color:{GOLD if b else "#F2D9A8"}">{e(y)}</p><p style="font-size:26px; line-height:1.3">{e(t)}</p></div>' for y,t,b in ar["frise"])
    inner = head(f"Lecture critique · {ar['auteur']}", ar["frise_titre"], col=GOLD) + (
      f'<div style="display:flex; border-top:6px solid {GOLD}; padding-top:32px">{cells}</div>'
      f'<p style="font-family:{HAND}; font-size:44px; color:#F2D9A8">{e(ar["frise_bas"])}</p>')
    return slide(f"critique-{ar['id']}-frise", INK, PAPER, inner, foot=footer(w))

SLIDE_IDS = ["cover","objectifs","seances","enigme","frise","auteurs","outil","texte1","texte2","methode","nouvelle","labo","italia","bilan"]

def deck(w):
    n = w["n"]
    s = [s_cover(w), s_objectifs(w), s_seances(w), s_enigme(w), s_frise(w), s_auteurs(w), s_outil(w),
         s_texte(w,0), s_texte(w,1), s_methode(w), s_nouvelle(w), s_labo(w), s_italia(w), s_bilan(w)]
    ids = list(SLIDE_IDS)
    crit_s, crit_i = [], []
    for ar in ARTICLES.get(n, []):
        crit_s.append(s_critique(w, ar)); crit_i.append(f"critique-{ar['id']}")
        if ar.get("frise"):
            crit_s.append(s_critique_frise(w, ar)); crit_i.append(f"critique-{ar['id']}-frise")
    s[7:7] = crit_s; ids[7:7] = crit_i
    nd = NOTES.get(n, {})
    base = dict(zip(SLIDE_IDS, w["notes"]))
    notes = [nd.get(i) or base.get(i) or "" for i in ids]
    missing = [i for i,x in zip(ids,notes) if not x]
    assert not missing, (n, missing)
    old = old_slides(n) if (w.get("raw_after_cover") or w.get("raw_after_outil")) else {}
    if w.get("raw_after_cover"):
        for j, sid in enumerate(w["raw_after_cover"]):
            sec, nt = old[sid]; s.insert(1+j, sec); notes.insert(1+j, nt)
    if w.get("raw_after_outil"):
        pos = 7 + len(w.get("raw_after_cover", [])) + len(crit_s)
        for j, sid in enumerate(w["raw_after_outil"]):
            sec, nt = old[sid]
            sec = re.sub(r"Semaine 8 · [^<]*· UniCT 2026", e(footer(w)), sec)
            s.insert(pos+j, sec); notes.insert(pos+j, nt)
    return s, notes

# ------------------------------------------------------------------ page shell
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..800;1,400..700&family=Source+Sans+3:wght@400;600;700&family=Caveat:wght@500;700&display=swap">')
def shell(title, desc, active, body):
    nav = (f'<a href="index.html"{" aria-current=page" if active=="home" else ""}>Accueil</a>'
           f'<a href="s1.html"{" aria-current=page" if active=="week" else ""}>Semaines</a>'
           f'<a href="carnet.html"{" aria-current=page" if active=="carnet" else ""}>Carnet</a>'
           f'<a href="{APP}" target=_blank rel=noopener>Atelier du siècle ↗</a>')
    return (f'<!doctype html>\n<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
            f'<title>{e(title)}</title><meta name="description" content="{a(desc)}">{FONTS}\n<link rel="stylesheet" href="site.css"></head><body>'
            f'<header class="bar"><a class="logo" href="index.html">Catania · <i>Lettres 1780–1930</i></a><nav>{nav}</nav></header>{body}'
            f'<footer class="foot">Gökhan Dinar · Visiting Professor, DISUM, Università di Catania · automne 2026 · {e(COURSE)} (L-LIN/03)</footer></body></html>')

JS = """<script>
const NOTES=%s;
const frames=[...document.querySelectorAll('.frame')];let i=0;
function fit(){const w=document.getElementById('stage').clientWidth;document.querySelectorAll('.scaler').forEach(s=>s.style.transform='scale('+(w/1920)+')');document.getElementById('stage').style.height=(w*1080/1920)+'px';}
function show(k){i=Math.max(0,Math.min(frames.length-1,k));frames.forEach((f,j)=>f.hidden=j!==i);document.getElementById('count').textContent=(i+1)+' / '+frames.length;const n=document.getElementById('notes');n.textContent=NOTES[i]||'Pas de note pour cette diapositive.';try{history.replaceState(null,'','#'+(i+1))}catch(e){}}
document.getElementById('prev').onclick=()=>show(i-1);document.getElementById('next').onclick=()=>show(i+1);
document.addEventListener('keydown',e=>{if(e.target.tagName==='INPUT'||e.target.tagName==='SUMMARY')return;if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();show(i+1)}if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();show(i-1)}});
document.getElementById('stage').addEventListener('click',e=>{const r=e.currentTarget.getBoundingClientRect();show(e.clientX-r.left>r.width/3?i+1:i-1)});
let x0=null;document.getElementById('stage').addEventListener('touchstart',e=>x0=e.touches[0].clientX,{passive:true});document.getElementById('stage').addEventListener('touchend',e=>{if(x0===null)return;const d=e.changedTouches[0].clientX-x0;if(Math.abs(d)>40)show(d<0?i+1:i-1);x0=null});
document.getElementById('shownotes').onchange=e=>{document.getElementById('notes').hidden=!e.target.checked;try{localStorage.setItem('notes',e.target.checked?'1':'')}catch(_){}};
try{if(localStorage.getItem('notes')==='1'){document.getElementById('shownotes').checked=true;document.getElementById('notes').hidden=false}}catch(_){}
document.getElementById('fs').onclick=()=>{const s=document.getElementById('stage');(s.requestFullscreen||s.webkitRequestFullscreen||(()=>{})).call(s)};
document.addEventListener('fullscreenchange',()=>setTimeout(fit,50));
window.addEventListener('resize',fit);fit();show((parseInt(location.hash.slice(1))||1)-1);
</script>"""

def route(w):
    ob = "".join(f"<li>{e(o)}</li>" for o in w["objectifs"])
    pr = "".join(f'<li><b>{e(t)}</b> {e(x)}</li>' for t,x in w["prog"])
    av = "".join(f"<li>{e(x)}</li>" for x in w["avant"])
    an = "".join(f"<li>{e(x)}</li>" for x in w["anthologie"])
    se = "".join(f'<li><b>Séance {k}</b> {e(t)} : {e(x)}</li>' for k,(t,x) in zip("ABC", w["seances"]))
    nxt = "Après le cours" if w["n"]==8 else f"Avant la semaine {w['n']+1}"
    return (f'<section class="route" aria-label="Feuille de route de la semaine {w["n"]}">'
      f'<div class="rc"><h2>Je peux…</h2><ul class="checks">{ob}</ul></div>'
      f'<div class="rc"><h2>Dans la fiche du cours</h2><ul>{pr}</ul></div>'
      f'<div class="rc"><h2>Les trois séances</h2><ul>{se}</ul></div>'
      f'<div class="rc"><h2>{e(nxt)}</h2><ul>{av}</ul><p class="prod"><b>Ma production :</b> {e(w["production"])}</p></div>'
      f'<div class="rc"><h2>Pour mon anthologie (A.2)</h2><ul>{an}</ul></div>'
      f'<div class="rc ia"><h2>Labo IA</h2><p><b>{e(w["labo"]["title"])}</b></p><ol>' + "".join(f"<li><b>{e(k)}</b> {e(v)}</li>" for k,v in w["labo"]["steps"]) + f'</ol><p><a href="{APP}" target=_blank rel=noopener>Ouvrir l\'Atelier du siècle ↗</a></p></div>'
      + "".join(f'<div class="rc crit"><h2>Lecture critique</h2><p><b>{e(ar["court"])}</b></p><p>{e(ar["route"])}</p><p class="small">{e(ar["ref"])} <a href="{a(ar["lien"])}" target=_blank rel=noopener>Cairn ↗</a></p></div>' for ar in ARTICLES.get(w["n"], []))
      + f'</section>')

def week_page(w):
    slides, notes = deck(w)
    frames = "".join(f'<div class="frame" data-i="{i}"{" hidden" if i else ""}><div class="scaler">{s}</div></div>' for i, s in enumerate(slides))
    tabs = "".join(f'<a href="s{x["n"]}.html"{" aria-current=page" if x["n"]==w["n"] else ""} title="{a(x["title"])}">S{x["n"]}</a>' for x in WEEKS)
    aud = "".join(f"<p>{e(p)}</p>" for p in w["audio"])
    prev = f'<a href="s{w["n"]-1}.html">← Semaine {w["n"]-1}</a>' if w["n"]>1 else '<a href="index.html">← Accueil</a>'
    nxt = f'<a href="s{w["n"]+1}.html">Semaine {w["n"]+1} →</a>' if w["n"]<8 else '<a href="carnet.html">Carnet →</a>'
    body = (f'<main class="deckpage"><div class="weektabs" aria-label="Semaines">{tabs}</div>'
      f'<div class="deckhead"><p class="eyebrow">Semaine {w["n"]} · {e(w["dates"])} 2026 · {e(w["period"])}</p><h1>{e(w["title"])}</h1><p class="sub">{e(w["sub"])}</p></div>'
      + route(w) +
      f'<section class="audio" aria-label="Résumé audio de la semaine {w["n"]}"><div class="audio-head"><p class="eyebrow">Résumé audio · environ 1 min 30</p><audio controls preload="none" src="audio/s{w["n"]}.mp3">Votre navigateur ne lit pas l\'audio : <a href="audio/s{w["n"]}.mp3">télécharger le MP3</a>.</audio></div><details><summary>Lire la transcription</summary>{aud}</details><p class="audio-note">Voix de synthèse : en cas de doute sur une prononciation, le texte écrit fait foi.</p></section>'
      f'<h2 class="deckt">La présentation</h2>'
      f'<div class="stage" id="stage" tabindex="0" aria-label="Présentation, flèches pour naviguer">{frames}</div>'
      '<div class="controls"><button id="prev" aria-label="Diapositive précédente">←</button><span id="count" class="count"></span><button id="next" aria-label="Diapositive suivante">→</button><span class="spacer"></span><label class="tog"><input type="checkbox" id="shownotes"> Notes de l\'enseignant</label><button id="fs">Plein écran</button></div>'
      f'<div class="notes" id="notes" hidden></div><div class="pager">{prev}{nxt}</div></main>'
      + JS % json.dumps(notes, ensure_ascii=False))
    page = shell(f"S{w['n']} · {w['title']} · Catania 2026", f"Semaine {w['n']} du cours de littérature française, Université de Catane : {w['title']}.", "week", body)
    open(os.path.join(OUT, f"s{w['n']}.html"), "w", encoding="utf-8").write(page)
    return len(slides)

# ------------------------------------------------------------------ A.1 / B map
A1 = [("1","Recueil de poèmes","Lamartine, Méditations poétiques (1820)",2,"René Vivien, Études et préludes",7),
      ("2","Poème long","Rimbaud, Le Bateau ivre (1871)",6,"Cendrars, Prose du Transsibérien (1913)",8),
      ("3","Poèmes en prose","Baudelaire, Le Spleen de Paris (1869)",4,"Gide, Les Nourritures terrestres (1897)",7),
      ("4","Manifeste littéraire","Moréas, Le Symbolisme (1886)",6,"Marinetti, Manifeste du futurisme (1909)",8),
      ("5","Théâtre","Wilde, Salomé (1891–1893)",7,"Jarry, Ubu Roi (1896)",7),
      ("6","Roman bref","Alain-Fournier, Le Grand Meaulnes (1913)",8,"Gide, Les Caves du Vatican (1914)",8)]
B = [("Qu'est-ce qu'une nouvelle ? Grojnowski, Schaeffer",1),("Mérimée, Mateo Falcone",2),("Gautier, La Morte amoureuse",3),
     ("Flaubert, Un cœur simple",4),("Les Soirées de Médan ; Maupassant, Boule de suif, Le Horla",5),
     ("Barbey d'Aurevilly, Les Diaboliques ; Daudet, La Dernière Classe",5),("Villiers de l'Isle-Adam, Véra (Contes cruels)",6)]
def wl(n): return f'<a href="s{n}.html">S{n}</a>'
def a1_table():
    r = "".join(f'<tr><td>{p}</td><td>{e(g)}</td><td>{e(x)} · {wl(xn)}</td><td>{e(y)} · {wl(yn)}</td></tr>' for p,g,x,xn,y,yn in A1)
    return f'<table><thead><tr><th>Paire</th><th>Genre</th><th>Œuvre</th><th>ou</th></tr></thead><tbody>{r}</tbody></table>'
def b_table():
    r = "".join(f'<tr><td>{e(t)}</td><td>{wl(n)}</td></tr>' for t,n in B)
    return f'<table><thead><tr><th>Partie B : la nouvelle au XIXe siècle</th><th>Semaine</th></tr></thead><tbody>{r}</tbody></table>'

def tagline(w):
    a1=sum(1 for t,_ in w["prog"] if t.startswith("A.1")); b=sum(1 for t,_ in w["prog"] if t.startswith("Partie B"))
    p=[]
    if a1: p.append(f"Liste A.1 : {a1} paire{'s' if a1>1 else ''}")
    if b: p.append("Partie B : nouvelle")
    return " · ".join(p) or "Contexte et méthode"

def index_page():
    cards = "".join(f'<a class="wk" href="s{w["n"]}.html"><span class="wn">{w["n"]}</span><span class="wd">{e(w["dates"])} · {e(w["period"])}</span><b>{e(w["title"])}</b><span class="ws">{e(w["sub"].split(" · ")[0])}</span><span class="wr">{e(w["recit"])}</span><span class="wa">{tagline(w)}</span></a>' for w in WEEKS)
    body = (f'<main class="home"><section class="hero"><p class="eyebrow">Università di Catania · DISUM · automne 2026</p>'
      '<h1>Du préromantisme<br><i>aux Années folles</i></h1>'
      '<p class="lead">Huit semaines pour lire la littérature française de Rousseau aux Années folles : un texte du programme travaillé de près, une nouvelle, une méthode de commentaire pas à pas, et un atelier où l\'IA propose et le lecteur vérifie.</p>'
      '<p class="hand">Qui a le pouvoir de dire ce qu\'est la bonne littérature ?</p>'
      '<p class="meta">Gökhan Dinar, Visiting Professor · du 12 octobre au 5 décembre 2026 · trois séances de 2 heures par semaine</p></section>'
      '<section class="how"><h2>Comment on travaille</h2><div class="howgrid">'
      '<div><b>Chaque semaine</b>Des objectifs clairs, les textes de la fiche du cours, trois séances (contexte, texte, nouvelle et IA) et une petite production à déposer sur Studium.</div>'
      '<div><b>La fiche du cours</b>Les six paires de la liste A.1, les nouvelles de la partie B et des extraits pour votre anthologie A.2 sont tous travaillés en classe, par extraits.</div>'
      '<div><b>L\'examen</b>Je ne fais pas passer l\'examen. Le cours vous y prépare : commentaire écrit en huit étapes, lecture expressive, traduction, contexte.</div>'
      '<div><b>Pour réviser</b>Un résumé audio d\'une minute et demie par semaine, avec sa transcription, et l\'Atelier du siècle pour s\'entraîner.</div>'
      '</div></section>'
      f'<h2>Les semaines</h2><div class="weeks">{cards}</div>'
      f'<h2>Le programme dans le cours</h2><p class="lead small">Pour la liste A.1, vous choisissez une œuvre dans chaque paire et vous la lisez en entier. En classe, nous lisons les deux par extraits.</p>'
      f'<div class="prose wide">{a1_table()}{b_table()}<p class="small">Liste A.2 : chaque semaine propose deux ou trois extraits (rubrique Pour mon anthologie) pour construire votre liste personnelle de 50 extraits, à faire valider avant l\'examen.</p></div>'
      + (f'<h2>Lectures critiques</h2><div class="prose wide"><ul>' + "".join(f'<li><a href="s{n}.html">Semaine {n}</a> · {e(ar["ref"])}</li>' for n in sorted(ARTICLES) for ar in ARTICLES[n]) + '</ul></div>' if ARTICLES else '')
      + '<h2>Outils du cours</h2><div class="toolgrid">'
      f'<a class="tool" href="{APP}" target=_blank rel=noopener><b>L\'Atelier du siècle ↗</b><span>Dialoguer avec des écrivains de 1802 à 1924 et faire relire son commentaire selon la grille du cours. Fonctionne sur claude.ai ou dans l\'application Claude, connecté à son compte.</span></a>'
      '<a class="tool" href="carnet.html"><b>Carnet de l\'enseignant</b><span>Déroulé des 24 séances avec les durées, correspondance avec la fiche du cours, points à confirmer.</span></a></div>'
      '<div class="charte"><div><b>Déclarer</b>Tout travail rendu indique ce que l\'IA a fait et ce que vous avez fait.</div><div><b>Vérifier</b>Chaque date, chaque citation, chaque attribution se contrôle dans l\'édition.</div><div><b>Écrire soi-même</b>Aucun texte généré n\'est rendu tel quel. Votre lecture reste la vôtre.</div><div><b>Rester critique</b>Les auteurs simulés sont des hypothèses de lecture, pas des témoins.</div></div>'
      '</main>')
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(shell("Du préromantisme aux Années folles · Catania 2026", "Site du cours de littérature française de Gökhan Dinar à l'Université de Catane, automne 2026.", "home", body))

def biblio():
    items = "".join(f'<li>S{n} · {e(ar["ref"])} <a href="{a(ar["lien"])}" target=_blank rel=noopener>lien</a></li>' for n in sorted(ARTICLES) for ar in ARTICLES[n])
    return f'<h2>Bibliothèque critique du cours</h2><p>Articles et chapitres ajoutés au fil des semaines, utilisés dans les présentations (diapositive Lecture critique) et dans les notes.</p><ul>{items}</ul>' if items else ""

def carnet_page():
    cal = "".join(f'<tr><td>{w["n"]}</td><td>{e(w["dates"])}</td><td><a href="s{w["n"]}.html">{e(w["title"])}</a></td><td>{e("; ".join(x for t,x in w["prog"] if not t.startswith("A.2")))}</td><td>{w["methode"][0]}. {e(w["methode"][1])}</td></tr>' for w in WEEKS)
    weeks = ""
    for w in WEEKS:
        c = w["carnet"]
        weeks += (f'<h2 id="s{w["n"]}">Semaine {w["n"]} · {e(w["title"])} ({e(w["dates"])})</h2>'
          f'<p><strong>Objectif :</strong> {e(c["objectif"])} <a href="s{w["n"]}.html">Présentation S{w["n"]}</a></p>'
          f'<p><strong>Séance A.</strong> {e(c["A"])}</p><p><strong>Séance B.</strong> {e(c["B"])}</p><p><strong>Séance C.</strong> {e(c["C"])}</p>'
          f'<p><strong>À anticiper.</strong> {e(c["anticiper"])}</p>'
          f'<p><strong>Production des étudiants.</strong> {e(w["production"])}</p>'
          + "".join(f'<p><strong>Lecture critique.</strong> {e(ar["ref"])} Idées utilisées en classe : ' + "; ".join(e(k)+" ("+e(v)+")" for k,v in ar["idees"]) + f'. À discuter : {e(ar["debat"])}</p>' for ar in ARTICLES.get(w["n"], [])))
    body = (f'<main class="prose"><p class="eyebrow">Carnet de l\'enseignant · Catania 2026</p><h1>Carnet de l\'enseignant</h1><p class="sub">Gökhan Dinar · mis à jour le 5 octobre 2026</p>'
      '<h2>Architecture du cours</h2>'
      '<p>48 heures en 8 semaines, du 12 octobre au 5 décembre 2026, en trois séances de 2 heures par semaine. Le cours suit la fiche de Carminella Sipala (Laurea L11, L-LIN/03) : partie A, fondements du XIXe siècle et des vingt premières années du XXe, avec les six paires de la liste A.1 ; partie B, la nouvelle au XIXe siècle. La méthode est la mienne : la sociocritique comme lecture, l\'IA comme outil vérifié, une production par semaine.</p>'
      '<p><strong>Examen.</strong> Je ne fais pas passer l\'examen (écrit de commentaire puis oral, en français, selon la fiche). Le cours y prépare : méthode du commentaire en huit étapes, lecture expressive, traduction italienne, contexte, fiches A.1 et anthologie A.2. Deux ateliers de commentaire (semaines 5 et 8) reçoivent un retour écrit, sans note.</p>'
      '<p><strong>Principe de simplicité.</strong> Chaque semaine : quatre objectifs en je, deux textes à la loupe, un outil sociocritique en trois mots, une étape de méthode, une nouvelle ou une scène, un labo IA en trois gestes (demander, vérifier, améliorer).</p>'
      '<h2>Rythme d\'une semaine</h2><table><thead><tr><th>Séance</th><th>Contenu</th></tr></thead><tbody>'
      '<tr><td>A · Contexte</td><td>énigme, frise, auteurs, outil sociocritique, premier texte</td></tr>'
      '<tr><td>B · Atelier du texte</td><td>texte du programme, lecture expressive, traduction, étape de méthode</td></tr>'
      '<tr><td>C · Nouvelle et IA</td><td>nouvelle de la partie B, labo IA, pont italien, devoirs</td></tr></tbody></table>'
      f'<h2>Calendrier</h2><table><thead><tr><th>S</th><th>Dates</th><th>Titre</th><th>Fiche du cours</th><th>Méthode</th></tr></thead><tbody>{cal}</tbody></table>'
      f'<h2>Correspondance avec la fiche</h2>{a1_table()}{b_table()}'
      '<p>Liste A.2 : la rubrique Pour mon anthologie propose chaque semaine des extraits hors A.1 et hors partie B. Références de la fiche reprises dans le cours : Brunel et al., Histoire de la littérature française, t. 2 (Bordas) ; Lagarde et Michard ; Bergez, L\'Explication de texte littéraire ; Grojnowski, Lire la nouvelle ; Schaeffer, Qu\'est-ce qu\'un genre littéraire ? Références propres : Duchet, Bourdieu (Les Règles de l\'art), Zima, M. Juan, J.-Y. Le Naour.</p>'
      + biblio() + weeks +
      '<h2>Points à confirmer avec Prof. Rizzo</h2><ul>'
      '<li class="todo">Volume horaire définitif : 48 h (plan actuel) ou programme élargi.</li>'
      '<li class="todo">Qui organise l\'écrit et l\'oral, et à quelles dates.</li>'
      '<li class="todo">Contenu de la première semaine assurée par Carminella Sipala.</li>'
      '<li class="todo">Accès des étudiants à claude.ai en classe.</li>'
      '<li class="todo">Diffusion du lien du site sur Studium.</li></ul>'
      '<h2>Détails à vérifier dans les éditions</h2><ul>'
      '<li>René Vivien, Études et préludes : la fiche indique 1902, l\'édition originale (Lemerre) est généralement datée de 1901.</li>'
      '<li>Le Lac : ponctuation de la strophe du temps selon l\'édition utilisée.</li>'
      '<li>Gautier à Hernani : gilet rouge dans la tradition, pourpoint rose dans son Histoire du romantisme.</li>'
      '<li>Droits : Cendrars, Breton, Maran, Morand ne sont pas dans le domaine public ; citations courtes seulement sur Studium.</li></ul>'
      '</main>')
    open(os.path.join(OUT, "carnet.html"), "w", encoding="utf-8").write(shell("Carnet de l'enseignant · Catania 2026", "Carnet de l'enseignant : déroulé des séances, calendrier et correspondance avec la fiche du cours.", "carnet", body))

if __name__ == "__main__":
    counts = [week_page(w) for w in WEEKS]
    index_page(); carnet_page()
    json.dump({str(w["n"]): w["audio"] for w in WEEKS}, open(os.path.join(OUT, "_audio.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("slides per week:", counts)
