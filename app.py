import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="V8.5 Creation + News Neuve", layout="wide")
st.title("L'EXTREMISTE & LE SAGE - V8.5 Garde persos, news neuve")

BIBLE_FILE = "bible_vivante.json"

# 1. MEMOIRE PERMANENTE - PERSONNAGES SEULEMENT
def load_bible_persos():
    if os.path.exists(BIBLE_FILE):
        try:
            f = open(BIBLE_FILE, "r", encoding="utf-8")
            data = json.load(f)
            f.close()
            return data
        except:
            pass
    return {
        "Le Sage": "Labrador noir couronne or cape beige sage 4 pattes",
        "Bas-Rouge": "Beauceron noir et feu casque aile viking torche foulard rouge 4 pattes",
        "Mark Carney": "Golden Retriever PM Canada 4 pattes",
        "Husky Kahnawake": "Husky mohawk gilet orange APTN 4 pattes",
        "Garde Faune": "Berger allemand garde faune 4 pattes",
        "Familles": "Caniches citoyens 4 pattes"
    }

bible_persos = load_bible_persos()

with st.sidebar:
    st.header("TES PERSOS (garde toujours)")
    for k in bible_persos.keys():
        st.caption(k)
    nn = st.text_input("Nouveau perso")
    dd = st.text_input("Desc 4 pattes")
    if st.button("Ajouter perso"):
        bible_persos[nn] = dd
        fw = open(BIBLE_FILE, "w", encoding="utf-8")
        json.dump(bible_persos, fw, ensure_ascii=False, indent=2)
        fw.close()
        st.rerun()

    if st.button("Reset decor seulement"):
        st.session_state["decor"] = ""
        st.success("Decor efface, persos gardes")

# 2. MEMOIRE EPHEMERE - DECOR / NOUVELLE - SEULEMENT SUJET DU JOUR
sujet = st.text_input("SUJET / NOUVELLE DU JOUR (seule source decor)", value="Super El Nino 2.7C record Pacifique")
sujet_low = sujet.lower()

# DECOR DU JOUR - CALCULE A CHAQUE FOIS SUR SUJET, PAS SUR MEMOIRE ANCIENNE
decor_jour = ""
if "saguenay" in sujet_low or "fjord" in sujet_low:
    decor_jour = "FJORD SAGUENAY bleuets montagnes quai"
elif "gaspesie" in sujet_low or "matane" in sujet_low or "rimouski" in sujet_low:
    decor_jour = "GASPESIE mer quai peche"
elif "el nino" in sujet_low or "pacifique" in sujet_low:
    decor_jour = "OCEAN PACIFIQUE chaud thermometre 30C soleil furieux"
elif "ottawa" in sujet_low or "parlement" in sujet_low:
    decor_jour = "OTTAWA parlement pupitre drapeau"
elif "montreal" in sujet_low:
    decor_jour = "MONTREAL port ville"
else:
    decor_jour = "LIEU REEL DU SUJET " + sujet

st.caption("Decor du jour (neuf a chaque fois): " + decor_jour)
st.caption("Persos gardes: " + str(len(bible_persos)))

bible_json = json.dumps(bible_persos, ensure_ascii=False)

if st.button("GENERER TOP1 - PERSOS GARDES / NEWS NEUVE"):
    today = str(date.today())
    up = sujet.upper()
    p = ""
    p = p + "L'EXTREMISTE & LE SAGE -- " + today + " -- " + up + " -- 100% CHIENS 4 PATTES\n"
    p = p + "STYLE: Uderzo parchemin epure bulles blanches BOLD 8 mots max CHAQUE CHIEN 4 PATTES\n"
    p = p + "BIBLE PERSONNAGES PERMANENTS (garder): " + bible_json + "\n"
    p = p + "DECOR DU JOUR EPHEMERE (seulement ce sujet, pas memoire ancienne): " + decor_jour + "\n"
    p = p + "REGLE ANTI-JAM: Utiliser personnages permanents MAIS decor et contexte SEULEMENT sur sujet du jour. Si sujet ne contient pas Fjord, ne pas mettre Fjord. Chaque generation est neuve sur la nouvelle.\n"
    p = p + "9 CASES VARIEES SUR " + up + " AVEC DECOR " + decor_jour + ":\n"
    p = p + "Case1 Le Sage decouvre " + sujet + " dans " + decor_jour + " -- 4 pattes\n"
    p = p + "Case2 Husky ou Carney selon sujet dans " + decor_jour + " -- 4 pattes\n"
    p = p + "Case3 Caniches selon sujet dans " + decor_jour + " -- 4 pattes\n"
    p = p + "Case4 Bas-Rouge torche face " + sujet + " geant dans " + decor_jour + " -- 4 pattes\n"
    p = p + "Case5 Le Sage + Garde faune jumelles " + decor_jour + " -- 4 pattes\n"
    p = p + "Case6 Caniches pancarte alerte " + sujet + " -- 4 pattes\n"
    p = p + "Case7 Duo Le Sage + Bas-Rouge " + decor_jour + " coucher soleil -- 4 pattes\n"
    p = p + "Case8 Carney pupitre ministere sur " + sujet + " -- 4 pattes\n"
    p = p + "Case9 Finale " + sujet + " passe memoire reste " + decor_jour + " -- 4 pattes\n"

    st.code(p, language="text")
    st.download_button("Telecharger prompt V8.5", p, file_name="prompt_v8_5.txt")
    st.success("Persos gardes, decor neuf sur: " + decor_jour)
