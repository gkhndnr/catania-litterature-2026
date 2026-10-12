# Semaine 1 · Seuils du siècle : présentation en deux séances de 1 h 45 (version du 12 octobre 2026,
# reprise de « Semaine 1 · Seuils du siècle.pptx »). 25 diapositives, notes dans s1_notes.json.
# Utilisé par build.py (deck() et slide_label() pour la semaine 1) et par s1_patch.py (mise à jour directe du site).
import html, json, os, re

INK, PAPER, PAPER2, CARD, LINE = "#1F1A24", "#F5EFE3", "#EDE4D3", "#FBF8F2", "#E2D8C6"
WINE, BLUE, GOLD, SOFT, MUTE = "#A1343C", "#2E6A8E", "#D9A441", "#4A4453", "#7A7282"
SERIF = "'Playfair Display', Georgia, serif"
SANS = "'Source Sans 3', Arial, sans-serif"
HAND = "'Caveat', 'Brush Script MT', cursive"
FOOT = "Semaine 1 · Seuils du siècle"
DARK = (INK, WINE, BLUE)

def nb(t):
    t = re.sub(r" ([?!;:»])", " \\1", t)
    return t.replace("« ", "« ")
def e(s):
    """Échappe, puis rétablit <i> et <b>."""
    t = nb(html.escape(s, quote=False))
    for tag in ("i", "b"):
        t = t.replace(f"&lt;{tag}&gt;", f"<{tag}>").replace(f"&lt;/{tag}&gt;", f"</{tag}>")
    return t

def slide(sid, bg, inner, foot=None, pad="128px 128px 160px", gap="40px", justify=""):
    color = PAPER if bg in DARK else INK
    fc = "#BDB3C4" if bg == INK else ("#E9D6D2" if bg == WINE else ("#CFE0EA" if bg == BLUE else MUTE))
    f = (f'<p style="position:absolute; left:128px; bottom:60px; width:1664px; font-size:24px; color:{fc}">{e(foot)}</p>' if foot else "")
    j = f" justify-content:{justify};" if justify else ""
    return (f'<section class="slide" id="{sid}" style="background:{bg}; color:{color}; font-family:{SANS}; '
            f'padding:{pad}; display:flex; flex-direction:column; gap:{gap};{j}">\n{inner}\n{f}\n</section>')

def eyebrow(t, col=WINE):
    return f'<p style="font-size:24px; letter-spacing:4px; text-transform:uppercase; font-weight:700; color:{col}">{e(t)}</p>'

def head(eb, title, col=WINE, size=72):
    return (f'<div style="display:flex; flex-direction:column; gap:12px">{eyebrow(eb, col)}'
            f'<h2 style="font-family:{SERIF}; font-size:{size}px; font-weight:700; line-height:1.1">{e(title)}</h2></div>')

def hand(t, col, size=52, rot=-1.5):
    return f'<p style="font-family:{HAND}; font-size:{size}px; line-height:1.15; color:{col}; transform:rotate({rot}deg); transform-origin:left">{e(t)}</p>'

def card(inner, top=WINE, bg=CARD, pad="32px 36px", flex="flex:1", color=INK):
    return (f'<div style="{flex}; display:flex; flex-direction:column; gap:14px; background:{bg}; color:{color}; padding:{pad}; '
            f'border-top:8px solid {top}; border-radius:12px">{inner}</div>')

def img(src, w, h, alt, border=None):
    b = f" border:6px solid {border};" if border else ""
    return (f'<img src="img/s1/{src}.jpg" alt="{html.escape(alt, quote=True)}" loading="lazy" '
            f'style="width:{w}px; height:{h}px; object-fit:cover; object-position:50% 20%; border-radius:10px;{b} display:block">')

def label_row(k, v, kw=180, kcol=BLUE, size=28):
    return (f'<div style="display:flex; gap:24px; align-items:baseline; padding:12px 0; border-bottom:1px solid {LINE}">'
            f'<p style="flex:none; width:{kw}px; font-size:24px; font-weight:700; letter-spacing:1px; color:{kcol}">{e(k)}</p>'
            f'<p style="flex:1; font-size:{size}px; line-height:1.38">{e(v)}</p></div>')

