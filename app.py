import streamlit as st
import random
import json
import os

st.set_page_config(page_title="L'EXTREMISTE & LE SAGE V9.6", layout="wide")

FICHIER_JSON = "personnages.json"

def charger_ou_initialiser_personnages():
    """Charge le fichier JSON existant ou crée la base par défaut si besoin."""
    base_defaut = {
        "LE_SAGE": "Le Sage Labrador noir couronne or yeux sages exorbitees Uderzo 4 pattes jamais humain",
        "BAS_ROUGE": "Bas-Rouge Beauceron 120lbs casque viking cornes torche flamme yeux furieux Uderzo 4 pattes",
        "CANICHE_BEIGE": "Caniche Beige economique tuque beige camionnette vieille yeux astucieux Uderzo 4 pattes",
        "CARNEY": "Golden Carney Labrador blond cravate rouge politicien sage yeux exorbitees Uderzo 4 pattes",
        "BAR_RAYE": "Berger Allemand garde-peche jumelles uniforme vert yeux vigilants Uderzo 4 pattes"
    }
    
    if os.path.exists(FICHIER_JSON):
        try:
            with open(FICHIER_JSON, "r", encoding="utf-8") as f:
                data = json.load(f)
                for k, v in base_defaut.items():
                    if k not in data:
                        data[k] = v
                return data
        except Exception:
            return base_defaut
    else:
        with open(FICHIER_JSON, "w", encoding="utf-8") as f:
            json.dump(base_defaut, f, ensure_ascii=False, indent=4)
        return base_defaut

def sauvegarder_personnages(bible):
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        json.dump(bible, f, ensure_ascii=False, indent=4)

# Chargement de la BIBLE JSON au démarrage
BIBLE = charger_ou_initialiser_personnages()

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
        punch = ["201.6 TABARNAC VOLEURS", "187.9 LOIN 30KM GRRR", "DIMANCHE MOINS 1.7 MAIS JOB", "TAXE 10C 8 SEPT OUCH", "2.4M ALLEGEMENT GAZ 201.6"]
    elif is_carney:
        faits = ["CARNEY RENCONTRE TRUMP TARIFS 25P POURCENT", "CARNEY SAGE VS TRUMP FOU IRONIE", "2.4M ALLEGEMENT MAIS GAZ 201.6"]
        emotion = "inquietude + ironie politique"
        punch = ["CARNEY SAGE TRUMP FOU", "25P POURCENT TABARNAC PEUR", "2.4M OU CA"]
    elif is_bar:
        faits = ["BAR RAYE TAILLE 50 A 65CM CONFUSION", "AMENDE 500 DOLLARS SI TROP PETIT", "RETOUR BAR RAYE JOIE MAIS REGLES"]
        emotion = "joie retour + frustration regles"
        punch = ["50-65CM CONFUS GRRR", "500 DOLLARS AMENDE OUCH", "BAR RAYE ENFIN"]
    else:
        faits = [f"SUJET {sujet.upper()} ANALYSE", "FAIT 1 EXTRAIT IA", "FAIT 2 IRONIE DETECTEE"]
        emotion = "analyse"
        punch = [f"{sujet[:12].upper()} TABARNAC", "RAGE ESPOIR QUOI"]
    
    return {"faits": faits, "emotion": emotion, "punch": punch, "is_gaz": is_gaz, "is_carney": is_carney, "is_bar": is_bar}

def generer_prompt(sujet, analyse):
    races = RACES_25.copy()
    random.shuffle(races)
    
    if analyse["is_gaz"]:
        allié_cle = "CANICHE_BEIGE"
        allié_nom = "FORCE GAZ"
    elif analyse["is_carney"]:
        allié_cle = "CARNEY"
        allié_nom = "FORCE CARNEY"
    elif analyse["is_bar"]:
        allié_cle = "BAR_RAYE"
        allié_nom = "FORCE BAR RAYE"
    else:
        allié_cle = "CANICHE_BEIGE"
        allié_nom = "FORCE"

    # Grille fixe stricte 3x3 (9 cases de 1 à 9 sans doublons)
    cases = {}
    cases[1] = f"CASE1: {BIBLE.get('LE_SAGE', 'Le Sage')} - LE SAGE TOUJOURS"
    cases[2] = f"CASE2: {BIBLE.get(allié_cle, 'Allie')} - {allié_nom}"
    cases[4] = f"CASE4: {BIBLE.get('BAS_ROUGE', 'Bas-Rouge')} - BAS-ROUGE TOUJOURS"
    
    cases_libres = [3, 5, 6, 7, 8, 9]
    for c_num in cases_libres:
        if races:
            r = races.pop()
            cases[c_num] = f"CASE{c_num}: {r} - RACE VARIEE ANTI-DOUBLON UDERZO 4 PATTES"

    casting = [cases[i] for i in sorted(cases.keys())]
    
    prompt = f"STYLE UDERZO gros nez yeux exorbitees 4 pattes jamais humain 9 cases 3x3 grille stricte BD quebecoise\n"
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
    prompt += "REGLES: Grille 3x3 exacte de 9 cases numerotees de 1 a 9. Le Sage Case1. Bas-Rouge Case4. 7 races differentes sans doublon. Bulles BOLD 8 mots max. 4 pattes jamais humain. Gros nez yeux exorbitees quebequois Saguenay.\n"
    return prompt

st.title("L'EXTREMISTE & LE SAGE V9.6 - JSON & FIX GRILLE")

sujet = st.text_input("Sujet", "prix du gaz Saguenay 201.6")

# Panneau pour voir et enrichir la base JSON des personnages
with st.expander("🛠️ Gérer la base de données JSON des personnages"):
    nouveau_cle = st.text_input("Clé du personnage (ex: NOUVEAU_PERSO)")
    nouveau_desc = st.text_input("Description Uderzo")
    if st.button("Ajouter / Mettre à jour"):
        if nouveau_cle and nouveau_desc:
            BIBLE[nouveau_cle.upper()] = nouveau_desc
            sauvegarder_personnages(BIBLE)
            st.success(f"Personnage {nouveau_cle.upper()} enregistré dans {FICHIER_JSON} !")
        else:
            st.error("Remplis les deux champs.")
    
    st.write("Contenu actuel du JSON :")
    st.json(BIBLE)

if st.button("ANALYSE IA EXPERTE + GENERER PROMPT 9 CASES", type="primary"):
    analyse = ia_analyse_experte(sujet)
    st.subheader("ANALYSE IA")
    st.write(f"Emotion: {analyse['emotion']}")
    for f in analyse["faits"]:
        st.write(f"- {f}")
    for p in analyse["punch"]:
        st.write(f"- {p}")
    final = generer_prompt(sujet, analyse)
    st.code(final, language="text")
    st.success("Génération réussie avec le JSON et la grille 3x3 propre !")
    
