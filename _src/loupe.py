# La langue à la loupe (ajout du 11 octobre 2026).
# Répond à la fiche du cours (Learning objectives, Carminella Sipala) : analyse grammaticale du texte,
# du métrique-prosodique au lexical et au morpho-syntaxique, repérage des séries isotopiques,
# signification globale, dialectique entre individualité et codes supra-personnels.
# Une grille par semaine, appliquée à un passage du dossier de textes (passages.py, relevés sur Wikisource).
# Rendu : diapositive « loupe » après la méthode, carte « La langue à la loupe » (En classe),
# un objectif « Je peux… » de plus, glossaire du guide de l'enseignant, ligne du carnet.
from notes_lib import N

FONTANILLE = "J. Fontanille, « Isotopie : cohérence, cohésion, congruence », Sémiotique et littérature, PUF, 1999, p. 15-40 (Cairn)"
GREIMAS = "A. J. Greimas, Sémantique structurale, Larousse, 1966 ; rééd. PUF, 2002"

GLOSS_BASE = [
 ("Isotopie", "Répétition, dans un texte, d'un même trait de sens (Greimas, 1966) : orages, vents, tempêtes forment l'isotopie de l'orage. Elle assure la cohérence du texte et guide la lecture."),
 ("Série isotopique", "Liste des mots d'un passage qui portent le même trait de sens. On la relève au crayon de couleur, une couleur par isotopie."),
 ("Champ lexical", "Ensemble des mots qui renvoient à un même thème. Notion scolaire proche de l'isotopie ; l'isotopie retient aussi des mots qui ne sont pas du même champ mais portent le même sème (enflammé et désirs, pour le feu de la passion)."),
 ("Congruence", "Point où deux isotopies se croisent et se traduisent l'une dans l'autre, souvent grâce à une métaphore (Fontanille, 1999)."),
 ("Codes supra-personnels", "Ce qui ne vient pas de l'auteur seul : règles du genre, de la versification, de la langue, de l'époque, du public. La voix singulière se lit contre ces codes."),
]