# ------------------------------------------------------------------ diapositives
def s01():
    inner = (f'<div style="position:absolute; left:1312px; top:0; width:608px; height:1080px; border-left:8px solid {WINE}">'
             f'<img src="img/s1/friedrich.jpg" alt="Caspar David Friedrich, Le Voyageur contemplant une mer de nuages" style="width:100%; height:100%; object-fit:cover; object-position:50% 30%; display:block"></div>'
             f'<div style="width:1120px; display:flex; flex-direction:column; gap:28px">'
             + eyebrow("Semaine 1 · 12–16 octobre 2026 · deux séances de 1 h 45", GOLD)
             + f'<h1 style="font-family:{SERIF}; font-size:120px; font-weight:700; line-height:1.02">Seuils du siècle</h1>'
             + f'<p style="font-size:40px; font-style:italic; line-height:1.3; color:#E4DCE8">Rousseau, Bernardin, Chateaubriand, Staël, Constant · 1782–1820</p>'
             + hand("Levez-vous vite, orages désirés…", GOLD, 64, -3) + '</div>'
             f'<div style="width:1120px; display:flex; flex-direction:column; gap:8px">'
             f'<p style="font-size:30px; font-weight:700">Letteratura francese dal Preromanticismo a Les années folles</p>'
             f'<p style="font-size:24px; color:#BDB3C4">Gökhan Dinar · Visiting Professor · DISUM, Università di Catania</p>'
             f'<p style="font-size:22px; color:#9A90A3">Image : C. D. Friedrich, <i>Le Voyageur contemplant une mer de nuages</i>, v. 1817</p></div>')
    return slide("cover", INK, inner, pad="128px", justify="space-between", gap="0")

def s02():
    def seance(eb, t, d, col):
        return card(f'<p style="font-size:24px; letter-spacing:3px; text-transform:uppercase; font-weight:700; color:{col}">{e(eb)}</p>'
                    f'<p style="font-family:{SERIF}; font-size:44px; font-weight:700; line-height:1.15">{e(t)}</p>'
                    f'<p style="font-size:28px; line-height:1.4; color:{SOFT}">{e(d)}</p>', top=col, pad="36px 40px")
    inner = (head("La semaine en deux séances", "Situer d'abord, lire ensuite")
             + '<div style="display:flex; gap:40px">'
             + seance("Séance 1 · 1 h 45", "Se rencontrer, situer", "Présentations · l'énigme du mal du siècle · la frise 1782–1820 · galerie de sept voix · Dossier, partie 1", WINE)
             + seance("Séance 2 · 1 h 45", "Lire à la loupe", "Dire, Former, Taire · Rousseau et René · deux isotopies · la nouvelle · labo IA · Dossier, parties 2 et 3", BLUE)
             + '</div>'
             + f'<div style="display:flex; flex-direction:column; gap:14px; padding-top:8px">{eyebrow("À la fin de la semaine, je peux…", INK)}'
             + f'<p style="font-size:30px; line-height:1.45">situer le préromantisme · repérer qui dit <i>je</i> · définir la nouvelle · relever une isotopie · utiliser l\'IA selon la charte</p></div>')
    return slide("seances", PAPER, inner, foot=FOOT + " · UniCT 2026")

def s03():
    rows = [("2011", "Licence de langue et littérature françaises, Université Atatürk (Erzurum)"),
            ("2017", "Master de traduction et d'interprétation, Université technique Yıldız (Istanbul)"),
            ("2025", "Doctorat, Université Pamukkale : lecture sociocritique de la trilogie de Leïla Slimani"),
            ("2026", "Maître de conférences en didactique du FLE, Université d'Istanbul-Cerrahpaşa")]
    tl = "".join(f'<div style="display:flex; gap:24px; align-items:baseline"><p style="flex:none; width:130px; font-family:{SERIF}; font-size:42px; font-weight:700; color:{WINE}">{y}</p>'
                 f'<p style="font-size:30px; line-height:1.35">{e(t)}</p></div>' for y, t in rows)
    ch = "".join(f'<p style="font-size:29px; line-height:1.35">{e(t)}</p>' for t in
                 ("<b>Sociocritique</b> du roman francophone", "<b>IA et FLE</b> : lire avec la machine, et contre elle", "<b>Traduction</b> et champ, avec Bourdieu"))
    inner = (head("Présentations · qui vous parle ?", "Gökhan Dinar, lecteur entre deux rives")
             + f'<div style="display:flex; gap:56px; align-items:flex-start"><div style="flex:1; display:flex; flex-direction:column; gap:22px">{tl}</div>'
             + f'<div style="width:540px; flex:none; display:flex; flex-direction:column; gap:18px; background:{INK}; color:{PAPER}; padding:40px; border-radius:12px">'
             + f'<p style="font-size:24px; letter-spacing:3px; text-transform:uppercase; font-weight:700; color:{GOLD}">Trois chantiers</p>{ch}</div></div>'
             + hand("Istanbul, puis Catane : deux seuils entre l'Orient et l'Europe.", WINE, 50))
    return slide("moi", PAPER2, inner, foot=FOOT + " · UniCT 2026")

