 import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="L'Extremiste & Le Sage V8.3", layout="wide")
st.title("L'EXTREMISTE & LE SAGE - V8.3 Syntaxe Clean 4 Pattes Quebecois")

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
        "Husky Kahnawake": "Husky mohawk gilet orange APTN 4 pattes",
        "Familles": "Caniches Saguenay bleuets 4 pattes",
        "Gardes": "Bergers allemands garde faune 4 pattes"
    }

bible = load_bible()

with st.sidebar:
    st.header("Banque")
    st.write(str(len(bible)) + " chiens")
    for k in bible.keys():
        st.caption(k)
    nn = st.text_input("Nouveau perso")
    dd = st.text_input("Desc 4 pattes")
    if st.button("Ajouter"):
        if nn and dd:
            bible[nn] = dd
            with open(BIBLE_FILE, "w", encoding="utf-8") as fw:
                json.dump(bible, fw, ensure_ascii=False, indent=2)
            st.rerun()

sujet_input = st.text_input("SUJET DU JOUR", value="Bar raye ds le Saguenay ironique quebecois")
sujet_lower = sujet_input.lower()

detect_map = {
    "legault": ("Legault", "Loup gris PM Quebec 4 pattes"),
    "trump": ("Trump", "Bouledogue USA 4 pattes"),
    "bar raye": ("Garde Faune", "Berger allemand garde faune Fjord 4 pattes"),
    "tarifs": ("Douane", "Berger belge douane 4 pattes"),
    "el nino": ("Meteo", "Husky meteo thermometre El Nino 4 pattes")
}

nouveaux = []
for cle in detect_map:
    nom_bible, desc = detect_map[cle]
    if cle in sujet_lower and nom_bible not in bible:
        bible[nom_bible] = desc
        nouveaux.append(nom_bible)

if nouveaux:
    with open(BIBLE_FILE, "w", encoding="utf-8") as fw:
        json.dump(bible, fw, ensure_ascii=False, indent=2)
    st.toast("Auto-banque ajoute: " + ", ".join(nouveaux))

tags_exclus = []
if "11 sept" not in sujet_lower:
    tags_exclus.append("Drones")
if "trump" not in sujet_lower and "tarif" not in sujet_lower:
    tags_exclus.append("Trump")

bible_filtre = {}
for k, v in bible.items():
    if k not in tags_exclus:
        bible_filtre[k] = v

bible_json = json.dumps(bible_filtre, ensure_ascii=False)

if st.button("GENERER TOP1 9 CASES"):
    today = str(date.today())
    upper_sujet = sujet_input.upper()

    prompt = ""
    prompt = prompt + "L'EXTREMISTE & LE SAGE -- NEWS TOP1 -- " + today + " -- SUJET: " + upper_sujet + " -- 100% CHIENS 4 PATTES EXACTEMENT\n"
    prompt = prompt + "STYLE: Uderzo -- parchemin epure -- bulles blanches contour noir -- BOLD MAJUSCULE 8 mots max -- gros nez -- CHAQUE CHIEN EXACTEMENT 4 PATTES SEULEMENT 4 JAMBES ANATOMIE CORRECTE PAS DE MAIN HUMAINE -- 100% chiens -- AUCUN DRONE\n"
    prompt = prompt + "BIBLE ACTIVE: " + bible_json + "\n"
    prompt = prompt + "EXCLUE: " + str(tags_exclus) + "\n"
    prompt = prompt + "BUT: Caricaturer " + sujet_input + " avec Le Sage et Bas-Rouge, casting varie, ironique quebecois joual\n\n"
    prompt = prompt + "9 CASES VARIEES CHAQUE CHIEN 4 PATTES EXACTEMENT:\n"
    prompt = prompt + "Case1 Le Sage decouvre " + sujet_input + " Fjord Saguenay -- 4 pattes\n"
    prompt = prompt + "BULLE LE SAGE: QUOI? BAR RAYE ICI? AU SAG? BEN VOYONS!\n"
    prompt = prompt + "BULLE NARRATEUR: 2026. BAR RAYE REMONTE AU FJORD.\n"
    prompt = prompt + "Case2 Husky Kahnawake filet bar raye -- 4 pattes\n"
    prompt = prompt + "BULLE HUSKY: BAR RAYE AU SAG? TABARNAC! GROS!\n"
    prompt = prompt + "Case3 Caniches Saguenay barque remise -- 4 pattes\n"
    prompt = prompt + "BULLE CANICHE: ON R'MET! FJORD SAGUENAY! VITE!\n"
    prompt = prompt + "Case4 Bas-Rouge torche face bar raye geant Fjord -- 4 pattes exactement\n"
    prompt = prompt + "BULLE BAS-ROUGE: C EST QUOI CA? AU SAGUENAY? MAUDIT FURIEUX!\n"
    prompt = prompt + "Case5 Le Sage + Garde faune Berger jumelles Fjord -- chaque chien 4 pattes\n"
    prompt = prompt + "BULLE LE SAGE: CALME-TOE. ON JASE. ON PROTEGE.\n"
    prompt = prompt + "BULLE GARDE: ON WATCH! FJORD PROTEGE! BEN OUI!\n"
    prompt = prompt + "Case6 Caniches quai pancarte PECHE FJORD PERMIS EST -- 4 pattes\n"
    prompt = prompt + "BULLE CANICHE: SAGUENAY? BEN OUI! C EST ICITTE TOE!\n"
    prompt = prompt + "Case7 Duo Le Sage + Bas-Rouge Fjord coucher soleil -- 2 chiens 4 pattes chacun\n"
    prompt = prompt + "BULLE LE SAGE: ON VEILLE. SAGUENAY. ENSEMBLE TOE.\n"
    prompt = prompt + "BULLE BAS-ROUGE: FURIEUX! MAIS BLEUET! TABARNAC!\n"
    prompt = prompt + "Case8 Carney Golden pupitre Faune FJORD -- 4 pattes\n"
    prompt = prompt + "BULLE CARNEY: ESPECE REMONTE! FJORD! 20 ANS ASTHEURE!\n"
    prompt = prompt + "Case9 Finale Le Sage + Bas-Rouge coucher soleil bar raye saute -- 4 pattes\n"
    prompt = prompt + "BULLE LE SAGE: BAR RAYE SAGUENAY PASSE. FRETTE RESTE.\n"
    prompt = prompt + "BULLE BAS-ROUGE: CHAQUE RAYURE, UNE POUTINE FJORD!\n"
    prompt = prompt + "BULLE FIN: UNITE ET COEUR. FJORD BLEUET.\n"
    prompt = prompt + "TITRE: L'EXTREMISTE & LE SAGE -- " + today + " -- " + upper_sujet + " -- TOP1 -- 100% CHIENS 4 PATTES -- QUEBECOIS\n"

    st.code(prompt, language="text")
    st.download_button("Telecharger prompt V8.3", prompt, file_name="prompt_v8_3.txt")
    st.success("V8.3 genere -- 0 erreur syntaxe -- " + str(len(bible_filtre)) + " chiens -- 4 pattes -- Quebecois")

st.caption("V8.3 - Fix definitif: plus de + en chaine, plus de accolades, 4 pattes exact, bulles quebecoises")
