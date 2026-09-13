import streamlit as st
import json, os, datetime
from pathlib import Path

# --- CONFIG MÉMOIRE NON CONTAMINABLE ---
BIBLE_FILE = "bible_personnages_v9_2_1.json"
CORRECTIONS_FILE = "corrections_sens.json"
HISTOIRE_FILE = "histoires_bd.json"

# Bible de base verrouillée
BIBLE_BASE = {
  "Le Sage": {"race": "Labrador noir", "prompt": "Labrador noir couronne or 5 pointes cape beige clair sage yeux doux exorbités gros nez Uderzo 4 pattes jamais humain", "case_fixe": 1},
  "Bas-Rouge": {"race": "Beauceron noir et feu", "prompt": "Beauceron noir et feu 120lbs casque aile viking argent torche flamme foulard rouge yeux rouges furieux collier clous Uderzo 4 pattes jamais humain", "case_fixe": 4},
}

RACES_DISPO = ["Caniche Beige tuque", "Border Collie noir blanc", "Berger Allemand", "Rottweiler", "Labrador Brun", "Pitbull gris", "Bouledogue Francais", "Malamute Alaska", "St-Bernard", "Terrier Ecossais", "Caniche Royal", "Beagle", "Corgi", "Husky", "Labrador Chocolat"]

def load_json(file, default):
    if os.path.exists(file):
        return json.loads(Path(file).read_text(encoding='utf-8'))
    return default

def save_json(file, data):
    Path(file).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

# --- AGENT 1: CHERCHEUR WEB (à brancher sur ton API Tavily / DuckDuckGo) ---
def agent_chercheur_web(sujet):
    # ICI tu branches ta recherche internet
    # Exemple: from tavily import TavilyClient; client.search(sujet)
    # Pour l'instant je simule avec les news du jour qu'on a trouvées
    return {
        "sujet": sujet,
        "faits": [
            f"SUJET {sujet} ACTION FORTE - lieu réel",
            "FAIT 1 EXTRAIT IA: 62 fermes ouvertes UPA 10h-16h 22e édition + Postes Canada fin porte Sept-Îles",
            "FAIT 2 IRONIE: 130M$ référendum + 27.6G$ riposte Carney vs Trump 50% - Québec perd 60G$ PIB 100k jobs"
        ],
        "ironie": "Le Québec ouvre ses fermes gratuitement pendant qu'on lui ferme la porte du courrier et qu'on lui facture 130M$ pour voter",
        "punchlines": [f"{sujet} TABARNAC", "RAGE ESPOIR QUOI", "27.6G$! TABARNAC!"]
    }

# --- AGENT 2: CASTING MANAGER AVEC MÉMOIRE ---
def agent_casting(sujet, faits, bible):
    # Garde Le Sage et Bas-Rouge
    casting = {}
    casting[1] = bible["Le Sage"]
    casting[4] = bible["Bas-Rouge"]

    # Choisis 7 races variées anti-doublon selon sujet
    # Ici logique simple: si sujet = ELECTION -> politiciens, si sujet = FERMES -> animaux ferme
    dispo = [r for r in RACES_DISPO if r not in [bible["Le Sage"]["race"], bible["Bas-Rouge"]["race"]]]
    import random; random.shuffle(dispo)
    cases_restantes = [2,3,5,6,7,8,9]
    for i, case_num in enumerate(cases_restantes):
        race = dispo[i]
        # Si race jamais vue, on la crée et on la garde en mémoire pour la prochaine fois
        if race not in bible:
            bible[race] = {"race": race, "prompt": f"{race} Uderzo gros nez yeux exorbitees 4 pattes jamais humain", "creation": sujet, "date": str(datetime.date.today())}
        casting[case_num] = bible[race]
    save_json(BIBLE_FILE, bible)
    return casting