def s04():
    items = "".join(f'<div style="display:flex; gap:24px; align-items:baseline"><p style="flex:none; width:56px; font-family:{SERIF}; font-size:44px; font-weight:700; color:{GOLD}">{k}</p>'
                    f'<p style="font-size:38px; line-height:1.3">{e(t)}</p></div>' for k, t in
                    (("1", "Votre prénom et votre année"), ("2", "Un livre lu en entier, dans la langue de votre choix"), ("3", "Un mot, italien ou français, qui évoque pour vous le XIXe siècle")))
    inner = (head("Et vous ? · tour de table, 1 minute chacun", "Un prénom, un livre, un mot", col=GOLD, size=88)
             + f'<div style="display:flex; flex-direction:column; gap:22px">{items}</div>'
             + hand("Va bene anche in italiano, per cominciare…", "#F2D9A8", 60))
    return slide("vous", WINE, inner, pad="128px", justify="center")

def s05():
    inner = (eyebrow("L'énigme de la semaine", GOLD)
             + f'<h2 style="font-family:{SERIF}; font-size:84px; font-weight:700; line-height:1.12; max-width:1600px">Pourquoi toute une jeunesse européenne souffre-t-elle du même mal vers 1800&nbsp;?</h2>'
             + f'<p style="font-size:34px; line-height:1.45; max-width:1500px; color:#F3E3E0">Rousseau, Chateaubriand, Goethe, Foscolo : partout en Europe, de jeunes héros doués, sensibles, qui ne trouvent pas leur place.</p>'
             + hand("le mal du siècle, avant le siècle…", "#F2D9A8", 64))
    return slide("enigme", WINE, inner, pad="128px", justify="center", gap="36px")

def s06():
    ev = [("1782", "Rousseau, <i>Rêveries du promeneur solitaire</i> (posthume)", 0), ("1788", "Bernardin de Saint-Pierre, <i>Paul et Virginie</i>", 0),
          ("1793", "La Convention supprime les académies (8 août)", 1), ("1802", "Chateaubriand, <i>René</i>, dans le <i>Génie du christianisme</i>", 0),
          ("1804", "Napoléon empereur : la censure s'installe", 1), ("1813", "Staël, <i>De l'Allemagne</i>, publié à Londres", 0),
          ("1816", "Constant, <i>Adolphe</i>, publié à Londres et à Paris", 0)]
    cells = "".join(f'<div style="flex:1; display:flex; flex-direction:column; gap:12px; border-top:6px solid {WINE if p else BLUE}; padding:22px 16px 0 0">'
                    f'<p style="font-family:{SERIF}; font-size:44px; font-weight:700; color:{WINE if p else BLUE}">{y}</p>'
                    f'<p style="font-size:26px; line-height:1.3">{e(t)}</p></div>' for y, t, p in ev)
    inner = (head("Frise · 1782–1816", "Trente ans pour changer de monde")
             + f'<div style="display:flex; gap:12px">{cells}</div>'
             + f'<p style="font-size:26px"><b style="color:{WINE}">Rouge</b> : l\'histoire politique &nbsp;·&nbsp; <b style="color:{BLUE}">Bleu</b> : les œuvres</p>'
             + hand("Révolution, exil, Empire : trois mots à retenir.", WINE, 54))
    return slide("frise", PAPER, inner, foot=FOOT + " · UniCT 2026")

GAL = [("rousseau", "Rousseau", "1712–1778", 0), ("bernardin", "Bernardin", "1737–1814", 0), ("chateaubriand", "Chateaubriand", "1768–1848", 0),
       ("stael", "Staël", "1766–1817", 0), ("constant", "Constant", "1767–1830", 0), ("goethe", "Goethe", "1749–1832", 1), ("foscolo", "Foscolo", "1778–1827", 1)]
def s07():
    g = "".join(f'<div style="flex:1; display:flex; flex-direction:column; gap:10px">{img(f, 212, 290, n, GOLD if eu else None)}'
                f'<p style="font-size:28px; font-weight:700">{n}</p><p style="font-size:24px; color:#BDB3C4">{d}</p></div>' for f, n, d, eu in GAL)
    inner = (head("Galerie · les voix de la semaine", "Qui écrit, d'où, contre qui ?", col=GOLD)
             + f'<div style="display:flex; gap:28px">{g}</div>'
             + hand("Cinq voix françaises, deux voix d'Europe (cadre doré).", GOLD, 52))
    return slide("auteurs", INK, inner, foot=FOOT + " · UniCT 2026 · portraits : domaine public (Wikimedia Commons)")

