import streamlit as st, json, os
from datetime import date

st.set_page_config(page_title="L'Extremiste & Le Sage - Editeur v3", layout="wide")
st.title("L'EXTREMISTE & LE SAGE — Editeur Bible Vivante v3")

BIBLE_FILE = "bible_vivante.json"

def load_bible():
    if os.path.exists(BIBLE_FILE):
        with open(BIBLE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

bible = load_bible()

with st.sidebar:
    st.header("📖 Bible Vivante — Création permanente")
    st.write(f"{len(bible)} persos créés")
    for k in bible.keys():
        st.caption(f"• {k}")

    st.divider()
    st.subheader("Ajouter nouveau perso permanent")
    new_nom = st.text_input("Nom perso")
    new_desc = st.text_input("Description chien 4 pattes unique")
    if st.button("➕ Ajouter à bible vivante"):
        bible[new_nom] = new_desc
        with open(BIBLE_FILE,"w",encoding="utf-8") as fw:
            json.dump(bible,fw,ensure_ascii=False,indent=2)
        st.success(f"{new_nom} ajouté!")
        st.rerun()

st.subheader("🔄 Nouvelle Analyse — Repartir à zéro pour chaque sujet")
st.write("Modèle et création gardés, mais analyse neuve")

col1, col2 = st.columns(2)
with col1:
    sujet = st.text_input("SUJET DU JOUR (ex: El Niño, Trump tarifs, 11 sept)", value="El Niño")
    top = st.selectbox("TOP", ["TOP1","TOP2","TOP3","TOP4","TOP5"])
with col2:
    # Filtre intelligent
    st.write("Persos pertinents pour ce sujet :")
    # Tags automatiques
    tags_exclus = []
    if "11 sept" not in sujet.lower() and "drones" not in sujet.lower() and "2977" not in sujet:
        tags_exclus.append("Drones Hommage 2977")
        tags_exclus.append("Tribute in Light")
    if "trump" not in sujet.lower() and "tarif" not in sujet.lower():
        tags_exclus.append("Trump")

    bible_filtre = {k:v for k,v in bible.items() if k not in tags_exclus}

    for k in bible_filtre.keys():
        st.checkbox(k, value=True, key=f"check_{k}", disabled=False)

    if tags_exclus:
        st.caption(f"🚫 Exclus auto pour ce sujet: {', '.join(tags_exclus)} (pas ramenés)")

if st.button("🎨 GENERER PROMPT ANALYSE NEUVE — BIBLE GARDÉE"):
    # Recup seulement ceux cochés
    bible_active = {}
    for k in bible.keys():
        if f"check_{k}" in st.session_state and st.session_state[f"check_{k}"]:
            bible_active[k] = bible[k]
        elif k not in tags_exclus: # par defaut si pas de checkbox
            if k in bible_filtre:
                bible_active[k] = bible[k]

    prompt_final = f"""L'EXTRÉMISTE & LE SAGE — NEWS {top} — {date.today()} — SUJET: {sujet} — VERSION EPUREE BIBLE VIVANTE 100% CHIENS 4 PATTES 3x3
NOUVELLE ANALYSE — SUJET NEUF — ON REPART A ZERO POUR L'ANALYSE MAIS ON GARDE CREATION ET MODELE
BIBLE ACTIVE POUR CE SUJET SEULEMENT: {json.dumps(bible_active, ensure_ascii=False)}
BIBLE EXCLUE POUR CE SUJET (ne pas ramener): {tags_exclus}
9 cases parchemin epure gros texte bold lisible Uderzo max 12 mots case:
Case1: Sujet {sujet} — contexte actuel
Case2-7: Developpement sujet avec persos actifs seulement
Case8: Bas-Rouge Beauceron casque aile torche — reaction sujet actuel
Case9: Le Sage Labrador + Bas-Rouge dialogue memoire transmission sujet {sujet}
Titre: L'EXTRÉMISTE & LE SAGE — {date.today()} — {sujet} — {top} — BIBLE VIVANTE {len(bible_active)} persos — 100% CHIENS
AUCUN HUMAIN — CHAQUE CHIEN UNIQUE — NOUVELLE ANALYSE — MEME MODELE
"""
    st.code(prompt_final, language="text")
    st.download_button("📥 Télécharger prompt neuf", prompt_final, file_name=f"prompt_{sujet}_{top}.txt")
    st.success(f"✅ Nouvelle analyse pour {sujet} — {len(bible_active)} persos gardés, {len(tags_exclus)} exclus (drones pas ramenés)")
