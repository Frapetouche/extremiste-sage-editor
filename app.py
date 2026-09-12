import streamlit as st, json, os
from datetime import date

st.set_page_config(page_title="L'Extremiste & Le Sage - V5", layout="wide")
st.title("L'EXTREMISTE & LE SAGE — V5 Bulles Punché — TOP1 Auto")

BIBLE_FILE = "bible_vivante.json"

def load_bible():
    if os.path.exists(BIBLE_FILE):
        with open(BIBLE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

bible = load_bible()

with st.sidebar:
    st.header("📖 Bible Vivante Permanente")
    st.write(f"{len(bible)} persos")
    for k in bible.keys():
        st.caption(f"• {k}")
    st.divider()
    st.subheader("➕ Ajouter perso")
    new_nom = st.text_input("Nom")
    new_desc = st.text_input("Desc chien 4 pattes")
    if st.button("Ajouter"):
        bible[new_nom] = new_desc
        with open(BIBLE_FILE,"w",encoding="utf-8") as fw:
            json.dump(bible,fw,ensure_ascii=False,indent=2)
        st.rerun()

st.subheader("🔄 Nouvelle Analyse — TOP1 Auto — Bulles Punché")
top = "TOP1"  # Fixe, plus de sélection

sujet = st.text_input("SUJET DU JOUR", value="Sécheresse")
tags_exclus = []
if "11 sept" not in sujet.lower() and "2977" not in sujet.lower() and "drone" not in sujet.lower():
    tags_exclus.extend(["Drones Hommage 2977","Tribute in Light"])
if "trump" not in sujet.lower() and "tarif" not in sujet.lower():
    tags_exclus.append("Trump")

bible_filtre = {k:v for k,v in bible.items() if k not in tags_exclus}

if st.button(f"🎨 GENERER {top} — {sujet} — BULLES PUNCHÉ"):
    prompt_final = f"""L'EXTRÉMISTE & LE SAGE — NEWS {top} — {date.today()} — SUJET: {sujet} — VERSION EPUREE BIBLE VIVANTE 100% CHIENS 4 PATTES 3x3 — BULLES COURTES PUNCHÉ UDERZO MAX 8 MOTS
STYLE: Uderzo Astérix — BULLES PUNCHÉES MAX 8 MOTS — TEXTE BOLD MAJUSCULE LISIBLE — GROS NEZ EXPRESSIF
BIBLE ACTIVE: {json.dumps(bible_filtre, ensure_ascii=False)}
EXCLUE: {tags_exclus}
AUCUN DRONE SI SUJET != 11 SEPT

9 CASES BULLES PUNCHÉES:
Case1: Contexte {sujet} terre craquelée satellite
BULLE NARRATEUR: "2026. {sujet.upper()} FRAPPE. FORT."
Case2: Carney Golden pupitre drapeau
BULLE CARNEY: "{sujet.upper()} + CHAUD = EXTRÊMES!"
BULLE NARRATEUR: "Ottawa s'inquiète."
Case3: Husky Kahnawake 40°C thermomètre sueur
BULLE HUSKY: "40°C! ON CUIT ICITTE!"
BULLE NARRATEUR: "Chantier = fournaise."
Case4: Doug Ford Bulldog plan chaleur
BULLE DOUG: "PLAN CHALEUR! ACTION!"
BULLE NARRATEUR: "Ontario en sueur."
Case5: Sylvia Jones Caniche blanc santé hôpital ventilateur
BULLE SYLVIA: "HYDRATEZ! RESTEZ FRAIS!"
BULLE NARRATEUR: "Hôpitaux débordent."
Case6: Familles Caniches solidarité bougies ventilateur
BULLE CANICHE: "ON S'ENTRAIDE! UNITÉ!"
BULLE NARRATEUR: "Voisins = force."
Case7: Pompiers FDNY Bergers feux forêt
BULLE POMPIER: "FEUX PARTOUT! ON TIENT!"
BULLE NARRATEUR: "Courage. Devoir."
Case8: Bas-Rouge Beauceron casque aile torche face désert
BULLE BAS-ROUGE: "FURIEUX! MAIS ON VEILLE! GRRR!"
BULLE NARRATEUR: "L'Extrémiste veille."
Case9: Le Sage + Bas-Rouge dialogue final
BULLE LE SAGE: "{sujet.upper()} PASSE. MÉMOIRE RESTE."
BULLE BAS-ROUGE: "CHAQUE GOUTTE, UNE HISTOIRE!"
BULLE NARRATEUR FIN: "UNITÉ & COEUR. PROTÉGER."
TITRE: L'EXTRÉMISTE & LE SAGE — {date.today()} — {sujet.upper()} — {top} — BULLES PUNCHÉES 100% CHIENS
"""
    st.code(prompt_final, language="text")
    st.download_button("📥 Télécharger prompt", prompt_final, file_name=f"prompt_{sujet}_{top}.txt")
    st.success(f"✅ TOP1 {sujet} — {len(bible_filtre)} persos — prêt à coller ici")
