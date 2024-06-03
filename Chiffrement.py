# ====================================================================================
# Author : Groupe 8
# Date : 2024/05/23
# PROGRAMME: CHIFFREMENT CESAR
# ====================================================================================

import string

alphabet = string.ascii_lowercase


# alphabet.find('t') # Renvoie l’index (position) de la lettre t dans l’alphabet
# new_character = alphabet[8] # Renvoie la lettre de l’alphabet qui a pour index 8

# ====================================================================================
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


# ====================================================================================
# FONCTION 2: ÉCRIRE DANS LA CONSOLE
def ecrire_console():
    print(""
          ""
          "")
    texte_string = input('Ecrivez la phrase/texte à coder: ')
    texte_minuscule = texte_string.lower()
    liste_caracteres = list(texte_minuscule)
    return liste_caracteres


# ====================================================================================
# FONCTION 3: DÉCALLER LES LETTRES SELON LA CLÉ (positive ou négative)
def decaller_lettres(liste, cle):
    liste_result = []
    for i in range(len(liste)):
        if liste[i] in alphabet:
            indice = alphabet.find(liste[i]) + cle + 26
            indice %= 26
            liste_result.append(alphabet[indice])
        else:
            liste_result.append(liste[i])
            continue
    return liste_result


# ====================================================================================
# FONCTION 4: RETOURNE LE RESULTAT DU CHIFFREMENT DANS LA CONSOLE
def traiter_resultat_console(liste):
    resultat = ''.join(map(str, liste))
    return resultat


# ====================================================================================
# FONCTION 5: RETOURNE LE RESULTAT DU CHIFFREMENT DANS UN NOUVEAU FICHIER TEXTE
def traiter_resultat_fichier(liste):
    fichier_creer = open('chiffrement_cesar.txt', 'x')
    new = traiter_resultat_console(liste)
    fichier_creer.write(new)
    fichier_creer.close()


# ====================================================================================
# FONCTION 6: PASSER LE DICTIONNAIRE EN LISTE DE MOTS
def passer_dictionnaire_en_liste():
    with open('dictionnaire_francais.txt', "r", encoding='utf-8') as text_file:
        lines = text_file.read().split()
    return lines


# ====================================================================================
# FONCTION 7: DECRYPTAGE SANS CLE (méthode brute_force)
def decrypter_sans_cle(liste_caracteres, liste_dictionnaire):
    print("Nous allons tenter de déchiffrer votre message. Cette procédure peut prendre quelques instants.")
    cle = 1
    while cle < 27:
        liste_decallee = decaller_lettres(liste_caracteres, cle)
        liste_mots_decallee = ''.join(map(str, liste_decallee)).split(' ')
        for mot in liste_mots_decallee:
            if mot in liste_dictionnaire and len(mot) >= 4:
                cle_trouve = cle + 26
                cle_trouve %= 26
                texte_trouve = ' '.join(map(str, liste_mots_decallee))
                print('La clé trouvée est:', 26 - cle_trouve, 'et le texte crypté est:', texte_trouve)
                essai = str(input('Est-ce bien votre texte (oui ou non) ?'))
                if essai == 'non':
                    continue
                return cle_trouve
        cle += 1


# ====================================================================================
# FONCTION 8: CHIFFRER A NOUVEAU
def chiffrer_a_nouveau():
    print("\n\n")
    print('As-tu autre chose à chiffrer?')
    choix = input('Répondre: oui ou non ')
    if choix == 'oui':
        chiffrer()  # appel récurrent de la fonction
        return True
    else:
        print('A BIENTOT')
        return False


# ====================================================================================
# FONCTION PRINCIPALE
def chiffrer():
    # Initialisation
    liste_decallee = []
    print("****************************************************************************** "
          "\nTu t'appretes à utiliser un code de chiffrement basé sur la méthode de César"
          "\n******************************************************************************")
    print("\n\n\n\n")

    while True:
        try:
            choix_forme = int(input('→ Veux-tu utiliser un fichier (tape 0) ou écrire le message dans la console ('
                                    'tape 1): '))
            if choix_forme == 1 or choix_forme == 0:
                break
        except ValueError:
            print("Le format n'est pas bon. Veuillez réessayer.")

    # Choix de la forme du texte:
    # Fichier
    if choix_forme == 0:
        liste_caracteres = lire_fichier()

    # Console
    else:
        liste_caracteres = ecrire_console()

    # Choix: encryptage ou décryptage
    print("\n\n\n\n")
    while True:
        try:
            choix_action = int(input('→ Veux-tu encrypter (tape 0) ou décrypter un message (tape 1): '))
            if choix_action == 1 or choix_action == 0:
                break
        except ValueError:
            print("Le format n'est pas bon. Veuillez réessayer.")

    # Encryptage (avec clé connue)
    if choix_action == 0:
        print("\n\n\n\n")
        while True:
            try:
                cle = int(input('→ 🔑 Entrez la valeur de la clé (positive ou négative): '))
                if isinstance(cle, int):
                    break
            except ValueError:
                print("Le format n'est pas bon. Un nombre entier est attendu. Veuillez réessayer.")

        liste_decallee = decaller_lettres(liste_caracteres, cle)

    # Décryptage (avec clé connue ou non)
    else:
        choix_cle = str(input('Connaissez vous la valeur de la cle de chiffrement ? Entrez oui ou non: '))

        # Avec clé connue
        if choix_cle == 'oui':
            print("\n\n\n\n")
            cle = int(input(' 🔑 Entrez la valeur de la clé (positive ou négative): '))
            cle = -cle
            liste_decallee = decaller_lettres(liste_caracteres, cle)

        # Décryptage sans clé
        if choix_cle == 'non':
            liste_dictionnaire = passer_dictionnaire_en_liste()
            cle_trouve = decrypter_sans_cle(liste_caracteres, liste_dictionnaire)
            liste_decallee = decaller_lettres(liste_caracteres, cle_trouve)

    # Résultat fourni selon la forme initiale choisie
    # Fichier
    if choix_forme == 0:
        traiter_resultat_fichier(liste_decallee)
        print('Le fichier créé se nomme: chiffrement_cesar.txt')

    # Console
    else:
        texte_crypte = traiter_resultat_console(liste_decallee)
        print("\n\n\n\n")
        print('Le texte encrypté (ou décrypté) avec la clé donnée est:', texte_crypte)

    # Retour au choix utilisateur
    chiffrer_a_nouveau()


# Appel fonction principale
chiffrer()
