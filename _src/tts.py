import json,sys,os,numpy as np,soundfile as sf
T=json.load(open('transcripts.json'))
import re
FIX=[(r'\bWeimar\b','Vaïmare'),(r'\bShakespeare\b','Chèkspire'),(r'\brythme','ritme'),(r'\bBovary\b','Bovari'),
(r'\bBaker\b','Békeur'),(r"\bD'Annunzio\b",'Dannoun-tsio'),(r'\bGiovanni\b','Djovanni'),(r'\bMalavoglia\b','Malavolia'),
(r'\bUngaretti\b','Oun-garétti'),(r'\bMateo\b','Matéo'),(r'\bOrtis\b','Ortisse'),(r'\bMaeterlinck\b','Métèrlinck'),
(r'\bHuysmans\b','Uïsmansse'),(r'\bDreyfus\b','Drèfusse'),(r'Leconte de Lisle','Leconte de Lile'),(r"l'Isle-Adam","l'Ile-Adam"),(r'\bSpleen\b','Splîne'),(r"d'Aurevilly","d'Aurvilli"),(r'\bWilde\b','Ouaïlde'),(r'\bAlfred Jarry\b','Alfrède Jari'),(r'\bJarry\b','Jari'),(r'Nathanaël','Nataniel'),(r'Van Tieghem','Vent Tiguème')]
def fix(p):
    for a,b in FIX: p=re.sub(a,b,p)
    return p
def kokoro(paras,out,speed=0.8,voice='ff_siwis'):
    from kokoro_onnx import Kokoro
    k=Kokoro(os.environ.get('KOKORO_MODEL','kokoro-v1.0.onnx'),os.environ.get('KOKORO_VOICES','voices-v1.0.bin'))
    chunks=[]
    for p in paras:
        a,sr=k.create(fix(p),voice=voice,speed=speed,lang='fr-fr')
        chunks+= [a, np.zeros(int(sr*0.6),dtype=a.dtype)]
    sf.write(out,np.concatenate([np.zeros(int(sr*0.3),dtype=a.dtype)]+chunks),sr)
def piper(paras,out,ls=1.12):
    from piper import PiperVoice
    from piper.config import SynthesisConfig
    v=PiperVoice.load('voices/fr-siwis-medium.onnx')
    cfg=SynthesisConfig(length_scale=ls,noise_scale=0.5,noise_w_scale=0.6)
    sr=v.config.sample_rate; chunks=[]
    for p in paras:
        for c in v.synthesize(p,syn_config=cfg):
            chunks+=[c.audio_float_array, np.zeros(int(sr*0.25),dtype=np.float32)]
        chunks.append(np.zeros(int(sr*0.4),dtype=np.float32))
    sf.write(out,np.concatenate(chunks),sr)
if __name__=='__main__':
    eng,wk,out=sys.argv[1],sys.argv[2],sys.argv[3]
    paras=T[wk] if len(sys.argv)<5 else T[wk][:int(sys.argv[4])]
    (kokoro if eng=='kokoro' else piper)(paras,out)
