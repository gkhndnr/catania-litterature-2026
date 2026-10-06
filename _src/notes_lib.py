# Format commun des notes de l'enseignant.
# Chaque note est un texte en rubriques (ÉTIQUETTE · contenu), séparées par une ligne vide.
# Les questions et réponses sont écrites sur des lignes « Q. » et « R. » ;
# les citations commencent par « ; les listes par « – ».
# Le site les met en forme (diapositives, guide imprimable).

def N(duree, deroule, qr=None, essentiel=None, citations=None, piege=None, plus=None, source=None,
      questions=None, attendus=None):
    parts = [f"DURÉE · {duree}"]
    if essentiel: parts.append(f"L'ESSENTIEL POUR L'ENSEIGNANT · {essentiel}")
    parts.append(f"DÉROULÉ · {deroule}")
    if qr:
        parts.append("QUESTIONS ET RÉPONSES · " + "\n".join(f"Q. {q}\nR. {r}" for q, r in qr))
    elif questions:
        parts.append(f"QUESTIONS ET RÉPONSES · Q. {questions}" + (f"\nR. {attendus}" if attendus else ""))
    if citations:
        parts.append("CITATIONS D'APPUI · " + "\n".join(f"« {t} » ({s})" for t, s in citations))
    if piege: parts.append(f"POINT DE VIGILANCE · {piege}")
    if plus: parts.append(f"POUR ALLER PLUS LOIN · {plus}")
    if source: parts.append(f"SOURCES · {source}")
    return "\n\n".join(parts)
