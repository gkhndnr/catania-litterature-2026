# Lectures critiques ajoutées semaine par semaine.
# Chaque entrée produit une diapositive (idées + citations), une frise facultative,
# une carte « Lecture critique » sur la page de la semaine, une entrée dans le carnet
# et dans la bibliographie.
# Règle : citations courtes, source indiquée, jamais le PDF dans le dépôt public.
# citations : (texte, source affichée telle quelle)

STALLONI_REF = ("Yves Stalloni, Écoles et courants littéraires, Paris, Armand Colin, coll. « Cursus », "
                "3e éd., 2015, chapitre « Le dix-neuvième siècle » (Romantisme, Parnasse, Réalisme, Naturalisme, Symbolisme, Félibrige).")
STALLONI_LIEN = "https://shs.cairn.info/resultats-de-recherche?searchTerm=Stalloni%20%C3%89coles%20et%20courants%20litt%C3%A9raires"
BAINVILLE_REF = ("Jacques Bainville, Au seuil du siècle. Études critiques, Paris, Éditions du Capitole, 1927 "
                 "(articles de 1900 à 1913 réunis par René Groos ; texte du domaine public, Wikisource).")
BAINVILLE_LIEN = "https://fr.wikisource.org/w/index.php?search=Bainville+Au+seuil+du+si%C3%A8cle"

