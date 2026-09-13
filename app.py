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

if st.button("GENERER V9.2.1 FORCE + ALEATOIRE"):
    faits,decor=fetch_percutant_auto(sujet)
    slow=sujet.lower()
    persos_forces=[]
    req=set(["Le Sage","Bas-Rouge"])
    for mot,perso in CASTING_DICO.items():
        if mot in slow:
            persos_forces.append(perso)
            req.add(perso)
    persos_forces=list(dict.fromkeys(persos_forces))

    for p in req:
        if p not in bible:
            bible[p]=f"{p} chien 4 pattes auto {sujet} 4 pattes"

    bible_filtree={k:bible[k] for k in req if k in bible}
    bible_json=json.dumps(bible_filtree,ensure_ascii=False)
    faits_str=" | ".join(faits)

    cases=[]
    deja=[]
    force_map={1:"Le Sage",2:persos_forces[0] if persos_forces else "Golden Carney",4:"Bas-Rouge",5:"Berger Allemand"}
    types_cases=["cher choque 201.6 TABARNAC","annonce officielle pupitre","ecart curieux 187.9 204.9","furieux voleurs GRRR torche","surveillance dimanche moins cher","economie Super Gaz 187.9 content","taxe grognon 10 cents","2.4 milliards allegement","finale multi races"]

    for i in range(1,10):
        t=types_cases[i-1]
        if i in force_map:
            nom_force=force_map[i]
            race_full=next((r[0] for r in RACES_POOL if nom_force.split()[0].lower() in r[0].lower()), nom_force)
            expr_full=next((r[1] for r in RACES_POOL if nom_force.split()[0].lower() in r[0].lower()), "serieux")
            cases.append(f"{race_full} expression {expr_full} FORCE {t} dans {decor} -- 4 pattes")
            deja.append(nom_force.split()[0])
        else:
            race,expr=race_aleatoire(t,deja)
            deja.append(race.split()[0])
            cases.append(f"{race} expression {expr} ALEATOIRE {t} dans {decor} -- 4 pattes")

    p=""
    p+=f"L'EXTREMISTE & LE SAGE -- {date.today()} -- {sujet.upper()} -- 100% CHIENS 4 PATTES\n"
    p+="STYLE: Uderzo caricature quebecoise percutante gros nez yeux exorbites bulles blanches BOLD 8 mots max CHAQUE CHIEN 4 PATTES JAMAIS HUMAIN\n"
    p+=f"BIBLE CASTING FORCE: {bible_json}\n"
    p+=f"FAITS PERCUTANTS REELS: {faits_str}\n"
    p+=f"DECOR DU JOUR: {decor}\n"
    p+=f"REGLE V9.2.1: Persos {persos_forces} FORCE Case2,5. Le Sage Case1, Bas-Rouge Case4 TOUJOURS. Races variees.\n"
    p+=f"9 CASES SUR {sujet.upper()}:\n"
    for i,c in enumerate(cases,1):
        p+=f"Case{i} {c}\n"

    open(BIBLE_FILE,"w",encoding="utf-8").write(json.dumps(bible,ensure_ascii=False,indent=2))
    st.code(p,language="text")
    st.download_button("Telecharger V9.2.1 Fix",p,file_name="prompt_v921_fix.txt")
    st.success(f"Fix OK: Forces {persos_forces} + Le Sage + Bas-Rouge | decor {decor}")

st.caption("V9.2.1 FIX - SyntaxError corrige - Le Sage + Bas-Rouge toujours presents + detection Carney/Bar raye/Gaz auto")
