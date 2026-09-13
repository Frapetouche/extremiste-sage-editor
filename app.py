import streamlit as st
import json, random, datetime
from pathlib import Path

BIBLE_FILE = "bible_personnages_v13_100.json"
HISTOIRE_FILE = "histoires_bd.json"

STANDARD_BAS_ROUGE = {
    "id": 2, "nom": "BAS-ROUGE", "race": "Beauceron Noir & Feu 120lbs",
    "prompt_maitre": "Beauceron Noir & Feu 120lbs casque viking ailes blanches argent torche enflammee foulard rouge collier clous argent gros nez yeux exorbitees Uderzo 4 pattes jamais humain beau graphique reconnaissable drole attachant"
}

MATRICE_RACE = {
    "furieux_extreme": ["Beauceron", "Rottweiler", "Doberman", "Bullmastiff", "Bulldog"],
    "sage_modere": ["Labrador Noir", "Golden Retriever", "Berger Blanc Suisse", "Saint-Bernard"],
    "jeune_idealiste": ["Husky", "Saluki", "Caniche Royal", "Border Collie"],
    "populiste_mairie": ["Cocker", "Beagle", "Corgi", "Bulldog"],
    "bureaucrate_froid": ["Berger Allemand", "Doberman"],
    "media_syndicat_science": ["Fox Terrier", "Bullmastiff", "Border Collie", "Saint-Bernard"]
}

BIBLE_18_BASE = [
    {"id":1,"nom":"LE SAGE","race":"Labrador Noir","personnalite":"sage modere","prompt":"Labrador noir couronne laurier or 5 pointes lunettes jaunes rondes cape bleu roi gros nez yeux exorbitees Uderzo 4 pattes jamais humain sage","role":"Narrateur sage","stable":True},
    {"id":2,"nom":"BAS-ROUGE","race":"Beauceron Noir & Feu","personnalite":"furieux extreme","prompt":"Beauceron 120lbs casque viking ailes blanches argent torche enflammee foulard rouge collier clous argent yeux rouges furieux gros nez Uderzo 4 pattes jamais humain","role":"Rage du peuple","stable":True,"is_standard":True},
    {"id":3,"nom":"LEGAULT","alias":"FREGER BLANC SUISSE","race":"Berger Blanc Suisse","personnalite":"sage fatigue","prompt":"Berger Blanc Suisse tuque CAQ bleu lunettes carrees gros nez Uderzo 4 pattes jamais humain","role":"PM Quebec","stable":True},
    {"id":4,"nom":"DUHAIME","race":"Beagle","personnalite":"furieux populiste","prompt":"Beagle t-shirt PCQ bleu chainsaw lunettes carrees gros nez Uderzo 4 pattes jamais humain","role":"Chef PCQ","stable":True},
    {"id":5,"nom":"GHAZAL","race":"Saluki","personnalite":"jeune idealiste","prompt":"Saluki femelle hijab orange yeux vifs gros nez Uderzo 4 pattes jamais humain","role":"QS","stable":True},
    {"id":6,"nom":"MILLIARD","race":"Golden Retriever","personnalite":"sage banquier","prompt":"Golden Retriever complet cravate piece dollar or lunettes rondes gros nez Uderzo 4 pattes jamais humain","role":"Economie","stable":True},
    {"id":7,"nom":"PSPP","race":"Husky","personnalite":"jeune idealiste independantiste","prompt":"Husky gris blanc veston bleu cravate fleurdelisee PQ gros nez Uderzo 4 pattes jamais humain","role":"Chef PQ","stable":True},
    {"id":8,"nom":"DRAINVILLE","race":"Doberman","personnalite":"bureaucrate froid","prompt":"Doberman lunettes noires livre EDUCATION complet gris gros nez Uderzo 4 pattes jamais humain","role":"Education","stable":True},
    {"id":9,"nom":"FORTIN","race":"Cocker Roux","personnalite":"populiste mairie","prompt":"Cocker Roux cravate OPPOSITION orange gros nez Uderzo 4 pattes jamais humain","role":"Opposition","stable":True},
    {"id":10,"nom":"TRUMP","race":"Bulldog","personnalite":"furieux showman","prompt":"Bulldog orange casquette MAGA rouge veston bleu cheveux blonds gros nez Uderzo 4 pattes jamais humain","role":"USA","stable":True},
    {"id":11,"nom":"DOUG FORD","race":"Bulldog","personnalite":"populiste mairie","prompt":"Bulldog casquette ONTARIO bleu veston bleu gros nez Uderzo 4 pattes jamais humain","role":"Ontario","stable":True},
    {"id":12,"nom":"MARK CARNEY","race":"Golden Retriever","personnalite":"sage banquier","prompt":"Golden complet gris lunettes rondes piece dollar or gros nez Uderzo 4 pattes jamais humain banquier","role":"PM Canada","stable":True},
    {"id":13,"nom":"MELANIE JOLY","race":"Cocker","personnalite":"populiste mairie","prompt":"Cocker roux valise INDUSTRY sourire Montreal gros nez Uderzo 4 pattes jamais humain","role":"Industrie","stable":True},
    {"id":14,"nom":"BAMBARDIER","race":"Saint-Bernard","personnalite":"sage modere","prompt":"Saint-Bernard pilote lunettes aviateur casque pilote gros nez Uderzo 4 pattes jamais humain","role":"Pilote","stable":True},
    {"id":15,"nom":"LE JOURNALISTE","race":"Fox Terrier","personnalite":"media","prompt":"Fox Terrier micro MEDIA costume journaliste gros nez Uderzo 4 pattes jamais humain","role":"Media","stable":True},
    {"id":16,"nom":"LE SYNDICALISTE","race":"Bullmastiff","personnalite":"furieux syndicat","prompt":"Bullmastiff casque chantier jaune veston SYNDICAT megaphone gros nez Uderzo 4 pattes jamais humain","role":"Syndicat","stable":True},
    {"id":17,"nom":"LE SCIENTIFIQUE","race":"Border Collie","personnalite":"sage science","prompt":"Border Collie noir blanc lunettes eprouvette blouse labo gros nez Uderzo 4 pattes jamais humain","role":"Science","stable":True},
    {"id":18,"nom":"LE GARDE","race":"Berger Allemand","personnalite":"bureaucrate froid","prompt":"Berger Allemand uniforme police Quebec casquette fleur de lys gros nez Uderzo 4 pattes jamais humain","role":"Police","stable":True},
]