VOIX = [
  ("voix-rousseau", "rousseau", "Maurice Quentin de La Tour, pastel, 1753", 1, "Jean-Jacques Rousseau", "1712–1778",
   [("D'où", "Genève, puis la France. L'<i>Émile</i> est brûlé en 1762 ; chassé, brouillé avec les philosophes, il écrit en reclus."),
    ("Œuvres", "<i>La Nouvelle Héloïse</i> (1761) · <i>Les Confessions</i> (posthumes) · <i>Les Rêveries</i> (écrites en 1776–1778, publiées en 1782)"),
    ("Invente", "Le moi seul face à la nature : la confidence devient littérature.")],
   ("quote", "« Me voici donc seul sur la terre… »", "")),
  ("voix-bernardin", "bernardin", "Rembrandt Peale, 1808", 2, "Bernardin de Saint-Pierre", "1737–1814",
   [("D'où", "Le Havre. Ingénieur et voyageur, il vit à l'île de France (Maurice) de 1768 à 1770 ; ami de Rousseau vieillissant."),
    ("Œuvres", "<i>Voyage à l'île de France</i> (1773) · <i>Études de la nature</i> (1784) · <i>Paul et Virginie</i> (1788)"),
    ("Invente", "L'idylle exotique : deux enfants, une île, une nature qui enseigne la vertu. L'esclavage reste à l'arrière-plan.")],
   ("quote", "« Elle avait lu <i>Paul et Virginie</i> et elle avait rêvé la maisonnette de bambous… »", "Flaubert, Madame Bovary")),
  ("voix-chateaubriand", "chateaubriand", "Anne-Louis Girodet, vers 1809", 3, "François-René de Chateaubriand", "1768–1848",
   [("D'où", "Saint-Malo, cadet noble et ruiné. Amérique (1791), armée des émigrés, puis exil et misère à Londres (1793–1800)."),
    ("Œuvres", "<i>Atala</i> (1801) · <i>Génie du christianisme</i>, avec <i>René</i> (1802) · <i>Mémoires d'outre-tombe</i> (posthumes)"),
    ("Invente", "Le héros mélancolique et le « vague des passions ».")],
   ("quote", "« On habite avec un cœur plein un monde vide… »", "")),
  ("voix-stael", "stael", "D'après François Gérard, portrait posthume", 4, "Germaine de Staël", "1766–1817",
   [("D'où", "Paris, fille du ministre Necker, femme de salon. Opposée à Napoléon, éloignée de Paris dès 1803 : Coppet, l'Allemagne, l'Italie."),
    ("Œuvres", "<i>De la littérature</i> (1800) · <i>Corinne ou l'Italie</i> (1807) · <i>De l'Allemagne</i> (pilonné en 1810, Londres 1813)"),
    ("Apporte", "La littérature comme produit d'une société ; elle ouvre la France aux littératures du Nord.")],
   ("quote", "« … la poésie romantique comme celle qui tient de quelque manière aux traditions chevaleresques. »", "")),
  ("voix-constant", "constant", "Lina Vallier, 1847 (posthume)", 5, "Benjamin Constant", "1767–1830",
   [("D'où", "Lausanne, protestant. Compagnon de Staël à Coppet ; écarté par Bonaparte, puis député libéral sous la Restauration."),
    ("Œuvres", "<i>Adolphe</i> (écrit en 1806, publié en 1816) · <i>De la liberté des Anciens comparée à celle des Modernes</i> (1819)"),
    ("Apporte", "Le roman d'analyse : un amour qui s'use, disséqué de l'intérieur par celui qui ne sait plus aimer.")],
   ("hand", "Après René qui rêve, Adolphe qui s'analyse.", "")),
]
def s_voix(v):
    sid, f, cap, k, name, dates, rows, (kind, q, src) = v
    big = 64 if len(name) < 26 else 58
    rows_h = "".join(label_row(a_, b_, kw=150, kcol=BLUE, size=28) for a_, b_ in rows)
    if kind == "quote":
        end = (f'<p style="font-family:{SERIF}; font-style:italic; font-size:34px; line-height:1.3">{e(q)}</p>'
               + (f'<p style="font-size:24px; color:{MUTE}">{e(src)}</p>' if src else ""))
    else:
        end = hand(q, WINE, 52)
    inner = (f'<div style="display:flex; gap:72px; flex:1">'
             f'<div style="flex:none; width:500px; display:flex; flex-direction:column; gap:14px">{img(f, 500, 640, name)}'
             f'<p style="font-size:22px; color:{MUTE}">{e(cap)}</p></div>'
             f'<div style="flex:1; display:flex; flex-direction:column; gap:14px">'
             + eyebrow(f"Les voix · {k} sur 5")
             + f'<h2 style="font-family:{SERIF}; font-size:{big}px; font-weight:700; line-height:1.1">{e(name)}</h2>'
             + f'<p style="font-family:{SERIF}; font-size:40px; font-weight:700; color:{WINE}">{dates}</p>'
             + f'<div style="display:flex; flex-direction:column">{rows_h}</div>'
             + f'<div style="display:flex; flex-direction:column; gap:6px; padding-top:10px">{end}</div></div></div>')
    return slide(sid, PAPER2, inner, foot=FOOT + " · UniCT 2026", pad="128px 128px 150px")