LOUPE = {
1: dict(
 titre="Deux isotopies qui se croisent",
 texte="René, la page des orages (dossier de textes)",
 grille=[
  ("Isotopie", "Le vent, l'orage, le voyage : vent, souffle du nord, oiseaux de passage, migration, vol, orages, emporter. Une seconde série dit la mort : feuille séchée, cime dépouillée, jonc flétri, le vent de la mort."),
  ("Lexique", "Adjectifs du déclin (séchée, dépouillée, flétri, désert) ; noms du lointain (bords ignorés, climats lointains, régions inconnues)."),
  ("Morpho-syntaxe", "Imparfaits de l'habitude (je m'égarais, me tourmentait) ; impératif et apostrophe (Levez-vous vite, orages désirés) ; René parle de lui à la troisième personne."),
  ("Rythme", "Énumération d'articles indéfinis (une feuille, une cabane, une roche) ; chez Rousseau, gradation de frère à société."),
  ("Voix et codes", "Le cri est singulier, mais le texte suit un code : il illustre le chapitre Du vague des passions d'une apologie chrétienne, et le père Souël condamne René à la fin."),
 ],
 consigne="Surlignez en bleu l'isotopie du vent et du voyage, en rouge celle de la mort. Où les deux séries se rejoignent-elles ? (le vent de la mort, puis orages désirés)",
 ia="Demander à l'Atelier du siècle : relève l'isotopie du voyage dans ce passage. Vérifier chaque mot dans le texte et barrer les mots inventés.",
 objectif="Je relève une isotopie (une série de mots qui portent le même sens) et je dis ce qu'elle fait au texte.",
 carnet="La langue à la loupe (15 min) prise sur René : deux isotopies au crayon de couleur, partie 2 du Dossier.",
 gloss=[("Apostrophe", "Figure par laquelle on s'adresse directement à un être ou à une chose (orages désirés)."),
        ("Énumération", "Suite de termes de même fonction ; elle peut aller crescendo (gradation)." )],
 note=N("15 min, séance B, après la lecture de René",
  "Distribuer deux crayons de couleur par groupe. Lire à voix haute la page des orages (dossier de textes). Consigne : en bleu, tout ce qui dit le vent, l'air, le voyage ; en rouge, tout ce qui dit la mort et le déclin. Mettre en commun au tableau en deux colonnes, puis poser la question du croisement. Finir par la ligne Voix et codes : un cri personnel dans un livre qui le condamne.",
  essentiel="La fiche du cours demande l'analyse grammaticale du texte, du métrique-prosodique au lexical et au morpho-syntaxique, et le repérage des séries isotopiques. Une isotopie est la répétition d'un même trait de sens (Greimas) ; c'est elle qui fait la cohérence d'un texte. Quand deux isotopies se croisent dans une image, on parle de congruence (Fontanille) : ici le vent de la mort et les orages désirés relient le voyage et la mort. Cette grille revient chaque semaine sur un passage du dossier.",
  qr=[("Quelle différence entre isotopie et champ lexical ?",
       "Le champ lexical regroupe des mots du même thème (bruyères, forêts, étang : la campagne). L'isotopie suit un trait de sens, même dans des mots de thèmes différents : flétri, séchée, dépouillée et la mort appartiennent à l'isotopie du déclin."),
      ("Où les deux isotopies se croisent-elles ?",
       "Dans le vent de la mort (la voix du ciel) puis dans orages désirés : l'orage, phénomène de l'air, devient le moyen de partir dans une autre vie. Le voyage est une image de la mort."),
      ("Pourquoi parler de codes ?",
       "Parce que René n'est pas un journal intime : c'est un épisode du Génie du christianisme (1802), qui montre le vague des passions pour le condamner. La voix singulière de René est encadrée par un code religieux et par un genre, l'apologie.")],
  piege="Ne pas transformer l'exercice en liste de mots : chaque isotopie doit déboucher sur une phrase d'interprétation (Cette isotopie montre que…).",
  source=FONTANILLE + " ; " + GREIMAS + "."),
),
2: dict(
 titre="Le temps est une eau qui coule",
 texte="Lamartine, Le Lac (dossier de textes)",
 grille=[
  ("Isotopie", "Le temps : temps, heures, jours, moments, l'heure fugitive. L'eau : lac, flots, onde, rivage, écume, coulez. Elles se rejoignent : le temps n'a point de rive ; il coule."),
  ("Lexique", "Verbes de la fuite (fuit, échappe, s'envolent, engloutissez) contre verbes de la retenue (suspends, gardez, fixer)."),
  ("Morpho-syntaxe", "Impératifs et vocatifs (Ô temps ! suspends ton vol) ; passage du tu au vous ; le nous du couple."),
  ("Métrique", "Strophes de trois alexandrins et d'un hexasyllabe ; dans la prière de Julie, alternance 12 / 6 : Suspendez votre cours compte six syllabes."),
  ("Voix et codes", "Le deuil personnel (Julie Charles, Elvire) passe par un code ancien : l'élégie et le thème du carpe diem."),
 ],
 consigne="Scandez la strophe Ô temps ! suspends ton vol, puis relevez les mots du temps et les mots de l'eau : quel vers les fond en une seule image ?",
 ia="Demander à l'Atelier de scander la strophe ; recompter soi-même et noter l'erreur éventuelle (e muet, diérèse).",
 objectif="Je relie la métrique du Lac (12 / 6) et ses isotopies du temps et de l'eau.",
 carnet="La langue à la loupe (10 min) dans l'atelier du vers : temps et eau, l'image du vers L'homme n'a point de port.",
 gloss=[("Élégie", "Poème de la plainte, du deuil ou de l'amour perdu."),
        ("Vocatif", "Mot qui désigne celui à qui l'on parle (Ô temps, Ô lac).")],
 note=N("10 min, séance B, après le comptage des syllabes",
  "Après la scansion, revenir au sens : deux colonnes au tableau, le temps et l'eau. Faire chercher le vers où elles fusionnent : L'homme n'a point de port, le temps n'a point de rive ; Il coule, et nous passons ! Montrer que la forme (alternance longue et brève) imite le temps qui file.",
  essentiel="Le Lac associe le temps et l'eau : le lac est le lieu du souvenir, le temps est un fleuve sans rive. La strophe de la prière alterne alexandrins et hexasyllabes : la brièveté du vers court mime la fuite des heures.",
  qr=[("Quel vers fond les deux isotopies ?", "L'homme n'a point de port, le temps n'a point de rive ; / Il coule, et nous passons ! Le temps reçoit les mots de l'eau (rive, coule) : c'est une métaphore filée."),
      ("Pourquoi des vers de six syllabes ?", "Ils cassent l'élan de l'alexandrin : le lecteur sent la coupure, comme le temps qui interrompt le bonheur."),
      ("Où sont les codes ?", "Dans l'élégie et le carpe diem (Horace, Ronsard) : Lamartine reprend un thème très ancien, mais avec une voix intime qui a frappé les lecteurs de 1820.")],
  source=FONTANILLE + "."),
),
3: dict(
 titre="Le regard qui conquiert",
 texte="Balzac, Le Père Goriot, dernière page ; Stendhal, le miroir (dossier de textes)",
 grille=[
  ("Isotopie", "Le regard : vit, yeux, regard, et chez Stendhal miroir, reflète, montre. La conquête : pénétrer, pomper le miel, défi, À nous deux."),
  ("Lexique", "Adverbes en -ment (tortueusement, avidement) ; Paris en ruche bourdonnant : métaphore animale."),
  ("Morpho-syntaxe", "Passés simples de l'action (fit, vit, lança, dit) puis présent du discours direct ; nous réunit Rastignac et Paris."),
  ("Rythme", "La phrase s'élève avec le regard, du cimetière aux lumières, et retombe sur une réplique de quatre mots."),
  ("Voix et codes", "Rastignac défie la Société, mais son défi suit le code du monde : il va dîner chez madame de Nucingen."),
 ],
 consigne="Relevez l'isotopie du regard et celle de la conquête : à quel moment le regard devient-il une prise ?",
 ia="Demander à l'Atelier une problématique sur la dernière page du Père Goriot ; vérifier qu'elle s'appuie sur des mots du texte.",
 objectif="Je m'appuie sur une isotopie pour formuler une problématique.",
 carnet="La langue à la loupe (10 min) pendant l'atelier Rastignac : regard et conquête.",
 gloss=[("Passé simple", "Temps des actions de premier plan dans le récit écrit (il fit, il vit)."),
        ("Métaphore filée", "Image prolongée sur plusieurs mots (ruche, bourdonnant, miel).")],
 note=N("10 min, séance B",
  "Faire relever en deux couleurs le regard et la conquête dans la page de Balzac. Montrer que la métaphore de la ruche fait passer de l'un à l'autre : regarder, c'est déjà pomper le miel. Conclure par la phrase finale, qui ramène le défi aux codes mondains.",
  qr=[("Que dit le nous de À nous deux ?", "Il oppose deux adversaires, Rastignac et Paris personnifié : le duel devient la forme de l'ambition."),
      ("Pourquoi la dernière phrase est-elle ironique ?", "Le premier acte du défi est un dîner chez sa maîtresse, fille de Goriot : la révolte individuelle passe par les règles du monde qu'elle prétend défier.")],
  source=FONTANILLE + "."),
),
4: dict(
 titre="Nier les liens, aimer les nuages",
 texte="Baudelaire, L'Étranger (dossier de textes)",
 grille=[
  ("Isotopie", "Les liens : père, mère, sœur, frère, amis, patrie, or. L'ailleurs : nuages, passent, là-bas."),
  ("Lexique", "Le questionneur emploie des étiquettes (homme énigmatique, extraordinaire étranger) ; l'étranger répond par des mots simples."),
  ("Morpho-syntaxe", "Négation en ni… ni ; phrases nominales (Tes amis ? Ta patrie ?) ; le questionneur tutoie, l'étranger vouvoie."),
  ("Rythme", "Poème en prose sans vers : le rythme vient des répétitions et des points de suspension (là-bas… là-bas…)."),
  ("Voix et codes", "La forme du catéchisme ou de l'interrogatoire (question, réponse) sert à refuser les valeurs bourgeoises."),
 ],
 consigne="Relevez les deux isotopies, puis comptez les tu et les vous : qui domine le dialogue ?",
 ia="Demander à l'Atelier un plan en deux axes ; vérifier que chaque axe repose sur une isotopie du poème.",
 objectif="Je fonde les axes de mon plan sur des isotopies et sur des faits de langue.",
 carnet="La langue à la loupe (10 min) sur L'Étranger : isotopies et tutoiement / vouvoiement.",
 gloss=[("Phrase nominale", "Phrase sans verbe conjugué (Ta patrie ?)."),
        ("Poème en prose", "Poème sans vers ni rimes, organisé par le rythme et les reprises.")],
 note=N("10 min, séance B",
  "Deux lecteurs jouent le dialogue. Relever les deux isotopies au tableau. Faire remarquer l'asymétrie tu / vous : le questionneur tutoie comme un maître, l'étranger répond avec une politesse distante. Les deux isotopies donnent les deux axes du plan.",
  qr=[("Que montre l'asymétrie tu / vous ?", "Le questionneur parle au nom de la société et de ses valeurs ; l'étranger garde ses distances : la grammaire dit le refus."),
      ("Pourquoi des points de suspension à la fin ?", "La phrase se perd comme les nuages : le rythme imite l'ailleurs qu'elle désigne.")],
  source=FONTANILLE + "."),
),
5: dict(
 titre="La débandade dans les mots",
 texte="Maupassant, Boule de suif, ouverture ; Barbey d'Aurevilly, Le Rideau cramoisi, cadre (dossier de textes)",
 grille=[
  ("Isotopie", "La défaite qui défait : lambeaux, déroute, hordes débandées, guenilles, débris, moulue, accablés, éreintés."),
  ("Lexique", "Vocabulaire militaire précis (mobilisés, moblots, culottes rouges, artilleurs, dragon, lignards) ; chez Barbey, terriblement d'années, intensif appliqué au temps."),
  ("Morpho-syntaxe", "Plus-que-parfait (avaient traversé) et imparfaits descriptifs ; énumération de groupes nominaux. Barbey : je narrateur et adresse au lecteur (je vous demanderai)."),
  ("Rythme", "Phrases longues, sans action principale : la marche molle de l'armée passe dans la syntaxe."),
  ("Voix et codes", "Maupassant suit le code naturaliste du groupe de Médan (narrateur effacé) ; Barbey reprend le code du récit oral enchâssé."),
 ],
 consigne="Relevez l'isotopie de la défaite dans les cinq premières lignes de Boule de suif : comment l'introduction de votre commentaire peut-elle l'annoncer ?",
 ia="Demander à l'Atelier une introduction ; vérifier que l'amorce et la problématique citent bien le texte.",
 objectif="J'annonce dans mon introduction une isotopie relevée dans le texte.",
 carnet="La langue à la loupe (10 min) sur l'ouverture de Boule de suif avant l'atelier d'introduction.",
 gloss=[("Plus-que-parfait", "Temps de l'antériorité dans le passé (avaient traversé)."),
        ("Récit enchâssé", "Récit raconté par un personnage à l'intérieur d'un autre récit.")],
 note=N("10 min, séance B",
  "Lecture de la première page de Boule de suif. Relever l'isotopie de la défaite : les mots de la désagrégation (lambeaux, débandées, débris, moulue) décrivent une armée qui n'en est plus une. Montrer que l'introduction du commentaire peut annoncer cette isotopie dans sa problématique.",
  qr=[("Pourquoi lambeaux d'armée ?", "Un lambeau est un morceau de tissu déchiré : la métaphore montre une armée en pièces, dès la première phrase."),
      ("En quoi Barbey s'oppose-t-il à Maupassant ?", "Barbey installe un je qui parle au lecteur et prépare une histoire racontée : c'est le code du récit oral, à l'opposé du narrateur effacé du naturalisme.")],
  source=FONTANILLE + "."),
),
6: dict(
 titre="Un je qui largue les amarres",
 texte="Rimbaud, Le Bateau ivre, premières strophes (dossier de textes)",
 grille=[
  ("Isotopie", "La navigation : fleuves, haleurs, équipages, marées, flots. La libération : ne… plus guidé, insoucieux, où je voulais, je courus."),
  ("Lexique", "Mots rares et sonores (tohu-bohus, clapotements, Péninsules démarrées) : le lexique déborde comme le bateau."),
  ("Morpho-syntaxe", "Imparfait de fond (je descendais) et passé simple de rupture (je ne me sentis plus) ; je désigne le bateau."),
  ("Métrique", "Alexandrins en rimes croisées (impassibles / cibles, haleurs / couleurs) : le vers reste régulier quand le sens se libère."),
  ("Voix et codes", "Rimbaud, seize ans, écrit dans l'alexandrin des Parnassiens : la révolte se dit d'abord dans le code qu'elle veut briser."),
 ],
 consigne="Scandez le premier vers, puis relevez l'isotopie de la navigation et celle de la libération : écrivez un paragraphe d'analyse sur leur rencontre.",
 ia="Demander à l'Atelier la lecture d'une strophe ; vérifier les rimes et le compte des syllabes avant d'accepter l'analyse.",
 objectif="J'analyse dans un paragraphe une isotopie et un fait de versification.",
 carnet="La langue à la loupe (10 min) sur les trois premières strophes du Bateau ivre.",
 gloss=[("Rimes croisées", "Disposition ABAB."),
        ("Sociolecte", "Langue d'un groupe social ou littéraire (le jargon des symbolistes, raillé par les parodistes).")],
 note=N("10 min, séance B",
  "Scansion du premier vers (Com-me-je-des-cen-dais / des-Fleu-ves-im-pas-si-bles : 12 syllabes). Relever ensuite les deux isotopies. Le paragraphe d'analyse doit citer un mot de chaque série et un fait de versification.",
  qr=[("Le premier vers compte-t-il douze syllabes ?", "Oui : le e de Comme compte devant la consonne de je ; dans Fleuves, la finale -es compte devant impassibles, car le s empêche l'élision ; le e final de impassibles, en fin de vers, ne compte pas."),
      ("Pourquoi parler de codes ?", "Parce que la forme reste celle de la tradition (alexandrin, quatrains) : la nouveauté passe par les images et le lexique.")],
  source=FONTANILLE + "."),
),
7: dict(
 titre="La lune, la morte, la princesse",
 texte="Wilde, Salomé, première scène ; Jarry, Ubu Roi, acte I, scène 1 (dossier de textes)",
 grille=[
  ("Isotopie", "La femme et la mort autour de la lune : princesse, femme morte, tombeau, voile jaune, pieds d'argent, colombes, danse."),
  ("Lexique", "Chez Jarry, mots fabriqués ou déformés : merdre, estes, assom'je, coupe-choux, fiole."),
  ("Morpho-syntaxe", "Comparaisons répétées (On dirait…, Elle ressemble à…, comme) ; phrases courtes juxtaposées."),
  ("Rythme", "Wilde répète ses phrases comme une litanie ; Jarry casse le rythme du dialogue tragique par un mot grossier."),
  ("Voix et codes", "Wilde écrit en français et suit le code symboliste ; Jarry parodie le code de la tragédie et de l'exposition."),
 ],
 consigne="Relevez l'isotopie de la mort dans la première scène de Salomé : que prépare-t-elle pour la fin de la pièce ?",
 ia="Demander à l'Atelier une conclusion qui ouvre ; vérifier que l'ouverture renvoie à un texte réel.",
 objectif="Je relie une isotopie de l'ouverture à la fin d'une œuvre pour conclure.",
 carnet="La langue à la loupe (10 min) : Salomé et Ubu, deux premières scènes.",
 gloss=[("Litanie", "Suite de répétitions sur un rythme de prière."),
        ("Néologisme", "Mot nouveau ou déformé (merdre).")],
 note=N("10 min, séance B",
  "Lire à deux voix le début de Salomé. Relever l'isotopie de la mort (femme morte, tombeau) mêlée à celle de la princesse : la lune annonce le destin de Salomé. Comparer avec Ubu : le premier mot de la pièce détruit le code de l'exposition.",
  qr=[("Que prépare l'isotopie de la mort ?", "La fin de la pièce, où Salomé est mise à mort : la première scène annonce le dénouement."),
      ("Merdre est-il un simple mot grossier ?", "C'est un mot déformé (un r ajouté) : la langue elle-même est parodiée, comme le code tragique.")],
  source=FONTANILLE + "."),
),
8: dict(
 titre="La maison perdue",
 texte="Alain-Fournier, Le Grand Meaulnes, incipit (dossier de textes) ; Marinetti, Manifeste du futurisme",
 grille=[
  ("Isotopie", "La demeure : maison, bâtiments, cour, préaux, portail, grille, demeure. La perte : ne nous appartienne plus, quitté, ne reviendrons jamais, s'écoulèrent."),
  ("Lexique", "Lieux précis et noms propres (Sainte-Agathe, La Gare) ; chez Marinetti, splendeur, beauté nouvelle, vitesse."),
  ("Morpho-syntaxe", "Il arriva : pronom sans nom, Meaulnes n'est pas encore nommé ; passé simple, puis présent du narrateur (Je continue) et passé composé (Nous avons quitté)."),
  ("Rythme", "Longue phrase nominale du plan de la maison, close par une comparaison (comme des vagues sur un rocher désert)."),
  ("Voix et codes", "Le manifeste parle au nom d'un nous collectif qui déclare ; Alain-Fournier fait entendre un je qui se souvient."),
 ],
 consigne="Relevez les deux isotopies de l'incipit, puis rédigez une conclusion qui compare le nous de Marinetti et le chez nous d'Alain-Fournier.",
 ia="Bilan : comparer un commentaire produit par l'IA et le vôtre ; noter trois différences dans la façon de citer le texte.",
 objectif="Je mobilise isotopies, faits de langue et codes du genre dans un commentaire complet.",
 carnet="La langue à la loupe (10 min) : l'incipit du Grand Meaulnes avant le commentaire complet.",
 gloss=[("Incipit", "Les premières lignes d'une œuvre."),
        ("Performatif", "Énoncé qui accomplit ce qu'il dit (Nous déclarons).")],
 note=N("10 min, séance B",
  "Lecture de l'incipit. Relever la demeure et la perte. Faire remarquer le pronom Il de la première phrase : le héros entre sans nom. Opposer le nous qui déclare de Marinetti et le chez nous mis entre guillemets par le narrateur.",
  qr=[("Pourquoi chez nous est-il entre guillemets ?", "Le narrateur sait que la maison ne lui appartient plus : il cite ses propres mots d'enfant, avec distance. Le temps de l'écriture n'est plus celui de l'histoire."),
      ("Quel lien avec Marinetti ?", "Deux rapports au temps en 1909-1913 : la vitesse tournée vers l'avenir, la mémoire tournée vers une enfance perdue.")],
  source=FONTANILLE + "."),
),
}

