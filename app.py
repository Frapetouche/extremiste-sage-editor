import streamlit as st
import json
import os
import random
from datetime import date

st.set_page_config(page_title="V8.6 Option A Varie", layout="wide")
st.title("L'EXTREMISTE & LE SAGE - V8.6 Option A - 9 cases variees")

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
        "Le Sage": "Labrador noir couronne or cape beige sage yeux doux 4 pattes jamais humain",
        "Bas-Rouge": "Beauceron noir et feu casque aile viking torche foulard rouge yeux rouges furieux respectueux 4 pattes",
        "Mark Carney": "Golden Retriever premier ministre Canada cravate rouge drapeau Canada 4 pattes",
        "Monteur acier Kahnawake": "Husky mohawk casque chantier gilet orange calepin APTN drapeau Kahnawake 4 pattes",
        "Pompiers FDNY": "Bergers allemands casques FDNY tenue pompier courage 4 pattes",
        "Familles victimes": "Caniches blanc beige noir marron bougies recueillement 4 pattes",
        "Garde Faune": "Berger allemand garde faune jumelles chapeau vert 4 pattes"
    }

bible = load_bible()

with st.sidebar:
    st.header("BIBLIO PERSOS - Option A")
    st.caption(str(len(bible)) + " chiens - grossit auto")
    for k in list(bible.keys())[:12]:
        st.caption("- " + k)
    st.divider()
    nn = st.text_input("Nouveau perso manuel")
    dd = st.text_input("Description 4 pattes")
    if st.button("Ajouter perso"):
        if nn and dd:
            bible[nn] = dd
            fw = open(BIBLE_FILE, "w", encoding="utf-8")
            json.dump(bible, fw, ensure_ascii=False, indent=2)
            fw.close()
            st.rerun()
    if st.button("Reset decor seulement (garde persos)"):
        if "last_decor" in st.session_state:
            del st.session_state["last_decor"]
        st.success("Decor efface, persos gardes")

st.subheader("SUJET DU JOUR - source unique decor")
sujet = st.text_input("Sujet / nouvelle", value="Bal raye Quebec")
sujet_low = sujet.lower()

decor_jour = ""
if "saguenay" in sujet_low or "fjord" in sujet_low:
    decor_jour = "FJORD SAGUENAY bleuets montagnes quai"
    if "Fjord Bleuets" not in bible:
        bible["Fjord Bleuets"] = "Caniches Saguenay bleuets fjord 4 pattes"
elif "gaspesie" in sujet_low or "matane" in sujet_low or "rimouski" in sujet_low or "bal raye" in sujet_low or "bar raye" in sujet_low:
    decor_jour = "FLEUVE SAINT-LAURENT GASPESIE RIMOUSKI phare quai peche"
    if "Pecheur Gaspesie" not in bible:
        bible["Pecheur Gaspesie"] = "Caniches pecheurs Gaspesie tuques filets 4 pattes"
elif "el nino" in sujet_low or "pacifique" in sujet_low:
    decor_jour = "OCEAN PACIFIQUE chaud thermometre 30C soleil furieux"
    if "Meteo Pacifique" not in bible:
        bible["Meteo Pacifique"] = "Husky meteo thermometre El Nino 4 pattes"
elif "ottawa" in sujet_low or "parlement" in sujet_low:
    decor_jour = "OTTAWA PARLEMENT colline drapeau Canada pupitre"
elif "montreal" in sujet_low:
    decor_jour = "MONTREAL PORT ville quai"
elif "trump" in sujet_low or "tarif" in sujet_low:
    decor_jour = "FRONTIERE USA CANADA camions tarifs douane"
    if "Trump" not in bible:
        bible["Trump"] = "Bulldog orange cheveux orange tarifs 4 pattes"
else:
    decor_jour = "LIEU REEL DU SUJET " + sujet

if decor_jour!= "":
    st.info("Decor du jour (neuf): " + decor_jour + " | Biblio: " + str(len(bible)) + " chiens")

bible_json = json.dumps(bible, ensure_ascii=False)

