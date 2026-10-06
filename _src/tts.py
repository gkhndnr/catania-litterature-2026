# Résumés audio (Kokoro, voix ff_siwis) avec corrections de prononciation.
# Usage : python3 tts.py <_audio.json> <dossier_audio> [semaines...]
# Modèles : KOKORO_MODEL (kokoro-v1.0.onnx) et KOKORO_VOICES (voices-v1.0.bin).
# Le texte affiché sur le site (transcription) n'est jamais modifié : les corrections
# ne s'appliquent qu'au texte envoyé à la voix de synthèse.
import json, os, re, subprocess, sys, tempfile

# Respellings : le phonétiseur (espeak) lit certains noms à l'anglaise ou les nasalise.
FIX = [
 (r"\bStaël\b", "Stal"), (r"\bGoethe\b", "Gueute"), (r"\bWerther\b", "Vèrtère"), (r"\bCromwell\b", "Cromouelle"),
 (r"\bWeimar\b", "Vaïmare"), (r"\bShakespeare\b", "Chèkspire"), (r"\brythme", "ritme"), (r"\bBovary\b", "Bovari"),
 (r"\bBaker\b", "Békeur"), (r"\bD'Annunzio\b", "Dannoun-tsio"), (r"\bGiovanni\b", "Djovanni"), (r"\bMalavoglia\b", "Malavolia"),
 (r"\bUngaretti\b", "Oun-garétti"), (r"\bMateo\b", "Matéo"), (r"\bOrtis\b", "Ortisse"), (r"\bMaeterlinck\b", "Métèrlinck"),
 (r"\bHuysmans\b", "Uïsmansse"), (r"\bDreyfus\b", "Drèfusse"), (r"Leconte de Lisle", "Leconte de Lile"), (r"l'Isle-Adam", "l'Ile-Adam"),
 (r"\bSpleen\b", "Splîne"), (r"d'Aurevilly", "d'Aurvilli"), (r"\bWilde\b", "Ouaïlde"), (r"\bAlfred Jarry\b", "Alfrède Jari"),
 (r"\bJarry\b", "Jari"), (r"Nathanaël", "Nataniel"), (r"Van Tieghem", "Vent Tiguème"), (r"\bChatterton\b", "Chattertonne"),
 (r"\bGianetto\b", "Djanetto"), (r"\bCapuana\b", "Capouana"), (r"\bStudium\b", "Stoudioum"), (r"Lugné-Poe", "Lugné-Pô"),
 (r"\bPirandello\b", "Pira-ndèllo"), (r"\bManzoni\b", "Ma-ndzoni"), (r"\bVerga\b", "Vèrga"), (r"\bCatania\b", "Catania"),
 (r"\bStalloni\b", "Stalloni"), (r"\bMeaulnes\b", "Môn"), (r"\bCendrars\b", "Sandrar"),
 (r"\bFortunato\b", "Fortounato"), (r"\bFoscolo\b", "Foscolo"), (r"\bVerdi\b", "Vèrdi"), (r"\bErnani\b", "Èrnani"),
 (r"\bMarinetti\b", "Marinètti"), (r"\bGide\b", "Jide"), (r"\bUbu\b", "Ubu"), (r"\bSappho\b", "Sapho"),
 (r"\bBatouala\b", "Batouala"), (r"\bMédan\b", "Médan"),
 (r"\bl'IA\b", "l'i a"), (r"quatre-vingt-(?=[a-z])", "quatre-vin-"),
]

def fix(p):
    for a, b in FIX: p = re.sub(a, b, p)
    return p

def kokoro(paras, out_wav, speed=0.8, voice="ff_siwis"):
    import numpy as np, soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(os.environ.get("KOKORO_MODEL", "kokoro-v1.0.onnx"), os.environ.get("KOKORO_VOICES", "voices-v1.0.bin"))
    chunks, sr = [], 24000
    for p in paras:
        a, sr = k.create(fix(p), voice=voice, speed=speed, lang="fr-fr")
        chunks += [a, np.zeros(int(sr * 0.6), dtype=a.dtype)]
    sf.write(out_wav, np.concatenate([np.zeros(int(sr * 0.3), dtype=chunks[0].dtype)] + chunks), sr)

def master(wav, mp3):
    af = "highpass=f=80,equalizer=f=3000:t=q:w=1:g=2.5,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,loudnorm=I=-16:TP=-1.5"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-af", af, "-ac", "1", "-ar", "44100", "-b:a", "128k", mp3], check=True)

if __name__ == "__main__":
    T = json.load(open(sys.argv[1], encoding="utf-8"))
    outdir = sys.argv[2]
    weeks = sys.argv[3:] or sorted(T, key=int)
    for wk in weeks:
        with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
            kokoro(T[wk], tmp.name)
            master(tmp.name, os.path.join(outdir, f"s{wk}.mp3"))
        print("ok", wk)
