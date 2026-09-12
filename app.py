import streamlit as st
import json, os, random
from datetime import date

st.set_page_config(page_title="V9.2.1 FIX", layout="wide")
st.title("L'EXTREMISTE & LE SAGE - V9.2.1 Fix + Force + Races Aleatoires")

BIBLE_FILE="bible_vivante.json"

RACES_POOL = [
    ("Le Sage Labrador noir couronne or cape beige sage", "triste choque doux sage"),
    ("Bas-Rouge Beauceron noir feu casque viking torche foulard rouge", "furieux extreme dents torche"),
    ("Caniche Beige tuque beige camionnette", "content economie heureux"),
    ("Caniche Blanc poilu conducteur station", "content neutre"),
    ("Beagle oreilles longues curieux", "curieux etonne"),
    ("Berger Allemand garde faune jumelles", "surveillance serieux controle"),
    ("Husky gris blanc thermometre", "choque glace froid"),
    ("Bulldog orange grognon", "grognon fache"),
    ("Caniche Noir lunettes caissier", "serieux lunettes"),
    ("Caniche Brun ouvrier bleu", "heureux travail"),
    ("Golden Carney cravate rouge PM Canada", "sourire banquier ironique"),
    ("Labrador Brun triste fleuve", "triste doux"),
    ("Zelensky Terrier ukrainien treillis", "courageux"),
    ("Rottweiler noir feu dents sorties", "furieux extreme"),
]

def load_bible():
    if os.path.exists(BIBLE_FILE):
        try:
            return json.load(open(BIBLE_FILE,"r",encoding="utf-8"))
        except:
            pass
    return {
        "Le Sage": "Labrador noir couronne or cape beige sage 4 pattes jamais humain",
        "Bas-Rouge": "Beauceron noir feu casque viking torche foulard rouge furieux 4 pattes",
        "Caniche Beige": "Caniche beige tuque camionnette content economie 4 pattes",
        "Caniche Blanc": "Caniche blanc conducteur 4 pattes",
        "Beagle": "Beagle curieux 4 pattes",
        "Berger Allemand": "Berger allemand garde faune 4 pattes",
        "Husky": "Husky thermometre 4 pattes",
        "Bulldog": "Bulldog orange grognon 4 pattes",
        "Golden Carney": "Golden Retriever cravate rouge 4 pattes",
    }

bible=load_bible()

CASTING_DICO={
    "carney":"Golden Carney", "zelensky":"Zelensky",
    "bar raye":"Berger Allemand", "bal raye":"Berger Allemand",
    "gaz":"Caniche Beige", "essence":"Caniche Beige"
}

def fetch_percutant_auto(sujet):
    s=sujet.lower()
    if "bar raye" in s or "bal raye" in s:
        faits=["INTERDICTION TOTALE filet maillant bar raye","REGLEMENTATION 1er mai 2026 remise eau obligatoire","RIMOUSKI MATANE GASPESIE zone interdiction","PECHEURS EN COLERE manifestation quai","GARDE FAUNE controle amende 500$"]
        decor="FLEUVE SAINT-LAURENT GASPESIE phare quai peche"
    elif "gaz" in s or "essence" in s:
        faits=["201.6 cents moyenne Montreal 225 stations","187.9 a 204.9 ecart 17c","+17.8 au-dessus habituel 183.8","Dimanche moins cher -1.7","Super Gaz 187.9 economie 6.85 sur 50L","Taxe 10 cents revient 8 sept 2026","2.4 milliards allegement fiscal 2026"]
        decor="STATION ESSENCE MONTREAL QUEBEC pompe 201.6"
    else:
        faits=[f"{sujet.upper()} ACTION FORTE",f"Lieu reel {sujet} 2026",f"Annonce sur {sujet}"]
        decor="LIEU REEL "+sujet
    return faits,decor

def race_aleatoire(type_case, deja):
    pool=RACES_POOL[:]
    random.shuffle(pool)
    tl=type_case.lower()
    if "furieux" in tl or "voleurs" in tl:
        pool=sorted(pool,key=lambda x: 0 if "furieux" in x[1] else 1)
    elif "economie" in tl or "super gaz" in tl:
        pool=sorted(pool,key=lambda x: 0 if "content" in x[1] or "heureux" in x[1] else 1)
    for race,expr in pool:
        nom=race.split()[0]
        if nom not in deja[-2:]:
            return race,expr
    return random.choice(RACES_POOL)

st.subheader("V9.2.1 - Fix + Force + Races Aleatoires")
sujet=st.text_input("Sujet / nouvelle (tout type)",value="Prix du gaz Saguenay")

if st.button("GENERER V9
