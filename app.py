import streamlit as st
import json, os, random
from datetime import date

st.set_page_config(page_title="V9.2.1 FORCE", layout="wide")
st.title("L'EXTREMISTE & LE SAGE - V9.2.1 Force + Races Aleatoires + Expressions")

BIBLE_FILE="bible_vivante.json"

RACES_POOL = [
    ("Le Sage Labrador noir couronne or cape beige sage", "triste choque doux sage"),
    ("Bas-Rouge Beauceron noir feu casque viking torche foulard rouge", "furieux extreme dents torche"),
    ("Golden Carney Golden Retriever cravate rouge PM Canada", "sourire banquier ironique"),
    ("Rottweiler noir feu dents sorties furieux", "furieux extreme colere"),
    ("Beagle oreilles longues curieux", "curieux etonne"),
    ("Berger Allemand Berger allemand garde faune jumelles", "surveillance serieux controle"),
    ("Husky gris blanc thermometre El Nino", "choque glace froid"),
    ("Bulldog orange grognon", "grognon fache"),
    ("Caniche Blanc poilu conducteur station", "content neutre"),
    ("Caniche Beige tuque camionnette", "content economie heureux"),
    ("Caniche Noir lunettes caissier", "serieux lunettes"),
    ("Caniche Brun ouvrier bleu travail", "heureux travail"),
    ("Caniche Gris chapeau retraite", "sage retraite"),
    ("Labrador Brun triste fleuve", "triste doux"),
    ("Zelensky Terrier ukrainien treillis kaki", "courageux")
]

def load_bible():
    if os.path.exists(BIBLE_FILE):
        try: return json.load(open(BIBLE_FILE,"r",encoding="utf-8"))
        except: pass
    return {
        "Le Sage": "Labrador noir couronne or cape beige sage gros nez 4 pattes jamais humain",
        "Bas-Rouge": "Beauceron noir feu casque aile viking torche foulard rouge yeux rouges furieux 4 pattes jamais humain",
        "Golden Carney": "Golden Retriever cravate rouge drapeau Canada gros nez banquier 4 pattes",
        "Rottweiler": "Rottweiler noir feu dents sorties furieux 4 pattes",
        "Beagle": "Beagle oreilles longues curieux 4 pattes",
        "Berger Allemand": "Berger allemand garde faune jumelles chapeau vert controle 4 pattes",
        "Husky": "Husky gris blanc thermometre choque 4 pattes",
        "Bulldog": "Bulldog orange grognon cheveux orange 4 pattes",
        "Caniche Blanc": "Caniche blanc poilu conducteur station essence 4 pattes",
        "Caniche Beige": "Caniche beige tuque camionnette content economie 4 pattes",
        "Caniche Noir": "Caniche noir lunettes caissier serieux 4 pattes",
        "Caniche Brun": "Caniche brun ouvrier bleu heureux travail 4 pattes",
        "Caniche Gris": "Caniche gris chapeau retraite sage 4 pattes",
        "Labrador Brun": "Labrador brun triste fleuve 4 pattes",
        "Zelensky": "Terrier ukrainien treillis kaki barbe drapeau Ukraine 4 pattes",
        "Pecheur Gaspesie": "Caniches pecheurs Gaspesie tuques filets colere quai 4 pattes"
    }

bible=load_bible()

CASTING_DICO={
    "carney":"Golden Carney", "zelensky":"Zelensky", "zelenski":"Zelensky",
    "trump":"Bulldog", "bar raye":"Berger Allemand", "bal raye":"Berger Allemand",
    "barre raye":"Berger Allemand", "gaspesie":"Pecheur Gaspesie",
    "matane":"Pecheur Gaspesie", "rimouski":"Berger Allemand",
    "el nino":"Husky", "pacifique":"Husky", "ukraine":"Zelensky",
    "russie":"Bas-Rouge", "ottawa":"Golden Carney", "calgary":"Golden Carney",
    "hells":"Rottweiler", "gaz":"Caniche Beige", "prix du gaz":"Caniche Beige",
    "essence":"Caniche Beige", "drones":"Zelensky", "freya":"Golden Carney",
    "fjord":"Labrador Brun", "saguenay":"Labrador Brun"
}