def s13():
    def side(f, y, t, d, alt):
        return (f'<div style="flex:1; display:flex; gap:32px">{img(f, 300, 400, alt)}'
                f'<div style="display:flex; flex-direction:column; gap:12px"><p style="font-family:{SERIF}; font-size:46px; font-weight:700; color:{GOLD}">{y}</p>'
                f'<p style="font-size:36px; font-weight:700">{e(t)}</p><p style="font-size:28px; line-height:1.4; color:#E4DCE8">{e(d)}</p></div></div>')
    inner = (head("Ponte con l'Italia · et au-delà des Alpes", "Un même mal, d'autres patries", col=GOLD)
             + '<div style="display:flex; gap:56px">'
             + side("goethe", "1774", "Goethe, <i>Werther</i>", "Un jeune homme aime une femme promise à un autre et se tue. Le modèle européen.", "Goethe par Joseph Karl Stieler, 1828")
             + side("foscolo", "1802", "Foscolo, <i>Jacopo Ortis</i>", "La même année que <i>René</i> : un amour impossible et une patrie perdue, Venise cédée à l'Autriche.", "Foscolo par François-Xavier Fabre, 1813")
             + '</div>' + hand("René et Ortis côte à côte : deux douleurs, deux patries.", GOLD, 52))
    return slide("italia", INK, inner, foot=FOOT + " · UniCT 2026 · Stieler, 1828 · Fabre, 1813")

def s14():
    gr = "".join(card(f'<p style="font-size:24px; font-weight:700; color:{WINE}">{g}</p><p style="font-family:{SERIF}; font-size:40px; font-weight:700">{n}</p>', top=WINE, pad="26px 30px")
                 for g, n in (("Groupes 1 et 2", "Rousseau"), ("Groupes 3 et 4", "Bernardin"), ("Groupes 5 et 6", "Chateaubriand"), ("Groupes 7 et 8", "Staël")))
    qs = [("1. Qui écrit ?", "Origine, rang, métier"), ("2. D'où ?", "Un lieu, une situation : exil, cour, salon"),
          ("3. Contre qui, contre quoi ?", ""), ("4. Un mot", "pour son mal du siècle")]
    qh = "".join(f'<p style="font-size:32px; line-height:1.35"><b style="color:{BLUE}">{e(a_)}</b> {e(b_)}</p>' for a_, b_ in qs)
    inner = (head("En groupe · 10 minutes · Dossier du mal du siècle, partie 1", "Une voix, quatre questions")
             + f'<div style="display:flex; gap:28px">{gr}</div>'
             + f'<div style="display:grid; grid-template-columns:1fr 1fr; gap:18px 48px">{qh}</div>')
    return slide("groupes", PAPER, inner, foot=FOOT + " · UniCT 2026 · restitution : 1 minute par groupe")

def s15():
    ids = "".join(f'<div style="flex:1; display:flex; flex-direction:column; gap:12px"><p style="font-family:{SERIF}; font-size:60px; font-weight:700; color:{GOLD}">{k}</p>'
                  f'<p style="font-size:32px; line-height:1.4">{e(t)}</p></div>' for k, t in
                  (("1", "Le préromantisme est une étiquette posée après coup, pas une école."),
                   ("2", "Révolution, exil, Empire : la politique déplace la littérature."),
                   ("3", "Le mal du siècle est européen : <i>Werther</i>, <i>René</i>, <i>Ortis</i>.")))
    inner = (head("Fin de la séance 1", "Trois idées, une préparation", col=GOLD)
             + f'<div style="display:flex; gap:48px">{ids}</div>'
             + f'<div style="display:flex; flex-direction:column; gap:12px; background:{WINE}; border-radius:12px; padding:30px 40px">'
             + eyebrow("Pour la séance 2", "#F2D9A8")
             + f'<p style="font-size:30px; line-height:1.4">Relire les deux passages du dossier de textes (Rousseau, <i>René</i>) · apporter deux crayons, un bleu et un rouge.</p></div>')
    return slide("fin-seance1", INK, inner, foot=FOOT + " · UniCT 2026")

def s16():
    inner = (eyebrow("Séance 2 · 1 h 45 · lire à la loupe", "#F2D9A8")
             + f'<h2 style="font-family:{SERIF}; font-size:96px; font-weight:700; line-height:1.1">Comment un texte dit-il <i>je</i>&nbsp;?</h2>'
             + f'<p style="font-size:36px; line-height:1.45; max-width:1500px; color:#E3EEF4">Hier : qui écrit, d\'où, contre qui. Aujourd\'hui : avec quels mots, quelles phrases, quels silences.</p>'
             + hand("deux crayons : un bleu, un rouge", "#F2D9A8", 64))
    return slide("seance2", BLUE, inner, pad="128px", justify="center", gap="36px")

