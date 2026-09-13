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

# ===== FIX BULLLES - RESUME COURT
