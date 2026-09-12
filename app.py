import streamlit as st, json, urllib.parse

st.set_page_config(page_title="L'Extremiste & Le Sage - BD", layout="wide")
st.title("L'EXTREMISTE & LE SAGE — Generateur BD 9 cases — Gratuit")

with open("bible_vivante.json", "r", encoding="utf-8") as f:
    bible = json.load(f)

with st.sidebar:
    st.header("📖 Bible Vivante")
    st.write(f"{len(bible)} persos")
    for k,v in bible.items():
        st.caption(f"**{k}**")
    new_nom = st.text_input("Nouveau perso")
    new_desc = st.text_input("Desc chien 4 pattes")
    if st.button("Ajouter"):
        bible[new_nom] = new_desc
        with open("bible_vivante.json","w",encoding="utf-8") as fw:
            json.dump(bible,fw,ensure_ascii=False,indent=2)
        st.rerun()

sujet = st.text_input("Sujet du jour", value="25e anniversaire 11 sept 2026 - 2,977 drones 1 drone=1 vie tours avec drones echelle reelle + coeur")
top = st.selectbox("TOP", ["TOP1","TOP2","TOP3","TOP4","TOP5"])

if st.button("🎨 GENERER PROMPT BD"):
    prompt_bd = f"""L'EXTRÉMISTE & LE SAGE — NEWS {top} — {sujet} — VERSION EPUREE BIBLE VIVANTE 100% CHIENS 4 PATTES 3x3
BIBLE: {json.dumps(bible, ensure_ascii=False)}
9 cases parchemin epure gros texte bold lisible Uderzo max 12 mots case:
1: 9 SEPT 2026 2,977 Lights NY Harbor 1 drone=1 vie tours echelle reelle faites drones helice Statue Liberte
2: Carney Golden declaration Il y a 25 ans matin clair journee sombre
3: Husky Kahnawake APTN monteur acier temoigne 25e
4: Hommage drones coeur + tours drones 2,977 drones=2,977 vies chaque lumiere une vie art transmet memoire Brenda Berkman
5-6: Ceremonie drapeaux USA Canada bougies coquelicots devoir memoire unite
8: Bas-Rouge Beauceron casque aile torche memoire respectueux On n'oublie jamais 2,977 vies chaque lumiere histoire famille
9: Le Sage Labrador noir couronne + Bas-Rouge dialogue memoire vivante transmission unite=force proteger memoire
Titre L'EXTRÉMISTE & LE SAGE — {sujet} — {top} — VIVE MEMOIRE!
Aucun humain tous chiens uniques 4 pattes
"""
    st.subheader("Prompt final prêt")
    st.code(prompt_bd, language="text")
    
    # Bouton pour copier et venir generer ici
    encoded = urllib.parse.quote(prompt_bd[:500])
    st.success("✅ Copie le prompt ci-dessus et colle-le ici dans Meta AI — je te genere la BD 9 cases instant!")
    st.download_button("📥 Telecharger prompt", prompt_bd, file_name="prompt_bd.txt")
    
    st.divider()
    st.info("Workflow gratuit: 1) Tu gardes ta bible dans l'app 2) Tu generes prompt 3) Tu colles ici → je te sors la BD")
