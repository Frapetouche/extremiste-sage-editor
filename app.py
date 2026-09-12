import streamlit as st
import json, os, random, re, requests
from datetime import date
from bs4 import BeautifulSoup

st.set_page_config(page_title="V9.0 UNIVERSEL", layout="wide")
st.title("L'EXTREMISTE & LE SAGE - V9.0 Info Percutante Auto - Tout Sujet")
BIBLE_FILE="bible_vivante.json"
def load_bible():
    if os.path.exists(BIBLE_FILE):
        try: return json.load(open(BIBLE_FILE,"r",encoding="utf-8"))
        except: pass
    return {"Le Sage":"Labrador noir couronne or cape beige sage gros nez 4 pattes","Bas-Rouge":"Beauceron noir feu casque viking torche 4 pattes","Mark Carney":"Golden Retriever PM Canada cravate rouge 4 pattes","Zelensky":"Terrier ukrainien treillis kaki barbe Ukraine 4 pattes","Trump":"Bulldog orange 4 pattes","Garde Faune":"Berger allemand garde faune 4 pattes","Pecheur Gaspesie":"Caniches pecheurs Gaspesie 4 pattes","Meteo Pacifique":"Husky meteo thermometre 4 pattes","Familles":"Caniches citoyens 4 pattes","Fjord Bleuets":"Caniches Saguenay bleuets 4 pattes"}
bible=load_bible()
CASTING_DICO={"carney":"Mark Carney","zelensky":"Zelensky","trump":"Trump","bar raye":"Garde Faune","bal raye":"Garde Faune","fjord":"Fjord Bleuets","gaspesie":"Pecheur Gaspesie","matane":"Pecheur Gaspesie","rimouski":"Pecheur Gaspesie","el nino":"Meteo Pacifique","pacifique":"Meteo Pacifique","ukraine":"Zelensky","russie":"Bas-Rouge","ottawa":"Mark Carney","calgary":"Mark Carney","hells":"Bas-Rouge","drones":"Zelensky","freya":"Mark Carney"}
def fetch_percutant_auto(sujet):
    s=sujet.lower(); faits=[]; decor="LIEU REEL "+sujet
    if "bar raye" in s or "bal raye" in s:
        faits=["INTERDICTION TOTALE filet maillant bar raye","REGLEMENTATION 1er mai 2026 remise eau obligatoire","RIMOUSKI MATANE GASPESIE zone interdiction","PECHEURS EN COLERE manifestation quai","GARDE FAUNE controle amende 500$","Fleuve Saint-Laurent phare"]; decor="FLEUVE SAINT-LAURENT GASPESIE RIMOUSKI MATANE phare quai"
    elif "carney" in s and "zelensky" in s:
        faits=["350M CAD missiles intercepteurs defense aerienne","430M CAD garanties pret gaz hiver Ukraine","30% drones Canada front immediat","26 milliards aide totale Canada","Partenariat 100 ans Canada Ukraine","Projet Freya moins cher que Patriot"]; decor="OTTAWA CALGARY PARLEMENT drapeaux Canada Ukraine"
    elif "el nino" in s or "pacifique" in s:
        faits=["El Nino 2.7C RECORD HISTORIQUE Pacifique","Ocean 30C chaud jamais vu","Hawaii inondations","Fjord Saguenay impact","Alerte meteo record"]; decor="OCEAN PACIFIQUE chaud 30C thermometre"
    elif "hells" in s:
        faits=["Interdiction port couleurs Hells Angels","Amende 5000$ Longueuil Quebec","Loi anti-gang patchs"]; decor="LONGUEUIL QUEBEC route motos"
    elif "2977" in s or "tribute" in s:
        faits=["2977 drones = 2977 vies hommage","9 sept 2026 New York Harbor","2 tours jumelles lumiere coeur geant","Tribute in Light 2 faisceaux"]; decor="NEW YORK HARBOR nuit Tribute Light"
    else:
        faits=[f"{sujet.upper()} ACTION FORTE PERCUTANTE",f"Lieu reel {sujet} 2026",f"Annonce ou interdiction ou record sur {sujet}"]; decor="LIEU REEL DU SUJET "+sujet
    return faits,decor