# Lectures critiques consultées sur Cairn.info (octobre 2026) pour la bibliographie de la semaine 1.
BIB_ADD = {
1: ["Anthony Glinoer et Vincent Laisney, « De quoi vivaient-ils ? Le mécénat littéraire au XIXe siècle », dans Le Mécénat littéraire aux XIXe et XXe siècles, 2019, p. 13 sq. (Cairn) : après la Révolution, un mécénat d'État géré par des demandes de pension.",
    "Deborah Gutermann, « Mal du siècle et mal du « sexe » dans la première moitié du XIXe siècle », Sociétés & Représentations, n° 24, 2007, p. 195-210 (Cairn).",
    "Marc Lits, « Nouvelle littéraire et nouvelle journalistique », Le français aujourd'hui, n° 134, 2001, p. 43-52 (Cairn).",
    "Claude Duchet, « La sociocritique dans l'histoire littéraire », Revue d'histoire littéraire de la France, 1995, n° 7, p. 179-184 (Cairn).",
    "Jacques Fontanille, « Isotopie : cohérence, cohésion, congruence », Sémiotique et littérature, Paris, PUF, 1999, p. 15-40 (Cairn).",
    "Algirdas Julien Greimas, Sémantique structurale, Paris, Larousse, 1966 ; rééd. PUF, 2002.",
    "Ingrid Mayeur, « Envisager l'intelligence artificielle générative comme média éducatif à l'université », dans Information et intelligence artificielle, De Boeck Supérieur, 2025, p. 239-250 (Cairn)."],
}