ARTICLES = {
1: [dict(
  id="vantieghem",
  auteur="Philippe Van Tieghem",
  court="Van Tieghem, « Le Préromantisme »",
  ref="Philippe Van Tieghem, « Le Préromantisme », chapitre I de Le Romantisme français, Paris, PUF, coll. Que sais-je ?, p. 5-14.",
  lien="https://www.cairn.info/le-romantisme-francais--9782130444336-page-5.htm",
  titre="Une sensibilité avant une école",
  idees=[
    ("Transition","De la seconde moitié du XVIIIe siècle au début de la Restauration : des sentiments nouveaux dans des formes encore classiques."),
    ("Rousseau","La Nouvelle Héloïse (1761) fait passer en littérature ce qui restait dans les lettres et les journaux intimes."),
    ("Thèmes","Amour naturel, mélancolie, nature sauvage, ruines, religiosité vague."),
    ("Passeurs","Staël élargit le goût classique sans le ruiner ; Chateaubriand renouvelle l'imagination."),
  ],
  citations=[("Le Préromantisme est donc une évolution de la sensibilité suivie d'une évolution du goût littéraire.","Van Tieghem, p. 6"),
             ("La mélancolie devient le mal du siècle.","Van Tieghem, p. 10")],
  debat="Une histoire de la sensibilité suffit-elle ? Où sont le public, l'exil, la censure, le marché du livre ?",
  frise_titre="La sensibilité vient d'ailleurs",
  frise=[("1742–45","Young, Les Nuits (Angleterre)",0),("1751","Gray, Élégie écrite dans un cimetière de campagne",0),
         ("1760–63","Poèmes d'Ossian",0),("1761","Rousseau, La Nouvelle Héloïse",1),
         ("1774","Goethe, Werther",0),("1800–10","Staël, De la littérature ; De l'Allemagne",1)],
  frise_bas="Van Tieghem, p. 12-13 : les modèles du préromantisme français sont anglais et allemands.",
  route="Lecture critique de la semaine : la définition du préromantisme comme histoire de la sensibilité, à discuter avec la sociocritique.",
)],

2: [dict(
  id="stalloni-romantisme",
  auteur="Yves Stalloni",
  court="Stalloni, Écoles et courants littéraires : « Le Romantisme »",
  ref=STALLONI_REF, lien=STALLONI_LIEN,
  titre="Le romantisme, une bataille de groupes",
  idees=[
    ("Deux sens","Un romantisme éternel (une sensibilité) et un romantisme historique, l'école de 1820 à 1843 (Peyre, Milner)."),
    ("Le mot","De l'italien romanzesco à l'anglais romantic puis à l'allemand romantisch ; Staël l'oppose à classique (1810)."),
    ("Cénacles","Abbaye-aux-Bois, Arsenal de Nodier (1824), rue Notre-Dame-des-Champs chez Hugo (1827), petit Cénacle."),
    ("Manifestes","Racine et Shakespeare (1823), Préface de Cromwell (1827), préface d'Hernani : le libéralisme en littérature."),
  ],
  citations=[("Le mot bataille n'est pas trop fort tant l'histoire du Romantisme s'est écrite sur le mode du conflit…","Stalloni, « La bataille romantique »"),
             ("On sent le romantique, on ne le définit pas.","L.-S. Mercier, cité par Stalloni")],
  debat="Une école se définit-elle par une doctrine, ou par des lieux, des revues et des amitiés ?",
  frise_titre="Les cénacles, salles d'armes de 1830",
  frise=[("1819","Le Conservateur littéraire des frères Hugo",0),("1823","Stendhal, Racine et Shakespeare ; La Muse française",0),
         ("1824","Nodier ouvre l'Arsenal ; fondation du Globe",1),("1827","Préface de Cromwell ; Hugo rue Notre-Dame-des-Champs",0),
         ("1829","Le petit Cénacle chez Jehan du Seigneur",1),("1830","25 février : Hernani",1)],
  frise_bas="Stalloni : les cénacles se font et se défont selon les amitiés littéraires et les convictions politiques.",
  route="Lecture critique : comment une école se fabrique (mots, cénacles, revues, préfaces). On l'utilise en séance A pour préparer le jeu d'Hernani.",
)],

4: [dict(
  id="stalloni-parnasse",
  auteur="Yves Stalloni",
  court="Stalloni, Écoles et courants littéraires : « Le Parnasse », « Le Réalisme »",
  ref=STALLONI_REF, lien=STALLONI_LIEN,
  titre="Art pour l'art, Parnasse, réalisme : des refus",
  idees=[
    ("Gautier","Préface de Mademoiselle de Maupin : le beau ne doit servir à rien ; Baudelaire dédie Les Fleurs du mal au « poète impeccable »."),
    ("Parnasse","1866 : Le Parnasse contemporain chez Lemerre, 37 poètes ; culte du travail, de la forme, refus du lyrisme."),
    ("Réalisme","Courbet, Champfleury (Le Réalisme, 1857), Duranty : le vrai contre l'idéal, le présent contre le passé."),
    ("Étiquettes","Flaubert refuse réalisme et naturalisme : « la même ineptie » (à Maupassant, 1876)."),
  ],
  citations=[("Il n'y a de vraiment beau que ce qui ne peut servir à rien ; tout ce qui est utile est laid.","Gautier, préface de Mademoiselle de Maupin, cité par Stalloni"),
             ("Le Réalisme n'a pas apporté d'œuvre majeure à la littérature…","Stalloni, « Le Réalisme »")],
  debat="Flaubert et Baudelaire sont rangés dans des écoles qu'ils refusent : qui pose les étiquettes, l'écrivain, le critique ou le manuel ?",
  route="Lecture critique : l'art pour l'art, le Parnasse et le réalisme comme deux façons de refuser l'utilité et la morale. Utile pour le tribunal de 1857.",
)],

5: [dict(
  id="stalloni-naturalisme",
  auteur="Yves Stalloni",
  court="Stalloni, Écoles et courants littéraires : « Le Naturalisme », « Le Félibrige »",
  ref=STALLONI_REF, lien=STALLONI_LIEN,
  titre="Le naturalisme, une école en trois temps",
  idees=[
    ("Formation","1865-1876 : Germinie Lacerteux, Mes Haines (1866), Thérèse Raquin (1867) ; Zola devient chef d'école."),
    ("Âge d'or","1876-1884 : dîner Trapp (16 avril 1877), Les Soirées de Médan (1880), Le Roman expérimental (1880)."),
    ("Éclatement","1884-1893 : À rebours (1884), Manifeste des Cinq contre La Terre (1887), enquête de Huret (1891)."),
    ("Méthode","Enquête, document, milieu, hérédité : un coin de la création vu à travers un tempérament."),
  ],
  citations=[("Une œuvre d'art est un coin de la création vu à travers un tempérament.","Zola, Mes Haines, 1866, cité par Stalloni"),
             ("Naturalisme pas mort. Lettre suit.","télégramme de Paul Alexis à Huret, 1891, cité par Stalloni")],
  debat="Une école qui se dit scientifique peut-elle échapper aux luttes de groupes, aux dîners et aux manifestes ?",
  frise_titre="L'école de Médan, de la naissance à la dispersion",
  frise=[("1865","Goncourt, Germinie Lacerteux",0),("1877","Dîner Trapp : Flaubert invité d'honneur",1),
         ("1880","Les Soirées de Médan ; Le Roman expérimental",0),("1884","Huysmans, À rebours",0),
         ("1887","Manifeste des Cinq contre La Terre",1),("1891","Enquête de Jules Huret dans L'Écho de Paris",1)],
  frise_bas="D'après Stalloni, qui suit les trois phases proposées par Colette Becker.",
  route="Lecture critique : l'histoire du naturalisme comme histoire d'un groupe (naissance, âge d'or, dispersion), et le Félibrige de Mistral et Daudet.",
), dict(
  id="bainville-zola",
  auteur="Jacques Bainville",
  court="Bainville, Au seuil du siècle : « L'école naturaliste » (4 octobre 1902)",
  ref=BAINVILLE_REF, lien=BAINVILLE_LIEN,
  titre="Le naturalisme vu par un adversaire",
  idees=[
    ("Date","Article du 4 octobre 1902, cinq jours après la mort de Zola (29 septembre), au cœur de l'affaire Dreyfus."),
    ("Tri","Flaubert, les Goncourt, Daudet, Maupassant sont des « gentilshommes » ; Zola seul est « peuple »."),
    ("Armes","Mépris de classe, vocabulaire de la maladie, et un racisme ouvert contre l'origine italienne de Zola."),
    ("Position","Bainville, proche de l'Action française et antidreyfusard : sa critique est une prise de position."),
  ],
  citations=[("Zola, c'était en somme la personnification du certificat d'études primaires.","Bainville, 4 octobre 1902"),
             ("Ce qui est écrit pour un jour devrait périr avec le jour.","Bainville, avant-propos, 1927")],
  debat="Ce texte nous apprend-il plus sur Zola ou sur la place que Bainville veut occuper dans le champ ?",
  frise_titre="Zola, de J'accuse au Panthéon",
  frise=[("1898","13 janvier : J'accuse… !, dans L'Aurore",1),("1899","Revue L'Action française, nationaliste et antidreyfusarde",1),
         ("1902","29 septembre : mort de Zola ; article de Bainville",0),("1906","Dreyfus réhabilité",1),
         ("1908","Les cendres de Zola au Panthéon",1),("1927","Bainville réédite ses articles",0)],
  frise_bas="La valeur d'un écrivain se joue aussi dans la presse, les ligues, les tribunaux et les cérémonies.",
  route="Lecture critique d'époque : un jeune critique antidreyfusard juge l'école naturaliste en 1902. Document à lire avec distance, en sociocritique.",
)],

6: [dict(
  id="stalloni-symbolisme",
  auteur="Yves Stalloni",
  court="Stalloni, Écoles et courants littéraires : « Le Symbolisme »",
  ref=STALLONI_REF, lien=STALLONI_LIEN,
  titre="Du café décadent au manifeste symboliste",
  idees=[
    ("Décadence","Après 1870 : Zutistes, Hydropathes, le Chat noir ; Verlaine, « Je suis l'Empire à la fin de la Décadence » (1883)."),
    ("Manifeste","Moréas dans Le Figaro (1886) ; revues : Le Symboliste, La Plume, Mercure de France, La Revue blanche."),
    ("Suggérer","Mallarmé : ne pas nommer l'objet mais le suggérer ; Verlaine : la musique avant toute chose."),
    ("Vers libre","Gustave Kahn, Laforgue, Viélé-Griffin : le rythme suit le souffle, plus le décompte."),
  ],
  citations=[("Nommer un objet, c'est supprimer les trois-quarts de la jouissance du poème…","Mallarmé, enquête Huret, 1891, cité par Stalloni"),
             ("Les grands créateurs du Symbolisme se situent en marge de l'École.","Stalloni, « Le Symbolisme »")],
  debat="Pourquoi Rimbaud, Verlaine et Mallarmé restent-ils en marge de l'école qui se réclame d'eux ?",
  route="Lecture critique : la décadence, le manifeste de Moréas, Mallarmé et le vers libre. Attention : le manuel date le manifeste de 1866 au lieu de 1886.",
)],

7: [dict(
  id="bainville-symbolistes",
  auteur="Jacques Bainville",
  court="Bainville, Au seuil du siècle : « Le poète maudit » (1904), « Un poète vraiment mystique » (1904)",
  ref=BAINVILLE_REF, lien=BAINVILLE_LIEN,
  titre="Que deviennent les poètes de 1889 ?",
  idees=[
    ("Cénacles","Petites revues, livres tirés à cinquante exemplaires, mépris de tout ce qui n'est pas le culte du verbe."),
    ("Destins","Vingt ans après : la Bourse, un riche mariage, la presse à grand tirage, la politique pendant l'affaire Dreyfus."),
    ("Maudit","Verlaine, rejeté selon Bainville par les catholiques (sa vie) et par les révolutionnaires (sa foi)."),
    ("Regard","Le critique ne décrit pas seulement : il distribue les bons et les mauvais destins."),
  ],
  citations=[("Il y avait des cénacles, et de jeunes revues, et des livres qu'on imprimait à cinquante exemplaires.","Bainville, 30 juillet 1904"),
             ("Alors Paul Verlaine était prince.","Bainville, 30 juillet 1904")],
  debat="Vers 1900, qui consacre un poète : ses pairs, l'Église, l'État, la presse ou le public ?",
  route="Lecture critique d'époque : ce que deviennent les jeunes symbolistes vers 1900, vus par un critique de droite. À relier au scandale et à la consécration.",
)],
}
