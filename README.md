Ce code permet de chiffrer/déchiffrer un texte à l'aide du chiffrement de César. 

Entrées :
(e1) texte .txt ou un str entrée dans la console
(e2) Choix : cryptage / décriptage
(e3*) clé de codage/décoage positive ou négative (facultatif)

Sorties :
2 sorties possibles :
(s1) Si le texte est à l'origine un fichier .txt :
   Un nouveau fichier {nom_oroginal}+'cripte' ou 'decripte' doit être créé
(s2) Si le texte est entré dans la console :
   Le texte cripté/décripté est print dans la console

Fonction et noms associés :
# chiffrement_de_cesar() :
fonction principale, demande le texte (e1), le choix (e2) et la clé (e3*) et donne en sortie le texte converti (s1) et (s2)

# lire_fichier() :
permet de lire le fichier .txt et retourne une liste de tous les carachtères présents dans le fichier
Sortie : list_text

# decaller(texte) :
fonction qui permet d'encripter le texte selon la clé de criptage qui est demandée

# decripter_brute_force(texte) :
fonction qui ballaie les 26 codages possibles et propose la meilleure solution en sortie

# traiter_resultat_console(texte):
fonction qui convertie le texte modifié dans son tableau en string et retourne le texte modifié sous format texte ou crée un nouveau fichier .txt

# traiter_resultat_fichier(texte) :
fonction qui convertie le texte modifié dans son tableau en string et retourne le texte modifié sous format texte ou crée
