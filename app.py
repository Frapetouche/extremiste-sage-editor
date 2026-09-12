import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="V8.3.1 Fix", layout="wide")
st.title("L'EXTREMISTE & LE SAGE - V8.3.1 Fix Indent")

BIBLE_FILE = "bible_vivante.json"

def load_bible():
    if os.path.exists(BIBLE_FILE):
        try:
            f = open(BIBLE_FILE, "r", encoding="utf-8")
            data = json.load(f)
            f.close()
            return data
        except:
            pass
    return {
        "Le Sage": "Labrador noir couronne or cape beige 4 pattes",
        "Bas-Rouge": "Beauceron noir et feu casque aile viking torche foulard rouge 4 pattes",
        "Mark Carney": "Golden Retriever PM Canada 4 pattes",
        "Husky Kahnawake": "Husky mohawk gilet orange APTN 4 pattes"
    }

bible = load_bible()

with st.sidebar:
    st.header("Banque")
    st.write(str(len(bible)) + " chiens")
    nn = st.text_input("Nouveau perso")
    dd = st.text_input("Desc 4 pattes")
    if st.button("Ajouter"):
        if nn and dd:
            bible[nn] = dd
            fw = open(BIBLE_FILE, "w", encoding="utf-8")
            json.dump(bible, fw, ensure_ascii=False, indent=2)
            fw.close()
            st.rerun()

sujet = st.text_input("SUJET DU JOUR", value="Bar raye ds le Saguenay ironique quebecois")
bible_json = json.dumps(bible, ensure_ascii=False)

if st.button("GENERER TOP1 - 9 CASES"):
    today = str(date.today())
    up = sujet.upper()
    p = ""
    p = p + "L'EXTREMISTE & LE SAGE -- " + today + " -- " + up + " -- 100% CHIENS 4 PATTES\n"
    p = p + "STYLE: Uderzo parchemin epure bulles blanches BOLD 8 mots max 4 PATTES EXACTEMENT\n"
    p = p + "BIBLE: " + bible_json + "\n"
    p = p + "9 CASES QUEBECOIS FJORD:\n"
    p = p + "Case1 Le Sage Fjord -- QUOI? BAR RAYE ICI? AU SAG? BEN VOYONS! -- 4 pattes\n"
    p = p + "Case2 Husky -- TABARNAC! GROS! -- 4 pattes\n"
    p = p + "Case3 Caniches remise -- ON R'MET! VITE DE MEME! -- 4 pattes\n"
    p = p + "Case4 Bas-Rouge -- C EST QUOI CA? MAUDIT FURIEUX! -- 4 pattes\n"
    p = p + "Case5 Le Sage + Garde -- CALME-TOE. ON JASE. ON PROTEGE. / ON WATCH! FJORD PROTEGE! BEN OUI! -- 4 pattes\n"
    p = p + "Case6 Pancarte -- BEN OUI! C EST ICITTE TOE! -- 4 pattes\n"
    p = p + "Case7 Duo -- ON VEILLE. SAGUENAY. ENSEMBLE TOE. / FURIEUX! MAIS BLEUET! TABARNAC! -- 4 pattes\n"
    p = p + "Case8 Carney Faune -- ESPECE REMONTE! FJORD! 20 ANS ASTHEURE! -- 4 pattes\n"
    p = p + "Case9 Finale -- BAR RAYE SAGUENAY PASSE. FRETTE RESTE. / CHAQUE RAYURE, UNE POUTINE FJORD! -- 4 pattes\n"
    st.code(p, language="text")
    st.download_button("Telecharger prompt", p, file_name="prompt_v8_3_1.txt")
    st.success("OK -- 0 erreur -- pret")