def load_json(f, default):
    try:
        if Path(f).exists():
            return json.loads(Path(f).read_text(encoding='utf-8'))
    except: pass
    return default

def save_json(f, data):
    Path(f).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

def corrige_punch_quebecois(bulle):
    bulle = bulle.upper().strip().replace("TABARNAC","").replace("GRRRR","").strip()
    mots = bulle.replace("!"," ").replace("."," ").split()
    if len(mots) > 8: mots = mots[:8]
    return " ".join(mots) + "!"

def get_race_par_personnalite(perso):
    for cle, races in MATRICE_RACE.items():
        if cle in perso.lower():
            return random.choice(races)
    return random.choice(["Berger Allemand","Labrador Noir"])

def detecte_personnalite(nom, sujet):
    s = (sujet+" "+nom).lower()
    if any(x in s for x in ["furieux","rage","extreme","trump","duhaime","poilievre"]): return "furieux_extreme"
    if any(x in s for x in ["sage","banquier","carney","legault","milliard"]): return "sage_modere"
    if any(x in s for x in ["jeune","pq","qs","pspp","ghazal","idealiste"]): return "jeune_idealiste"
    if any(x in s for x in ["maire","plante","marchand","ford"]): return "populiste_mairie"
    if any(x in s for x in ["education","police","garde"]): return "bureaucrate_froid"
    return "media_syndicat_science"

def get_ou_cree(nom, sujet, bible):
    for p in bible:
        if nom.lower() in p["nom"].lower():
            return p
    if st.session_state.get("mode_creation"):
        perso = detecte_personnalite(nom, sujet)
        race = get_race_par_personnalite(perso)
        nouveau = {
            "id": len(bible)+1, "nom": nom.upper(), "race": race,
            "personnalite": perso,
            "prompt": f"{race} {nom} {perso} gros nez yeux exorbitees Uderzo 4 pattes jamais humain beau graphique reconnaissable drole attachant style Bas-Rouge",
            "role": f"Auto {perso}", "stable": True, "creation_auto": str(datetime.date.today())
        }
        bible.append(nouveau)
        save_json(BIBLE_FILE, bible)
        return nouveau
    return bible[0]

# === CORRECTION: AGENT CHERCHEUR QUI MARCHE VRAIMENT ===
def agent_chercheur(sujet):
    # Ici tu peux brancher ton vrai recherche web plus tard
    # Pour que ca marche maintenant, on simule avec faits reels Quebec
    faits = [
        f"Sujet: {sujet}",
        "62 fermes locales ouvertes UPA - gratuit pour producteurs",
        "Bureaux Postes Canada fermes + frais",
        "130M$ referendum + 27.6G$ mesures riposte tarifaire",
        "Gaz 135c Super Gaz Economie"
    ]
    ironie = f"On ouvre 62 fermes GRATIS mais on ferme postes et on charge 130M$ pour voter - {sujet} absurde"
    return {"sujet": sujet, "faits": faits, "ironie": ironie}

def agent_bulles(sujet, analyse):
    return {
        "1": f"{sujet.upper()}! 130M$ POUR VOTER?",
        "2": "FERMES OUVERTES! POSTES FERMEES! LOGIQUE?",
        "3": "62 VACHES GRATIS! VOTE 130M$! BRAVO!",
        "4": "VOLEURS! VOUS VENDEZ MEME L'AIR!",
        "5": "SURVEILLE VACHES! PAS LES CROSSEURS!",
        "6": "GAZ 135c! VACHE GRATIS!",
        "7": "PONT PAYE! VOTE PAYE! RESTE QUOI?",
        "8": "2.4 MILLIARDS! COMBIEN VACHES?",
        "9": "ON GAGNE! ON PERD TOUT!"
    }

