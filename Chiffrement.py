# ====================================================================================
# Author : Groupe 8
# Date : 2024/05/23
# PROGRAMME: CHIFFREMENT CESAR
# ====================================================================================

import string

alphabet = string.ascii_lowercase


# alphabet.find('t') # Renvoie l’index (position) de la lettre t dans l’alphabet
# new_character = alphabet[8] # Renvoie la lettre de l’alphabet qui a pour index 8

# FONCTION 1: LIRE LE FICHIER TEXTE ET METTRE SOUS FORME DE LISTE DE CARACTERES
def lire_fichier():
    while True:
        try:
            chemin_acces = input('Entrez le chemin d accès de votre fichier: ')
            fichier = open(chemin_acces, 'r', encoding='utf-8')
            texte_string = fichier.read()
            texte_minuscule = texte_string.lower()
            print(texte_minuscule)
            liste_caracteres = list(texte_minuscule)
            break
        except FileNotFoundError:  # message d'erreur si le fichier n'est pas trouvé
            print('Fichier non trouvé, essais à nouveau !!')
    return liste_caracteres


# FONCTION 2: ÉCRIRE DANS LA CONSOLE
def ecrire_console():
    print(""
          ""
          "")
    texte_string = input('Ecrivez la phrase/texte à coder: ')
    texte_minuscule = texte_string.lower()
    liste_caracteres = list(texte_minuscule)
    return liste_caracteres


# FONCTION 3: DÉCALLER LES LETTRES SELON LA CLÉ (positive ou négative)
def decaller_lettres(liste, cle):
    for i in range(len(liste)):
        if liste[i] in alphabet:
            indice = alphabet.find(liste[i]) + cle + 26
            indice %= 26
            liste[i] = alphabet[indice]
        else:
            continue
    return liste


# FONCTION 4: RETOURNE LE RESULTAT DU CHIFFREMENT DANS LA CONSOLE
def traiter_resultat_console(liste):
    resultat = ''.join(map(str, liste))
    return resultat


# FONCTION 5: RETOURNE LE RESULTAT DU CHIFFREMENT DANS UN NOUVEAU FICHIER TEXTE
def traiter_resultat_fichier(liste):
    fichier_creer = open('chiffrement_cesar.txt', 'x')
    new = traiter_resultat_console(liste)
    fichier_creer.write(new)
    fichier_creer.close()


# FONCTION 6: DECRYPTAGE SANS CLE

# a faire

# FONCTION 7: CHIFFRER A NOUVEAU
def chiffrer_a_nouveau():
    print(''
          '')
    print('As-tu autre chose à chiffrer?')
    choix = input('Répondre: oui ou non ')
    if choix == 'oui':
        chiffrer() # appel récurrent de la fonction
        return True
    else:
        print('A BIENTOT')
        return False


# FONCTION PRINCIPALE
def chiffrer():
    # Initialisation
    liste_decallee = []
    print("****************************************************************************** "
          "\nTu t'appretes à utiliser un code de chiffrement basé sur la méthode de César"
          "\n******************************************************************************")
    print(''
          ''
          ''
          '')
    choix_forme = int(input('→ Veux-tu utiliser un fichier (tape 0) ou écrire le message dans la console (tape 1): '))

    # Choix de la forme du texte:
    # Fichier
    if choix_forme == 0:
        liste_caracteres = lire_fichier()

    # Console
    else:
        liste_caracteres = ecrire_console()

    # Choix: encryptage ou décryptage
    print(''
          ''
          ''
          '')
    choix_action = int(input('→ Veux-tu encrypter (tape 0) ou décrypter un message (tape 1): '))

    # Encryptage (avec clé connue)
    if choix_action == 0:
        print(""
              ""
              "")
        cle = int(input('→ 🔑 Entrez la valeur de la clé (positive ou négative): '))
        liste_decallee = decaller_lettres(liste_caracteres, cle)

    # Décryptage (avec clé connue ou non)
    else:
        choix_cle = str(input('Connaissez vous la valeur de la cle de chiffrement ? Entrez oui ou non: '))

        # Avec clé connue
        if choix_cle == 'oui':
            print(""
                  ""
                  "")
            cle = int(input(' 🔑 Entrez la valeur de la clé (positive ou négative): '))
            cle = -cle
            liste_decallee = decaller_lettres(liste_caracteres, cle)

        # Décryptage sans clé
        else:
            print('programme pas encore codé')

    # Résultat fourni selon la forme initiale choisie
    # Fichier
    if choix_forme == 0:
        traiter_resultat_fichier(liste_decallee)
        print('Le fichier créé se nomme: chiffrement_cesar.txt')

    # Console
    else:
        texte_crypte = traiter_resultat_console(liste_decallee)
        print(""
              ""
              "")
        print('Le texte encrypté avec la clé donnée est:', texte_crypte)
    chiffrer_a_nouveau()

# Appel fonction principale
chiffrer()
