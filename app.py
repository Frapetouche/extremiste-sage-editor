import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="V8.3 Fix", layout="wide")
st.title("L'EXTREMISTE & LE SAGE - V8.3 Fix Definitif")

BIBLE_FILE = "bible_vivante.json"

def load_bible():
    if os.path.exists(BIBLE_FILE):
        try:
            f = open(BIBLE_FILE, "r", encoding="utf-8")
            return json.load(f)
        except:
            pass
    return {"Le Sage": "Labrador 4 pattes", "Bas-Rouge": "Beauceron 4 pattes"}

bible = load_bible()

with st.sidebar:
    st.write(str(len(bible)) + " chiens en banque")
    nn = st.text_input("Nouveau")
    dd = st.text_input("Desc 4 pattes")
    if st.button("Ajouter"):
        bible[nn] = dd
        fw = open(BIBLE_FILE, "w", encoding="utf-8")
        json.dump(bible, fw, ensure_ascii=False, indent=2)
        fw.close()
        st.rerun()

sujet = st.text_input("SUJET", value="Bar raye ds le Saguenay ironique quebecois")
sujet_low = sujet.lower()
bible_json = json.dumps(bible, ensure_ascii=False)

if st.button("GENERER"):
    today = str(date.today())
    up = sujet.upper()
    p = ""
    p = p + "L'EXTREMISTE & LE SAGE -- " + today + " -- " + up + " -- 100% CHIENS 4 PATTES\n"
    p = p + "STYLE Uderzo parchemin epure bulles blanches BOLD 8 mots max CHAQUE CHIEN 4 PATTES SEULEMENT\n"
    p = p + "BIBLE: " + bible_json + "\n"
    p = p + "9 CASES FJORD SAGUENAY QUEBECOIS:\n"
    p = p + "Case1 Le Sage Fjord -- BULLE: QUOI? BAR RAYE ICI? AU SAG? BEN VOYONS! -- 4 pattes\n"
    p = p + "Case2 Husky filet -- BULLE: TABARNAC! GROS! -- 4 pattes\n"
    p = p + "Case3 Caniches barque remise -- BULLE: ON R'MET! VITE DE MEME! -- 4 pattes\n"
    p = p + "Case4 Bas-Rouge torche face bar raye -- BULLE: C EST QUOI CA? MAUDIT FURIEUX! -- 4 pattes\n"
    p = p + "Case5 Le Sage + Garde faune -- BULLE: CALME-TOE. ON JASE. ON PROTEGE. / ON WATCH! FJORD PROTEGE! BEN OUI! -- 4 pattes\n"
    p = p + "Case6 Pancarte FJORD -- BULLE: BEN OUI! C EST ICITTE TOE! -- 4 pattes\n"
    p = p + "Case7 Duo veille -- BULLE: ON VEILLE. SAGUENAY. ENSEMBLE TOE. / FURIEUX! MAIS BLEUET! TABARNAC! -- 4 pattes\n"
    p = p + "Case8 Carney Ministere Faune -- BULLE: ESPECE REMONTE! FJORD! 20 ANS ASTHEURE! -- 4 pattes\n"
    p = p + "Case9 Finale coucher soleil -- BULLE: BAR RAYE SAGUENAY PASSE. FRETTE RESTE. / CHAQUE RAYURE, UNE POUTINE FJORD! -- FIN UNITE ET COEUR FJORD BLEUET -- 4 pattes\n"
    st.code(p)
    st.download_button("Telecharger", p, file_name="prompt.txt")
    st.success("OK 0 erreur syntaxe")
