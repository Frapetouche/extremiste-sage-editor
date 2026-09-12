import streamlit as st, json, os
from datetime import date

st.set_page_config(page_title="L'Extremiste & Le Sage - V4 Bulles", layout="wide")
st.title("L'EXTREMISTE & LE SAGE — V4 Bulles Punché Uderzo")

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
    st.subheader("➕ Ajouter perso permanent")
    new_nom = st.text_input("Nom")
    new_desc = st.text_input("Desc chien 4 pattes unique")
    if st.button("Ajouter à bible"):
        bible[new_nom] = new_desc
        with open(BIBLE_FILE,"w",encoding="utf-8") as fw:
            json.dump(bible,fw,ensure_ascii=False,indent=2)
        st.rerun()

st.subheader("🔄 Nouvelle Analyse — Bulles Punché Uderzo")
st.caption("Modèle gardé, analyse neuve à chaque sujet, bulles courtes 8 mots max")

col1, col2 = st.columns(2)
with col1:
    sujet = st.text_input("SUJET DU JOUR", value="El Niño")
    top = st.selectbox("TOP", ["TOP1","TOP2","TOP3","TOP4","TOP5"])
with col2:
    tags_exclus = []
    if "11 sept" not in sujet.lower() and "2977" not in sujet.lower() and "drone" not in sujet.lower():
        tags_exclus.extend(["Drones Hommage 2977","Tribute in Light"])
    if "trump" not in sujet.lower() and "tarif" not in sujet.lower():
        tags_exclus.append("Trump")
    st.write("✅ Inclus / 🚫 Exclus auto:")
    if tags_exclus:
        st.caption(f"🚫 Exclus: {', '.join(tags_exclus)}")

# Filtre actif
bible_filtre = {k:v for k,v in bible.items() if k not in tags_exclus}

st.divider()
if st.button("🎨 GENERER PROMPT BULLES PUNCHÉ UDERZO"):
    bible_active = bible_filtre

    prompt_final = f"""L'EXTRÉMISTE & LE SAGE — NEWS {top} — {date.today()} — SUJET: {sujet} — VERSION EPUREE BIBLE VIVANTE 100% CHIENS 4 PATTES 3x3 — BULLES COURTES PUNCHÉ UDERZO MAX 8 MOTS
STYLE OBLIGATOIRE: Uderzo Astérix — BULLES PUNCHÉES — MAX 8 MOTS PAR BULLE — HUMOUR LEGER — GROS NEZ EXPRESSIF — TEXTE BOLD MAJUSCULE LISIBLE
BIBLE ACTIVE SEULEMENT (garder création): {json.dumps(bible_active, ensure_ascii=False)}
BIBLE EXCLUE (NE PAS RAMENER DU TOUT): {tags_exclus}
AUCUN DRONE SI SUJET != 11 SEPT

9 CASES AVEC BULLES PUNCHÉES:
Case1: Contexte {sujet} vue satellite / Pacifique rouge
BULLE NARRATEUR haut: "2026. {sujet.upper()} FRAPPE. FORT."

Case2: Carney Golden pupitre drapeau Canada
BULLE CARNEY: "{sujet} + CHAUD = EXTRÊMES!"
BULLE NARRATEUR bas: "Ottawa s'inquiète."

Case3: Husky Kahnawake chantier thermomètre 40°C sueur gouttes
BULLE HUSKY: "40°C! ON CUIT ICITTE!"
BULLE NARRATEUR: "Chantier = fournaise."

Case4: Doug Ford Bulldog plan chaleur papier PLAN CHALEUR Queens Park
BULLE DOUG: "PLAN CHALEUR! ACTION!"
BULLE NARRATEUR: "Ontario en sueur."

Case5: Sylvia Jones Caniche blanc santé hôpital ventilateur
BULLE SYLVIA: "HYDRATEZ! RESTEZ FRAIS!"
BULLE NARRATEUR: "Hôpitaux débordent."

Case6: Familles Caniches solidarité bougies ventilateur drapeaux entraide
BULLE CANICHE: "ON S'ENTRAIDE! UNITÉ!"
BULLE NARRATEUR: "Voisins = force."

Case7: Pompiers FDNY Bergers Allemands feux forêt sécheresse tuyau
BULLE POMPIER: "FEUX PARTOUT! ON TIENT!"
BULLE NARRATEUR: "Courage. Devoir."

Case8: Bas-Rouge Beauceron casque aile viking torche foulard rouge face océan déchaîné vagues énormes El Niño furieux yeux rouges
BULLE BAS-ROUGE grosse colère: "FURIEUX! MAIS ON VEILLE! GRRR!"
BULLE NARRATEUR: "L'Extrémiste veille."

Case9: Le Sage Labrador noir couronne cape + Bas-Rouge dialogue final bord mer coucher soleil
BULLE LE SAGE: "{sujet.upper()} PASSE. MÉMOIRE RESTE."
BULLE BAS-ROUGE: "CHAQUE DEGRÉ, UNE HISTOIRE!"
BULLE NARRATEUR FIN: "UNITÉ & COEUR. PROTÉGER."

TITRE HAUT: L'EXTRÉMISTE & LE SAGE — {date.today()} — {sujet.upper()} — {top} — BULLES PUNCHÉES UDERZO — 100% CHIENS
BAS: 3x3 — BIBLE VIVANTE — CHAQUE CHIEN UNIQUE — AUCUN HUMAIN — BULLES COURTES — {sujet.upper()} 2026
CONSIGNES: parchemin épuré, bulles blanches contour noir style Astérix, texte bold majuscule max 8 mots, chiens très expressifs gros nez, couleurs vives, 100% chiens 4 pattes aucun humain, AUCUN DRONE si sujet != 11 sept, humour punché Uderzo
"""
    st.code(prompt_final, language="text")
    st.download_button("📥 Télécharger prompt bulles", prompt_final, file_name=f"prompt_{sujet}_{top}_bulles.txt")
    st.success(f"✅ Prompt bulles punché généré — {len(bible_active)} persos actifs — colle-le ici pour BD")        
