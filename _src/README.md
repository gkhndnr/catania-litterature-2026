# Sources du site (non publiées)

Ce dossier commence par `_` : GitHub Pages (Jekyll) ne le publie pas. Il contient tout ce qu'il faut pour reconstruire le site lors des mises à jour hebdomadaires.

| Fichier | Rôle |
|---|---|
| `content_a.py`, `content_b.py` | Contenu des semaines 1-4 et 5-8 : objectifs, fiche du cours, séances, énigme, frise, auteurs, outil, textes, méthode, nouvelle, labo IA, pont italien, devoirs, carnet, transcription audio |
| `articles.py` | Lectures critiques ajoutées semaine par semaine (diapositive Lecture critique, frise facultative, carte sur la page, carnet, bibliographie) |
| `notes_lib.py` | Format des notes de l'enseignant (rubriques, lignes Q. / R., citations) |
| `notes_a.py`, `notes_b.py` | Notes de l'enseignant développées, par identifiant de diapositive : chaque question posée a sa réponse |
| `prof.py` | Guide imprimable de chaque semaine : l'essentiel, glossaire, prononciation des noms, questions fréquentes |
| `loupe.py` | La langue à la loupe (11 octobre 2026) : grille hebdomadaire isotopie, lexique, morpho-syntaxe, rythme ou métrique, voix et codes, pour répondre aux Learning Objectives de la fiche ; diapositive après la méthode, carte En classe, objectif Je peux, glossaire, carnet, encadré du dossier de textes PDF, références Cairn de la semaine 1 |
| `biblio.py` | Bibliographie : références par semaine et bibliographie générale |
| `guide.py`, `shots.py`, `shots.json` | Page Mode d'emploi et captures d'écran annotées (Playwright) |
| `s1_deck.py`, `s1_notes.json` | Semaine 1 (12 octobre 2026) : présentation en deux séances de 1 h 45, 25 diapositives reprises du fichier « Semaine 1 · Seuils du siècle.pptx », notes de l'enseignant par diapositive ; portraits dans `img/s1/` |
| `s1_patch.py` | `python3 _src/s1_patch.py .` : remplace la présentation et les notes dans `s1.html` et `prof-s1.html` sans reconstruire le reste (garde les corrections faites à la main) |
| `build.py` | Générateur : `python3 build.py <ancien_site> <sortie>` (l'ancien site sert à récupérer les diapositives conservées telles quelles : S1 présentation, S8 envers de la fête) |
| `tts.py` | Résumés audio : `python3 tts.py <sortie>/_audio.json audio [semaines]` (Kokoro, voix ff_siwis, vitesse 0,8, corrections de prononciation `FIX`, mastering ffmpeg) |

## Mise à jour type

1. Modifier le contenu (`content_*.py`, `articles.py`, `notes_*.py`, `prof.py`, `biblio.py`).
2. `python3 _src/build.py . /tmp/out`, copier `site.css` et `img/` dans `/tmp/out`, vérifier les débordements des diapositives.
3. Si l'interface change : `python3 _src/shots.py /tmp/out img`, puis reconstruire.
4. Si une transcription change : `python3 _src/tts.py /tmp/out/_audio.json audio <n>`.
5. Copier les pages HTML dans le dépôt et publier.

## Ajouter un article

1. Lire l'article et en tirer 3 ou 4 idées, 1 ou 2 citations courtes avec source, une question à discuter.
2. Ajouter une entrée dans `articles.py` sous le numéro de semaine (frise facultative).
3. Ajouter les notes `critique-<id>` (et `critique-<id>-frise`) dans `notes_a.py` ou `notes_b.py`, avec l'essentiel sur l'auteur et les réponses aux questions.
4. Ajouter la référence dans `biblio.py` (BIB_WEEK).
5. Reconstruire, vérifier, publier.

Ne jamais déposer les PDF des articles dans ce dépôt public : seulement la référence, le lien et des citations courtes.

## Notes sur les sources (octobre 2026)

- Ajout du 11 octobre 2026 (La langue à la loupe) : lectures Cairn consultées : Fontanille 1999 (isotopie), Glinoer et Laisney 2019 (mécénat d'État après la Révolution), Gutermann 2007 (mal du siècle), Lits 2001 (nouvelle et presse), Mayeur 2025 (IA générative comme média éducatif). Les grilles s'appuient sur les passages du dossier (passages.py).

- Stalloni, Écoles et courants littéraires (Armand Colin, Cursus) : erreurs de date relevées et signalées en classe (manifeste de Moréas daté de 1866 pour 1886 ; La Morte amoureuse datée de 1844 pour 1836 ; Jack de Daudet daté de 1896 pour 1876).
- Bainville, Au seuil du siècle (1927, domaine public) : critique d'Action française ; l'article sur Zola contient un passage raciste, traité dans les notes comme document de combat.
- Citations des œuvres du XIXe siècle vérifiées sur Project Gutenberg (Trois Contes, Madame Bovary, Contes du lundi, Le Horla, Boule de suif, Contes cruels, Germinal, Ubu Roi, Salomé, Le Grand Meaulnes).