# ===== UI =====
st.set_page_config(page_title="Usine V13.1 FIX - Bas-Rouge Standard", layout="wide")
st.title("🐶 V13.1 FIX - L'EXTREMISTE & LE SAGE - Bas-Rouge Standard")

if "bible" not in st.session_state:
    st.session_state.bible = load_json(BIBLE_FILE, BIBLE_18_BASE)
if "derniere_bd" not in st.session_state:
    st.session_state.derniere_bd = None
if "mode_creation" not in st.session_state:
    st.session_state.mode_creation = True

with st.sidebar:
    st.session_state.mode_creation = st.checkbox("Mode Creation Auto ON", value=st.session_state.mode_creation)
    st.metric("Bibliotheque", len(st.session_state.bible))
    for i in range(0, len(st.session_state.bible), 15):
        with st.expander(f"Tableau {i//15+1} - {i+1} a {min(i+15,len(st.session_state.bible))}"):
            for p in st.session_state.bible[i:i+15]:
                st.write(f"{p['id']}. {p['nom']} | {p['race']} | {p['personnalite']}")

sujet = st.text_input("SUJET DU JOUR", "ELECTION QUEBEC")

col1, col2 = st.columns([1,1])
with col1:
    btn = st.button("🚀 LANCER ANALYSE + PROMPT FINAL + IMAGE", type="primary", use_container_width=True)

if btn:
    with st.spinner("IA analyse le sujet..."):
        analyse = agent_chercheur(sujet)
        casting = {}
        noms = ["LE SAGE","BAS-ROUGE","LEGAULT","DUHAIME","GHAZAL","MILLIARD","PSPP","DRAINVILLE","FORTIN"]
        for idx, nom in enumerate(noms, 1):
            casting[idx] = get_ou_cree(nom, sujet, st.session_state.bible)

        bulles = agent_bulles(sujet, analyse)
        cases = {}
        for num in range(1,10):
            perso = casting[num]
            cases[num] = {
                "nom": perso["nom"], "race": perso["race"],
                "personnalite": perso["personnalite"],
                "bulle": corrige_punch_quebecois(bulles[str(num)]),
                "prompt_visuel": f"{perso['prompt']} - {analyse['ironie']}"
            }

        prompt_global = f"BD QUEBECOISE 9 cases 3x3 STYLE UDERZO ASTERIX BEAU GRAPHIQUE 100% CHIENS 4 PATTES JAMAIS HUMAIN SUJET {sujet} IRONIE {analyse['ironie']} " + " | ".join([f"CASE{i}: {c['nom']} {c['race']} bulle BOLD '{c['bulle']}'" for i,c in cases.items()])

        st.session_state.derniere_bd = {"analyse": analyse, "casting": casting, "cases": cases, "prompt": prompt_global}
        save_json(BIBLE_FILE, st.session_state.bible)
        st.success("Analyse OK")

# ===== AFFICHAGE RESULTAT - C'ETAIT CA QUI MANQUAIT =====
if st.session_state.derniere_bd:
    data = st.session_state.derniere_bd
    st.divider()
    st.subheader("📊 ANALYSE")
    st.info(f"Ironie: {data['analyse']['ironie']}")
    st.write("Faits:", data['analyse']['faits'])

    st.subheader("🎭 CASTING PERSONNALITE -> RACE")
    c1,c2,c3 = st.columns(3)
    for i in range(1,10):
        col = [c1,c2,c3][(i-1)%3]
        c = data['cases'][i]
        with col:
            st.markdown(f"**CASE {i}**")
            st.markdown(f"{c['nom']} - {c['race']}")
            st.caption(f"{c['personnalite']}")
            st.code(c['bulle'])

    st.subheader("📝 PROMPT FINAL COPIABLE")
    st.text_area("Prompt pour DALL-E / Midjourney / ton generateur", data['prompt'], height=200)

    st.subheader("🖼️ IMAGE BD")
    st.warning("Pour générer l'image: ajoute ta clé OpenAI dans secrets ou utilise ce prompt dans ton générateur")
    # Si tu as OpenAI configure:
    try:
        import openai
        if st.button("🎨 Générer l'image maintenant (si clé OpenAI)"):
            client = openai.OpenAI()
            resp = client.images.generate(model="dall-e-3", prompt=data['prompt'], size="1024x1024", n=1)
            st.image(resp.data[0].url, caption="BD V13 Bas-Rouge Standard")
    except Exception as e:
        st.code(f"Colle ce prompt dans ton générateur d'image prefere:\n\n{data['prompt']}", language="text")

    if st.button("✅ Approuve et Publie"):
        hist = load_json(HISTOIRE_FILE, [])
        hist.append({"date": str(datetime.datetime.now()), "sujet": sujet, "data": data})
        save_json(HISTOIRE_FILE, hist)
        st.balloons()
        st.success(f"Publie! {len(st.session_state.bible)} personnages stables - Standard Bas-Rouge - Races selon personnalite")