def fetch_percutant_auto(sujet):
    s=sujet.lower()
    if "bar raye" in s or "bal raye" in s:
        faits=["INTERDICTION TOTALE filet maillant bar raye","REGLEMENTATION 1er mai 2026 remise eau obligatoire","RIMOUSKI MATANE GASPESIE zone interdiction","PECHEURS EN COLERE manifestation quai","GARDE FAUNE controle amende 500$","Fleuve Saint-Laurent phare"]
        decor="FLEUVE SAINT-LAURENT GASPESIE RIMOUSKI MATANE phare quai peche"
    elif "carney" in s and "zelensky" in s:
        faits=["350M CAD missiles intercepteurs defense aerienne","430M CAD garanties pret gaz hiver Ukraine","30% drones Canada front immediat","26 milliards aide totale Canada","Partenariat 100 ans Canada Ukraine","Projet Freya moins cher que Patriot"]
        decor="OTTAWA CALGARY PARLEMENT drapeaux Canada Ukraine"
    elif "gaz" in s or "essence" in s:
        faits=["201.6 cents moyenne Montreal 225 stations 187.9 a 204.9 ecart 17c","+17.8 cents au-dessus prix habituel 183.8","Dimanche moins cher ecart 8.1 -1.7","Super Gaz 187.9 -13.7 economie 6.85$ sur 50L","Taxe federale 10 cents revient 8 sept 2026","2.4 milliards allegement fiscal 2026"]
        decor="STATION ESSENCE MONTREAL QUEBEC pompe 201.6 affichage"
    elif "el nino" in s:
        faits=["El Nino 2.7C RECORD HISTORIQUE Pacifique","Ocean 30C chaud jamais vu","Hawaii inondations","Fjord impact"]
        decor="OCEAN PACIFIQUE chaud 30C thermometre"
    elif "hells" in s:
        faits=["Interdiction port couleurs Hells Angels","Amende 5000$ Longueuil Quebec","Loi anti-gang patchs"]
        decor="LONGUEUIL QUEBEC route motos"
    elif "2977" in s or "tribute" in s:
        faits=["2977 drones = 2977 vies hommage","9 sept 2026 New York Harbor","2 tours jumelles lumiere coeur geant","Tribute in Light 2 faisceaux"]
        decor="NEW YORK HARBOR nuit Tribute Light 2 faisceaux"
    else:
        faits=[f"{sujet.upper()} ACTION FORTE PERCUTANTE",f"Lieu reel {sujet} 2026",f"Annonce ou interdiction sur {sujet}",f"Impact Quebec sur {sujet}"]
        decor="LIEU REEL DU SUJET "+sujet
    return faits,decor

def race_aleatoire_pour_case(type_case, deja):
    pool=RACES_POOL[:]
    random.shuffle(pool)
    tl=type_case.lower()
    if "furieux" in tl or "voleurs" in tl or "grrr" in tl:
        pool=sorted(pool,key=lambda x: 0 if "furieux" in x[1] or "grognon" in x[1] else 1)
    elif "economie" in tl or "moins cher" in tl or "super gaz" in tl:
        pool=sorted(pool,key=lambda x: 0 if "content" in x[1] or "heureux" in x[1] else 1)
    elif "cher" in tl or "tabarnac" in tl:
        pool=sorted(pool,key=lambda x: 0 if "choque" in x[1] or "triste" in x[1] else 1)
    for race,expr in pool:
        nom=race.split()[0]
        if nom not in deja[-2:]:
            return race,expr
    return random.choice(RACES_POOL)

with st.sidebar:
    st.header("BIBLIO Option A")
    st.caption(f"{len(bible)} chiens | Pool {len(RACES_POOL)} races")
    st.divider()
    for k in list(bible.keys())[:10]:
        st.caption(f"- {k}")

st.subheader("V9.2.1 - Force detection + Races Aleatoires + Expression scene")
sujet=st.text_input("Sujet / nouvelle (tout type)",value="Prix du gaz Montreal")