def s17():
    def verb(v, q, bg):
        return (f'<div style="flex:1; display:flex; flex-direction:column; gap:14px; background:{bg}; color:{PAPER}; border-radius:12px; padding:36px 40px">'
                f'<p style="font-family:{SERIF}; font-size:58px; font-weight:700">{v}</p><p style="font-size:30px; line-height:1.4">{e(q)}</p></div>')
    inner = (head("Boîte à outils · lire la société dans le texte", "La sociocritique en trois verbes", col=BLUE)
             + '<div style="display:flex; gap:32px">'
             + verb("Dire", "Que dit le texte de sa société ?", BLUE) + verb("Former", "Comment le dit-il : genre, langue, figures ?", INK)
             + verb("Taire", "Que tait-il ? Qui n'a pas la parole ?", WINE) + '</div>'
             + f'<div style="display:flex; flex-direction:column; gap:12px; background:{CARD}; border:1px solid {LINE}; border-radius:12px; padding:30px 40px">'
             + eyebrow("Exemple · Paul et Virginie", INK)
             + f'<p style="font-size:32px; line-height:1.4">Il <b>dit</b> le bonheur, sous la <b>forme</b> d\'une idylle, et <b>tait</b> le travail des esclaves.</p></div>')
    return slide("outil", PAPER, inner, foot=FOOT + " · UniCT 2026 · d'après Claude Duchet (1971)")

def s18():
    cols = "".join(f'<div style="flex:1; display:flex; flex-direction:column; gap:12px; border-top:6px solid {c}; padding-top:20px">'
                   f'<p style="font-size:26px; font-weight:700; color:{c}">{k}</p><p style="font-size:30px; line-height:1.4">{e(v)}</p></div>' for k, v, c in
                   (("Thèmes", "Amour naturel, mélancolie, nature sauvage, ruines, religiosité vague", BLUE),
                    ("Modèles", "Young, <i>Les Nuits</i> · Ossian · <i>Werther</i> : la sensibilité vient du Nord", BLUE),
                    ("À discuter", "Où sont le public, l'exil, la censure, le marché du livre ?", WINE)))
    inner = (head("Lecture critique · Philippe Van Tieghem", "Une sensibilité avant une école", col=BLUE)
             + f'<p style="font-family:{SERIF}; font-style:italic; font-size:46px; line-height:1.3; border-left:8px solid {WINE}; padding-left:36px">« Le Préromantisme est donc une évolution de la sensibilité suivie d\'une évolution du goût littéraire. »</p>'
             + f'<div style="display:flex; gap:40px">{cols}</div>')
    return slide("critique-vantieghem", PAPER2, inner, foot="Van Tieghem, Le Romantisme français, PUF, Que sais-je ?, chap. I, p. 6")

def s_texte(sid, f, cap, eb, q, rows, foot, alt):
    rh = "".join(label_row(a_, b_, kw=200, kcol=BLUE, size=30) for a_, b_ in rows)
    inner = (f'<div style="display:flex; gap:64px; flex:1">'
             f'<div style="flex:none; width:360px; display:flex; flex-direction:column; gap:14px">{img(f, 360, 460, alt)}'
             f'<p style="font-size:22px; line-height:1.35; color:{MUTE}">{e(cap)}</p></div>'
             f'<div style="flex:1; display:flex; flex-direction:column; gap:28px">' + eyebrow(eb)
             + f'<p style="font-family:{SERIF}; font-style:italic; font-size:50px; line-height:1.28">{e(q)}</p>'
             + f'<div style="display:flex; flex-direction:column">{rh}</div></div></div>')
    return slide(sid, PAPER, inner, foot=foot, pad="128px 128px 150px")

def s19():
    return s_texte("texte1", "rousseau", "Rousseau, <i>Rêveries du promeneur solitaire</i> (1782), Première promenade", "Texte à la loupe · 1 · Rousseau",
                   "« Me voici donc seul sur la terre, n'ayant plus de frère, de prochain, d'ami, de société que moi-même. »",
                   [("Énonciation", "Qui parle ? Comment le <i>je</i> est-il mis en valeur ?"), ("Rythme", "Repérez l'énumération : que produit-elle ?"),
                    ("Société", "Que dit cette solitude de la société du temps ? Que tait-elle ?")],
                   FOOT + " · dossier de textes, page 2, § 1", "Rousseau par Maurice Quentin de La Tour")

def s20():
    return s_texte("texte2", "chateaubriand", "Chateaubriand, <i>René</i> (1802, dans le <i>Génie du christianisme</i>)", "Texte à la loupe · 2 · René",
                   "« Levez-vous vite, orages désirés, qui devez emporter René dans les espaces d'une autre vie ! »",
                   [("Énonciation", "René parle de lui à la troisième personne : pourquoi ?"), ("Figures", "Apostrophe et impératif : à qui s'adresse-t-il ?"),
                    ("Désir", "Que cherche René dans l'orage : partir, ou mourir ?")],
                   FOOT + " · dossier de textes, page 3, § 1–2", "Chateaubriand par Anne-Louis Girodet")

