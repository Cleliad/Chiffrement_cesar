# Chiffrement Cesar

## BUT:
Ce code permet de chiffrer/déchiffrer un texte à l'aide de la méthode de chiffrement de César. 

### Entrées :
- **(e1)** texte .txt présent sur la machine exécutant le code ou une entrée texte (str) dans la console
- **(e2)** Choix de l'action à effetuer par le code : cryptage / décryptage
- **(e3)** Clé de codage/décodage positive ou négative (facultatif)

### Sorties :
2 sorties possibles :
- **(s1)** Si le texte est à l'origine un fichier .txt :
   Un nouveau fichier est créé avec le texte crypté/décrypté
- **(s2)** Si le texte est entré dans la console :
   Le texte crypté/décrypté est renvoyé dans la console

## Structure du code:

Fonction et noms associés :


**lire_fichier() :**
Permet de lire le fichier .txt avec un chemin d'accés et retourne une liste de tous les caractères présents dans le fichier en minuscule et sans accents.
- *Entrée : input de l'utilisateur (chemin d'accés au fichier)*
- *Sortie : list_text*


**ecrire_console() :**
Récupère le texte à coder dans la console et retourne une liste de caractères en minuscule. 
- *Entrée : input de l'utilisateur (texte à coder)*
- *Sortie : list_caracteres*


**decaller_lettres(liste,cle) :**
fonction qui permet d'encripter le texte selon la clé de criptage qui est demandée
- *Entrée : liste (liste des caractères du texte à traiter), cle (clé de codage pour le criptage)*
- *Sortie : liste_result (liste de caractères du texte encodé)*


**traiter_resultat_console(liste) :**
concatene la liste de caractère en entrée et retroune un texte *(string)*. 
- *Entrée : liste (liste des caractères du texte à traiter)*
- *Sortie : resultat (texte concatené en str)*


**passer_dictionnaire_en_liste() :**
ouvre le fichier texte *'dictionnaire_francais.txt'* présent en annexe du code et créer une liste contenant l'ensemble des mots du fichier. 
- *Entrée : va chercher 'dictionnaire_francais.txt' dans le dossier du fichier python*
- *Sortie : lines (tableau contenant l'ensemble des mots contenus dans le fichier)*


**traiter_resultat_fichier(liste) :**
concatene la liste de caractère en entrée et crée un nouveau fichier avec le texte concatené. 
- *Entrée : liste (liste des caractères du texte à traiter)*
- *Sortie : (texte concatené en dans un nouveau fichier)*


**decripter_sans_cle() :**
fonction qui part du fichier encodé et va tester des encodages successifs par incrément d'un jusqu'à ce qu'un mot du dictionnaire français soit trouvé dans le texte décodé. Alors la fonction retourne la clé de décodage.
Si aucune clé ne semble fonctionner la fonction retourne un message d'excuse et des explications. 
- *Entrée : liste_caractères (liste des caractères du texte à traiter), liste_dictionnaire (liste des mots du dictionnaire fournis par la fonction passer_dictionnaire_en_liste())*
- *Sortie : (texte concatené en dans un nouveau fichier)*

**chiffrer_a_nouveau() :**
fonction qui relance le code si l'utilisateur souhaite coder/décoder un nouveau texte/fichier. La fonction fait appel à chiffrer pour relancer le code.
- *Entrée : input de réponse de l'utilisateur*
- *Sortie :*
   - si reponse == 'oui' *relance la fonction chiffrer()*
   - sinon retourne 'A bientot'


**chiffrer() :**
fonction principale qui fait appel à l'ensemble des fonctions décrites précédement afin de répondre au besoin de l'utilisateur.
- *Entrée : input de réponse de l'utilisateur*
- *Sortie :*
   - si reponse == 'oui' *relance la fonction chiffrer()*
   - sinon retourne 'A bientot'

Fait appel à : 
- **decaller_lettres(),**
- **lire_fichier(),**
- **ecrire_console(),**
- **passer_dictionnaire_en_liste(),**
- **decrypter_sans_cle(),**
- **decaller_lettres(),**
- **traiter_resultat_console(),**
- **traiter_resultat_fichier(),**
- **chiffrer_a_nouveau()**

Selon les inputs de l'utilisateur la fonction principale fera appel à une suite de fonction permettant :
- _cripter_ ou _décripter_ :
   - un _fichier .txt_ donné par l'utilisateur et d'écrire un _nouveau fichier .txt_
   - une _entrée string dans la console_ et _imprimer la réponse dans la console_
- _décripter un fichier sans clé_ pour les deux cas précédents

PS: *La fonction va également proposer de traiter un nouveau texte après une utilisation.* 


**Autre :**
*alphabet* est une variable globale contenant les 26 caractères de l'alphabet français. 
- Appelé dans : **decaller_lettres**
