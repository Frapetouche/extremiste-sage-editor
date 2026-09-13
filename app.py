import streamlit as st
import json, random, datetime
from pathlib import Path

BIBLE_FILE = "bible_personnages_v13_100.json"
HISTOIRE_FILE = "histoires_bd.json"

# ===== STANDARD BAS-ROUGE - MODELE MAITRE POUR LES 100 =====
STANDARD_BAS_ROUGE = {
    "id": 2,
    "nom": "BAS-ROUGE",
    "race": "Beauceron Noir & Feu 120lbs",
    "prompt_maitre": "Beauceron Noir & Feu 120lbs casque viking ailes blanches argent torche enflammee foulard rouge collier clous argent gros nez yeux exorbitees Uderzo 4 pattes jamais humain beau graphique reconnaissable drole attachant",
    "traits": "Furieux Loyal Protecteur Extreme",
    "is_standard": True
}

# ===== MATRICE PERSONNALITE -> RACE - BEAU GRAPHIQUE =====
MATRICE_RACE = {
    "furieux_extreme": ["Beauceron", "Rottweiler", "Doberman", "Bullmastiff", "Bulldog"],
    "sage_modere": ["Labrador Noir", "Golden Retriever", "Berger Blanc Suisse", "Saint-Bernard"],
    "jeune_idealiste": ["Husky", "Saluki", "Caniche Royal", "Border Collie"],
    "populiste_mairie": ["Cocker", "Beagle", "Corgi", "Bulldog"],
    "bureaucrate_froid": ["Berger Allemand", "Doberman"],
    "media_syndicat_science": ["Fox Terrier", "Bullmastiff", "Border Collie", "Saint-Bernard"]
}

# ===== 18 STABLES VUE FACE - BIBLIOTHEQUE =====
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
    return json.loads(Path(f).read_text(encoding='utf-8')) if Path(f).exists() else default

def save_json(f, data):
    Path(f).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

# ===== PUNCH QUEBECOIS DROLE CRITIQUE 8 MOTS MAX =====
def corrige_punch_quebecois(bulle):
    bulle = bulle.upper().strip()
    bulle = bulle.replace("TABARNAC","").replace("GRRRR","").strip()
    mots = bulle.replace("!"," ").replace("."," ").split()
    if len(mots) > 8:
        mots = mots[:8]
    result = " ".join(mots)
    return result + "!" if not result.endswith("!") else result

# ===== DETECTION PERSONNALITE -> RACE =====
def get_race_par_personnalite(personnalite_detectee):
    for cle, races in MATRICE_RACE.items():
        if any(m in personnalite_detectee.lower() for m in cle.split("_")):
            return random.choice(races)
    return random.choice(["Berger Allemand","Labrador Noir","Border Collie"])

def detecte_personnalite(nom, sujet):
    sujet_low = (sujet + " " + nom).lower()
    if any(x in sujet_low for x in ["furieux","rage","extreme","trump","duhaime","polievre"]):
        return "furieux_extreme"
    if any(x in sujet_low for x in ["sage","banquier","carney","legault","milliard"]):
        return "sage_modere"
    if any(x in sujet_low for x in ["jeune","pq","qs","pspp","ghazal","idealiste"]):
        return "jeune_idealiste"
    if any(x in sujet_low for x in ["maire","plante","marchand","populiste","ford"]):
        return "populiste_mairie"
    if any(x in sujet_low for x in ["bureaucrate","education","police","garde"]):
        return "bureaucrate_froid"
    return "media_syndicat_science"

# ===== MODE CREATION AUTOMATIQUE BASE SUR BAS-ROUGE =====
def get_ou_cree_personnage(nom_public, sujet, bible):
    # Cherche dans bible
    for p in bible:
        if nom_public.lower() in p["nom"].lower():
            p["utilisations"] = p.get("utilisations",0)+1
            return p

    # Si pas trouve et mode creation ON -> cree avec race selon personnalite
    if st.session_state.get("mode_creation", False):
        personnalite = detecte_personnalite(nom_public, sujet)
        race = get_race_par_personnalite(personnalite)
        trait = f"trait {nom_public} {personnalite}"

        nouveau = {
            "id": len(bible)+1,
            "nom": nom_public.upper(),
            "race": race,
            "personnalite": personnalite,
            "prompt": f"{race} {trait} gros nez yeux exorbitees Uderzo 4 pattes jamais humain beau graphique reconnaissable drole attachant style Bas-Rouge",
            "role": f"Auto {personnalite}",
            "creation_auto": str(datetime.date.today()),
            "sujet_creation": sujet,
            "stable": True,
            "utilisations": 1,
            "cree_depuis_standard": "BAS-ROUGE"
        }
        bible.append(nouveau)
        save_json(BIBLE_FILE, bible)
        st.toast(f"Nouveau: {nom_public} -> {race} ({personnalite}) cree et garde en reserve")
        return nouveau

    return bible[0] # Le Sage par defaut

