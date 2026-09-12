import streamlit as st
import random
import re
from datetime import datetime

st.set_page_config(page_title="L'EXTREMISTE & LE SAGE V9.4 IA EXPERTE", layout="wide")

# ===================== BANQUE DE DONNEES - TOUJOURS INTACTE =====================
BIBLE_PERSOS = {
    "LE_SAGE": "Le Sage Labrador noir majestueux couronne or, yeux sages exorbitees Uderzo, 4 pattes, jamais humain",
    "BAS_ROUGE": "Bas-Rouge Beauceron 120lbs casque viking cornes torche flamme, yeux furieux exorbitees Uderzo, 4 pattes",
    "CANICHE_BEIGE": "Caniche Beige economique tuque beige camionnette vieille, yeux astucieux Uderzo, 4 pattes",
    "CARNEY": "Golden Carney Labrador blond cravate rouge politicien sage, yeux exorbitees Uderzo, 4 pattes",
    "BAR_RAYE": "Berger Allemand garde-peche jumelles uniforme vert, yeux vigilants Uderzo, 4 pattes"
}

RACES_25_VARIETES = [
    "Samoyede blanc neige fourrure epaisse",
    "Dalmatien taches noires",
    "Bouledogue Francais gris costaud",
    "Border Collie noir blanc intelligent",
    "Beagle tricolore curieux",
    "Berger Allemand noir feu",
    "Labrador Chocolat",
    "Husky gris yeux bleus",
    "Corgi courtes pattes",
    "Shiba Inu roux",
    "Caniche Royal blanc",
    "Bouvier Bernois tricolore",
    "Jack Russell blanc taches",
    "Teckel allonge saucisse",
    "Boxer fauve",
    "Chow Chow langue bleue",
    "Lévrier Afghan poil long",
    "Saint-Bernard enorme",
    "Chihuahua mini",
    "Dogue Allemand geant",
    "Colley a poil long Lassie",
    "Epagneul Cocker oreilles longues",
    "Terrier Ecossais noir",
    "Braque Allemand chasse",
    "Malamute Alaska puissant"
]

# ===================== V9.4 IA EXPERTE ANALYSE CRITIQUES =====================
def ia_analyse_experte(sujet):
    """
    NOUVEAU CERVEAU V9.4 - Analyse en mode IA experte critique quebecoise
    Au lieu de juste prendre les mots, elle comprend la rage, l'ironie, l'espoir
    """
    sujet_lower = sujet.lower()
    faits = []
    emotion = "neutre"
    forces = []
    punchlines = []
    
    # DETECTION AUTO AVEC IA EXPERTE
    is_gaz = any(w in sujet_lower for w in ["gaz", "essence", "201.6", "saguenay prix"])
    is_carney = any(w in sujet_lower for w in ["carney", "trump", "tarif", "politique"])
    is_bar = any(w in sujet_lower for w in ["bar raye", "peche", "poisson"])
    
    # --- ANALYSE EXPERTE GAZ ---
    if is_gaz:
        # Cherche les chiffres dans le sujet comme une IA
        chiffres = re.findall(r"\d+\.?\d*", sujet)
        faits = [
            "MOYENNE 201.6 CENTS SAGUENAY = RECORD +17.8 VS HABITUEL 183.8",
            "ECART 17 CENTS 187.9-204.9 = 2 PRIX POUR MEME GAZ = CROSSE",
            "SUPER GAZ 187.9 = -13.7 = 6.85$ ECONOMIE SUR 50L MAIS 30KM LOIN",
            "DIMANCHE -1.7 = ASTUCE CANICHE BEIGE MAIS MONDE TRAVAILLE",
            "TAXE 10C RETOUR 8 SEPT = OUCH FUTUR + 2.4 MILLIARDS ALLEGEMENT IRONIE"
        ]
        emotion = "frustration + petite lueur espoir Super Gaz + ironie 2.4M"
        forces = ["LE_SAGE", "BAS_ROUGE", "CANICHE_BEIGE"]
        punchlines = [
            "201.6? TABARNAC! VOLEURS!",
            "187.9 LOIN! 30KM! GRRR!",
            "DIMANCHE -1.7! MAIS JOB!",
            "TAXE 10C! 8 SEPT! OUCH!",
            "2.4M ALLEGEMENT? GAZ 201.6!"
        ]
    
    elif is_carney:
        faits = [
            "CARNEY RENCONTRE TRUMP TARIFS 25% = PEUR ECONOMIE",
            "CARNEY SAGE VS TRUMP FOU = IRONIE",
            "2.4 MILLIARDS ALLEGEMENT MAIS GAZ 201.6 = CONTRADICTION"
        ]
        emotion = "inquietude + ironie politique + espoir sage"
        forces = ["LE_SAGE", "BAS_ROUGE", "CARNEY"]
        punchlines = ["CARNEY SAGE? TRUMP FOU!", "25%? TABARNAC! PEUR!", "2.4M? OU CA?"]
    
    elif is_bar:
        faits = [
            "BAR RAYE TAILLE LIMITE 50-65CM = CONFUSION PECHEURS",
            "AMENDE 500$ SI TROP PETIT/GRAND = STRESS",
            "RETOUR BAR RAYE = JOIE MAIS REGLES
