## BUT:
Ce code permet de chiffrer/déchiffrer un texte à l'aide du chiffrement de César. 

### Entrées :
(e1) texte .txt ou un str entré dans la console
(e2) Choix : cryptage / décryptage
(e3) Clé de codage/décodage positive ou négative (facultatif)

### Sorties :
2 sorties possibles :
(s1) Si le texte est à l'origine un fichier .txt :
   Un nouveau fichier est créé avec le texte crypté/décrypté
(s2) Si le texte est entré dans la console :
   Le texte crypté/décrypté est renvoyé dans la console

## Structure du code:

Fonction et noms associés :
### chiffrer() :
Fonction principale, demande le texte (e1), le choix (e2) et la clé (e3*) et donne en sortie le texte converti (s1) et (s2)

### lire_fichier() :
Permet de lire le fichier .txt et retourne une liste de tous les carachtères présents dans le fichier
Sortie : list_text

### decaller_lettre(liste,cle) :
fonction qui permet d'encripter le texte selon la clé de criptage qui est demandée

### chiffrer_a_nouveau(): 
demande à l'utilisateur s'il a besoin de chiffrer un nouveau texte, sinon il quitte le code

### decripter_brute_force() :
fonction qui ballaie les 26 codages possibles et propose la meilleure solution en sortie

### traiter_resultat_console(liste):
fonction qui convertie le texte modifié dans son tableau en string et retourne le texte modifié sous format texte ou crée un nouveau fichier .txt

### traiter_resultat_fichier(liste) :
fonction qui convertie le texte modifié dans son tableau en string et retourne le texte modifié sous format texte ou crée
