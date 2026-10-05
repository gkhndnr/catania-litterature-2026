# Sources du site (non publiées)

Ce dossier commence par `_` : GitHub Pages (Jekyll) ne le publie pas. Il contient tout ce qu'il faut pour reconstruire le site lors des mises à jour hebdomadaires.

| Fichier | Rôle |
|---|---|
| `content_a.py`, `content_b.py` | Contenu des semaines 1-4 et 5-8 : objectifs, fiche du cours, séances, énigme, frise, auteurs, outil, textes, méthode, nouvelle, labo IA, pont italien, devoirs, carnet, transcription audio |
| `articles.py` | Lectures critiques ajoutées semaine par semaine (diapositive Lecture critique, carte sur la page, carnet, bibliothèque) |
| `notes_a.py`, `notes_b.py` | Notes de l'enseignant développées, par identifiant de diapositive |
| `build.py` | Générateur : `python3 build.py <ancien_site> <sortie>` (l'ancien site sert à récupérer les diapositives conservées telles quelles : S1 présentation, S8 envers de la fête) |
| `tts.py` | Résumés audio (Kokoro, voix ff_siwis, vitesse 0,8) avec corrections de prononciation (`FIX`) |

## Ajouter un article

1. Lire l'article et en tirer 3 ou 4 idées, 1 ou 2 citations courtes avec page, une question à discuter.
2. Ajouter une entrée dans `articles.py` sous le numéro de semaine (frise facultative).
3. Ajouter les notes `critique-<id>` (et `critique-<id>-frise`) dans `notes_a.py` ou `notes_b.py`.
4. Reconstruire, vérifier les débordements, publier.

Ne jamais déposer les PDF des articles dans ce dépôt public : seulement la référence, le lien et des citations courtes.

## Audio

Mastering : `highpass=f=80, equalizer=f=3000:g=2.5, acompressor, loudnorm=I=-16:TP=-1.5`, MP3 mono 128 kbps 44,1 kHz.