if st.button("GENERER TOP1 - 9 CASES VARIEES AUTO - OPTION A"):
    today = str(date.today())
    up = sujet.upper()

    intros = [
        "Le Sage decouvre " + sujet + " dans " + decor_jour,
        "Le Sage + jumelles bord " + decor_jour + " repere " + sujet,
        "Le Sage capte nouvelle " + sujet + " radio " + decor_jour,
        "Le Sage lit journal " + sujet + " " + decor_jour
    ]
    c2_list = [
        "Husky filet " + sujet + " dans " + decor_jour,
        "Carney annonce " + sujet + " pupitre " + decor_jour,
        "Husky drone survole " + sujet + " " + decor_jour,
        "Carney + graphique " + sujet + " " + decor_jour
    ]
    c3_list = [
        "Caniches citoyens debattent " + sujet + " " + decor_jour,
        "Caniches pecheurs remise " + sujet + " " + decor_jour,
        "Caniches quai file attente " + sujet,
        "Caniches marche protestation " + sujet
    ]
    c4_list = [
        "Bas-Rouge torche face " + sujet + " geant " + decor_jour,
        "Bas-Rouge casque viking hurle sur " + sujet,
        "Bas-Rouge moto arrive " + decor_jour + " torche " + sujet,
        "Bas-Rouge aile viking charge " + sujet
    ]
    c5_list = [
        "Le Sage + Garde faune jumelles " + decor_jour,
        "Le Sage + Husky plan " + decor_jour,
        "Le Sage + Carney discutent " + sujet
    ]
    c6_list = [
        "Caniches pancarte REGLEMENT QUEBEC " + sujet,
        "Caniches pancarte ALERTE " + sujet,
        "Caniches panneau route " + decor_jour + " " + sujet
    ]
    c7_list = [
        "Duo Le Sage + Bas-Rouge " + decor_jour + " coucher soleil",
        "Duo Le Sage + Bas-Rouge face a face " + sujet,
        "Duo Le Sage + Bas-Rouge dos a dos protegent " + decor_jour
    ]
    c8_list = [
        "Carney pupitre Ministere sur " + sujet,
        "Carney point presse " + decor_jour + " carte " + sujet,
        "Carney + graphique climat " + sujet
    ]
    c9_list = [
        "Finale Le Sage + Bas-Rouge coucher soleil " + sujet + " saute " + decor_jour,
        "Finale tous chiens unis " + decor_jour + " " + sujet + " memoire",
        "Finale " + sujet + " + chiens amitie " + decor_jour
    ]

    c1 = random.choice(intros)
    c2 = random.choice(c2_list)
    c3 = random.choice(c3_list)
    c4 = random.choice(c4_list)
    c5 = random.choice(c5_list)
    c6 = random.choice(c6_list)
    c7 = random.choice(c7_list)
    c8 = random.choice(c8_list)
    c9 = random.choice(c9_list)

    p = ""
    p = p + "L'EXTREMISTE & LE SAGE -- " + today + " -- " + up + " -- 100% CHIENS 4 PATTES\n"
    p = p + "STYLE: Uderzo parchemin epure bulles blanches contour noir BOLD MAJUSCULE 8 mots max CHAQUE CHIEN 4 PATTES EXACTEMENT\n"
    p = p + "BIBLE PERSONNAGES PERMANENTS Option A garde: " + bible_json + "\n"
    p = p + "DECOR DU JOUR EPHEMERE seulement sujet: " + decor_jour + " -- VARIATION AUTO -- JAMAIS MEME\n"
    p = p + "REGLE ANTI-JAM: Persos permanents gardes, decor et contexte seulement sur sujet du jour. Si sujet ne contient pas Fjord, ne pas mettre Fjord. 9 cases variees tirees aleatoirement.\n"
    p = p + "9 CASES VARIEES SUR " + up + " AVEC DECOR " + decor_jour + ":\n"
    p = p + "Case1 " + c1 + " -- 4 pattes\n"
    p = p + "Case2 " + c2 + " -- 4 pattes\n"
    p = p + "Case3 " + c3 + " -- 4 pattes\n"
    p = p + "Case4 " + c4 + " -- 4 pattes\n"
    p = p + "Case5 " + c5 + " -- 4 pattes\n"
    p = p + "Case6 " + c6 + " -- 4 pattes\n"
    p = p + "Case7 " + c7 + " -- 4 pattes\n"
    p = p + "Case8 " + c8 + " -- 4 pattes\n"
    p = p + "Case9 " + c9 + " -- 4 pattes\n"

    fw = open(BIBLE_FILE, "w", encoding="utf-8")
    json.dump(bible, fw, ensure_ascii=False, indent=2)
    fw.close()

    st.code(p, language="text")
    st.download_button("Telecharger prompt V8.6", p, file_name="prompt_v8_6_optionA.txt")
    st.success("Option A: Biblio gardee " + str(len(bible)) + " chiens, decor neuf: " + decor_jour + " - 9 cases variees auto")
    