# --- AGENT 3: STORYTELLER 3 ACTES (améliore sens et punch) ---
def agent_storyteller(sujet, analyse, casting):
    # Structure qui change selon l'ironie, pas fixe
    actes = {
        "Acte 1 CHOC": [1,2,3],
        "Acte 2 CONFRONTATION": [4,5,6],
        "Acte 3 PUNCH": [7,8,9]
    }
    cases = {}
    # Exemple de sens dynamique
    cases[1] = {"role": "LE CHOC INNOCENT", "sens": f"Le Sage découvre {analyse['faits'][0]} et est choqué", "bulle": f"{sujet}! TABARNAC! CHOC!"}
    cases[2] = {"role": "L'ANNONCE ABSURDE", "sens": "Le porte-parole annonce la nouvelle officielle avec un sourire", "bulle": "CAMPAGNE! DÉBAT! ACTION FORTE!"}
    cases[3] = {"role": "LA COMPARAISON QUI TUE", "sens": analyse['ironie'], "bulle": "ÉCART! COMPARE! CURIOSITÉ!"}
    cases[4] = {"role": "LA RAGE DU PEUPLE", "sens": "Bas-Rouge explose contre les voleurs", "bulle": "VOLEURS! GRRR! FOU!"}
    cases[5] = {"role": "LE CONTRÔLE IRONIQUE", "sens": "Surveillance du système qui se contredit", "bulle": "SURVEILLANCE! CONTRÔLE! QUÉBEC!"}
    cases[6] = {"role": "QUI PAYE", "sens": "Qui profite de l'économie", "bulle": "SUPER GAZ! ÉCONOMIE!"}
    cases[7] = {"role": "LA FACTURE", "sens": "Le citoyen triste reçoit la taxe", "bulle": "TAXE! OUCH! GROGNON!"}
    cases[8] = {"role": "LE CHIFFRE MONSTRE", "sens": f"Brandit {analyse['punchlines'][0]}", "bulle": "2,4 MILLIARDS! TABARNAC!"}
    cases[9] = {"role": "VICTOIRE AMÈRE", "sens": "Finale multi races drapeaux", "bulle": "QUÉBEC! VICTOIRE! LIBERTÉ!"}
    return cases

# --- STREAMLIT UI ---
st.set_page_config(page_title="L'EXTREMISTE & LE SAGE - Usine V43", layout="wide")
st.title("🐶 L'EXTREMISTE & LE SAGE - V43 Multi-Agents avec Mémoire")

bible = load_json(BIBLE_FILE, BIBLE_BASE)
corrections = load_json(CORRECTIONS_FILE, {})

with st.sidebar:
    st.header("📚 Bible Personnages")
    st.json(bible)
    st.header("📝 Corrections (non contaminantes)")
    st.json(corrections)

sujet = st.text_input("SUJET NEWS DU JOURS", "ELECTION QUÉBEC")
if st.button("🚀 Lancer pipeline Analyse → Casting → BD"):
    with st.spinner("Agent Chercheur fouille internet..."):
        analyse = agent_chercheur_web(sujet)
        st.success(f"Faits trouvés: {analyse['faits']}")
        st.info(f"Ironie détectée: {analyse['ironie']}")

    with st.spinner("Agent Casting choisit personnages..."):
        casting = agent_casting(sujet, analyse['faits'], bible)
        st.write(casting)

    with st.spinner("Agent Storyteller écrit l'histoire..."):
        cases = agent_storyteller(sujet, analyse, casting)
        st.write(cases)

    # Génération image - tu branches ton générateur ici (DALL-E, SDXL, ou ton API image_gen)
    prompt_bd = f"BD QUEBECOISE 9 cases 3x3 STYLE UDERZO gros nez yeux exorbitees 4 pattes jamais humain SUJET {sujet} - {analyse['ironie']} CASTING {casting}"
    st.code(prompt_bd, language="text")
    st.warning("Branche ici ton generateur d'image avec ce prompt")

    # Sauvegarde histoire pour approbation
    histoire = {"date": str(datetime.datetime.now()), "sujet": sujet, "analyse": analyse, "casting": casting, "cases": cases, "prompt": prompt_bd}
    histoires = load_json(HISTOIRE_FILE, [])
    histoires.append(histoire)
    save_json(HISTOIRE_FILE, histoires)
    st.success("BD prête pour approbation!")

st.divider()
st.header("✏️ Corriger le sens sans contaminer le modèle")
case_a_corriger = st.selectbox("Case à corriger", list(range(1,10)))
nouveau_sens = st.text_area("Nouveau sens / Punch amélioré (8 mots max BOLD)")
if st.button("Sauvegarder correction"):
    corrections[f"case_{case_a_corriger}_{datetime.datetime.now().isoformat()}"] = nouveau_sens
    save_json(CORRECTIONS_FILE, corrections)
    st.success("Correction sauvée dans corrections.json - bible non contaminée!")

if st.button("✅ Approuver cette caricature et publier"):
    st.balloons()
    st.success("Caricature approuvée! Elle garde son humour pour le petit peuple.")
        