def apply(weeks, notes, bib_week):
    """Intègre la grille dans les semaines : objectif, carnet, note de la diapositive, références."""
    for w in weeks:
        L = LOUPE.get(w["n"])
        if not L or w.get("_loupe"): continue
        w["_loupe"] = True
        w["objectifs"] = list(w["objectifs"]) + [L["objectif"]]
        w["prog"] = list(w["prog"]) + [("Analyse du texte", "Fiche : du métrique au lexical et au morpho-syntaxique, séries isotopiques, voix et codes")]
        w["carnet"] = dict(w["carnet"]); w["carnet"]["B"] = w["carnet"]["B"].rstrip() + " " + L["carnet"]
        notes.setdefault(w["n"], {})["loupe"] = L["note"]
    for n, refs in BIB_ADD.items():
        for r in refs:
            if r not in bib_week.setdefault(n, []): bib_week[n].append(r)


def glossaire(n):
    L = LOUPE.get(n, {})
    base = GLOSS_BASE if n == 1 else GLOSS_BASE[:1]
    return list(base) + list(L.get("gloss", []))


def loupe_box_pdf(n, e):
    """Encadré pour le dossier de textes (PDF A4)."""
    L = LOUPE.get(n)
    if not L: return ""
    rows = "".join(f"<li><b>{e(k)}</b> {e(v)}</li>" for k, v in L["grille"])
    return (f'<h2>La langue à la loupe · {e(L["titre"])}</h2><p class="small">{e(L["texte"])}. Une isotopie est une série de mots qui portent le même trait de sens : '
            f'relevez-la au crayon de couleur, puis dites ce qu\'elle fait au texte.</p><ul>{rows}</ul>'
            f'<div class="box"><b>À faire</b> {e(L["consigne"])}<br><b>Avec l\'IA</b> {e(L["ia"])}</div>')