def s21():
    B = lambda t: f'<b style="color:{BLUE}">{t}</b>'
    R = lambda t: f'<b style="color:{WINE}">{t}</b>'
    txt = (f"… une feuille {R('séchée')} que le {B('vent')} chassait devant moi, … la cime {R('dépouillée')} des arbres, la mousse qui tremblait au {B('souffle du nord')}, "
           f"… le jonc {R('flétri')} … les {B('oiseaux de passage')} … attends que le {B('vent')} de la {R('mort')} se lève, alors tu déploieras ton {B('vol')}…")
    inner = (head("La langue à la loupe · isotopies", "Deux séries de sens qui se croisent", col=BLUE)
             + '<div style="display:flex; gap:56px">'
             + f'<div style="flex:1; background:{CARD}; border:1px solid {LINE}; border-radius:12px; padding:40px 44px"><p style="font-family:{SERIF}; font-size:36px; line-height:1.55">{nb(txt)}</p></div>'
             + f'<div style="width:540px; flex:none; display:flex; flex-direction:column; gap:22px">'
             + f'<div style="border-top:6px solid {BLUE}; padding-top:16px; display:flex; flex-direction:column; gap:8px"><p style="font-size:28px; font-weight:700; color:{BLUE}">Bleu · vent et voyage</p><p style="font-size:26px; line-height:1.4">vent, souffle du nord, oiseaux de passage, migration, vol, orages, emporter</p></div>'
             + f'<div style="border-top:6px solid {WINE}; padding-top:16px; display:flex; flex-direction:column; gap:8px"><p style="font-size:28px; font-weight:700; color:{WINE}">Rouge · déclin et mort</p><p style="font-size:26px; line-height:1.4">séchée, dépouillée, flétri, désert, mort</p></div>'
             + hand("le croisement : « le vent de la mort »", WINE, 50) + '</div></div>')
    return slide("loupe", PAPER2, inner, foot=FOOT + " · Greimas (1966), Fontanille (1999)")

def s22():
    st = "".join(f'<div style="flex:1; display:flex; flex-direction:column; gap:12px"><p style="font-family:{SERIF}; font-size:72px; font-weight:700; color:{WINE}">{k}</p>'
                 f'<p style="font-size:32px; line-height:1.4">{e(t)}</p></div>' for k, t in
                 (("1", "Lire le texte deux fois, dont une à voix haute."), ("2", "Noter le genre, l'époque et qui parle."), ("3", "Écrire une hypothèse de lecture en une phrase.")))
    inner = (head("Méthode du commentaire · étape 1 sur 8", "Lire avant d'analyser")
             + f'<div style="display:flex; gap:48px">{st}</div>'
             + f'<div style="display:flex; flex-direction:column; gap:12px; background:{INK}; color:{PAPER}; border-radius:12px; padding:30px 40px">'
             + eyebrow("Exercice · 3 minutes, seul", GOLD)
             + f'<p style="font-size:40px; line-height:1.35">Une phrase pour <i>René</i> : « Ce texte montre…, grâce à… »</p></div>')
    return slide("methode", PAPER, inner, foot=FOOT + " · UniCT 2026")

def s23():
    rows = [("Longueur", "Brève, une seule action", "Bref", "Long, plusieurs intrigues"),
            ("Monde", "Vraisemblable, souvent vrai", "Ouvert au merveilleux", "Une société entière"),
            ("Fin", "La chute, forte et brève", "Une morale, un retour", "Un dénouement"),
            ("Origine", "La presse, puis le recueil", "La tradition orale", "Le livre, le feuilleton")]
    th = (f'<tr><th style="width:240px; background:{PAPER2}"></th><th style="background:{PAPER2}; color:{WINE}">Nouvelle</th>'
          f'<th style="background:{PAPER2}; color:{BLUE}">Conte</th><th style="background:{PAPER2}">Roman</th></tr>')
    tb = "".join(f'<tr><td style="font-weight:700; color:{MUTE}">{a_}</td><td style="font-weight:600; background:#F7EDEA">{e(b_)}</td><td>{e(c_)}</td><td>{e(d_)}</td></tr>' for a_, b_, c_, d_ in rows)
    inner = (head("Fil rouge du semestre · la nouvelle", "Qu'est-ce qu'une nouvelle ?")
             + f'<table style="width:100%; font-size:30px; line-height:1.35; background:{CARD}; border:1px solid {LINE}"><thead>{th}</thead><tbody>{tb}</tbody></table>'
             + f'<p style="font-size:28px; line-height:1.4"><b>Notre parcours</b> · Mérimée, Gautier, Flaubert, Maupassant, Daudet, Barbey d\'Aurevilly, Villiers de l\'Isle-Adam</p>')
    return slide("nouvelle", PAPER, inner, foot=FOOT + " · Grojnowski, Lire la nouvelle (1993) · Schaeffer (1989)")

