# Passages pour le commentaire : textes du domaine public, relevés sur fr.wikisource.org (octobre 2026).
# Chaque passage : id, fiche (place dans la fiche du cours), titre, source, edition (note d'édition),
# vers (True = poésie, numérotation par vers), texte, questions (pour l'étudiant), pistes (pour l'enseignant).
# Les vers d'une même strophe sont séparés par \n ; les strophes et les paragraphes par une ligne vide.

PASSAGES = {
1: [
 dict(id="rousseau", fiche="A.2 (proposition)", titre="Rousseau, Me voici donc seul sur la terre",
  source="Rousseau, Les Rêveries du promeneur solitaire (1782), Première promenade, premier paragraphe",
  edition="Texte de l'édition originale sur Wikisource ; orthographe modernisée (et pour &, -ait pour -oit).",
  vers=False,
  texte="""Me voici donc seul sur la terre, n'ayant plus de frère, de prochain, d'ami, de société que moi-même. Le plus sociable et le plus aimant des humains en a été proscrit par un accord unanime. Ils ont cherché dans les raffinements de leur haine quel tourment pouvait être le plus cruel à mon âme sensible, et ils ont brisé violemment tous les liens qui m'attachaient à eux. J'aurais aimé les hommes en dépit d'eux-mêmes. Ils n'ont pu qu'en cessant de l'être se dérober à mon affection. Les voilà donc étrangers, inconnus, nuls enfin pour moi puisqu'ils l'ont voulu. Mais moi, détaché d'eux et de tout, que suis-je moi-même ? Voilà ce qui me reste à chercher. Malheureusement cette recherche doit être précédée d'un coup d'œil sur ma position. C'est une idée par laquelle il faut nécessairement que je passe, pour arriver d'eux à moi.""",
  questions=[("Repérer", "Relevez les pronoms (je, moi, ils, eux) : comment le texte oppose-t-il deux camps ?"),
             ("Analyser", "L'énumération de la première phrase : quel effet de dépouillement produit-elle ?"),
             ("Interpréter", "Que suis-je moi-même ? En quoi cette question ouvre-t-elle l'écriture du moi romantique ?"),
             ("Oral", "À quel public s'adresse un livre écrit, dit-il, pour lui seul ?")],
  pistes="Le texte construit une scène de procès inversé : ils (les hommes, la société des philosophes, le complot) ont proscrit, moi je suis la victime innocente. L'énumération négative (frère, prochain, ami, société) va du lien de sang au lien social : tout est retiré, il ne reste que moi-même. Le paradoxe central : le plus sociable des hommes est seul, ce qui fait de la solitude une injustice et non un choix. La question finale déplace le texte de la plainte vers l'introspection : d'eux à moi. Pour la sociocritique : un écrivain exclu du champ (rupture avec Diderot, Voltaire, les encyclopédistes) transforme son exclusion en capital symbolique, la sincérité. Écrit en 1776-1778, publié en 1782, après la mort de Rousseau (1778)."),
 dict(id="rene", fiche="A.2 (proposition)", titre="Chateaubriand, René : l'automne et les orages désirés",
  source="Chateaubriand, René (1802 dans le Génie du christianisme ; édition séparée 1805)",
  edition="Texte de Wikisource.", vers=False,
  texte="""Le jour, je m'égarais sur de grandes bruyères terminées par des forêts. Qu'il fallait peu de chose à ma rêverie ! une feuille séchée que le vent chassait devant moi, une cabane dont la fumée s'élevait dans la cime dépouillée des arbres, la mousse qui tremblait au souffle du nord sur le tronc d'un chêne, une roche écartée, un étang désert où le jonc flétri murmurait ! Le clocher solitaire s'élevant au loin dans la vallée a souvent attiré mes regards ; souvent j'ai suivi des yeux les oiseaux de passage qui volaient au-dessus de ma tête. Je me figurais les bords ignorés, les climats lointains où ils se rendent ; j'aurais voulu être sur leurs ailes. Un secret instinct me tourmentait ; je sentais que je n'étais moi-même qu'un voyageur, mais une voix du ciel semblait me dire : « Homme, la saison de ta migration n'est pas encore venue ; attends que le vent de la mort se lève, alors tu déploieras ton vol vers ces régions inconnues que ton cœur demande. »

« Levez-vous vite, orages désirés qui devez emporter René dans les espaces d'une autre vie ! »""",
  questions=[("Repérer", "Relevez les éléments du paysage : quelle saison, quelles couleurs, quels sons ?"),
             ("Analyser", "Qu'il fallait peu de chose : comment la phrase exclamative et l'énumération miment-elles la rêverie ?"),
             ("Interpréter", "Les oiseaux de passage et la migration : que désire René, partir ou mourir ?"),
             ("Langue", "René se nomme à la troisième personne dans la dernière phrase : quel effet ?")],
  pistes="Le paysage est un état d'âme : automne, feuille séchée, cime dépouillée, jonc flétri, tout dit le déclin. L'énumération avec articles indéfinis (une feuille, une cabane, une roche) montre une rêverie qui se nourrit de presque rien. Les oiseaux migrateurs ouvrent le thème du voyage, aussitôt converti en désir de mort (le vent de la mort). L'apostrophe finale aux orages, avec impératif et troisième personne, met en scène le moi comme un personnage tragique : c'est la naissance du vague des passions, que Chateaubriand prétend condamner (le père Souël blâme René à la fin du récit). Mal du siècle avant la lettre. Piège : René n'est pas un roman autobiographique au sens strict, c'est un épisode d'une apologie du christianisme."),
],
2: [
 dict(id="lac", fiche="A.1 · paire 1 (Méditations poétiques)", titre="Lamartine, Le Lac (poème intégral)",
  source="Lamartine, Méditations poétiques (1820), Le Lac",
  edition="Texte de l'édition originale de 1820 (Wikisource), orthographe modernisée (-ait pour -oit, abîmes pour abymes). Les éditions plus tardives présentent quelques variantes (Le flot plus attentif).",
  vers=True,
  texte="""Ainsi, toujours poussés vers de nouveaux rivages,
Dans la nuit éternelle emportés sans retour,
Ne pourrons-nous jamais sur l'océan des âges
Jeter l'ancre un seul jour ?

Ô lac ! l'année à peine a fini sa carrière,
Et près des flots chéris qu'elle devait revoir,
Regarde ! je viens seul m'asseoir sur cette pierre
Où tu la vis s'asseoir !

Tu mugissais ainsi sous ces roches profondes,
Ainsi tu te brisais sur leurs flancs déchirés,
Ainsi le vent jetait l'écume de tes ondes
Sur ses pieds adorés.

Un soir, t'en souvient-il ? nous voguions en silence ;
On n'entendait au loin, sur l'onde et sous les cieux,
Que le bruit des rameurs qui frappaient en cadence
Tes flots harmonieux.

Tout à coup des accents inconnus à la terre
Du rivage charmé frappèrent les échos ;
Le flot fut attentif, et la voix qui m'est chère
Laissa tomber ces mots :

« Ô temps ! suspends ton vol ; et vous, heures propices
Suspendez votre cours :
Laissez-nous savourer les rapides délices
Des plus beaux de nos jours !

« Assez de malheureux ici-bas vous implorent,
Coulez, coulez pour eux ;
Prenez avec leurs jours les soins qui les dévorent,
Oubliez les heureux.

« Mais je demande en vain quelques moments encore,
Le temps m'échappe et fuit ;
Je dis à cette nuit : Sois plus lente ; et l'aurore
Va dissiper la nuit.

« Aimons donc, aimons donc ! de l'heure fugitive,
Hâtons-nous, jouissons !
L'homme n'a point de port, le temps n'a point de rive ;
Il coule, et nous passons ! »

Temps jaloux, se peut-il que ces moments d'ivresse,
Où l'amour à longs flots nous verse le bonheur,
S'envolent loin de nous de la même vitesse
Que les jours du malheur ?

Eh quoi ! n'en pourrons-nous fixer au moins la trace ?
Quoi ! passés pour jamais ! quoi ! tout entiers perdus !
Ce temps qui les donna, ce temps qui les efface,
Ne nous les rendra plus !

Éternité, néant, passé, sombres abîmes,
Que faites-vous des jours que vous engloutissez ?
Parlez : nous rendrez-vous ces extases sublimes
Que vous nous ravissez ?

Ô lac ! rochers muets ! grottes ! forêt obscure !
Vous, que le temps épargne ou qu'il peut rajeunir,
Gardez de cette nuit, gardez, belle nature,
Au moins le souvenir !

Qu'il soit dans ton repos, qu'il soit dans tes orages,
Beau lac, et dans l'aspect de tes riants coteaux,
Et dans ces noirs sapins, et dans ces rocs sauvages
Qui pendent sur tes eaux.

Qu'il soit dans le zéphyr qui frémit et qui passe,
Dans les bruits de tes bords par tes bords répétés,
Dans l'astre au front d'argent qui blanchit ta surface
De ses molles clartés.

Que le vent qui gémit, le roseau qui soupire,
Que les parfums légers de ton air embaumé,
Que tout ce qu'on entend, l'on voit ou l'on respire,
Tout dise : Ils ont aimé !""",
  questions=[("Structure", "Repérez les trois voix du poème : le poète, la femme aimée, la nature invoquée. Où commence et où finit chacune ?"),
             ("Mètre", "Strophes 6 à 9 : comptez les vers (12 / 6). Pourquoi le rythme change-t-il quand la femme parle ?"),
             ("Figures", "Apostrophes et personnifications (Ô lac, Temps jaloux, Éternité) : à qui le poète parle-t-il, et pourquoi ?"),
             ("Interpréter", "Le poème finit sur Ils ont aimé : le temps est-il vaincu ou seulement retenu ?")],
  pistes="Seize quatrains. Strophes 1-5 : le poète revient seul au lac (le lac du Bourget, Aix-les-Bains) un an après ; la femme aimée (Julie Charles, l'Elvire des Méditations, malade et absente, morte en décembre 1817) ne viendra plus. Strophes 6-9 : discours rapporté de la femme, en alternance alexandrins / hexasyllabes, comme une barcarolle ; la strophe change de rythme parce que la voix change. Strophes 10-12 : retour du poète, questions rhétoriques, crescendo d'exclamations (Quoi ! passés pour jamais !). Strophes 13-16 : invocation à la nature, anaphore de Qu'il soit, énumération qui embrasse tous les sens (entend, voit, respire). Le temps n'est pas vaincu : la nature devient mémoire. Pour l'oral : public de la Restauration, lecteurs lassés de la poésie descriptive du XVIIIe siècle ; succès immédiat en 1820. Piège : le poème n'est pas un poème de deuil au sens strict, la femme est absente, pas encore morte dans la fiction."),
 dict(id="mateo", fiche="Partie B (B.1)", titre="Mérimée, Mateo Falcone : le dénouement",
  source="Mérimée, Mateo Falcone (Revue de Paris, 1829 ; Mosaïque, 1833), dernières pages",
  edition="Texte de Wikisource (Colomba et autres contes et nouvelles). L'édition porte roide mort ; les éditions modernes écrivent raide.",
  vers=False,
  texte="""Les sanglots et les hoquets de Fortunato redoublèrent, et Falcone tenait ses yeux de lynx toujours attachés sur lui. Enfin il frappa la terre de la crosse de son fusil, puis le jeta sur son épaule et reprit le chemin du mâquis en criant à Fortunato de le suivre. L'enfant obéit.

Giuseppa courut après Mateo et lui saisit le bras.

— C'est ton fils, lui dit-elle d'une voix tremblante en attachant ses yeux noirs sur ceux de son mari, comme pour lire ce qui se passait dans son âme.

— Laisse-moi, répondit Mateo : je suis son père.

Giuseppa embrassa son fils et entra en pleurant dans sa cabane. Elle se jeta à genoux devant une image de la Vierge et pria avec ferveur. Cependant Falcone marcha quelque deux cents pas dans le sentier, et ne s'arrêta que dans un petit ravin où il descendit. Il sonda la terre avec la crosse de son fusil et la trouva molle et facile à creuser. L'endroit lui parut convenable pour son dessein.

— Fortunato, va auprès de cette grosse pierre.

L'enfant fit ce qu'il lui commandait, puis il s'agenouilla.

— Dis tes prières.

— Mon père, mon père, ne me tuez pas.

— Dis tes prières ! répéta Mateo d'une voix terrible.

L'enfant, tout en balbutiant et en sanglotant, récita le Pater et le Credo. Le père, d'une voix forte, répondait Amen ! à la fin de chaque prière.

— Sont-ce là toutes les prières que tu sais ?

— Mon père, je sais encore l'Ave Maria et la litanie que ma tante m'a apprise.

— Elle est bien longue, n'importe.

L'enfant acheva la litanie d'une voix éteinte.

— As-tu fini ?

— Oh ! mon père, grâce ! pardonnez-moi ! Je ne le ferai plus ! Je prierai tant mon cousin le caporale qu'on fera grâce au Gianetto !

Il parlait encore ; Mateo avait armé son fusil et le couchait en joue en lui disant : Que Dieu te pardonne ! L'enfant fit un effort désespéré pour se relever et embrasser les genoux de son père ; mais il n'en eut pas le temps. Mateo fit feu, et Fortunato tomba roide mort.

Sans jeter un coup d'œil sur le cadavre, Mateo reprit le chemin de sa maison pour aller chercher une bêche afin d'enterrer son fils. Il avait fait à peine quelques pas qu'il rencontra Giuseppa, qui accourait alarmée du coup de feu.""",
  questions=[("Repérer", "Comptez les répliques de Mateo : combien de mots ? Que dit cette économie de parole ?"),
             ("Analyser", "Le narrateur juge-t-il ? Relevez les verbes d'action et l'absence de commentaire."),
             ("Interpréter", "Je suis son père : que signifie ici la paternité, l'amour ou la loi ?"),
             ("Comparer", "Une nouvelle classique : unité d'action, peu de personnages, chute. Montrez-le sur ce passage.")],
  pistes="Contexte : Fortunato, dix ans, a caché le bandit Gianetto, puis l'a livré aux voltigeurs contre une montre en argent. Mateo, qui a l'hospitalité pour loi, tue son fils unique pour trahison. Le passage est construit en accélération : phrases brèves, dialogue sec, prières énumérées (Pater, Credo, Ave Maria, litanie) qui retardent la mort et créent la tension. Le narrateur reste impassible (aucun adjectif de jugement sur Mateo) : c'est l'art de la concision de Mérimée, qui laisse au lecteur l'horreur. Sociocritique : la Corse est vue depuis Paris comme un monde d'honneur archaïque, objet d'exotisme pour les lecteurs de la Revue de Paris ; deux lois s'affrontent, celle de l'État (voltigeurs, caporal) et celle du clan. Piège : ne pas lire Mateo comme un monstre ; le texte présente un code, pas une pathologie."),
],
3: [
 dict(id="morte", fiche="Partie B (B.1)", titre="Gautier, La Morte amoureuse : l'ouverture",
  source="Gautier, La Morte amoureuse (Chronique de Paris, 1836), premier paragraphe",
  edition="Texte de Wikisource.", vers=False,
  texte="""Vous me demandez, frère, si j'ai aimé ; oui. — C'est une histoire singulière et terrible, et, quoique j'aie soixante-six ans, j'ose à peine remuer la cendre de ce souvenir. Je ne veux rien vous refuser, mais je ne ferais pas à une âme moins éprouvée un pareil récit. Ce sont des événements si étranges, que je ne puis croire qu'ils me soient arrivés. J'ai été pendant plus de trois ans le jouet d'une illusion singulière et diabolique. Moi, pauvre prêtre de campagne, j'ai mené en rêve toutes les nuits (Dieu veuille que ce soit un rêve !) une vie de damné, une vie de mondain et de Sardanapale. Un seul regard trop plein de complaisance jeté sur une femme pensa causer la perte de mon âme ; mais enfin, avec l'aide de Dieu et de mon saint patron, je suis parvenu à chasser l'esprit malin qui s'était emparé de moi. Mon existence s'était compliquée d'une existence nocturne entièrement différente. Le jour, j'étais un prêtre du Seigneur, chaste, occupé de la prière et des choses saintes ; la nuit, dès que j'avais fermé les yeux, je devenais un jeune seigneur, fin connaisseur en femmes, en chiens et en chevaux, jouant aux dés, buvant et blasphémant ; et lorsqu'au lever de l'aube je me réveillais, il me semblait au contraire que je m'endormais et que je rêvais que j'étais prêtre.""",
  questions=[("Situation", "Qui parle, à qui, et quand ? Que nous apprend la première phrase ?"),
             ("Fantastique", "Relevez les mots du doute (illusion, rêve, étranges) : le narrateur sait-il ce qu'il a vécu ?"),
             ("Structure", "Le jour / la nuit : montrez comment la phrase oppose deux vies, puis les fait basculer."),
             ("Ouvrir", "Pourquoi un prêtre comme narrateur ? Que gagne le récit fantastique à ce choix ?")],
  pistes="Récit enchâssé : le vieux prêtre Romuald (66 ans) répond à un jeune confrère. La première phrase est déjà une chute inversée : la réponse (oui) précède l'histoire. Le fantastique au sens de Todorov repose sur l'hésitation : illusion, rêve, (Dieu veuille que ce soit un rêve !) ; le narrateur lui-même ne tranche pas. La dernière phrase opère un renversement vertigineux : le réveil devient endormissement, la vie de prêtre devient le rêve. Clarimonde, courtisane morte devenue vampire, est l'objet de ce désir. Contexte : publiée en 1836 dans la Chronique de Paris, la revue de Balzac ; Gautier est l'auteur de la préface de Mademoiselle de Maupin (1835), manifeste de l'art pour l'art. Sociocritique : le conflit entre l'Église et la vie mondaine, entre le corps et le salut, dans une France de la monarchie de Juillet."),
 dict(id="stendhal", fiche="A.2 (proposition)", titre="Stendhal, le miroir sur la grande route",
  source="Stendhal, Le Rouge et le Noir (1830), livre II, chapitre 19",
  edition="Texte de Wikisource.", vers=False,
  texte="""Eh, monsieur, un roman est un miroir qui se promène sur une grande route. Tantôt il reflète à vos yeux l'azur des cieux, tantôt la fange des bourbiers de la route. Et l'homme qui porte le miroir dans sa hotte sera par vous accusé d'être immoral ! Son miroir montre la fange, et vous accusez le miroir ! Accusez bien plutôt le grand chemin où est le bourbier, et plus encore l'inspecteur des routes qui laisse l'eau croupir et le bourbier se former.""",
  questions=[("Situation", "Le narrateur interrompt son récit : à qui parle-t-il (Eh, monsieur) ?"),
             ("Image", "Développez la métaphore : le roman, le miroir, la route, la fange, l'inspecteur des routes."),
             ("Argument", "Comment le passage passe-t-il de la défense du romancier à l'accusation de la société ?"),
             ("Débat", "Un miroir est-il neutre ? Celui qui choisit la route choisit aussi ce qu'il reflète.")],
  pistes="Intrusion d'auteur au milieu du livre II, au moment où le personnage de Mathilde de La Mole pourrait choquer. La métaphore est une plaidoirie : le romancier ne fait que refléter, la faute est à la route (la société) et surtout à l'inspecteur des routes (le gouvernement de la Restauration). L'argument est ironique et politique. Pour l'oral : public visé, les lecteurs bien-pensants de 1830 ; nouveauté, revendiquer le roman comme document sur le présent. Sociocritique : le miroir n'est jamais neutre, il est porté dans une hotte par quelqu'un qui marche ; Bourdieu dirait que la position du romancier dans le champ (libéral, marginal) oriente le reflet."),
 dict(id="goriot", fiche="A.2 (proposition)", titre="Balzac, Le Père Goriot : À nous deux maintenant !",
  source="Balzac, Le Père Goriot (1835), dernière page",
  edition="Texte du domaine public (édition Furne).", vers=False,
  texte="""Rastignac, resté seul, fit quelques pas vers le haut du cimetière et vit Paris tortueusement couché le long des deux rives de la Seine, où commençaient à briller les lumières. Ses yeux s'attachèrent presque avidement entre la colonne de la place Vendôme et le dôme des Invalides, là où vivait ce beau monde dans lequel il avait voulu pénétrer. Il lança sur cette ruche bourdonnant un regard qui semblait par avance en pomper le miel, et dit ces mots grandioses :

« À nous deux maintenant ! »

Et pour premier acte du défi qu'il portait à la Société, Rastignac alla dîner chez madame de Nucingen.""",
  questions=[("Lieu", "Où est Rastignac ? Que voit-il ? Relevez les repères topographiques de Paris."),
             ("Image", "La ruche et le miel : que dit la métaphore de la société parisienne ?"),
             ("Ironie", "Mots grandioses, puis dîner chez madame de Nucingen : comment la dernière phrase retourne-t-elle la scène ?"),
             ("Ouvrir", "Fin d'un roman ou début d'une carrière ? Pensez au retour des personnages dans La Comédie humaine.")],
  pistes="Rastignac vient d'enterrer le père Goriot au Père-Lachaise, seul avec un domestique ; il a dû emprunter vingt sous. Du haut de la colline, il domine Paris : la verticalité dit l'ambition. Entre la place Vendôme et les Invalides, c'est le faubourg Saint-Germain et les quartiers riches. La ruche bourdonnant et le miel : la société est un organisme qui produit de la richesse, Rastignac veut en être le parasite. La dernière phrase est ironique : le défi commence par un dîner chez la fille du mort, maîtresse de Rastignac. Rastignac reviendra dans d'autres romans (ministre, pair de France) : c'est le principe du retour des personnages. Sociocritique : la scène met en image la conversion du capital (le jeune noble pauvre de province entre dans le champ du pouvoir parisien)."),
],
4: [
 dict(id="etranger", fiche="A.1 · paire 3 (Le Spleen de Paris)", titre="Baudelaire, L'Étranger (poème intégral)",
  source="Baudelaire, Le Spleen de Paris (Petits poèmes en prose, 1869), poème I",
  edition="Texte de Wikisource.", vers=False,
  texte="""— Qui aimes-tu le mieux, homme énigmatique, dis ? ton père, ta mère, ta sœur ou ton frère ?

— Je n'ai ni père, ni mère, ni sœur, ni frère.

— Tes amis ?

— Vous vous servez là d'une parole dont le sens m'est resté jusqu'à ce jour inconnu.

— Ta patrie ?

— J'ignore sous quelle latitude elle est située.

— La beauté ?

— Je l'aimerais volontiers, déesse et immortelle.

— L'or ?

— Je le hais comme vous haïssez Dieu.

— Eh ! qu'aimes-tu donc, extraordinaire étranger ?

— J'aime les nuages… les nuages qui passent… là-bas… là-bas… les merveilleux nuages !""",
  questions=[("Forme", "Un poème en prose dialogué : où sont le rythme et la musique sans vers ni rime ?"),
             ("Énonciation", "Tu d'un côté, vous de l'autre : que dit ce changement de pronom ?"),
             ("Valeurs", "Famille, amitié, patrie, beauté, or : dans quel ordre l'étranger refuse-t-il les valeurs ?"),
             ("Fin", "Pourquoi finir sur les nuages ? Comment la ponctuation (points de suspension) fait-elle sentir l'envol ?")],
  pistes="Premier poème du recueil, il sert de seuil : l'étranger est la figure du poète. Le questionneur tutoie (familiarité bourgeoise), l'étranger répond en vouvoyant (distance). Les valeurs refusées vont du plus intime au plus social, puis viennent la beauté (seule acceptée, au conditionnel, comme idéal inaccessible) et l'or (rejet violent, avec l'ironie : comme vous haïssez Dieu, le bourgeois est accusé d'athéisme pratique). La fin crée une musique par répétition (les nuages, là-bas) et ponctuation suspensive. Dans la dédicace à Arsène Houssaye, Baudelaire rêve d'une prose poétique, musicale sans rythme et sans rime : L'Étranger en est la démonstration. Pour l'oral : comparer avec Gide (paire 3), autre prose poétique adressée à un tu."),
 dict(id="enivrez", fiche="A.1 · paire 3 (Le Spleen de Paris)", titre="Baudelaire, Enivrez-vous (poème intégral)",
  source="Baudelaire, Le Spleen de Paris (1869), poème XXXIII",
  edition="Texte de Wikisource.", vers=False,
  texte="""Il faut être toujours ivre. Tout est là : c'est l'unique question. Pour ne pas sentir l'horrible fardeau du Temps qui brise vos épaules et vous penche vers la terre, il faut vous enivrer sans trêve.

Mais de quoi ? De vin, de poésie ou de vertu, à votre guise. Mais enivrez-vous.

Et si quelquefois, sur les marches d'un palais, sur l'herbe verte d'un fossé, dans la solitude morne de votre chambre, vous vous réveillez, l'ivresse déjà diminuée ou disparue, demandez au vent, à la vague, à l'étoile, à l'oiseau, à l'horloge, à tout ce qui fuit, à tout ce qui gémit, à tout ce qui roule, à tout ce qui chante, à tout ce qui parle, demandez quelle heure il est ; et le vent, la vague, l'étoile, l'oiseau, l'horloge, vous répondront : « Il est l'heure de s'enivrer ! Pour n'être pas les esclaves martyrisés du Temps, enivrez-vous ; enivrez-vous sans cesse ! De vin, de poésie ou de vertu, à votre guise. »""",
  questions=[("Structure", "Trois paragraphes : une thèse, une question, une scène. Résumez chacun en une phrase."),
             ("Rythme", "Repérez les reprises (enivrez-vous, à tout ce qui…, le vent, la vague) : comment la prose devient-elle musique ?"),
             ("Temps", "Le Temps avec une majuscule : quelle figure ? Comparez avec Le Lac (semaine 2)."),
             ("Plan", "Proposez une problématique et deux axes pour un commentaire.")],
  pistes="Poème injonctif (il faut, impératifs) qui ressemble à un sermon détourné. Le Temps personnifié écrase l'homme : c'est le spleen ; l'ivresse est la seule réponse, et son objet est indifférent (vin, poésie, vertu : la vertu placée à égalité avec le vin est une provocation). Le troisième paragraphe est une longue phrase circulaire : énumérations, gradation, puis reprise des mêmes mots dans la réponse de la nature, qui forme un refrain. Comparaison avec Lamartine : chez Lamartine, la nature garde le souvenir ; chez Baudelaire, elle répond par l'injonction de fuir le temps. Problématique possible : comment une prose sans vers fait-elle de l'ivresse une réponse au temps ? Axes : 1. une parole d'autorité qui renverse la morale ; 2. une musique de la prose qui produit l'ivresse qu'elle recommande."),
 dict(id="coeur", fiche="Partie B (B.1)", titre="Flaubert, Un cœur simple : l'ouverture",
  source="Flaubert, Un cœur simple (Trois Contes, 1877), chapitre I, début",
  edition="Texte de Wikisource.", vers=False,
  texte="""Pendant un demi-siècle, les bourgeoises de Pont-l'Évêque envièrent à Mme Aubain sa servante Félicité.

Pour cent francs par an, elle faisait la cuisine et le ménage, cousait, lavait, repassait, savait brider un cheval, engraisser les volailles, battre le beurre, et resta fidèle à sa maîtresse, — qui cependant n'était pas une personne agréable.

Elle avait épousé un beau garçon sans fortune, mort au commencement de 1809, en lui laissant deux enfants très jeunes avec une quantité de dettes. Alors, elle vendit ses immeubles, sauf la ferme de Toucques et la ferme de Geffosses, dont les rentes montaient à 5 000 francs tout au plus, et elle quitta sa maison de Saint-Melaine pour en habiter une autre moins dispendieuse, ayant appartenu à ses ancêtres et placée derrière les halles.

Cette maison, revêtue d'ardoises, se trouvait entre un passage et une ruelle aboutissant à la rivière. Elle avait intérieurement des différences de niveau qui faisaient trébucher. Un vestibule étroit séparait la cuisine de la salle où Mme Aubain se tenait tout le long du jour, assise près de la croisée dans un fauteuil de paille. Contre le lambris, peint en blanc, s'alignaient huit chaises d'acajou. Un vieux piano supportait, sous un baromètre, un tas pyramidal de boîtes et de cartons. Deux bergères de tapisserie flanquaient la cheminée en marbre jaune et de style Louis XV. La pendule, au milieu, représentait un temple de Vesta, — et tout l'appartement sentait un peu le moisi, car le plancher était plus bas que le jardin.""",
  questions=[("Incipit", "La première phrase résume cinquante ans : qui est le sujet grammatical ? qui est le personnage principal ?"),
             ("Énumération", "Relevez les verbes de la deuxième phrase : que dit leur accumulation de la vie de Félicité ?"),
             ("Argent", "Cent francs par an, 5 000 francs de rente : que montrent ces chiffres ?"),
             ("Description", "Le baromètre, la pendule, le moisi : quels détails réalistes portent un sens caché ?")],
  pistes="Ironie de la première phrase : Félicité n'est d'abord qu'un objet d'envie entre bourgeoises ; le conte va lui rendre le premier rôle. La deuxième phrase accumule les verbes de travail et se termine par une incise ironique (le tiret) sur la maîtresse. Les chiffres opposent le salaire de la servante (100 francs par an) à la rente de la maîtresse (5 000 francs) : deux classes, un même toit. La description de la maison est minutieuse mais signifiante : différences de niveau qui font trébucher, objets entassés, temple de Vesta (déesse du foyer, des vierges, comme Félicité), odeur de moisi (déclin d'une bourgeoisie). Flaubert écrit Un cœur simple pour George Sand, qui lui reprochait sa froideur (selon sa correspondance de 1876). Piège : le style indirect libre et l'impersonnalité ne sont pas de l'indifférence."),
],
5: [
 dict(id="boule", fiche="Partie B (Les Soirées de Médan)", titre="Maupassant, Boule de suif : la déroute",
  source="Maupassant, Boule de suif, Les Soirées de Médan (1880), premier paragraphe",
  edition="Texte de Wikisource.", vers=False,
  texte="""Pendant plusieurs jours de suite des lambeaux d'armée en déroute avaient traversé la ville. Ce n'était point de la troupe, mais des hordes débandées. Les hommes avaient la barbe longue et sale, des uniformes en guenilles, et ils avançaient d'une allure molle, sans drapeau, sans régiment. Tous semblaient accablés, éreintés, incapables d'une pensée ou d'une résolution, marchant seulement par habitude, et tombant de fatigue sitôt qu'ils s'arrêtaient. On voyait surtout des mobilisés, gens pacifiques, rentiers tranquilles, pliant sous le poids du fusil ; des petits moblots alertes, faciles à l'épouvante et prompts à l'enthousiasme, prêts à l'attaque comme à la fuite ; puis, au milieu d'eux, quelques culottes rouges, débris d'une division moulue dans une grande bataille ; des artilleurs sombres alignés avec ces fantassins divers ; et, parfois, le casque brillant d'un dragon au pied pesant qui suivait avec peine la marche plus légère des lignards.""",
  questions=[("Temps", "Plus-que-parfait et imparfait : pourquoi l'histoire commence-t-elle après la défaite ?"),
             ("Images", "Lambeaux, hordes, guenilles : quelle image de l'armée française de 1870 ?"),
             ("Énumération", "Mobilisés, moblots, culottes rouges, artilleurs, dragon : comment la phrase défait-elle l'ordre militaire ?"),
             ("Recueil", "Les six nouvelles de Médan parlent de la guerre de 1870 : pourquoi ce choix commun en 1880 ?")],
  pistes="Ouverture sur la débâcle de l'hiver 1870-1871, à Rouen occupée par les Prussiens. Les temps du passé installent l'après-coup : la guerre est perdue avant le récit. Le lexique déshumanise l'armée (lambeaux, hordes, débris, moulue) et défait l'héroïsme patriotique. L'énumération des corps de troupe mêle bourgeois armés et soldats de métier : la société entière est en déroute. Le recueil de Médan (1880) réunit Zola et cinq jeunes naturalistes (Maupassant, Huysmans, Céard, Hennique, Alexis) contre le récit patriotique de la guerre ; Boule de suif fait de Maupassant un auteur reconnu. Sociocritique : la diligence de Boule de suif est un modèle réduit de la société (nobles, bourgeois, religieuses, démocrate, prostituée) qui sacrifie la plus pauvre."),
 dict(id="rideau", fiche="Partie B (Les Diaboliques)", titre="Barbey d'Aurevilly, Le Rideau cramoisi : le cadre",
  source="Barbey d'Aurevilly, Le Rideau cramoisi, Les Diaboliques (1874), début",
  edition="Texte de Wikisource.", vers=False,
  texte="""Il y a terriblement d'années, je m'en allais chasser le gibier d'eau dans les marais de l'Ouest, — et comme il n'y avait pas alors de chemins de fer dans le pays où il me fallait voyager, je prenais la diligence de *** qui passait à la patte d'oie du château de Rueil et qui, pour le moment, n'avait dans son coupé qu'une seule personne. Cette personne, très remarquable à tous égards, et que je connaissais pour l'avoir beaucoup rencontrée dans le monde, était un homme que je vous demanderai la permission d'appeler le vicomte de Brassard. Précaution probablement inutile ! Les quelques centaines de personnes qui se nomment le monde à Paris sont bien capables de mettre ici son nom véritable…""",
  questions=[("Voix", "Qui dit je ? À qui s'adresse le vous ? Repérez le récit cadre."),
             ("Style", "Terriblement d'années : quel registre ? Quel effet sur le lecteur ?"),
             ("Monde", "Les quelques centaines de personnes qui se nomment le monde : quelle société, quel ton ?"),
             ("Ouvrir", "Pourquoi raconter une histoire dans une diligence, la nuit ?")],
  pistes="Récit encadré : un narrateur-témoin rencontre le vicomte de Brassard, ancien officier dandy, qui lui racontera, en passant devant une fenêtre au rideau cramoisi, l'aventure de sa jeunesse avec Alberte, jeune fille silencieuse qui se donne à lui la nuit et meurt dans ses bras. L'adverbe terriblement, inattendu devant d'années, donne le ton : hyperbole aristocratique, oralité de salon. L'ironie sur le monde (quelques centaines de personnes) dit l'appartenance de Barbey à une élite et son mépris pour le présent démocratique. Contexte : Les Diaboliques sont saisies en 1874 pour outrage à la morale ; Barbey, catholique et monarchiste, peint le mal pour le condamner, dit-il dans la préface. Sociocritique : un dandysme de la noblesse déclassée sous la Troisième République."),
 dict(id="classe", fiche="Partie B (B.1)", titre="Daudet, La Dernière Classe : Vive la France !",
  source="Daudet, La Dernière Classe (1872), Contes du lundi (1873), fin",
  edition="Texte de Wikisource.", vers=False,
  texte="""Tout de même, il eut le courage de nous faire la classe jusqu'au bout. Après l'écriture, nous eûmes la leçon d'histoire ; ensuite les petits chantèrent tous ensemble le ba be bi bo bu. Là-bas, au fond de la salle, le vieux Hauser avait mis ses lunettes, et, tenant son abécédaire à deux mains, il épelait les lettres avec eux. On voyait qu'il s'appliquait, lui aussi ; sa voix tremblait d'émotion, et c'était si drôle de l'entendre, que nous avions tous envie de rire et de pleurer. Ah ! je m'en souviendrai de cette dernière classe…

Tout à coup l'horloge de l'église sonna midi, puis l'Angelus. Au même moment, les trompettes des Prussiens qui revenaient de l'exercice éclatèrent sous nos fenêtres… M. Hamel se leva tout pâle, dans sa chaire. Jamais il ne m'avait paru si grand.

« Mes amis, dit-il, mes amis, je… je… »

Mais quelque chose l'étouffait. Il ne pouvait pas achever sa phrase.

Alors il se tourna vers le tableau, prit un morceau de craie et, en appuyant de toutes ses forces, il écrivit aussi gros qu'il put :

« VIVE LA FRANCE ! »

Puis il resta là, la tête appuyée au mur, et, sans parler, avec sa main, il nous faisait signe :

« C'est fini… allez-vous-en. »""",
  questions=[("Narrateur", "Le petit Frantz raconte : quel regard d'enfant ? Relevez les marques de l'émotion."),
             ("Sons", "Angelus, trompettes prussiennes, voix tremblante : comment les sons racontent-ils l'histoire ?"),
             ("Geste", "M. Hamel ne peut pas parler et écrit : que signifie ce passage de la voix à l'écriture ?"),
             ("Débat", "Un conte patriotique : quelle image de la langue française propose-t-il ? Qu'oublie-t-il (l'alsacien) ?")],
  pistes="Contexte : après la défaite de 1870 et le traité de Francfort (1871), l'Alsace et une partie de la Lorraine deviennent allemandes ; l'enseignement se fera en allemand. Le récit est fait par un écolier paresseux, Frantz, qui comprend trop tard la valeur de la langue. Le passage oppose les sons de la communauté (prières, épellation collective) aux trompettes de l'occupant. La parole se brise (je… je…) et l'écriture au tableau prend le relais : la langue devient un monument. Pour un public italien, rapprocher de la question des langues et de l'unité nationale. Débat utile : la plupart des Alsaciens parlaient alors un dialecte alémanique ; le conte construit un mythe national de la langue française. Le conte est devenu un classique des manuels scolaires de la Troisième République."),
 dict(id="horla", fiche="Partie B (B.1)", titre="Maupassant, Le Horla : la première entrée du journal",
  source="Maupassant, Le Horla (version de 1887), 8 mai",
  edition="Texte de Wikisource (recueil Le Horla, Ollendorff).", vers=False,
  texte="""8 mai. — Quelle journée admirable ! J'ai passé toute la matinée étendu sur l'herbe, devant ma maison, sous l'énorme platane qui la couvre, l'abrite et l'ombrage tout entière. J'aime ce pays, et j'aime y vivre parce que j'y ai mes racines, ces profondes et délicates racines, qui attachent un homme à la terre où sont nés et morts ses aïeux, qui l'attachent à ce qu'on pense et à ce qu'on mange, aux usages comme aux nourritures, aux locutions locales, aux intonations des paysans, aux odeurs du sol, des villages et de l'air lui-même.

J'aime ma maison où j'ai grandi. De mes fenêtres, je vois la Seine qui coule, le long de mon jardin, derrière la route, presque chez moi, la grande et large Seine, qui va de Rouen au Havre, couverte de bateaux qui passent.

À gauche, là-bas, Rouen, la vaste ville aux toits bleus, sous le peuple pointu des clochers gothiques. Ils sont innombrables, frêles ou larges, dominés par la flèche de fonte de la cathédrale, et pleins de cloches qui sonnent dans l'air bleu des belles matinées, jetant jusqu'à moi leur doux et lointain bourdonnement de fer, leur chant d'airain que la brise m'apporte, tantôt plus fort et tantôt plus affaibli, suivant qu'elle s'éveille ou s'assoupit.

Comme il faisait bon ce matin !""",
  questions=[("Forme", "Un journal intime daté : quels avantages pour un récit fantastique ?"),
             ("Bonheur", "Relevez le lexique de l'enracinement : pourquoi commencer par un bonheur si stable ?"),
             ("Indice", "La Seine couverte de bateaux qui passent : quel détail prépare la suite ?"),
             ("Lire la suite", "Repérez dans la nouvelle le trois-mâts brésilien : quel lien avec le Horla ?")],
  pistes="La première entrée installe un équilibre parfait (maison, racines, terre des aïeux, paysage rouennais) que le récit va détruire : le narrateur finira par brûler sa maison et envisager le suicide. Le journal, sans témoin ni contrôle, empêche le lecteur de trancher entre folie et présence surnaturelle : c'est l'hésitation fantastique. Indice : plus loin dans la même entrée, un trois-mâts brésilien passe sur la Seine et le narrateur le salue ; c'est avec lui que l'être invisible serait arrivé. Le Horla existe en deux versions (1886, récit fait devant des médecins ; 1887, journal) : la seconde est au programme. Contexte : intérêt de l'époque pour l'hypnose et le magnétisme (Charcot à la Salpêtrière, cours que Maupassant a suivis selon ses biographes). Piège : ne pas réduire la nouvelle à la maladie de Maupassant."),
],
6: [
 dict(id="bateau", fiche="A.1 · paire 2 (Le Bateau ivre)", titre="Rimbaud, Le Bateau ivre (poème intégral)",
  source="Rimbaud, Le Bateau ivre (écrit en 1871 ; publié en 1883 par Verlaine dans Les Poètes maudits)",
  edition="Texte de l'édition Vanier, 1895 (Wikisource). Certaines éditions modernes écrivent mufle et Péninsules démarrées sans virgule.",
  vers=True,
  texte="""Comme je descendais des Fleuves impassibles,
Je ne me sentis plus guidé par les haleurs ;
Des Peaux-Rouges criards les avaient pris pour cibles,
Les ayant cloués nus aux poteaux de couleurs.

J'étais insoucieux de tous les équipages,
Porteur de blés flamands ou de cotons anglais.
Quand avec mes haleurs ont fini ces tapages,
Les Fleuves m'ont laissé descendre où je voulais.

Dans les clapotements furieux des marées,
Moi, l'autre hiver, plus sourd que les cerveaux d'enfants,
Je courus ! Et les Péninsules démarrées,
N'ont pas subi tohu-bohus plus triomphants.

La tempête a béni mes éveils maritimes.
Plus léger qu'un bouchon j'ai dansé sur les flots
Qu'on appelle rouleurs éternels de victimes,
Dix nuits, sans regretter l'œil niais des falots.

Plus douce qu'aux enfants la chair des pommes sures,
L'eau verte pénétra ma coque de sapin
Et des taches de vins bleus et des vomissures
Me lava, dispersant gouvernail et grappin.

Et dès lors, je me suis baigné dans le poème
De la mer, infusé d'astres, et latescent,
Dévorant les azurs verts où, flottaison blême
Et ravie, un noyé pensif parfois descend,

Où, teignant tout à coup les bleuités, délires
Et rythmes lents sous les rutilements du jour,
Plus fortes que l'alcool, plus vastes que nos lyres,
Fermentent les rousseurs amères de l'amour.

Je sais les cieux crevant en éclairs, et les trombes,
Et les ressacs, et les courants, je sais le soir,
L'aube exaltée ainsi qu'un peuple de colombes,
Et j'ai vu quelquefois ce que l'homme a cru voir.

J'ai vu le soleil bas taché d'horreurs mystiques
Illuminant de longs figements violets,
Pareils à des acteurs de drames très antiques,
Les flots roulant au loin leurs frissons de volets ;

J'ai rêvé la nuit verte aux neiges éblouies,
Baisers montant aux yeux des mers avec lenteur,
La circulation des sèves inouïes
Et l'éveil jaune et bleu des phosphores chanteurs.

J'ai suivi des mois pleins, pareille aux vacheries
Hystériques, la houle à l'assaut des récifs,
Sans songer que les pieds lumineux des Maries
Pussent forcer le muffle aux Océans poussifs ;

J'ai heurté, savez-vous ? d'incroyables Florides,
Mêlant aux fleurs des yeux de panthères, aux peaux
D'hommes, des arcs-en-ciel tendus comme des brides,
Sous l'horizon des mers, à de glauques troupeaux ;

J'ai vu fermenter les marais énormes, nasses
Où pourrit dans les joncs tout un Léviathan,
Des écroulements d'eaux au milieu des bonaces,
Et les lointains vers les gouffres cataractant !

Glaciers, soleils d'argent, flots nacreux, cieux de braises.
Échouages hideux au fond des golfes bruns
Où les serpents géants dévorés des punaises
Choient des arbres tordus, avec de noirs parfums.

J'aurais voulu montrer aux enfants ces dorades
Du flot bleu, ces poissons d'or, ces poissons chantants.
Des écumes de fleurs ont béni mes dérades
Et d'ineffables vents m'ont ailé par instants.

Parfois, martyr lassé des pôles et des zones,
La mer dont le sanglot faisait mon roulis doux
Montait vers moi ses fleurs d'ombre aux ventouses jaunes
Et je restais, ainsi qu'une femme à genoux,

Presqu'île, ballottant sur mes bords les querelles
Et les fientes d'oiseaux clabaudeurs aux yeux blonds,
Et je voguais, lorsqu'à travers mes liens frêles
Des noyés descendaient dormir, à reculons.

Or moi, bateau perdu sous les cheveux des anses,
Jeté par l'ouragan dans l'éther sans oiseau,
Moi dont les Monitors et les voiliers des Hanses
N'auraient pas repêché la carcasse ivre d'eau,

Libre, fumant, monté de brumes violettes,
Moi qui trouais le ciel rougeoyant comme un mur
Qui porte, confiture exquise aux bons poètes,
Des lichens de soleil et des morves d'azur,

Qui courais taché de lunules électriques,
Plante folle, escorté des hippocampes noirs,
Quand les Juillets faisaient crouler à coups de triques
Les cieux ultramarins aux ardents entonnoirs,

Moi qui tremblais, sentant geindre à cinquante lieues
Le rut des Béhémots et les Maelstroms épais,
Fileur éternel des immobilités bleues,
Je regrette l'Europe aux anciens parapets.

J'ai vu des archipels sidéraux ! Et des îles
Dont les cieux délirants sont ouverts au vogueur :
— Est-ce en ces nuits sans fonds que tu dors et t'exiles,
Million d'oiseaux d'or, ô future Vigueur ?

Mais, vrai, j'ai trop pleuré ! Les aubes sont navrantes,
Toute lune est atroce et tout soleil amer.
L'âcre amour m'a gonflé de torpeurs enivrantes.
Oh ! que ma quille éclate ! Oh ! que j'aille à la mer !

Si je désire une eau d'Europe, c'est la flache
Noire et froide où, vers le crépuscule embaumé,
Un enfant accroupi, plein de tristesse, lâche
Un bateau frêle comme un papillon de mai.

Je ne puis plus, baigné de vos langueurs, ô lames,
Enlever leur sillage aux porteurs de cotons,
Ni traverser l'orgueil des drapeaux et des flammes,
Ni nager sous les yeux horribles des pontons !""",
  questions=[("Mouvement", "Découpez le poème en quatre temps : libération, immersion, visions, retour. Où placez-vous les frontières ?"),
             ("Je", "Le je est un bateau : relevez les mots qui font du bateau un corps (coque, quille, liens, carcasse)."),
             ("Voyance", "J'ai vu, je sais, j'ai rêvé : comment l'anaphore construit-elle une poésie de la vision ?"),
             ("Fin", "La flache, l'enfant, le bateau de papier : pourquoi finir sur l'enfance et l'impuissance ?")],
  pistes="Vingt-cinq quatrains d'alexandrins, rimes croisées. Strophes 1-4 : le bateau se libère (haleurs tués, cargaisons abandonnées, tempête qui bénit). Strophes 5-7 : baptême et immersion dans le poème de la mer (l'eau lave le vin et les vomissures). Strophes 8-17 : visions, avec l'anaphore j'ai vu, je sais, j'ai rêvé, et un lexique rare (latescent, bleuités, cataractant, Léviathan, Béhémots). Strophes 18-25 : épuisement, regret de l'Europe aux anciens parapets, désir de naufrage (que ma quille éclate), puis image finale de l'enfant qui lâche un bateau frêle sur une flache (flaque, mot régional des Ardennes). Le poème met en œuvre la lettre dite du Voyant (mai 1871) : se faire voyant par un long dérèglement de tous les sens. Écrit à Charleville par un adolescent de seize-dix-sept ans qui n'a jamais vu la mer ; il l'emporte à Paris pour Verlaine en septembre 1871. Pour l'oral : comparer avec la Prose du Transsibérien (voyage réel en train, vers libre, 1913). Piège : le bateau n'est pas une allégorie simple ; garder le double sens (navire et poète)."),
 dict(id="moreas", fiche="A.1 · paire 4 (Le Symbolisme)", titre="Moréas, Le Symbolisme : la définition",
  source="Jean Moréas, Le Symbolisme, Le Figaro, supplément littéraire du 18 septembre 1886",
  edition="Texte de Wikisource (Les Premières Armes du symbolisme, 1889).", vers=False,
  texte="""Ennemie de l'enseignement, de la déclamation, de la fausse sensibilité, de la description objective, la poésie symboliste cherche : à vêtir l'Idée d'une forme sensible qui, néanmoins, ne serait pas son but à elle-même, mais qui, tout en servant à exprimer l'Idée, demeurerait sujette. L'Idée, à son tour, ne doit point se laisser voir privée des somptueuses simarres des analogies extérieures ; car le caractère essentiel de l'art symbolique consiste à ne jamais aller jusqu'à la conception de l'Idée en soi. Ainsi, dans cet art, les tableaux de la nature, les actions des humains, tous les phénomènes concrets ne sauraient se manifester eux-mêmes : ce sont là des apparences sensibles destinées à représenter leurs affinités ésotériques avec des Idées primordiales.

L'accusation d'obscurité lancée contre une telle esthétique par des lecteurs à bâtons rompus n'a rien qui puisse surprendre. Mais qu'y faire ? Les Pythiques de Pindare, l'Hamlet de Shakespeare, la Vita Nuova de Dante, le Second Faust de Goethe, la Tentation de saint Antoine de Flaubert ne furent-ils pas aussi taxés d'ambiguïté ?""",
  questions=[("Ennemis", "Contre quoi le manifeste se définit-il ? À quelles écoles pensez-vous (Parnasse, naturalisme) ?"),
             ("Programme", "Vêtir l'Idée d'une forme sensible : reformulez avec vos mots."),
             ("Lexique", "Simarres, ésotériques, primordiales : quel effet produit ce vocabulaire rare ?"),
             ("Stratégie", "Pindare, Shakespeare, Dante, Goethe, Flaubert : pourquoi convoquer ces noms ?")],
  pistes="Le manifeste paraît dans Le Figaro, un grand quotidien : c'est un coup de force pour nommer une école (les jeunes poètes étaient appelés décadents, Moréas impose symbolistes). La première phrase définit par négation : contre l'enseignement (poésie didactique), la déclamation (Hugo, le romantisme oratoire), la fausse sensibilité, la description objective (Parnasse, naturalisme). Le programme est néoplatonicien : les choses sensibles renvoient à des Idées sans jamais les dire. La liste de grands noms est une stratégie de légitimation : l'obscurité est présentée comme un signe de génie. Bourdieu : un manifeste est un acte de prise de position dans le champ, pour une génération qui veut sa place ; ici l'avant-garde se dote d'un nom et d'une généalogie (Baudelaire, Mallarmé, Verlaine, Banville sont cités plus haut dans le texte). Pour l'oral : comparer avec Marinetti (paire 4), même journal, autre stratégie, la table rase."),
 dict(id="vera", fiche="Partie B (B.1)", titre="Villiers de l'Isle-Adam, Véra : l'ouverture",
  source="Villiers de l'Isle-Adam, Véra (1874), Contes cruels (1883), début",
  edition="Texte de Wikisource.", vers=False,
  texte="""L'amour est plus fort que la Mort, a dit Salomon : oui, son mystérieux pouvoir est illimité.

C'était à la tombée d'un soir d'automne, en ces dernières années, à Paris. Vers le sombre faubourg Saint-Germain, des voitures, allumées déjà, roulaient, attardées, après l'heure du Bois. L'une d'elles s'arrêta devant le portail d'un vaste hôtel seigneurial, entouré de jardins séculaires ; le cintre était surmonté de l'écusson de pierre, aux armes de l'antique famille des comtes d'Athol, savoir : d'azur, à l'étoile abîmée d'argent, avec la devise « Pallida Victrix », sous la couronne retroussée d'hermine au bonnet princier. Les lourds battants s'écartèrent. Un homme de trente à trente-cinq ans, en deuil, au visage mortellement pâle, descendit. Sur le perron, de taciturnes serviteurs élevaient des flambeaux. Sans les voir, il gravit les marches et entra. C'était le comte d'Athol.

Chancelant, il monta les blancs escaliers qui conduisaient à cette chambre où, le matin même, il avait couché dans un cercueil de velours et enveloppé de violettes, en des flots de batiste, sa dame de volupté, sa pâlissante épousée, Véra, son désespoir.""",
  questions=[("Épigraphe", "La première phrase cite le Cantique des cantiques : quelle thèse le conte va-t-il mettre à l'épreuve ?"),
             ("Décor", "Automne, soir, faubourg Saint-Germain, deuil : comment le décor annonce-t-il le récit ?"),
             ("Blason", "Pallida Victrix (la pâle victorieuse) : à qui pense-t-on ?"),
             ("Rythme", "La dernière phrase retarde le nom de Véra : quel effet ?")],
  pistes="Le comte d'Athol, après la mort de sa femme Véra, décide de vivre comme si elle était vivante : il s'enferme un an avec un vieux serviteur, Raymond, et la volonté d'illusion finit par la faire presque revenir, jusqu'au moment où il dit tout haut qu'elle est morte, et tout s'efface. Une clé du tombeau tombe alors, comme un signe. L'ouverture accumule les signes du deuil et de l'aristocratie (hôtel seigneurial, blason, devise latine) : Villiers, noble ruiné, écrit pour une élite et contre le positivisme bourgeois. Pallida Victrix annonce la morte victorieuse. La phrase finale suspend le nom de Véra jusqu'au dernier mot, après une gradation (dame de volupté, pâlissante épousée). Conte cruel : la cruauté tient à la fin, où le réel reprend ses droits. Pour l'oral : comparer avec La Morte amoureuse (S3), deux mortes aimées, deux traitements du fantastique."),
],
7: [
 dict(id="salome", fiche="A.1 · paire 5 (Salomé)", titre="Wilde, Salomé : la première scène",
  source="Oscar Wilde, Salomé, drame en un acte (écrit en français en 1891, publié à Paris en 1893), début",
  edition="Texte de Wikisource (édition originale française).", vers=False,
  texte="""LE JEUNE SYRIEN
Comme la princesse Salomé est belle ce soir !

LE PAGE D'HÉRODIAS
Regardez la lune. La lune a l'air très étrange. On dirait une femme qui sort d'un tombeau. Elle ressemble à une femme morte. On dirait qu'elle cherche des morts.

LE JEUNE SYRIEN
Elle a l'air très étrange. Elle ressemble à une petite princesse qui porte un voile jaune, et a des pieds d'argent. Elle ressemble à une princesse qui a des pieds comme des petites colombes blanches… On dirait qu'elle danse.

LE PAGE D'HÉRODIAS
Elle est comme une femme morte. Elle va très lentement. (Bruit dans la salle de festin.)

PREMIER SOLDAT
Quel vacarme ! Qui sont ces bêtes fauves qui hurlent ?

SECOND SOLDAT
Les Juifs. Ils sont toujours ainsi. C'est sur leur religion qu'ils discutent.

PREMIER SOLDAT
Pourquoi discutent-ils sur leur religion ?

SECOND SOLDAT
Je ne sais pas. Ils le font toujours… Ainsi les Pharisiens affirment qu'il y a des anges, et les Sadducéens disent que les anges n'existent pas.

PREMIER SOLDAT
Je trouve que c'est ridicule de discuter sur de telles choses.

LE JEUNE SYRIEN
Comme la princesse Salomé est belle ce soir !

LE PAGE D'HÉRODIAS
Vous la regardez toujours. Vous la regardez trop. Il ne faut pas regarder les gens de cette façon… Il peut arriver un malheur.""",
  questions=[("Répétition", "Comptez les reprises (belle ce soir, la lune, on dirait, regarder) : quel effet sur le spectateur ?"),
             ("Lune", "Le Syrien et le page voient la même lune : que voit chacun ? Que prépare cette double image ?"),
             ("Regard", "Il ne faut pas regarder : comment le thème du regard annonce-t-il le drame ?"),
             ("Débat", "Les propos des soldats sur les Juifs : comment lire aujourd'hui ces clichés mis dans la bouche des personnages ?")],
  pistes="Wilde écrit Salomé en français, à Paris, en 1891, dans une langue volontairement simple, répétitive, inspirée du Cantique des cantiques et de Maeterlinck. La première scène installe les motifs de la pièce : la lune (femme morte, princesse qui danse, double annonce de la danse et de la mort), le regard interdit (le Syrien qui regarde trop se tuera quand Salomé séduira Iokanaan), la répétition incantatoire. Les soldats introduisent le contexte religieux et une parole de mépris qu'il faut savoir commenter comme discours de personnages. Histoire de la pièce : les répétitions à Londres avec Sarah Bernhardt en 1892 sont arrêtées par la censure (interdiction de représenter des personnages bibliques) ; publication en français en 1893 ; création à Paris au Théâtre de l'Œuvre (Lugné-Poe) en 1896, quand Wilde est en prison. Fin de la pièce : danse des sept voiles, tête de Iokanaan sur un plat d'argent, baiser, et Hérode ordonne de tuer Salomé. Pour l'oral : choix d'un auteur irlandais d'écrire en français, capital symbolique de Paris."),
 dict(id="ubu", fiche="A.1 · paire 5 (Ubu Roi)", titre="Jarry, Ubu Roi : acte I, scène 1",
  source="Alfred Jarry, Ubu Roi (Mercure de France, 1896 ; créé au Théâtre de l'Œuvre le 10 décembre 1896), acte I, scène 1",
  edition="Texte de l'édition originale (Wikisource) ; le s long est transcrit s, l'orthographe archaïsante de Jarry (estes) est conservée.",
  vers=False,
  texte="""PÈRE UBU. — Merdre.

MÈRE UBU. — Oh ! voilà du joli, Père Ubu, vous estes un fort grand voyou.

PÈRE UBU. — Que ne vous assom'je, Mère Ubu !

MÈRE UBU. — Ce n'est pas moi, Père Ubu, c'est un autre qu'il faudrait assassiner.

PÈRE UBU. — De par ma chandelle verte, je ne comprends pas.

MÈRE UBU. — Comment, Père Ubu, vous estes content de votre sort ?

PÈRE UBU. — De par ma chandelle verte, merdre, madame, certes oui, je suis content. On le serait à moins : capitaine de dragons, officier de confiance du roi Venceslas, décoré de l'ordre de l'Aigle Rouge de Pologne et ancien roi d'Aragon, que voulez-vous de mieux ?

MÈRE UBU. — Comment ! Après avoir été roi d'Aragon vous vous contentez de mener aux revues une cinquantaine d'estafiers armés de coupe-choux, quand vous pourriez faire succéder sur votre fiole la couronne de Pologne à celle d'Aragon ?

PÈRE UBU. — Ah ! Mère Ubu, je ne comprends rien de ce que tu dis.

MÈRE UBU. — Tu es si bête !

PÈRE UBU. — De par ma chandelle verte, le roi Venceslas est encore bien vivant ; et même en admettant qu'il meure, n'a-t-il pas des légions d'enfants ?

MÈRE UBU. — Qui t'empêche de massacrer toute la famille et de te mettre à leur place ?""",
  questions=[("Premier mot", "Merdre : un juron déformé. Pourquoi ouvrir une pièce ainsi ? Qu'attendait le public de 1896 ?"),
             ("Parodie", "Une femme pousse son mari à tuer le roi : quelle tragédie de Shakespeare reconnaissez-vous ?"),
             ("Langue", "Estes, assom'je, de par ma chandelle verte, fiole : quels registres se mélangent ?"),
             ("Mise en scène", "Lisez la scène à deux voix : comment jouer Ubu sans psychologie ?")],
  pistes="Le premier mot provoque un quart d'heure de tumulte le soir de la création (10 décembre 1896, Théâtre de l'Œuvre, Firmin Gémier dans le rôle d'Ubu). La scène parodie Macbeth : Mère Ubu joue Lady Macbeth et pousse un mari lâche et stupide à tuer le roi Venceslas de Pologne (une Pologne qui, dit Jarry dans sa présentation, est nulle part). La langue mêle archaïsmes (estes, de par), jurons inventés (chandelle verte, merdre), argot (fiole pour tête, coupe-choux) : le comique naît du décalage. Ubu est né d'une farce de lycéens à Rennes contre un professeur de physique, M. Hébert. Pour l'oral : public visé, l'avant-garde symboliste du Théâtre de l'Œuvre ; nouveauté, un théâtre de marionnettes humaines qui refuse la psychologie et annonce le surréalisme et le théâtre de l'absurde. Comparer avec Salomé (paire 5), créée dans le même théâtre la même année."),
 dict(id="nourritures", fiche="A.1 · paire 3 (Les Nourritures terrestres)", titre="Gide, Les Nourritures terrestres : Livre I",
  source="André Gide, Les Nourritures terrestres (1897), Livre premier, deux fragments",
  edition="Texte de Wikisource (édition du Mercure de France).", vers=False,
  texte="""Ne souhaite pas, Nathanaël, trouver Dieu ailleurs que partout.

Chaque créature indique Dieu, aucune ne le révèle.

Dès que notre regard s'arrête à elle, chaque créature nous détourne de Dieu.

Tandis que d'autres publient ou travaillent, j'ai passé ces trois années de voyage à oublier au contraire tout ce que j'avais appris par la tête. Cette désinstruction fut lente et difficile ; elle me fut plus utile que toutes les instructions imposées par les hommes, et vraiment le commencement d'une éducation.

Tu ne sauras jamais les efforts qu'il nous a fallu faire pour nous intéresser à la vie ; mais maintenant qu'elle nous intéresse, ce sera comme toute chose — passionnément.

[…]

Il faut agir sans juger si l'action est bonne ou mauvaise. Aimer sans s'inquiéter si c'est le bien ou le mal.

Nathanaël je t'enseignerai la ferveur.

Une existence pathétique, Nathanaël, plutôt que la tranquillité. Je ne souhaite pas d'autre repos que celui du sommeil de la mort. J'ai peur que tout désir, toute puissance que je n'aurai pas satisfaits durant ma vie, pour leur survie ne me tourmentent. J'espère après avoir exprimé sur cette terre tout ce qui attendait en moi, — satisfait, — mourir complètement désespéré.""",
  questions=[("Destinataire", "Qui est Nathanaël ? Pourquoi le tutoiement et l'impératif ?"),
             ("Paradoxe", "Désinstruction, mourir complètement désespéré : relevez les paradoxes. Que renversent-ils ?"),
             ("Forme", "Versets, fragments, astérisques : est-ce de la prose, de la poésie, un sermon ?"),
             ("Comparer", "Baudelaire, Enivrez-vous (S4) et Gide : deux injonctions à l'intensité. Différences ?")],
  pistes="Un narrateur (qui se dit disciple de Ménalque) enseigne à un jeune homme imaginaire, Nathanaël, à vivre selon le désir et la ferveur, contre la morale apprise. Le livre suit la convalescence et les voyages de Gide en Afrique du Nord (1893-1895), qui furent pour lui une libération du corps et de la morale protestante. Les paradoxes (désinstruction, mourir désespéré au sens de sans plus rien espérer car tout a été vécu) renversent l'éducation et la morale chrétienne. Forme : versets bibliques, fragments, rondes et hymnes : une prose poétique qui imite l'Écriture pour la retourner. Réception : peu lu à sa parution, le livre devient le bréviaire d'une jeunesse après 1918. La dernière page du livre demande à Nathanaël de jeter le livre. Pour l'oral : comparer avec Le Spleen de Paris (paire 3), où la prose poétique naît de la ville, alors que chez Gide elle naît des sens et du voyage."),
 dict(id="vivien", fiche="A.1 · paire 1 (Études et préludes)", titre="René Vivien, Sonnet à la Mort",
  source="René Vivien, Études et préludes (Lemerre, 1901)",
  edition="Texte de Wikisource.", vers=True,
  texte="""J'attends, ô Bien-Aimée ! ô vierge au chaste front,
Par un soir triomphal de pompe et d'allégresse,
Ton hymen aux blancheurs d'éternelle tendresse.
Car ton baiser d'amour est subtil et profond.

Notre lit sera plein de fleurs qui frémiront,
Et l'orgue clamera la nuptiale ivresse
Dont le sanglot aigu ressemble à la détresse,
Cri d'orgueil où l'angoisse ardente se confond.

Et la paix des autels se remplira de flammes ;
Les larmes, les parfums et les épithalames,
La prière et l'encens monteront jusqu'à nous.

Malgré le jour levé, nous dormirons encore
Dans l'alanguissement des lendemains d'époux,
Et notre longue nuit ne craindra plus l'aurore.""",
  questions=[("Forme", "Un sonnet régulier : vérifiez les rimes (ABBA ABBA CCD EDE) et le mètre."),
             ("Allégorie", "La Mort est la Bien-Aimée : relevez le lexique des noces. Quel effet produit ce mélange ?"),
             ("Héritage", "Que doit ce poème à Baudelaire (La Mort des amants) ?"),
             ("Voix", "Le poète qui dit je attend une épouse : que change le fait de savoir que l'autrice est une femme ?")],
  pistes="Sonnet en alexandrins, rimes embrassées dans les quatrains (front, profond / allégresse, tendresse), puis CCD EDE. La Mort est figurée comme une épouse vierge : noces funèbres (hymen, lit, orgue, autels, épithalames), oxymores (sanglot de l'ivresse, angoisse d'orgueil). Héritage baudelairien évident (La Mort des amants, Les Fleurs du mal) et forme parnassienne. René Vivien est le pseudonyme de Pauline Mary Tarn (1877-1909), poétesse d'origine britannique écrivant en français, installée à Paris ; le premier recueil paraît sous le nom de R. Vivien, d'abord lu comme celui d'un homme. Sa poésie chante l'amour entre femmes (Natalie Clifford Barney, Violet Shillito) et la mort, d'où son surnom de Muse aux violettes. Pour l'oral : comparer avec Lamartine (paire 1) ; deux recueils, deux siècles, deux manières de lier amour et mort. Sociocritique : position d'une femme étrangère dans un champ poétique dominé par les hommes ; usage stratégique du pseudonyme masculin."),
],
8: [
 dict(id="meaulnes", fiche="A.1 · paire 6 (Le Grand Meaulnes)", titre="Alain-Fournier, Le Grand Meaulnes : l'incipit",
  source="Alain-Fournier, Le Grand Meaulnes (1913), première partie, chapitre I",
  edition="Texte de Wikisource.", vers=False,
  texte="""Il arriva chez nous un dimanche de novembre 189…

Je continue à dire « chez nous », bien que la maison ne nous appartienne plus. Nous avons quitté le pays depuis bientôt quinze ans et nous n'y reviendrons certainement jamais.

Nous habitions les bâtiments du Cours Supérieur de Sainte-Agathe. Mon père, que j'appelais M. Seurel, comme les autres élèves, y dirigeait à la fois le Cours Supérieur, où l'on préparait le brevet d'instituteur, et le Cours Moyen. Ma mère faisait la petite classe.

Une longue maison rouge, avec cinq portes vitrées, sous des vignes vierges, à l'extrémité du bourg ; une cour immense avec préaux et buanderie, qui ouvrait en avant sur le village par un grand portail ; sur le côté nord, la route où donnait une petite grille et qui menait vers La Gare, à trois kilomètres ; au sud et par derrière, des champs, des jardins et des prés qui rejoignaient les faubourgs… tel est le plan sommaire de cette demeure où s'écoulèrent les jours les plus tourmentés et les plus chers de ma vie — demeure d'où partirent et où revinrent se briser, comme des vagues sur un rocher désert, nos aventures.""",
  questions=[("Il", "Il arriva : qui est il ? Pourquoi le nom n'est-il pas donné ?"),
             ("Temps", "189…, quinze ans, jamais : relevez les marques de distance temporelle. Quel ton produisent-elles ?"),
             ("Lieu", "L'école, la maison, la route de la gare : comment le plan du lieu prépare-t-il l'aventure ?"),
             ("Image", "Comme des vagues sur un rocher désert : que dit la comparaison finale de la suite du roman ?")],
  pistes="Le narrateur François Seurel, fils des instituteurs, raconte depuis un présent lointain l'arrivée d'Augustin Meaulnes, le grand Meaulnes. Le pronom il sans antécédent fait de Meaulnes une présence avant d'être un nom. La date incomplète (189…) et l'adverbe jamais installent la nostalgie : le roman est un récit de souvenir et de perte. Le plan de la maison est précis, réaliste (Sologne, Cher), mais orienté vers la route et la gare : vers le départ. La comparaison finale annonce que les aventures se briseront : le domaine mystérieux, Yvonne de Galais, Frantz, tout sera perdu. Contexte : publié en 1913, le roman manque le prix Goncourt ; Alain-Fournier est tué en septembre 1914, ce qui fixe le livre comme roman unique d'une génération sacrifiée. Pour l'oral : comparer avec Les Caves du Vatican (paire 6), même moment, roman de l'enfance et de l'idéal contre sotie ironique."),
],
}

# Œuvres sans passage long dans le dossier, et pourquoi
SANS_PASSAGE = {
 8: [("Cendrars, Prose du Transsibérien (1913)", "Œuvre protégée par le droit d'auteur (Cendrars meurt en 1961) : seule une citation courte est reproduite. Lire le poème dans son édition personnelle ou en bibliothèque (Du monde entier, Poésie/Gallimard)."),
     ("Marinetti, Manifeste du futurisme (1909)", "Texte du domaine public, publié en français à la une du Figaro le 20 février 1909 : à lire sur Gallica (numéro du Figaro de ce jour) ou dans l'anthologie de la classe."),
     ("Gide, Les Caves du Vatican (1914)", "Texte entré dans le domaine public en Italie et en France, mais absent de Wikisource : lire dans une édition de poche (Folio) ou en bibliothèque.")],
}