if st.button("GENERER V9.2.1 FORCE + ALEATOIRE"):
    faits,decor=fetch_percutant_auto(sujet)
    sujet_low=sujet.lower()
    persos_forces=[]
    personnages_requis=set(["Le Sage","Bas-Rouge"])
    for mot,perso in CASTING_DICO.items():
        if mot in sujet_low:
            persos_forces.append(perso)
            personnages_requis.add(perso)
    persos_forces=list(dict.fromkeys(persos_forces))

    for _ in range(4):
        r,_=random.choice(RACES_POOL)
        for k in bible.keys():
            if r.split()[0].lower() in k.lower():
                personnages_requis.add(k)
                break

    for p in personnages_requis:
        if p not in bible:
            bible[p]=f"{p} chien 4 pattes auto-ajout {sujet} 4 pattes"

    bible_filtree={k:bible[k] for k in personnages_requis if k in bible}
    bible_json=json.dumps(bible_filtree,ensure_ascii=False)
    faits_str=" | ".join(faits)

    cases=[]
    deja=[]
    force_map={1:"Le Sage",2:persos_forces[0] if persos_forces else "Golden Carney",4:"Bas-Rouge",5:persos_forces[1] if len(persos_forces)>1 else "Berger Allemand",7:persos_forces[0] if persos_forces else "Labrador Brun",8:persos_forces[-1] if persos_forces else "Caniche Noir"}
    types_cases=["cher choque 201.6 TABARNAC decouvre","annonce officielle pupitre","ecart curieux compare 187.9 204.9","furieux voleurs GRRR torche geant","surveillance jumelles dimanche moins cher","economie Super Gaz 187.9 content","taxe grognon OUCH 10 cents","2.4 milliards allegement serieux Ministere","finale multi races memoire"]

    for i in range(1,10):
        t=types_cases[i-1]
        if i in force_map:
            nom_force=force_map[i]
            race_full=next((r[0] for r in RACES_POOL if nom_force.split()[0].lower() in r[0].lower()), nom_force)
            expr_full=next((r[1] for r in RACES_POOL if nom_force.split()[0].lower() in r[0].lower()), "serieux")
            cases.append(f"{race_full} expression {expr_full} FORCE DETECTION {t} dans {decor} -- 4 pattes")
            deja.append(nom_force.split()[0])
        else:
            race,expr=race_aleatoire_pour_case(t,deja)
            deja.append(race.split()[0])
            cases.append(f"{race} expression {expr} ALEATOIRE {t} dans {decor} -- 4 pattes")

    p=""
    p+=f"L'EXTREMISTE & LE SAGE -- {date.today()} -- {sujet.upper()} -- 100% CHIENS 4 PATTES FORCE+ALEATOIRE\n"
    p+="STYLE: Uderzo caricature quebecoise percutante gros nez yeux exorbites bulles blanches BOLD 8 mots max CHAQUE CHIEN EXACTEMENT 4 PATTES JAMAIS HUMAIN RACES DIVERSES ALEATOIRES EXPRESSION APPROPRIEE\n"
    p+=f"BIBLE CASTING FORCE: {bible_json}\n"
    p+=f"FAITS PERCUTANTS REELS: {faits_str}\n"
    p+=f"DECOR DU JOUR: {decor}\n"
    p+=f"REGLE V9.2.1 FORCE: Persos detectes {persos_forces} DOIVENT apparaitre OBLIGATOIRE Case2,5,7,8. Reste aleatoire races differentes expression qui fit scene (furieux si voleurs, content si economie, choque si cher, surveillance si dimanche, grognon si taxe). Gros nez.\n"
    p+=f"9 CASES FORCE+ALEATOIRE SUR {sujet.upper()}:\n"
    for i,c in enumerate(cases,1):
        p+=f"Case{i} {c}\n"

    open(BIBLE_FILE,"w",encoding="utf-8").write(json.dumps(bible,ensure_ascii=False,indent=2))
    st.code(p,language="text")
    st.download_button("Telecharger V9.2.1 Force",p,file_name="prompt_v921_force.txt")
    st.success(f"V9.2.1: Forces {persos_forces} + {len(personnages_requis)-len(persos_forces)} aleatoires | decor {decor}")
    st.info(f"Persos forces: {persos_forces} | Faits: {faits_str}")

st.caption("V9.2.1 FORCE - Si perso detecte (Bar raye->Garde Faune, Gaz->Caniche Beige, Carney->Golden) il DOIT apparaitre. Reste = races aleatoires expression scene. Fini 2 caniches blancs.")
