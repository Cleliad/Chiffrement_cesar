import string

alphabet = string.ascii_lowercase

alphabet.find('t') # Renvoie l’index (position) de la lettre t dans l’alphabet
new_character = alphabet[8] # Renvoie la lettre de l’alphabet qui a pour index 8


def lire_fichier():
    fichier= open('texte_test.txt', 'r', encoding='utf-8')
    texte_string = fichier.read()
    texte_minuscule = texte_string.lower()
    texte = list(texte_minuscule)
    return(texte)

print(lire_fichier())
texte=lire_fichier()

def decaller(texte):
    cle= int(input('entrez la valeur de la clé (positive ou négative)'))
    for i in range(len(texte)):
        if texte[i] in alphabet:
            indice= alphabet.find(texte[i]) + cle + 26
            indice %=26
            print(indice)
            texte[i]= alphabet[indice]
        else:
            continue
    return(texte)

'''''
def texte_console():
    texte_string=input('Ecrivez la phrase/texte à code: ')
    texte_minuscule = texte_string.lower()
    texte = list(texte_minuscule)
    return (texte)

print(texte_console())
'''''

def traiter_resultat_console(texte):
    resultat=''.join(map(str,texte))
    print(resultat)
    return(resultat)
    
traiter_resultat_console(texte)




new=decaller(texte)
print(new)
def traiter_resultat_fichier(new):
    fichier_creer = open('test.txt', 'x')
    new= traiter_resultat_console(new)
    fichier_creer.write(new)
    fichier_creer.close()

traiter_resultat_fichier(new)
