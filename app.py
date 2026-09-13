import streamlit as st
import random
import re
from datetime import datetime

st.set_page_config(page_title="L'EXTREMISTE & LE SAGE V9.5", layout="wide")

BIBLE = {
    "LE_SAGE": "Le Sage Labrador noir couronne or yeux sages exorbitees Uderzo 4 pattes jamais humain",
    "BAS_ROUGE": "Bas-Rouge Beauceron 120lbs casque viking cornes torche flamme yeux furieux Uderzo 4 pattes",
    "CANICHE_BEIGE": "Caniche Beige economique tuque beige camionnette vieille yeux astucieux Uderzo 4 pattes",
    "CARNEY": "Golden Carney Labrador blond cravate rouge politicien sage yeux exorbitees Uderzo 4 pattes",
    "BAR_RAYE": "Berger Allemand garde-peche jumelles uniforme vert yeux vigilants Uderzo 4 pattes"
}

RACES_25 = [
    "Samoyede blanc neige fourrure epaisse",
    "Dalmatien taches noires",
    "Bouledogue Francais gris costaud",
    "Border Collie noir blanc intelligent",
    "Beagle tricolore curieux",
    "Berger Allemand noir feu",
    "Labrador Chocolat",
    "Husky gris yeux bleus",
    "Corgi courtes pattes",
    "Shiba Inu roux",
    "Caniche Royal blanc",
    "Bouvier Bernois tricolore",
    "Jack Russell blanc taches",
    "Teckel allonge saucisse",
    "Boxer fauve",
    "Chow Chow langue bleue",
    "Levier Afghan poil long",
    "Saint-Bernard enorme",
    "Chihuahua mini",
    "Dogue Allemand geant",
    "Colley poil long Lassie",
    "Epagneul Cocker oreilles longues",
    "Terrier Ecossais noir",
    "Braque Allemand chasse",
    "Malamute Alaska puissant"
]

def ia_analyse_experte(sujet):
    s = sujet.lower()
    is_gaz = any(w in s for w in ["gaz", "essence", "201.6", "saguenay"])
    is_carney = any(w in s for w in ["carney", "trump", "tarif"])
    is_bar = any(w in s for w in ["bar raye", "peche", "poisson"])
    
    if is_gaz:
        faits = [
            "MOYENNE 201.6 CENTS SAGUENAY RECORD",
            "ECART 17 CENTS 187.9 A 204.9 MEME GAZ",
            "SUPER GAZ 187.9 MOINS 13.7 ECONOMIE 6.85 SUR 50L",
            "DIMANCHE MOINS 1.7 ASTUCE CANICHE",
            "TAXE 10C RETOUR 8 SEPT PLUS 2.4M IRONIE"
        ]
        emotion = "frustration + espoir Super Gaz + ironie"
        forces = ["LE_SAGE", "BAS_ROUGE", "CANICHE_BEIGE"]
        punch = ["201.6 TABARNAC VOLEURS", "187.9 LOIN 30KM GRRR", "DIMANCHE MOINS 1.7 MAIS JOB", "TAXE 10C 8 SEPT OUCH", "2.4M ALLEGEMENT GAZ 201.6"]
    elif is_carney:
        faits = ["CARNEY RENCONTRE TRUMP TARIFS 25P POURCENT", "CARNEY SAGE VS TRUMP FOU IRONIE", "2.4M ALLEGEMENT MAIS GAZ 201.6"]
        emotion = "inquietude + ironie politique"
        forces = ["LE_SAGE", "BAS_ROUGE", "CARNEY"]
        punch = ["CARNEY SAGE TRUMP FOU", "25P POURCENT TABARNAC PEUR", "2.4M OU CA"]
    elif is_bar:
        faits = ["BAR RAYE TAILLE 50 A 65CM CONFUSION", "AMENDE 500 DOLLARS SI TROP PETIT", "RETOUR BAR RAYE JOIE MAIS REGLES"]
        emotion = "joie retour + frustration regles"
        forces = ["LE_SAGE", "BAS_ROUGE", "BAR_RAYE"]
        punch = ["50-65CM CONFUS GRRR", "500 DOLLARS AMENDE OUCH", "BAR RAYE ENFIN"]
    else:
        faits = [f"SUJET {sujet.upper()} ANALYSE", "FAIT 1 EXTRAIT IA", "FAIT 2 IRONIE DETECTEE"]
        emotion = "analyse"
        forces = ["LE_SAGE", "BAS_ROUGE"]
        punch = [f"{sujet[:12].upper()} TABARNAC", "RAGE ESPOIR QUOI"]
    
    return {"faits": faits, "emotion": emotion, "forces": forces, "punch": punch, "is_gaz": is_gaz, "is_carney": is_carney, "is_bar": is_bar}

def generer_prompt(sujet, analyse):
    races = RACES_25.copy()
    random.shuffle(races)
    casting = []
    casting.append(f"CASE1: {BIBLE['LE_SAGE']} - LE SAGE TOUJOURS")
    casting.append(f"CASE4: {BIBLE['BAS_ROUGE']} - BAS-ROUGE TOUJOURS")
    if analyse["is_gaz"]:
        casting.append(f"CASE2: {BIBLE['CANICHE_BEIGE']} - FORCE GAZ")
    if analyse["is_carney"]:
        casting.append(f"CASE2: {BIBLE['CARNEY']} - FORCE CARNEY")
    if analyse["is_bar"]:
        casting.append(f"CASE2: {BIBLE['BAR_RAYE']} - FORCE BAR RAYE")
    for i in range(6):
        if races:
            r = races.pop()
            n = len(casting) + 1
            if n == 4:
                n = 7
            casting.append(f"CASE{n}: {r} - RACE VARIEE ANTI-DOUBLON UDERZO 4 PATTES")
    
    prompt = f"STYLE UDERZO gros nez yeux exorbitees 4 pattes jamais humain 9 cases 3x3 BD quebecoise\n"
    prompt += f"SUJET: {sujet.upper()}\n"
    prompt += f"ANALYSE: {analyse['emotion']}\n"
    prompt += "FAITS:\n"
    for f in analyse["faits"]:
        prompt += f"- {f}\n"
    prompt += "PUNCHLINES:\n"
    for p in analyse["punch"]:
        prompt += f"- {p}\n"
    prompt += "CASTING:\n"
    for c in casting:
        prompt += f"{c}\n"
    prompt += "REGLES: Le Sage Case1 Bas-Rouge Case4 7 races differentes jamais meme race bulles BOLD 8 mots max 4 pattes jamais humain gros nez yeux exorbitees quebequois Saguenay\n"
    return prompt

st.title("L'EXTREMISTE & LE SAGE V9.5 IA EXPERTE - FIX SYNTAX")

sujet = st.text_input("Sujet", "prix du gaz Saguenay 201.6")

if st.button("ANALYSE IA EXPERTE + GENERER PROMPT 9 CASES", type="primary"):
    analyse = ia_analyse_experte(sujet)
    st.subheader("ANALYSE IA")
    st.write(f"Emotion: {analyse['emotion']}")
    st.write(f"Forces: {', '.join(analyse['forces'])}")
    for f in analyse["faits"]:
        st.write(f"- {f}")
    for p in analyse["punch"]:
        st.write(f"- {p}")
    final = generer_prompt(sujet, analyse)
    st.code(final, language="text")
    st.success("V9.5 FIX - plus de SyntaxError - banque 25 races + Le Sage + Bas-Rouge OK")   
