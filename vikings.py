import random

# ============================================================
# TABLEAU DE HASHAGE VIKING (représenté en liste de listes)
# ============================================================
tableau_hashage = [
    ["A", "B", "C", "D", "E", "F", "G", "H", "I"],      # Valeurs unités (1 à 9)
    ["J", "K", "L", "M", "N", "O", "P", "Q", "R"],      # Valeurs dizaines (10 à 90)
    ["S", "T", "U", "V", "W", "X", "Y", "Z"]            # Valeurs centaines (100 à 800)
]

# ============================================================
# Fonction : créer le dictionnaire de correspondance
# ============================================================
def creer_dictionnaire_hashage():
    """
    Crée et retourne un dictionnaire associant chaque lettre à sa valeur numérique.
    """
    dictionnaire = {}

    # Première ligne : unités
    for i in range(len(tableau_hashage[0])):
        lettre = tableau_hashage[0][i]
        dictionnaire[lettre] = i + 1

    # Deuxième ligne : dizaines
    for i in range(len(tableau_hashage[1])):
        lettre = tableau_hashage[1][i]
        dictionnaire[lettre] = (i + 1) * 10

    # Troisième ligne : centaines
    for i in range(len(tableau_hashage[2])):
        lettre = tableau_hashage[2][i]
        dictionnaire[lettre] = (i + 1) * 100

    return dictionnaire


# ============================================================
# Fonction : calculer le hash d’un mot
# ============================================================
def hasher_mot(mot, dictionnaire):
    """
    Calcule la valeur hashée d’un mot en additionnant la valeur de chaque lettre.
    """
    total = 0
    mot = mot.upper()

    for lettre in mot:
        if lettre in dictionnaire:
            total += dictionnaire[lettre]
        else:
            # Ignore les caractères non reconnus (espaces, accents, ponctuation)
            continue
    return total


# ============================================================
# Fonction : hasher une phrase complète
# ============================================================
def hasher_phrase(phrase, dictionnaire):
    """
    Retourne une liste contenant la valeur hashée de chaque mot dans la phrase.
    """
    mots = phrase.split()
    resultats = []

    for mot in mots:
        valeur = hasher_mot(mot, dictionnaire)
        resultats.append(valeur)

    return resultats


# ============================================================
# Fonction : mode devinette
# ============================================================
def devinette_viking(dictionnaire):
    """
    Mode devinette : le programme affiche un nombre aléatoire
    et le joueur doit trouver un mot dont le hash correspond à ce nombre.
    """
    # On fixe une borne max raisonnable : 2000
    nombre_secret = random.randint(1, 2000)
    print("\nLe dieu Odin t’envoie une énigme numérique !")
    print(f"Trouve un mot dont le hash vaut : {nombre_secret}\n")

    tentative = input("Entre ton mot viking : ").strip().upper()
    valeur = hasher_mot(tentative, dictionnaire)

    print(f"\nTon mot '{tentative}' a pour hash : {valeur}")
    if valeur == nombre_secret:
        print("Bravo, ton mot ouvre le coffre du trésor d’Odin !")
    else:
        print("Faux ! Le code runique ne correspond pas au trésor...")


# Programme principal
dictionnaire = creer_dictionnaire_hashage()
choix = ""

while choix != "4":
    print("\n=== MENU DU HASHAGE VIKING ===")
    print("1. Hasher un mot")
    print("2. Hasher une phrase complète")
    print("3. Mode devinette viking")
    print("4. Quitter")
    choix = input("Ton choix : ")

    if choix == "1":
        mot = input("\nEntre ton mot viking : ")
        valeur = hasher_mot(mot, dictionnaire)
        print(f"Le hash de '{mot}' est : {valeur}")

    elif choix == "2":
        phrase = input("\nEntre ta phrase viking : ")
        resultats = hasher_phrase(phrase, dictionnaire)
        print("\nRésultat des hashages :")
        mots = phrase.split()
        for i in range(len(mots)):
            print(f"{mots[i]:<20} {resultats[i]}")

    elif choix == "3":
        devinette_viking(dictionnaire)

    elif choix == "4":
        print("\nLes coffres se referment !")
    else:
        print("\nChoix invalide. Réessaie, jeune viking !")


