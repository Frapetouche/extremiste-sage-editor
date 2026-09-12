import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="L'Extremiste & Le Sage - V8.1", layout="wide")
st.title("L'EXTREMISTE & LE SAGE — V8.1 Fix 4 Pattes")

BIBLE_FILE = "bible_vivante.json"

def load_bible():
    if os.path.exists(BIBLE_FILE):
        with open(BIBLE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "Le Sage": "Labrador noir couronne or cape beige sage yeux doux 4 pattes",
        "Bas-Rouge": "Beauceron noir et feu casque aile viking torche foulard rouge",
        "Mark Carney": "Golden Retriever PM Canada cravate rouge",
        "Husky Kahnawake": "Husky mohawk casque chantier gilet orange APTN",
        "Familles": "Caniches pêcheurs solidaires",
        "Gardes": "Bergers allemands garde faune"
    }

bible = load_bible()

with st.sidebar:
    st.header("Bible Vivante")
    for k in bible.keys():
        st.caption(k)
    st.divider()
    nn = st.text_input("Nouveau perso")
    dd = st.text_input("Desc chien")
    if st.button("Ajouter"):
        bible[nn]=dd
        with open(BIBLE_FILE,"w",encoding="utf-8") as fw:
            json.dump(bible,fw,ensure_ascii=False,indent=2)
        st.rerun()

st.subheader("Systeme recherche sujet")
mode = st.radio("Mode:", ["Recherche manuelle (tape sujet)", "Recherche auto news du jour"])
sujet = st.text_input("SUJET DU JOUR", value="Le bar raye ds le fleuve?")
top = "TOP1"

tags_exclus = []
if "11 sept" not in sujet.lower():
    tags_exclus = ["Drones Hommage 2977", "Tribute in Light"]
if "trump" not in sujet.lower() and "tarif" not in sujet.lower():
    tags_exclus.append("Trump")

bible_filtre = {k:v for k,v in bible.items() if k not in tags_exclus}
bible_json = json.dumps(bible_filtre, ensure_ascii=False)

if st.button("GENERER TOP1 - " + sujet + " - 9 CASES CARICATURE"):

    ligne1 = "L'EXTREMISTE & LE SAGE -- NEWS " + top + " -- " + str(date.today()) + " -- SUJET: " + sujet.upper() + " -- 100% CHIENS 4 PATTES EXACTEMENT\n"
    ligne2 = "STYLE: Uderzo -- parchemin epure -- bulles blanches contour noir -- BOLD MAJUSCULE 8 mots max -- gros nez expressif -- CHAQUE CHIEN EXACTEMENT 4 PATTES SEULEMENT 4 JAMBES PAS 5 PATTES ANATOMIE CORRECTE PATTES CHIEN SEULEMENT -- 100% chiens aucun humain -- AUCUN DRONE si sujet!= 11 sept\n"
    ligne3 = "BIBLE ACTIVE: " + bible_json + "\n"
    ligne4 = "EXCLUE: " + str(tags_exclus) + "\n"
    ligne5 = "BUT: CARICATURER nouvelle " + sujet + " en faisant interagir Le Sage et Bas-Rouge avec sujet, varier intervenants logiquement, jamais repetitif\n\n"

    ligne6 = "9 CASES VARIEES OBLIGATOIRES CARICATURE SENS " + sujet + ":\n"
    ligne7 = "Case1 Contexte " + sujet + " -- Le Sage decouvre nouvelle lieu reel fleuve -- Sage Labrador couronne cape bord fleuve -- exactement 4 pattes\n"
    ligne8 = "BULLE LE SAGE: QUOI? BAR RAYE ENCORE? FORT!\n"
    ligne9 = "BULLE NARRATEUR: 2026. BAR RAYE FRAPPE. FORT.\n"
    ligne10 = "Case2 Husky Kahnawake pecheur filet bar raye -- Husky mohawk gilet orange APTN -- 4 pattes exactement\n"
    ligne11 = "BULLE HUSKY: BAR RAYE REVIENT! GROS! BEAU!\n"
    ligne12 = "BULLE NARRATEUR: Plan gestion 2026.\n"
    ligne13 = "Case3 Caniches pecheurs barque remise bar raye -- 4 pattes\n"
    ligne14 = "BULLE CANICHE: ON REMET! ON PROTEGE! VITE!\n"
    ligne15 = "BULLE NARRATEUR: Capture = remise obligatoire.\n"
    ligne16 = "Case4 Bas-Rouge Beauceron torche casque aile viking face bar raye geant -- 4 pattes exactement\n"
    ligne17 = "BULLE BAS-ROUGE: C EST QUOI CA? GRRR! FURIEUX!\n"
    ligne18 = "BULLE NARRATEUR: L Extremiste debarque.\n"
    ligne19 = "Case5 Le Sage tempere + Berger garde faune jumelles bord fleuve -- chaque chien 4 pattes\n"
    ligne20 = "BULLE LE SAGE: CALME. ON COMPREND. ON PROTEGE.\n"
    ligne21 = "BULLE GARDE: ON SURVEILLE! ZONE PROTEGEE!\n"
    ligne22 = "Case6 Caniches quai pancarte PECHE INTERDITE OUEST RIMOUSKI carte fleuve -- 4 pattes\n"
    ligne23 = "BULLE CANICHE: INTERDIT OUEST! EST OK!\n"
    ligne24 = "BULLE NARRATEUR: Loi federale protege.\n"
    ligne25 = "Case7 Duo Le Sage + Bas-Rouge cote a cote face fleuve banc bar raye -- 2 chiens 4 pattes chacun\n"
    ligne26 = "BULLE LE SAGE: ON VEILLE. ENSEMBLE. FLEUVE.\n"
    ligne27 = "BULLE BAS-ROUGE: FURIEUX! MAIS PRESENT!\n"
    ligne28 = "Case8 Carney Golden pupitre Ministere Faune PLAN GESTION 2026 20 ANS -- 4 pattes\n"
    ligne29 = "BULLE CARNEY: ESPECE EMBLEMATIQUE! PROTEGEE! 20 ANS!\n"
    ligne30 = "BULLE NARRATEUR: Population retablie.\n"
    ligne31 = "Case9 Finale Le Sage + Bas-Rouge coucher soleil bar raye saute -- 4 pattes exactement\n"
    ligne32 = "BULLE LE SAGE: BAR RAYE PASSE. MEMOIRE RESTE.\n"
    ligne33 = "BULLE BAS-ROUGE: CHAQUE RAYURE, HISTOIRE FLEUVE!\n"
    ligne34 = "BULLE FIN: UNITE ET COEUR. PROTEGER FLEUVE.\n"
    ligne35 = "TITRE: L'EXTREMISTE & LE SAGE -- " + str(date.today()) + " -- " + sujet.upper() + " -- TOP1 -- 100% CHIENS 4 PATTES\n"

    prompt_final = ligne1 + ligne2 + ligne3 + ligne4 + ligne5 + ligne6 + ligne7 + ligne8 + ligne9 + ligne10 + ligne11 + ligne12 + ligne13 + ligne14 + ligne15 + ligne16 + ligne17 + ligne18 + ligne19 + ligne20 + ligne21 + ligne22 + ligne23 + ligne24 + ligne25 + ligne26 + ligne27 + ligne28 + ligne29 + ligne30 + ligne31 + ligne32 + ligne33 + ligne34 + ligne35

    st.code(prompt_final, language="text")
    st.download_button("Telecharger prompt V8.1", prompt_final, file_name="prompt_v8_1.txt")
    st.success("V8.1 genere -- 4 pattes fix -- syntaxe OK")
