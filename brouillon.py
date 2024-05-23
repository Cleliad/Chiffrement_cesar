
import string
def lire_fichier():
    try:
        chemin_acces= input('Entrez le chemin d accès de votre fichier: ')
        fichier= open(chemin_acces, 'r', encoding='utf-8')
        texte_string = fichier.read()
        texte_minuscule = texte_string.lower()
        print(texte_minuscule)
        liste_caracteres = list(texte_minuscule)
    except FileNotFoundError:
        print('Fichier non trouvé, essais à nouveau')
        lire_fichier()
    return (liste_caracteres)


lire_fichier()