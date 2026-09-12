import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="L'Extremiste & Le Sage - V8.2", layout="wide")
st.title("L'EXTREMISTE & LE SAGE — V8.2 Auto-Banque 4 Pattes")

BIBLE_FILE = "bible_vivante.json"

def load_bible():
    if os.path.exists(BIBLE_FILE):
        try:
            with open(BIBLE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {
        "Le Sage": "Labrador noir couronne or cape beige sage 4 pattes",
        "Bas-Rouge": "Beauceron noir et feu casque aile viking torche foulard rouge 4 pattes",
        "Mark Carney": "Golden Retriever PM Canada cravate rouge 4 pattes",
        "Husky Kahnawake": "Husky mohawk casque chantier gilet orange APTN 4 pattes",
        "Familles": "Caniches pecheurs solidaires 4 pattes",
        "Gardes": "Bergers allemands garde faune jumelles 4 pattes"
    }

bible = load_bible()

with st.sidebar:
    st.header("📖 Bible Vivante - Banque")
    st.write(f"{len(bible)} chiens")
    for k in bible.keys():
        st.caption(k)
    st.divider()
    nn = st.text_input("Nouveau perso")
    dd = st.text_input("Desc chien 4 pattes")
    if st.button("Ajouter manuel"):
        if nn and dd:
            bible[nn]=dd
            with open(BIBLE_FILE,"w",encoding="utf-8") as fw:
                json.dump(bible,fw,ensure_ascii=False,indent=2)
            st.rerun()

sujet_input = st.text_input("SUJET DU JOUR", value="Le bar raye ds le fleuve?")
top = "TOP1"

detect_map = {
    "legault": ("Legault", "Loup gris PM Quebec cravate bleue 4 pattes"),
    "trudeau": ("Trudeau", "Golden ancien PM Canada 4 pattes"),
    "trump": ("Trump", "Bouledogue americain casquette rouge 4 pattes"),
    "ford": ("Doug Ford", "Bulldog anglais Queens Park tarifs 4 pattes"),
    "bar raye": ("Garde Faune", "Berger allemand garde faune chapeau jumelles fleuve 4 pattes"),
    "tarifs": ("Douane", "Berger belge douanier Canada USA 4 pattes")
}

sujet_lower = sujet_input.lower()
nouveaux = []
for cle, (nom_bible, desc) in detect_map.items():
    if cle in sujet_lower and nom_bible not in bible:
        bible[nom_bible] = desc
        nouveaux.append(nom_bible)

if nouveaux:
    with open(BIBLE_FILE,"w",encoding="utf-8") as fw:
        json.dump(bible,fw,ensure_ascii=False,indent=2)
    st.toast(f"Auto-banque: {', '.join(nouveaux)} ajoutes!")

tags_exclus = []
if "11 sept" not in sujet_lower:
    tags_exclus.extend(["Drones Hommage 2977", "Tribute in Light"])
if "trump" not in sujet_lower and "tarif" not in sujet_lower:
    tags_exclus.append("Trump")

bible_filtre = {k:v for k,v in bible.items() if k not in tags_exclus}
bible_json = json.dumps(bible_filtre, ensure_ascii=False)

if st.button("GENERER TOP1 - " + sujet_input + " - 9 CASES"):
    ligne1 = "L'EXTREMISTE & LE SAGE -- NEWS " + top + " -- " + str(date.today()) + " -- SUJET: " + sujet_input.upper() + " -- 100% CHIENS 4 PATTES EXACTEMENT\n"
    ligne2 = "STYLE: Uderzo -- parchemin epure -- bulles blanches -- BOLD 8 mots max -- CHAQUE CHIEN EXACTEMENT 4 PATTES SEULEMENT 4 JAMBES PAS 5 PATTES ANATOMIE CORRECTE -- 100% chiens -- AUCUN DRONE si!=11 sept\n"
    ligne3 = "BIBLE ACTIVE: " + bible_json + "\n"
    ligne4 = "EXCLUE: " + str(tags_exclus) + "\n"
    ligne5 = "BUT: CARICATURER nouvelle " + sujet_input + " en faisant interagir Le Sage et Bas-Rouge, varier intervenants, jamais repetitif\n\n"
    ligne6 = "9 CASES VARIEES CASTING LOGIQUE CHAQUE CHIEN 4 PATTES:\n"
    ligne7 = "Case1 Le Sage decouvre " + sujet_input + " lieu reel -- 4 pattes\n"
    ligne8 = "BULLE LE SAGE: QUOI? SUJET ENCORE? FORT! -- BULLE NARRATEUR: 2026. " + sujet_input.upper() + " FRAPPE. FORT.\n"
    ligne9 = "Case2 Husky Kahnawake ou Carney selon sujet -- 4 pattes\n"
    ligne10 = "BULLE PERSO: 8 mots sens " + sujet_input + " -- BULLE NARRATEUR: Plan 2026.\n"
    ligne11 = "Case3 Caniches pecheurs ou caddie prix -- 4 pattes\n"
    ligne12 = "BULLE CANICHE: ON REMET! ON PROTEGE! VITE!\n"
    ligne13 = "Case4 Bas-Rouge torche face sujet geant -- 4 pattes exactement\n"
    ligne14 = "BULLE BAS-ROUGE: C EST QUOI CA? GRRR! FURIEUX! -- BULLE NARRATEUR: L Extremiste debarque.\n"
    ligne15 = "Case5 Le Sage + Garde faune Berger jumelles -- chaque chien 4 pattes\n"
    ligne16 = "BULLE LE SAGE: CALME. ON COMPREND. ON PROTEGE. -- BULLE GARDE: ON SURVEILLE! ZONE PROTEGEE!\n"
    ligne17 = "Case6 Caniches pancarte PECHE INTERDITE OUEST RIMOUSKI si bar raye ou epicerie si tarifs -- 4 pattes\n"
    ligne18 = "BULLE CANICHE: INTERDIT OUEST! EST OK!\n"
    ligne19 = "Case7 Duo Le Sage + Bas-Rouge cote a cote fleuve -- 2 chiens 4 pattes chacun\n"
    ligne20 = "BULLE LE SAGE: ON VEILLE. ENSEMBLE. -- BULLE BAS-ROUGE: FURIEUX! MAIS PRESENT!\n"
    ligne21 = "Case8 Carney ou Fedeli pupitre Ministere Faune ou Commerce -- 4 pattes\n"
    ligne22 = "BULLE CARNEY: ESPECE EMBLEMATIQUE! PROTEGEE! 20 ANS!\n"
    ligne23 = "Case9 Finale Le Sage + Bas-Rouge coucher soleil -- 4 pattes\n"
    ligne24 = "BULLE LE SAGE: " + sujet_input.upper() + " PASSE. MEMOIRE RESTE. -- BULLE BAS-ROUGE: CHAQUE RAYURE, HISTOIRE FLEUVE! -- FIN: UNITE ET COEUR. PROTEGER.\n"
    ligne25 = "TITRE: L'EXTREMISTE & LE SAGE -- " + str(date.today()) + " -- " + sujet_input.upper() + " -- TOP1 -- 100% CHIENS 4 PATTES -- AUTO-BANQUE\n"

    prompt_final = ligne1 + ligne2 + ligne3 + ligne4 + ligne5 + ligne6 + ligne7 + ligne8 + ligne9 + ligne10 + ligne11 + ligne12 + ligne13 + ligne14 + ligne15 + ligne16 + ligne17 + ligne18 + ligne19 + ligne20 + ligne21 + ligne22 + ligne23 + ligne24 + ligne25

    st.code(prompt_final, language="text")
    st.download_button("Telecharger prompt V8.2", prompt_final, file_name="prompt_v8_2.txt")
    st.success(f"V8.2 genere -- {len(bible_filtre)} chiens -- Auto-banque OK")