def s24():
    st = "".join(f'<div style="flex:1; display:flex; flex-direction:column; gap:14px; border-top:6px solid {GOLD}; padding-top:22px">'
                 f'<p style="font-family:{SERIF}; font-size:46px; font-weight:700; color:{GOLD}">{k}</p><p style="font-size:30px; line-height:1.4; color:#E4DCE8">{e(t)}</p></div>' for k, t in
                 (("1. Demander", "Chaque groupe pose une question à René selon son angle ; je la tape sur l'écran commun."),
                  ("2. Vérifier", "Choisir une affirmation de la réponse et la retrouver dans le texte : vraie, fausse ou invérifiable ?"),
                  ("3. Déclarer", "Noter la question, la réponse et la vérification : première ligne du carnet de vérification IA.")))
    inner = (head("Labo IA · l'Atelier du siècle · Dossier, partie 3", "L'IA propose, le lecteur vérifie", col=GOLD)
             + f'<div style="display:flex; gap:48px">{st}</div>' + hand("L'auteur, c'est vous.", GOLD, 64))
    return slide("labo", INK, inner, foot=FOOT + " · charte IA du cours : déclarer, vérifier, écrire soi-même")

def s25():
    def box(eb, lines, bg):
        ls = "".join(f'<p style="font-size:32px; line-height:1.4">{e(l)}</p>' for l in lines)
        return (f'<div style="flex:1; display:flex; flex-direction:column; gap:14px; background:{bg}; border-radius:12px; padding:32px 40px">'
                + eyebrow(eb, "#F2D9A8") + ls + '</div>')
    inner = (head("Bilan de la semaine et suite", "Pour la semaine 2", col=GOLD)
             + '<div style="display:flex; gap:40px">'
             + box("À lire", ["Lamartine, <i>Le Lac</i> (Classroom)", "Mérimée, <i>Mateo Falcone</i> (une dizaine de pages)"], WINE)
             + box("À déposer sur Classroom", ["En groupe : le Dossier du mal du siècle", "Seul : une fiche de lecture d'une page sur <i>René</i> et la première ligne du carnet IA"], BLUE)
             + '</div>'
             + f'<p style="font-size:30px; line-height:1.4"><b>Lecture intégrale</b> · parcourir le plan de lecture ; choisir les six œuvres A.1 avant la fin de la semaine 2.</p>'
             + hand("Et l'énigme ? Un monde détruit, un autre pas encore né.", GOLD, 56))
    return slide("bilan", INK, inner, foot=FOOT + " · gkhndnr.github.io/catania-litterature-2026 · Classroom : rxdffgje")

LABELS = ["Couverture", "La semaine en deux séances", "Présentation de l'enseignant", "Et vous ? Tour de table", "L'énigme · le mal du siècle",
          "Frise 1782–1816", "Galerie · les voix de la semaine", "Les voix 1 · Rousseau", "Les voix 2 · Bernardin de Saint-Pierre",
          "Les voix 3 · Chateaubriand", "Les voix 4 · Germaine de Staël", "Les voix 5 · Benjamin Constant", "Ponte con l'Italia · Werther et Ortis",
          "En groupe · Dossier du mal du siècle, partie 1", "Fin de la séance 1", "Séance 2 · Comment un texte dit-il je ?",
          "Boîte à outils · la sociocritique en trois verbes", "Lecture critique · Van Tieghem : une sensibilité avant une école",
          "Texte à la loupe 1 · Rousseau, Rêveries", "Texte à la loupe 2 · Chateaubriand, René", "La langue à la loupe · isotopies",
          "Méthode, étape 1 · Lire avant d'analyser", "Fil rouge · Qu'est-ce qu'une nouvelle ?", "Labo IA · L'IA propose, le lecteur vérifie",
          "Bilan et suite · pour la semaine 2"]

def deck():
    slides = [s01(), s02(), s03(), s04(), s05(), s06(), s07()] + [s_voix(v) for v in VOIX] + \
             [s13(), s14(), s15(), s16(), s17(), s18(), s19(), s20(), s21(), s22(), s23(), s24(), s25()]
    ids = [re.search(r'id="([^"]+)"', s).group(1) for s in slides]
    notes = json.load(open(os.path.join(os.path.dirname(__file__), "s1_notes.json"), encoding="utf-8"))
    assert len(slides) == len(notes) == len(LABELS) == 25 and len(set(ids)) == 25
    return slides, notes, ids

def label(sid):
    _, _, ids = deck()
    return LABELS[ids.index(sid)]
