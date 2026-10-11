# Documentaires à regarder, semaine par semaine.
# Chaque entrée produit une carte « Regarder » sur la page de la semaine
# et une ligne dans la bibliographie.
# Règle : lien vers la vidéo publiée par la chaîne officielle, jamais de copie dans le dépôt.
# debut / fin : secondes (le lien ouvre la vidéo au bon moment).

ARTE_ID = "_FjGuxCrYpY"
ARTE_REF = ("L'Armée des romantiques, série documentaire d'animation en quatre épisodes, "
            "réalisation Amélie Harrault, ARTE ; intégrale de 3 h 10 sur la chaîne YouTube d'ARTE.")

def yt(sec): return f"https://www.youtube.com/watch?v={ARTE_ID}&t={sec}s"

VIDEOS = {
2: [dict(
  serie="L'Armée des romantiques (ARTE)",
  episodes=[("Épisode 1 · La révolution romantique (1827-1832)", 0, 2933)],
  pourquoi="Le Paris des jeunes romantiques, au moment où Hugo et ses amis prennent la scène : la bataille de la semaine racontée comme une aventure collective.",
  questions=["Qui forme le groupe des jeunes romantiques ? Où et comment se retrouvent-ils ?",
             "Contre qui et contre quoi se battent-ils ? Relevez deux dates et comparez avec la frise de la semaine.",
             "Quels arts l'épisode fait-il dialoguer (poésie, théâtre, peinture, musique) ?"],
  socio="Le documentaire parle d'une armée. Que gagne-t-on, et que perd-on, à raconter un mouvement littéraire comme une bataille entre jeunes et anciens ?",
)],
3: [dict(
  serie="L'Armée des romantiques (ARTE)",
  episodes=[("Épisode 2 · La vie comme un roman (1833-1848)", 2933, 5684)],
  pourquoi="Les années du roman, de la presse et des vies d'artistes : Balzac, Sand, Dumas. Le fond social du thème de la semaine, le roman comme miroir et comme marché.",
  questions=["Comment les écrivains de l'épisode gagnent-ils leur vie ? Relevez ce qui touche à l'argent, aux dettes, aux journaux.",
             "Quelle place George Sand occupe-t-elle dans ce groupe d'hommes ?",
             "Pourquoi le titre La vie comme un roman ? Donnez un exemple tiré de l'épisode."],
  socio="Quand la presse fait vivre les écrivains, la vie de l'artiste devient-elle elle-même une marchandise ? Rapprochez de Sainte-Beuve, De la littérature industrielle (1839).",
)],
4: [dict(
  serie="L'Armée des romantiques (ARTE)",
  episodes=[("Épisode 3 · Le crépuscule romantique (1848-1855)", 5684, 8565),
            ("Épisode 4 · L'ère de l'émancipation (1855-1874)", 8565, 11435)],
  pourquoi="De la révolution de 1848 à l'exil et aux procès : comment la génération romantique se défait, et comment une autre idée de l'art (Baudelaire, Flaubert) prend la relève.",
  questions=["Que changent 1848 puis le coup d'État de 1851 pour les artistes de l'épisode 3 ?",
             "Pourquoi parler de crépuscule ? Qui part, qui reste, qui se tait ?",
             "Dans l'épisode 4, quelles formes d'émancipation voit-on : artistique, politique, féminine ?"],
  socio="Pour Bourdieu (Les Règles de l'art), les années 1848-1857 sont celles où le champ littéraire conquiert son autonomie. L'art pour l'art est-il une fuite hors du monde ou une conquête d'indépendance ?",
)],
}

CONSEIL = ("À regarder chez soi, de préférence avant la séance A. En classe, l'enseignant projette un extrait de cinq à dix minutes. "
           "Le documentaire est une œuvre : animation, voix, récit choisi. Il simplifie ; vérifiez dates et citations dans les textes.")
