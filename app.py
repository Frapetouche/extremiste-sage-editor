import streamlit as st
import json, random, datetime, re, urllib.parse
from pathlib import Path

BIBLE_FILE = "bible_personnages_v13_100.json"
HISTOIRE_FILE = "histoires_bd.json"

STANDARD_BAS_ROUGE = {
    "id": 2, "nom": "BAS-ROUGE", "race": "Beauceron Noir & Feu 120lbs",
    "prompt_maitre": "Beauceron Noir & Feu 120lbs casque viking ailes blanches argent torche enflammee foulard rouge collier clous argent yeux rouges furieux gros nez yeux exorbitees Uderzo 4 pattes jamais humain beau graphique reconnaissable drole attachant ultra detaille 4K"
}

MATRICE_RACE = {
    "furieux_extreme": ["Beauceron", "Rottweiler", "Doberman"],
    "sage_modere": ["Labrador Noir", "Golden Retriever", "Berger Blanc Suisse"],
    "jeune_idealiste": ["Husky", "Saluki", "Border Collie"],
    "populiste_mairie": ["Cocker", "Beagle", "Corgi"],
    "bureaucrate_froid": ["Berger Allemand", "Doberman"],
    "media_syndicat_science": ["Fox Terrier", "Bullmastiff", "Saint-Bernard"]
}