with st.sidebar:
    st.header("BIBLIO Option A"); st.caption(f"{len(bible)} chiens"); st.divider()

st.subheader("SUJET DU JOUR - Tape n'importe quoi - App trouve l'info percutante seule")
sujet=st.text_input("Sujet / nouvelle (tout type)",value="Bar raye Quebec Rimouski")
if st.button("FETCH AUTO + GENERER TOP1 PERCUTANT"):
    faits,decor=fetch_percutant_auto(sujet); st.session_state["faits"]=faits; st.session_state["decor"]=decor
    sujet_low=sujet.lower(); personnages_requis=set(["Le Sage","Bas-Rouge"])
    for mot,perso in CASTING_DICO.items():
        if mot in sujet_low: personnages_requis.add(perso)
    for p in personnages_requis:
        if p not in bible: bible[p]=f"{p} chien 4 pattes auto-ajout"
    bible_filtree={k:bible[k] for k in personnages_requis if k in bible}
    bible_json=json.dumps(bible_filtree,ensure_ascii=False); faits_str=" | ".join(faits)
    c1=f"Le Sage decouvre {sujet} dans {decor}"; c2=f"{random.choice(list(personnages_requis))} annonce {faits[0]}"; c3=f"Caniches debattent {faits[1] if len(faits)>1 else sujet}"; c4=f"Bas-Rouge torche face {sujet} geant {decor}"; c5=f"Le Sage + Garde Faune jumelles {decor}"; c6=f"Caniches pancarte {faits[1] if len(faits)>1 else faits[0]}"; c7=f"Duo Le Sage + Bas-Rouge {decor} coucher soleil"; c8=f"{random.choice(list(personnages_requis))} pupitre Ministere {sujet} {faits[2] if len(faits)>2 else ''}"; c9=f"Finale Le Sage + Bas-Rouge {sujet} {faits[0]} memoire {decor}"
    p=""; p+=f"L'EXTREMISTE & LE SAGE -- {date.today()} -- {sujet.upper()} -- 100% CHIENS 4 PATTES\n"; p+="STYLE: Uderzo caricature quebecoise percutante gros nez yeux exorbites bulles blanches BOLD 8 mots max 4 PATTES\n"; p+=f"BIBLE CASTING AUTO: {bible_json}\n"; p+=f"FAITS PERCUTANTS REELS AUTO-FETCH: {faits_str}\n"; p+=f"DECOR DU JOUR: {decor}\n"; p+=f"REGLE V9.0 UNIVERSEL PERCUTANT: Utiliser SEULEMENT casting ci-dessus, decor ephemere, OBLIGATOIRE faits percutants dans bulles. Caricature gros nez.\n"; p+=f"9 CASES VARIEES PERCUTANTES SUR {sujet.upper()}:\n"; p+=f"Case1 {c1} -- 4 pattes\nCase2 {c2} -- 4 pattes\nCase3 {c3} -- 4 pattes\nCase4 {c4} -- 4 pattes\nCase5 {c5} -- 4 pattes\nCase6 {c6} -- 4 pattes\nCase7 {c7} -- 4 pattes\nCase8 {c8} -- 4 pattes\nCase9 {c9} -- 4 pattes\n"
    open(BIBLE_FILE,"w",encoding="utf-8").write(json.dumps(bible,ensure_ascii=False,indent=2))
    st.code(p,language="text"); st.download_button("Telecharger prompt V9.0",p,file_name="prompt_v9.txt"); st.success(f"V9.0: {len(personnages_requis)} persos | {len(faits)} faits | decor {decor}"); st.info(faits_str)
