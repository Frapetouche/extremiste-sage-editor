import streamlit as st, json, os
from datetime import date

st.set_page_config(page_title="L'Extremiste & Le Sage - V8 Fix", layout="wide")
st.title("L'EXTREMISTE & LE SAGE — V8 Système Intelligent Fix")

BIBLE_FILE = "bible_vivante.json"
def load_bible():
    if os.path.exists(BIBLE_FILE):
        with open(BIBLE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
bible = load_bible()

with st.sidebar:
    st.header("📖 Bible Vivante")
    for k,v in bible.items():
        st.caption(f"• {k}")
    st.divider()
    new_nom = st.text_input("Nouveau perso connu -> chien")
    new_desc = st.text_input("Desc chien 4 pattes")
    if st.button("Ajouter"):
        bible[new_nom]=new_desc
        with open(BIBLE_FILE,"w",encoding="utf-8") as fw:
            json.dump(bible,fw,ensure_ascii=False,indent=2)
        st.rerun()

st.subheader("🎯 Système transformation auto")
sujet = st.text_input("SUJET DU JOUR", value="Guerre des tarifs")
top = "TOP1"

tags_exclus=[]
if "11 sept" not in sujet.lower() and "drone" not in sujet.lower():
    tags_exclus.extend(["Drones Hommage 2977","Tribute in Light"])
if "trump" not in sujet.lower() and "tarif" not in sujet.lower():
    tags_exclus.append("Trump")
bible_filtre={k:v for k,v in bible.items() if k not in tags_exclus}
bible_json = json.dumps(bible_filtre, ensure_ascii=False)

if st.button(f"🎨 GENERER {top} — {sujet} — 9 CASES CARICATURE"):
    prompt_final = (
    "L'EXTRÉMISTE & LE SAGE — NEWS " + top + " — " + str(date.today()) + " — SUJET: " + sujet.upper() + " — VERSION EPUREE BIBLE VIVANTE 100% CHIENS 4 PATTES 3x3 — BULLES COURTES PUNCHÉ UDERZO MAX 8 MOTS\n"
    "STYLE: Uderzo — parchemin épuré — bulles blanches contour noir — BOLD MAJUSCULE lisible max 8 mots — gros nez expressif — 100% chiens aucun humain — AUCUN DRONE si sujet != 11 sept\n"
    "BIBLE ACTIVE: " + bible_json + "\n"
    "EXCLUE: " + str(tags_exclus) + "\n"
    "BUT: CARICATURER la nouvelle " + sujet + " en faisant interagir Le Sage et Bas-Rouge avec le sujet, varier intervenants logiquement, jamais répétitif\n"
    "\n"
    "9 CASES VARIÉES OBLIGATOIRES:\n"
    "Case1 Contexte " + sujet + " — Le Sage découvre la nouvelle lieu réel du sujet\n"
    "BULLE LE SAGE: QUOI? SUJET ENCORE? FORT!\n"
    "BULLE NARRATEUR: 2026. " + sujet.upper() + " FRAPPE. FORT.\n"
    "Case2 Personnage connu transformé en chien selon sujet (Carney Golden PM si tarifs, Husky Kahnawake si bar rayé ou chantier, Lafreniere Golden si loi patchs, Fedeli si commerce) pupitre action\n"
    "BULLE PERSO: bulle 8 mots max adaptée au sens réel du sujet " + sujet + "\n"
    "BULLE NARRATEUR: narrateur varié adapté\n"
    "Case3 Terrain conséquence concrète de " + sujet + " — autre intervenant (ex: Caniches prix caddie si tarifs, pêcheurs barque remise si bar rayé, chantier 40C si chaleur)\n"
    "BULLE PERSO: 8 mots sens " + sujet + "\n"
    "BULLE NARRATEUR: varié\n"
    "Case4 Bas-Rouge Beauceron torche casque aile viking entre tôt face au sujet personnifié (containers USA feu si tarifs, banc bar rayé géant si bar rayé, pancarte patchs si loi)\n"
    "BULLE BAS-ROUGE: C EST QUOI CA? GRRR! FURIEUX!\n"
    "BULLE NARRATEUR: L Extremiste débarque.\n"
    "Case5 Le Sage tempère + autre connu (Ford Bulldog Queens Park si tarifs, Sylvia Jones santé si chaleur, Garde faune si bar rayé)\n"
    "BULLE LE SAGE: CALME. ON COMPREND. ON PROTEGE.\n"
    "BULLE PERSO: réponse courte sens sujet\n"
    "Case6 Familles Caniches citoyens impactés par " + sujet + " décor différent (épicerie prix, fleuve barque, Sépaq rando, Longueuil rue)\n"
    "BULLE CANICHE: bulle solidarité 8 mots sens " + sujet + "\n"
    "BULLE NARRATEUR: Voisins = force adapté\n"
    "Case7 Duo Le Sage + Bas-Rouge côte à côte face au coeur de " + sujet + " (carte Rimouski interdit ouest si bar rayé, containers douane si tarifs, barrière Longueuil si patchs)\n"
    "BULLE LE SAGE: ON VEILLE. ENSEMBLE.\n"
    "BULLE BAS-ROUGE: FURIEUX! MAIS PRESENT!\n"
    "Case8 Action solution intervenant #4 agit sur " + sujet + " (Vic Fedeli tableau COMMERCE 5000 si tarifs, Bergers gardes jumelles si bar rayé, Rottweilers menottés si patchs)\n"
    "BULLE PERSO: ON SURVEILLE! ON PROTEGE!\n"
    "BULLE NARRATEUR: Action. Protection.\n"
    "Case9 Finale philosophique Le Sage + Bas-Rouge coucher soleil bord fleuve St-Laurent, leçon de " + sujet + "\n"
    "BULLE LE SAGE: " + sujet.upper() + " PASSE. MEMOIRE RESTE.\n"
    "BULLE BAS-ROUGE: CHAQUE DETAIL, UNE HISTOIRE!\n"
    "BULLE NARRATEUR FIN: UNITE ET COEUR. PROTEGER.\n"
    "TITRE: L'EXTRÉMISTE & LE SAGE — " + str(date.today()) + " — " + sujet.upper() + " — " + top + " — BULLES PUNCHÉES 100% CHIENS — INTERACTION SAGE EXTREMISTE\n"
    "BAS: 3x3 — BIBLE VIVANTE — CHAQUE CHIEN UNIQUE — AUCUN HUMAIN — BULLES COURTES — CASTING LOGIQUE VARIE — " + sujet.upper() + " 2026\n"
    )

    st.code(prompt_final, language="text")
    st.download_button("📥 Télécharger prompt V8 fix", prompt_final, file_name=f"prompt_v8_{sujet}.txt")
    st.success(f"✅ V8 fix généré — {len(bible_filtre)} persos — interaction Sage + Bas-Rouge + casting varié")