BIBLE_18_BASE = [
    {"id":1,"nom":"LE SAGE","race":"Labrador Noir","personnalite":"sage modere","prompt":"Labrador noir couronne laurier or 5 pointes lunettes jaunes rondes cape bleu roi gros nez yeux exorbitees Uderzo 4 pattes jamais humain sage ultra detaille beau graphique","role":"Narrateur sage","stable":True},
    {"id":2,"nom":"BAS-ROUGE","race":"Beauceron Noir & Feu","personnalite":"furieux extreme","prompt":"Beauceron 120lbs casque viking ailes blanches argent torche enflammee foulard rouge collier clous argent yeux rouges furieux gros nez Uderzo 4 pattes jamais humain ultra detaille beau graphique","role":"Rage du peuple","stable":True,"is_standard":True},
    {"id":3,"nom":"LEGAULT","race":"Berger Blanc Suisse","personnalite":"sage fatigue","prompt":"Berger Blanc Suisse tuque CAQ bleu lunettes carrees gros nez Uderzo 4 pattes jamais humain","role":"PM Quebec","stable":True},
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

# ===== FIX BULLLES - RESUME COURT =====
def resume_sujet_court(sujet_long):
    sujet = sujet_long.lower()
    sujet = sujet.replace("- tva nouvelles","").replace("- radio-canada","").replace("seulement","").replace("depuis janvier","").replace("-"," ").strip()
    mots = sujet.split()
    stop = ["au","du","des","le","la","les","un","une","de","en","et","a","au","que","qui"]
    cles = [m for m in mots if m not in stop and len(m)>2][:3]
    court = " ".join(cles).upper()
    chiffres = re.findall(r'\d+', sujet_long)
    if chiffres:
        court = f"{chiffres[0]} {court[:15]}"
    return court[:20].strip()

def corrige_punch(bulle):
    bulle = bulle.upper().strip().replace("TABARNAC","").replace("GRRRR","").strip()
    mots = bulle.replace("!"," ").replace("."," ").split()
    if len(mots) > 8:
        mots = mots[:8]
    return " ".join(mots) + "!"

def get_race(perso):
    for k,v in MATRICE_RACE.items():
        if k in perso.lower(): return random.choice(v)
    return "Labrador Noir"

def detecte_perso(nom,sujet):
    s=(sujet+" "+nom).lower()
    if any(x in s for x in ["furieux","trump","duhaime","rage","electrique","chinois"]): return "furieux_extreme"
    if any(x in s for x in ["carney","legault","sage","banquier"]): return "sage_modere"
    if any(x in s for x in ["espace","hansen","jeune","pq","qs"]): return "jeune_idealiste"
    if any(x in s for x in ["maire","ford"]): return "populiste_mairie"
    if any(x in s for x in ["education","police"]): return "bureaucrate_froid"
    return "media_syndicat_science"

def get_ou_cree(nom,sujet,bible):
    for p in bible:
        if nom.lower() in p["nom"].lower(): return p
    if st.session_state.get("mode_creation"):
        perso=detecte_perso(nom,sujet)
        race=get_race(perso)
        nouveau={"id":len(bible)+1,"nom":nom.upper(),"race":race,"personnalite":perso,"prompt":f"{race} {nom} {perso} gros nez yeux exorbitees Uderzo 4 pattes jamais humain beau graphique ultra detaille 4K","role":f"Auto {perso}","stable":True}
        bible.append(nouveau); save_json(BIBLE_FILE,bible); return nouveau
    return bible[0]

def recherche_5_sujets(query="Quebec actualite"):
    try:
        import requests
        q=urllib.parse.quote(query)
        url=f"https://news.google.com/rss/search?q={q}&hl=fr&gl=CA&ceid=CA:fr"
        r=requests.get(url,headers={"User-Agent":"Mozilla/5.0"},timeout=10)
        titles=re.findall(r'<title>(.*?)</title>',r.text)[1:9]
        clean=[re.sub(r'<[^>]+>','',t).strip() for t in titles if len(t)>15]
        return clean[:5]
    except: return ["CARNEY ESPACE HANSEN","TRUMP TARIFS 50%","ELECTION QUEBEC","TRAMWAY QUEBEC","POSTES CANADA"]

def analyse_1_sujet(sujet_long):
    sujet_court=resume_sujet_court(sujet_long)
    faits=[]
    try:
        import requests
        q=urllib.parse.quote(f"{sujet_long} Quebec")
        r=requests.get(f"https://html.duckduckgo.com/html/?q={q}",headers={"User-Agent":"Mozilla/5.0"},timeout=12)
        snips=re.findall(r'<a class="result__snippet"[^>]*>(.*?)</a>',r.text,re.DOTALL)[:3]
        faits=[re.sub(r'<[^>]+>','',s).strip()[:120] for s in snips if len(s)>20]
    except: pass
    if not faits: faits=[f"{sujet_court} - Quebec actualite"]
    if "electrique" in sujet_long.lower() or "chinois" in sujet_long.lower():
        ironie=f"{sujet_court} - TAXE 100% mais entre pareil! {faits[0][:50]} - 62 fermes gratis!"
    elif "tarif" in sujet_long.lower():
        ironie=f"{sujet_court} - 50% tarifs 276G$ riposte - {faits[0][:50]}"
    else:
        ironie=f"{sujet_court} - {faits[0][:60]} - fermes gratis vote 130M$!"
    return {"sujet_long":sujet_long,"sujet_court":sujet_court,"faits":faits,"ironie":ironie,"date":str(datetime.datetime.now())}

def bulles_progression(sujet_long,analyse):
    sc=analyse["sujet_court"]
    if "electrique" in sujet_long.lower() or "chinois" in sujet_long.lower() or "vehicule" in sujet_long.lower():
        return {"1":f"{sc} CHOC!","2":f"{sc} TAXE 100%!","3":f"{sc} ENTRE QUAND MEME!","4":f"VOLEURS VENDEZ AIR!","5":f"QUEBEC RESTE QUEBEC!","6":f"GAZ 135C VE GRATIS?","7":f"PONT PAYE AUTO PAYEE!","8":f"2.4 MILLIARDS COMBIEN VE?","9":f"ON GAGNE ON PERD TOUT!"}
    return {"1":f"{sc} CHOC!","2":f"{sc} ACTION FORTE!","3":f"{sc} COURAGE RIPOSTE!","4":f"{sc} GRRR FOU!","5":f"QUEBEC RESTE {sc}!","6":f"{sc} ASSEZ FOLIE!","7":f"{sc} PLAN JUSTICE!","8":f"{sc} NON FOU!","9":f"{sc} VICTOIRE LIBERTE!"}

# ===== UI V32.1 =====
st.set_page_config(page_title="V32.1 QUALITE ORIGINALE FIX",layout="wide")
st.title("🐶 V32.1 FIX - 1 SUJET SEUL - QUALITE ORIGINALE")

if "bible" not in st.session_state: st.session_state.bible=load_json(BIBLE_FILE,BIBLE_18_BASE)
if "derniere_bd" not in st.session_state: st.session_state.derniere_bd=None
if "5_sujets" not in st.session_state: st.session_state["5_sujets"]=[]
if "mode_creation" not in st.session_state: st.session_state.mode_creation=True

with st.sidebar:
    st.session_state.mode_creation=st.checkbox("Mode Creation ON",value=True)
    st.metric("Bibliotheque",len(st.session_state.bible))
    for i in range(0,len(st.session_state.bible),15):
        with st.expander(f"Tableau {i//15+1}"):
            for p in st.session_state.bible[i:i+15]: st.write(f"{p['id']}. {p['nom']} | {p['race']}")

q_global=st.text_input("Sujet global","Quebec actualite")
if st.button("🔍 CHERCHER 5 SUJETS",use_container_width=True):
    st.session_state["5_sujets"]=recherche_5_sujets(q_global)

if st.session_state["5_sujets"]:
    st.subheader("Choisis 1 SUJET SEUL - chaque choix = nouvelle BD")
    choix=st.radio("5 sujets trouves:",st.session_state["5_sujets"],index=0)
    if st.button(f"🚀 CREER NOUVELLE BD: {choix}",type="primary",use_container_width=True):
        with st.spinner(f"Analyse {choix}..."):
            analyse=analyse_1_sujet(choix)
            casting={}; noms=["LE SAGE","BAS-ROUGE","LEGAULT","DUHAIME","GHAZAL","MILLIARD","PSPP","DRAINVILLE","FORTIN"]
            for idx,nom in enumerate(noms,1): casting[idx]=get_ou_cree(nom,choix,st.session_state.bible)
            bulles=bulles_progression(choix,analyse)
            cases={}
            for n in range(1,10):
                p=casting[n]
                cases[n]={"nom":p["nom"],"race":p["race"],"personnalite":p["personnalite"],"bulle":corrige_punch(bulles[str(n)]),"prompt":f"{p['prompt']} - {analyse['sujet_court']}"}
            prompt_master = f"Le Sage & L'Extremiste - EPISODE - NEWS DU JOUR {analyse['sujet_court']} - 1 SUJET SEUL - V28 V29 V30 master definitif - 100% DOGS - SUJET UNIQUE: {analyse['sujet_court']} - MASTER ORIGINAUX LOCKES - ULTRA BEAU GRAPHIQUE 4K - 100% CHIENS 4 PATTES JAMAIS HUMAIN - STYLE UDERZO ASTERIX FRANCO-BELGE ULTRA DETAILLE - IRONIE {analyse['ironie']} - " + " | ".join([f"CAS {i}: {c['nom']} {c['race']} bulle '{c['bulle']}'" for i,c in cases.items()])
            st.session_state.derniere_bd={"analyse":analyse,"cases":cases,"prompt":prompt_master}
            save_json(BIBLE_FILE,st.session_state.bible)

if st.session_state.derniere_bd:
    d=st.session_state.derniere_bd
    st.divider()
    st.subheader(f"BD NEUVE: {d['analyse']['sujet_court']} - {d['analyse']['sujet_long'][:60]}")
    st.info(d['analyse']['ironie'])
    c1,c2,c3=st.columns(3)
    for i in range(1,10):
        col=[c1,c2,c3][(i-1)%3]
        c=d['cases'][i]
        with col: st.markdown(f"**CASE {i} {c['nom']}**"); st.code(c['bulle'])
    st.text_area("PROMPT FINAL V32.1 - QUALITE ORIGINALE",d['prompt'],height=280)
    try:
        import openai
        if st.button("🎨 GENERER IMAGE HD 1792x1024"):
            client=openai.OpenAI()
            with st.spinner("Generation 4K comme tes photos originales..."):
                resp=client.images.generate(model="dall-e-3",prompt=d['prompt'],size="1792x1024",quality="hd",n=1)
                st.image(resp.data[0].url,caption=f"V32.1 - {d['analyse']['sujet_court']}")
    except: st.code(d['prompt'])