def agent_chercheur(sujet):
    faits = [f"{sujet} Quebec actualite", "62 fermes ouvertes UPA", "130M$ referendum + 27.6G$ riposte"]
    ironie = f"On ouvre 62 fermes gratis mais on charge 130M$ pour voter sur {sujet}"
    return {"sujet": sujet, "faits": faits, "ironie": ironie}

def agent_bulles_humour_quebecois(sujet, analyse):
    # Ici branche ton LLM pour vrai humour quebecois drole critique
    # Template temporaire - remplace par appel OpenAI/Mistral
    return {
        "1": f"{sujet.upper()}! CHER VOTE!",
        "2": "FERMES OUVERTES! POSTES FERMEES! LOGIQUE?",
        "3": "62 VACHES GRATIS! VOTE 130M$! BRAVO!",
        "4": "VOLEURS! VOUS VENDEZ MEME L'AIR!",
        "5": "SURVEILLE VACHES! PAS LES CROSSEURS!",
        "6": "GAZ 135c! VACHE GRATIS!",
        "7": "PONT PAYE! VOTE PAYE! RESTE QUOI?",
        "8": "2.4 MILLIARDS! COMBIEN VACHES?",
        "9": "ON GAGNE! ON PERD TOUT!"
    }

# ================= UI STREAMLIT V13 =================
st.set_page_config(page_title="Usine V13 - 100 Chiens - Bas-Rouge Standard", layout="wide")
st.title("🐶 L'EXTREMISTE & LE SAGE - V13 - 100 Personnages - Standard Bas-Rouge")

bible = load_json(BIBLE_FILE, BIBLE_18_BASE)
st.session_state.setdefault("derniere_bd", None)

with st.sidebar:
    st.header("⚙️ Mode Creation")
    st.session_state["mode_creation"] = st.checkbox("Mode Creation Auto ON (cree et garde en reserve)", value=True)
    st.info(f"Standard: BAS-ROUGE Beauceron - Matrice race selon personnalite active")
    st.divider()
    st.header("📚 Bibliotheque 18 Stables - Vue Face")
    st.metric("Personnages", len(bible))
    # Affiche 15 par tableau
    for i in range(0, len(bible), 15):
        with st.expander(f"Tableau {i//15+1} - Chiens {i+1} a {min(i+15,len(bible))}"):
            for p in bible[i:i+15]:
                st.write(f"{p['id']}. {p['nom']} - {p['race']} - {p['personnalite']}")

sujet = st.text_input("SUJET NEWS DU JOUR", "ELECTION QUEBEC")
if st.button("🚀 IA cherche + casting personnalite + bulles quebecoises"):
    analyse = agent_chercheur(sujet)

    # Casting avec variation race selon personnalite
    casting = {}
    noms_a_caster = ["LE SAGE","BAS-ROUGE","LEGAULT","DUHAIME","GHAZAL","MILLIARD","PSPP","DRAINVILLE","FORTIN"] # 9 pour BD 9 cases
    for idx, nom in enumerate(noms_a_caster, start=1):
        perso = get_ou_cree_personnage(nom, sujet, bible)
        casting[idx] = perso

    bulles = agent_bulles_humour_quebecois(sujet, analyse)
    cases = {}
    for num in range(1,10):
        perso = casting[num]
        cases[num] = {
            "race": perso["race"],
            "personnalite": perso["personnalite"],
            "bulle": corrige_punch_quebecois(bulles[str(num)]),
            "prompt_visuel": f"{perso['prompt']} - lieu {sujet} - {perso['personnalite']}"
        }

    prompt_global = f"BD QUEBECOISE 9 cases 3x3 UDERZO beau graphique reconnaissable drole attachant 4 pattes jamais humain SUJET {sujet} IRONIE {analyse['ironie']} " + " | ".join([f"CASE{i}:{v['bulle']} {v['race']} {v['personnalite']}" for i,v in cases.items()])

    st.session_state["derniere_bd"] = {"analyse": analyse, "casting": casting, "cases": cases, "prompt": prompt_global}
    save_json(BIBLE_FILE, bible)

if st.session_state["derniere_bd"]:
    data = st.session_state["derniere_bd"]
    st.info(f"Ironie: {data['analyse']['ironie']}")
    cols = st.columns(3)
    for i in range(1,10):
        c = data["cases"][i]
        with cols[(i-1)%3]:
            st.markdown(f"**CASE {i} - {c['race']} ({c['personnalite']})**")
            st.code(c["bulle"])
    st.code(data["prompt"])
    if st.button("✅ Approuve et Publie - Garde en reserve"):
        histoires = load_json(HISTOIRE_FILE, [])
        histoires.append({"date": str(datetime.datetime.now()), "sujet": sujet, "data": data})
        save_json(HISTOIRE_FILE, histoires)
        st.balloons()
        st.success(f"Publie! Bibliotheque: {len(bible)} personnages stables - Standard Bas-Rouge respecte - Races varient selon personnalite")
