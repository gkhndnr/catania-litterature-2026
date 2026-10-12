# Met à jour directement s1.html et prof-s1.html avec la présentation de s1_deck.py
# (sans reconstruire tout le site, pour garder les corrections faites à la main sur s1.html).
# Usage : python3 _src/s1_patch.py <dossier_du_site>
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import s1_deck as D

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
slides, notes, ids = D.deck()

# ---- s1.html : diapositives et notes
p = os.path.join(ROOT, "s1.html")
h = open(p, encoding="utf-8").read()
frames = "".join(f'<div class="frame" data-i="{i}"{" hidden" if i else ""}><div class="scaler">{s}</div></div>' for i, s in enumerate(slides))
a = h.index('<div class="stage" id="stage"')
a = h.index('>', a) + 1
b = h.index('<div class="controls">', a)
assert h[b-6:b] == '</div>', h[b-40:b]
h = h[:a] + frames + h[b-6:]
h, k = re.subn(r"const NOTES=\[.*?\];\n", lambda m: "const NOTES=" + json.dumps(notes, ensure_ascii=False) + ";\n", h, count=1, flags=re.S)
assert k == 1
open(p, "w", encoding="utf-8").write(h)

# ---- prof-s1.html : notes diapositive par diapositive
def nb(t):
    t = re.sub(r" ([?!;:»])", " \\1", t)
    return t.replace("« ", "« ")
def e(s): return nb(html.escape(s, quote=False))
def fmt_note(t):
    out = []
    for blk in re.split(r"\n\n+", t or ""):
        blk = e(blk)
        m = re.match(r"^([A-ZÀ-ÝŒ'’ ]{4,}) · ([\s\S]*)$", blk)
        lab, body = ("", blk)
        if m: lab, body = f"<h4>{m.group(1)}</h4>", m.group(2)
        ps = []
        for l in body.split("\n"):
            if l.startswith("Q. "): ps.append(f'<p class="q"><b>Q.</b> {l[3:]}</p>')
            elif l.startswith("R. "): ps.append(f'<p class="r"><b>R.</b> {l[3:]}</p>')
            elif l.startswith("« "): ps.append(f'<p class="cit">{l}</p>')
            elif l: ps.append(f"<p>{l}</p>")
        out.append(f"<section>{lab}{''.join(ps)}</section>")
    return "".join(out)

p = os.path.join(ROOT, "prof-s1.html")
h = open(p, encoding="utf-8").read()
toc = "".join(f'<li><a href="#d{k+1}">{k+1}. {e(D.LABELS[k])}</a></li>' for k in range(len(ids)))
body = "".join(f'<article class="pnote" id="d{k+1}"><h3><span class="pn">{k+1}</span> {e(D.LABELS[k])} <a class="noprint small" href="s1.html#{k+1}">voir la diapositive ↗</a></h3><div class="notes">{fmt_note(nt)}</div></article>' for k, nt in enumerate(notes))
a = h.index('<h2>Notes diapositive par diapositive</h2>')
b = h.index('</main>', a)
h = h[:a] + f'<h2>Notes diapositive par diapositive</h2><ol class="toc noprint">{toc}</ol>{body}' + h[b:]
open(p, "w", encoding="utf-8").write(h)
print("S1 :", len(slides), "diapositives")
