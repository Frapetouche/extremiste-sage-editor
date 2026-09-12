import streamlit as st
import json, os, random
from datetime import date

st.set_page_config(page_title="V9.3.1 FIX", layout="wide")
st.title("L'EXTREMISTE & LE SAGE - V9.3.1 FIX 35 RACES")

BIBLE_FILE="bible_vivante.json"

RACES_POOL = [
    ("Le Sage Labrador noir couronne or", "triste choque sage"),
    ("Bas-Rouge Beauceron noir feu casque viking", "furieux extreme"),
    ("Caniche Beige tuque camionnette", "content economie"),
    ("Caniche Blanc poilu station", "content neutre"),
    ("Caniche Brun ouvrier bleu", "heureux travail"),
    ("Caniche Noir lunettes Ministere", "serieux"),
    ("Caniche Gris chapeau retraite", "sage"),
    ("Caniche Abricot boucles peche", "curieux"),
    ("Rottweiler noir feu dents", "furieux colere"),
    ("Doberman noir garde", "furieux surveillance"),
    ("Pitbull gris muscle", "furieux grognon"),
    ("Mastiff beige baveux", "grognon"),
    ("Berger Allemand garde faune jumelles", "surveillance controle"),
    ("Berger Belge Malinois police", "surveillance"),
    ("Husky gris blanc thermometre", "choque froid"),
    ("Labrador Brun triste fleuve", "triste doux"),
    ("Golden Carney cravate rouge PM", "sourire ironique"),
    ("Beagle oreilles longues curieux", "curieux etonne"),
    ("Corgi pattes courtes sourire", "content heureux"),
    ("Bulldog orange grognon", "grognon fache"),
    ("Bouledogue Francais grognon", "grognon"),
    ("Samoyede blanc neige sourire", "content neige"),
    ("Dalmatien taches pompier", "surveillance"),
    ("Border Collie noir blanc berger", "surveillance curieux"),
    ("Zelensky Terrier kaki barbe", "courageux"),
]

def load_bible():
    if os.path.exists(BIBLE_FILE):
        try:
            return json.load(open(BIBLE_FILE,"r",encoding="utf-8"))
        except:
            pass
    d={}
    for race,_ in RACES_POOL:
        key=race.split()[0]
        if "Caniche" in race:
            key=race.split()[0]+" "+race.split()[1]
        d[key]=race+" 4 pattes jamais humain"
    return d

bible=load_bible()

CASTING={
    "carney":"Golden Carney",
    "zelensky":"Zelensky",
    "bar raye":"Berger Allemand",
    "bal raye":"Berger Allemand",
    "gaz":"Caniche Beige",
    "essence":"Caniche Beige",
}

def get_faits(sujet):
    s=sujet.lower()
    if "bar raye" in s:
        faits=["INTERDICTION filet maillant bar raye","1er mai 2026 remise eau obligatoire","RIMOUSKI MATANE GASPESIE interdiction","PECHEURS EN COLERE quai","GARDE FAUNE amende 500$"]
        decor="FLEUVE SAINT-LAURENT GASPESIE quai phare"
    elif "gaz" in s or "essence" in s:
        faits=["201.6 cents moyenne Montreal 225 stations","187.9 a 204.9 ecart 17c","+17.8 au-dessus habituel 183.8","Dimanche moins cher -1.7","Super Gaz 187.9 economie 6.85 sur 50L","Taxe 10 cents revient 8 sept 2026","2.4 milliards allegement fiscal"]
        decor="STATION ESSENCE MONTREAL pompe 201.6"
    else:
        faits=[sujet.upper()+" ACTION FORTE",sujet+" 2026 lieu reel",sujet+" annonce"]
        decor="LIEU REEL "+sujet
    return faits,decor

def race_unique(t, deja):
    pool=[r for r in RACES_POOL if r[0].split()[0] not in deja]
    if not pool:
        pool=RACES_POOL[:]
    random.shuffle(pool)
    return pool[0]

st.subheader("V9.3.1 FIX - Le Sage + Bas-Rouge toujours + Carney auto")
sujet=st.text_input("Sujet",value="Prix du gaz Saguenay")

if st.button("GENERER"):
    faits,decor=get_faits(sujet)
    slow=sujet.lower()
    forces=[]
    req=set(["Le Sage","Bas-Rouge"])
    for mot,perso in CASTING.items():
        if mot in slow:
            forces.append(perso)
            req.add(perso)
    forces=list(dict.fromkeys(forces))

    for p in req:
        if p not in bible:
            bible[p]=p+" chien 4 pattes"

    bible_f=json.dumps({k:bible[k] for k in req if k in bible},ensure_ascii=False)
    faits_str=" | ".join(faits)

    cases=[]
    deja=[]
    force_map={1:"Le Sage",2:forces[0] if forces else "Caniche Beige",4:"Bas-Rouge",5:forces[1] if len(forces)>1 else "Berger Allemand"}

    types=["cher choque TABARNAC","annonce officielle pupitre","ecart curieux compare","furieux voleurs GRRR","surveillance dimanche","economie Super Gaz content","taxe grognon OUCH","2.4 milliards allegement","finale multi races"]

    for i in range(1,10):
        t=types[i-1]
        if i in force_map:
            nf=force_map[i]
            if any(nf.split()[0] in d for d in deja):
                rf,ex=race_unique(t,deja)
            else:
                rf=next((r[0] for r in RACES_POOL if nf.split()[0].lower() in r[0].lower()), nf)
                ex=next((r[1] for r in RACES_POOL if nf.split()[0].lower() in r[0].lower()), "serieux")
            cases.append(f"{rf} expression {ex} FORCE {t} dans {decor} -- 4 pattes")
            deja.append(rf.split()[0])
        else:
            rf,ex=race_unique(t,deja)
            cases.append(f"{rf} expression {ex} ALEATOIRE {t} dans {decor} -- 4 pattes")
            deja.append(rf.split()[0])

    prompt=""
    prompt+=f"L'EXTREMISTE & LE SAGE -- {date.today()} -- {sujet.upper()} -- 100pct CHIENS 4 PATTES\n"
    prompt+="STYLE: Uderzo caricature quebecoise percutante gros nez bulles BOLD 8 mots max 4 PATTES JAMAIS HUMAIN RACES VARIEES\n"
    prompt+=f"BIBLE FORCE: {bible_f}\n"
    prompt+=f"FAITS: {faits_str}\n"
    prompt+=f"DECOR: {decor}\n"
    prompt+=f"REGLE: Le Sage Case1 + Bas-Rouge Case4 TOUJOURS + Forces {forces} Case2,5 + 5 races variees anti-doublon sur 25 races\n"
    prompt+=f"9 CASES SUR {sujet.upper()}:\n"
    for i,c in enumerate(cases,1):
        prompt+=f"Case{i} {c}\n"

    open(BIBLE_FILE,"w",encoding="utf-8").write(json.dumps(bible,ensure_ascii=False,indent=2))
    st.code(prompt,language="text")
    st.download_button("Telecharger FIX",prompt,file_name="prompt_fix.txt")
    st.success(f"OK Forces {forces} + Le Sage + Bas-Rouge | {len(set(deja))} races uniques")

st.caption("V9.3.1 FIX - 0 accent - syntax clean - Le Sage + Bas-Rouge toujours - Carney auto - 25 races variees anti-doublon")
