import streamlit as st
import json, os, random
from datetime import date

st.set_page_config(page_title="V9.3 MEGA POOL 35 RACES", layout="wide")
st.title("L'EXTREMISTE & LE SAGE - V9.3 Mega Pool 35 Races + Anti-doublon + Force")

BIBLE_FILE="bible_vivante.json"

RACES_POOL = [
    ("Le Sage Labrador noir couronne or cape beige sage", "triste choque doux sage"),
    ("Bas-Rouge Beauceron noir feu casque viking torche foulard rouge", "furieux extreme dents torche"),
    ("Caniche Beige tuque beige camionnette content economie", "content economie heureux"),
    ("Caniche Blanc poilu conducteur station essence", "content neutre"),
    ("Caniche Brun ouvrier bleu salopette marron", "heureux travail economie"),
    ("Caniche Noir lunettes noires caissier Ministere", "serieux lunettes"),
    ("Caniche Gris chapeau gris retraite sage", "sage retraite"),
    ("Caniche Abricot boucles peche abricot", "curieux content"),
    ("Caniche Chocolat tablier boulanger chocolat", "content heureux"),
    ("Rottweiler noir feu dents sorties furieux", "furieux extreme colere"),
    ("Doberman noir oreilles coupees garde securite", "furieux surveillance"),
    ("Pitbull gris muscle tatouage grognon", "furieux grognon"),
    ("Mastiff beige baveux grognon enorme", "grognon fache"),
    ("Berger Allemand garde faune jumelles chapeau vert", "surveillance serieux controle"),
    ("Berger Belge Malinois treillis police K9", "surveillance courageux"),
    ("Husky gris blanc thermometre El Nino glace", "choque glace froid"),
    ("Husky Brun yeux bleus choque etonne", "choque etonne"),
    ("Labrador Brun triste fleuve pecheur", "triste doux"),
    ("Labrador Blond doux lunettes blond", "triste doux sage"),
    ("Golden Carney Golden Retriever cravate rouge PM Canada", "sourire banquier ironique"),
    ("Golden Fonce lunettes banquier fonce", "sourire ironique"),
    ("Beagle oreilles longues curieux tricolore", "curieux etonne"),
    ("Beagle Harrier chasse oreilles longues", "curieux surveillance"),
    ("Corgi pattes courtes sourire royal", "content heureux"),
    ("Jack Russell blanc tache terrier excite", "curieux choque excite"),
    ("Teckel long saucisse lunettes saucisse", "serieux curieux"),
    ("Bulldog orange grognon Carney Trump orange", "grognon fache taxe"),
    ("Bouledogue Francais oreilles chauve-souris grognon", "grognon fache"),
    ("Boxer fauve dents sorties boxeur gants", "furieux colere"),
    ("Samoyede blanc neige sourire neige", "content heureux neige doux"),
    ("Chow Chow langue bleue grognon fourrure", "grognon"),
    ("Dalmatien taches noires pompier casque", "surveillance serieux"),
    ("Border Collie noir blanc berger moutons", "surveillance curieux intelligent"),
    ("Saint-Bernard tonneau alcool montagne neige", "sage doux triste"),
    ("Zelensky Terrier ukrainien treillis kaki barbe", "courageux triste"),
]

def load_bible():
    if os.path.exists(BIBLE_FILE):
        try: return json.load(open(BIBLE_FILE,"r",encoding="utf-8"))
        except: pass
    d={}
    for race,_ in RACES_POOL:
        cle=race.split()[0]+" "+race.split()[1] if "Caniche" in race else race.split()[0]+" "+race.split()[1] if "Berger" in race or "Golden" in race else race.split()[0]
        d[cle]=f"{race} 4 pattes jamais humain gros nez"
    return d

bible=load_bible()

CASTING_DICO={
    "carney":"Golden Carney", "zelensky":"Zelensky", "trump":"Bulldog",
    "bar raye":"Berger Allemand", "bal raye":"Berger Allemand", "gaspesie":"Caniche Beige",
    "matane":"Berger Allemand", "rimouski":"Berger Allemand", "el nino":"Husky",
    "pacifique":"Husky", "ukraine":"Zelensky", "gaz":"Caniche Beige",
    "prix du gaz":"Caniche Beige", "essence":"Caniche Beige", "hells":"Rottweiler",
    "fjord":"Labrador Brun", "saguenay":"Labrador Brun"
}

def fetch_percutant_auto(sujet):
    s=sujet.lower()
    if "bar raye" in s:
        faits=["INTERDICTION TOTALE filet maillant bar raye","REGLEMENTATION 1er mai 2026 remise eau obligatoire","RIMOUSKI MATANE GASPESIE zone interdiction","PECHEURS EN COLERE manifestation quai","GARDE FAUNE controle amende 500$","Fleuve Saint-Laurent phare"]
        decor="FLEUVE SAINT-LAURENT GASPESIE RIMOUSKI MATANE phare quai peche"
    elif "gaz" in s or "essence" in s:
        faits=["201.6 cents moyenne Montreal 225 stations 187.9 a 204.9 ecart 17c","+17.8 cents au-dessus prix habituel 183.8","Dimanche moins cher ecart 8.1 -1.7","Super Gaz 187.9 -13.7 economie 6.85$ sur 50L","Taxe federale 10 cents revient 8 sept 2026","2.4 milliards allegement fiscal 2026"]
        decor="STATION ESSENCE MONTREAL QUEBEC pompe 201.6 affichage"
    elif "carney" in s and "zelensky" in s:
        faits=["350M CAD missiles intercepteurs","430M CAD garanties pret gaz hiver Ukraine","30% drones Canada front immediat","26 milliards aide totale Canada","Partenariat 100 ans","Projet Freya moins cher que Patriot"]
        decor="OTTAWA CALGARY PARLEMENT drapeaux Canada Ukraine"
    else:
        faits=[f"{sujet.upper()} ACTION FORTE PERCUTANTE",f"Lieu reel {sujet} 2026",f"Annonce sur {sujet}",f"Impact Quebec {sujet}"]
        decor="LIEU REEL "+sujet
    return faits,decor

def race_unique(type_case, deja):
    pool=[r for r in RACES_POOL if r[0].split()[0] not in deja and (r[0].split()[1] if len(r[0].split())>1 else "") not in deja]
    if not pool:
        pool=RACES_POOL[:]
    random.shuffle(pool)
    tl=type_case.lower()
    if "furieux" in tl or "vole
