import streamlit as st, json, os, requests
from datetime import date

st.set_page_config(page_title="L'Extremiste & Le Sage - V6 Recherche", layout="wide")
st.title("L'EXTREMISTE & LE SAGE — V6 Recherche Auto + Manuelle")

BIBLE_FILE = "bible_vivante.json"
def load_bible():
    if os.path.exists(BIBLE_FILE):
        with open(BIBLE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
bible = load_bible()

# SIDEBAR BIBLE
with st.sidebar:
    st.header("📖 Bible Vivante")
    st.write(f"{len(bible)} persos")
    for k in bible.keys():
        st.caption(f"• {k}")
    st.divider()
    new_nom = st.text_input("Nouveau perso")
    new_desc = st.text_input("Desc chien 4 pattes")
    if st.button("Ajouter"):
        bible[new_nom]=new_desc
        with open(BIBLE_FILE,"w",encoding="utf-8") as fw:
            json.dump(bible,fw,ensure_ascii=False,indent=2)
        st.rerun()

# NOUVEAU: SYSTEME RECHERCHE
st.subheader("🔍 Système de recherche sujet")
mode = st.radio("Mode:", ["🔎 Recherche manuelle (tape sujet)", "🤖 Recherche auto news du jour"], horizontal=True)

sujet_final = ""
top = "TOP1"

if mode == "🔎 Recherche manuelle (tape sujet)":
    sujet_final = st.text_input("Sujet du jour", value="Sépaq gratuite")
    
else:
    st.write("🤖 Recherche automatique — 12 sept 2026")
    if st.button("🚀 Lancer recherche auto Québec/Canada"):
        with st.spinner("Recherche en cours..."):
            # Simulation recherche auto — remplace par vrai RSS plus tard
            news_auto = [
                {"titre": "Sépaq gratuite aujourd'hui 15e Journée parcs", "sujet": "Sépaq gratuite 2026", "source": "Espaces.ca"},
                {"titre": "Québec baisse immigration à 45k - Roberge", "sujet": "Immigration Québec 45k", "source": "Assemblée Nationale"},
                {"titre": "Rassemblement 13h30 devant parlement Québec C'EST NOUS", "sujet": "Rassemblement Québec 13h30", "source": "YouTube"},
                {"titre": "Loi anti-patchs 5000$ Longueuil Ian Lafreniere", "sujet": "Loi patchs 5000$ Longueuil", "source": "Québec.ca"},
                {"titre": "El Niño / Sécheresse 2026 alerte chaleur 40°C", "sujet": "Sécheresse 40°C Québec", "source": "Météo"}
            ]
            st.session_state["news_auto"] = news_auto
    
    if "news_auto" in st.session_state:
        st.write("### 📰 Résultats auto — Clique pour sélectionner:")
        for i, n in enumerate(st.session_state["news_auto"]):
            col1, col2 = st.columns([3,1])
            with col1:
                st.write(f"**{i+1}. {n['titre']}** — _{n['source']}_")
            with col2:
                if st.button(f"Choisir", key=f"choose_{i}"):
                    st.session_state["sujet_choisi"] = n["sujet"]
        
        if "sujet_choisi" in st.session_state:
            sujet_final = st.session_state["sujet_choisi"]
            st.success(f"✅ Sujet choisi: **{sujet_final}**")
            # Option éditer
            sujet_final = st.text_input("Modifier si besoin:", value=sujet_final)

# GENERATION PROMPT (même logique qu'avant)
if sujet_final:
    tags_exclus=[]
    if "11 sept" not in sujet_final.lower() and "drone" not in sujet_final.lower():
        tags_exclus.extend(["Drones Hommage 2977","Tribute in Light"])
    if "trump" not in sujet_final.lower():
        tags_exclus.append("Trump")
    bible_filtre={k:v for k,v in bible.items() if k not in tags_exclus}

    if st.button(f"🎨 GENERER {top} — {sujet_final} — BULLES PUNCHÉ"):
        prompt_final = f"""L'EXTRÉMISTE & LE SAGE — NEWS {top} — {date.today()} — SUJET: {sujet_final} — VERSION EPUREE BIBLE VIVANTE 100% CHIENS 4 PATTES 3x3 — BULLES COURTES PUNCHÉ UDERZO MAX 8 MOTS
STYLE: Uderzo — BULLES MAX 8 MOTS — BOLD LISIBLE — GROS NEZ EXPRESSIF
BIBLE ACTIVE: {json.dumps(bible_filtre, ensure_ascii=False)}
EXCLUE: {tags_exclus}
AUCUN DRONE SI SUJET != 11 SEPT

9 CASES BULLES PUNCHÉES:
Case1: Contexte {sujet_final} vue large
BULLE NARRATEUR: "2026. {sujet_final.upper()} FRAPPE. FORT."
Case2: Carney Golden pupitre drapeau
BULLE CARNEY: "{sujet_final.upper()} + CHAUD = EXTRÊMES!"
BULLE NARRATEUR: "Ottawa s'inquiète."
Case3: Husky Kahnawake 40°C thermomètre sueur
BULLE HUSKY: "40°C! ON CUIT ICITTE!"
BULLE NARRATEUR: "Chantier = fournaise."
Case4: Ian Lafreniere Golden Sécurité Québec loi
BULLE IAN: "LOI 5000$! ON SÉVIT!"
BULLE NARRATEUR: "Québec sévit."
Case5: Sylvia Jones Caniche santé hôpital
BULLE SYLVIA: "HYDRATEZ! RESTEZ FRAIS!"
BULLE NARRATEUR: "Hôpitaux débordent."
Case6: Familles Caniches solidarité bougies drapeaux
BULLE CANICHE: "ON S'ENTRAIDE! UNITÉ!"
BULLE NARRATEUR: "Voisins = force."
Case7: Pompiers FDNY Bergers feux forêt
BULLE POMPIER: "FEUX PARTOUT! ON TIENT!"
BULLE NARRATEUR: "Courage. Devoir."
Case8: Bas-Rouge Beauceron torche face {sujet_final}
BULLE BAS-ROUGE: "FURIEUX! MAIS ON VEILLE! GRRR!"
BULLE NARRATEUR: "L'Extrémiste veille."
Case9: Le Sage + Bas-Rouge dialogue final
BULLE LE SAGE: "{sujet_final.upper()} PASSE. MÉMOIRE RESTE."
BULLE BAS-ROUGE: "CHAQUE LOI, UNE HISTOIRE!"
BULLE NARRATEUR FIN: "UNITÉ & COEUR. PROTÉGER."
TITRE: L'EXTRÉMISTE & LE SAGE — {date.today()} — {sujet_final.upper()} — {top} — BULLES PUNCHÉES 100% CHIENS
"""
        st.code(prompt_final, language="text")
        st.download_button("📥 Télécharger prompt", prompt_final, file_name=f"prompt_{sujet_final}_{top}.txt")
