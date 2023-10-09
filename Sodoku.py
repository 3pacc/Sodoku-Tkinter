from tkinter import Tk,Canvas
     
    # GUI
     
fenetre = Tk() # Cette ligne crée une instance de la classe Tk qui représente la fenêtre principale de l'application.
fenetre.title("Solveur de Sudoku - NSI")#Cette ligne définit le titre de la fenêtre.
fenetre.resizable(False,False)#Cette ligne empêche le redimensionnement de la fenêtre en largeur et en hauteur. Les deux paramètres False signifient que la fenêtre ne peut pas être redimensionnée.
     
interface = Canvas(fenetre,width=400,height=500,bg="white")# Cette ligne crée un widget Canvas à l'intérieur de la fenêtre. Le widget Canvas est utilisé pour dessiner des graphiques, des formes et du texte.
interface.pack() # Cette ligne permet d'afficher le widget Canvas à l'intérieur de la fenêtre.

#Les quatre lignes suivantes créent des textes à l'intérieur du widget Canvas. Chaque ligne crée un texte différent avec une position spécifique (coordonnées x, y) et un contenu spécifique.
interface.create_text(5,400,anchor="nw",text="Pour ajouter un chiffre, survolez la case correspondante et appuyez sur\nle pavé numérique.",tags="i")
interface.create_text(5,435,anchor="nw",text="Pour supprimer un chiffre, survolez la case et appuyez sur 'Effacer'.",tags="i")
interface.create_text(5,455,anchor="nw",text="Pour résoudre la grille, appuyez sur 'Entrer'.",tags="i")
interface.create_text(5,480,anchor="nw",text="Pour tout effacer, appuyez sur 'Suppr'.",tags="i")
#Les quatres lignes suivantes créent des rectangles à l'intérieur du widget Canvas. Chaque ligne crée un rectangle différent avec des coordonnées spécifiques (x1, y1, x2, y2) et une couleur de remplissage spécifique ("black" signifie noir).    
interface.create_rectangle(12,7,15,379,fill="black")
interface.create_rectangle(381,7,384,379,fill="black")
interface.create_rectangle(12,7,384,10,fill="black")
interface.create_rectangle(12,376,384,379,fill="black")
cases = [[0]*9 for n in range(9)]#Cette ligne crée une liste 2D de 9 par 9 remplie de zéros. Cette liste sera utilisée pour stocker les références aux rectangles créés ultérieurement.
textCase = [[False]*9 for n in range(9)]#Cette ligne crée une autre liste 2D de 9 par 9 remplie de valeurs booléennes False. Cette liste sera utilisée pour suivre si un texte a été ajouté à une case spécifique.
ic = 0 #indices de colonnes
ie = 0 #indices de rangées
for i in range(15,369,40):  # itère de 15 à 369 avec un pas de 40. Cette boucle est utilisée pour créer les rectangles horizontaux de la grille du Sudoku.
    jc = 0 #indices des sous-colonnes
    je = 0 #indices des sous-rangées
    for j in range(10,364,40): #tère de 10 à 364 avec un pas de 40. Cette boucle est utilisée pour créer les rectangles verticaux de la grille du Sudoku.
        cases[jc][ic] = interface.create_rectangle(i+ie,j+je,i+ie+40,j+je+40,fill="white",activefill="#e0e0e0") # Cette ligne crée un rectangle à l'intérieur du widget Canvas et stocke sa référence dans la liste cases à l'indice [jc][ic]. Les coordonnées du rectangle sont déterminées par les variables i, j, ie et je.
        jc += 1 #Cette ligne incrémente la valeur de jc à chaque itération de la boucle intérieure, ce qui permet de suivre les indices des sous-colonnes.
        if jc in [3,6]: # Cette condition vérifie si la valeur de jc est égale à 3 ou 6. Si c'est le cas, cela signifie que nous avons atteint une limite de sous-colonne et nous devons créer une ligne noire horizontale supplémentaire.
            interface.create_rectangle(12,j+43+je,384,j+40+je,fill="black") #Cette ligne crée une ligne noire horizontale supplémentaire en dessous des rectangles de la grille.
            je += 3 #je += 3 : Cette ligne incrémente la valeur de je de 3 à chaque itération de la boucle intérieure, ce qui permet d'ajuster les coordonnées verticales pour la création des rectangles et des lignes noires.
    ic += 1 #Cette ligne incrémente la valeur de ic à chaque itération de la boucle extérieure, ce qui permet de suivre les indices des colonnes.
    if ic in [3,6]:#Cette condition vérifie si la valeur de ic est égale à 3 ou 6. Si c'est le cas, cela signifie que nous avons atteint une limite de colonne et nous devons créer une ligne noire verticale supplémentaire.
        interface.create_rectangle(i+43+ie,7,i+ie+40,379,fill="black") #Cette ligne crée une ligne noire verticale supplémentaire à gauche des rectangles de la grille.
        ie += 3 #incrémente la valeur de ie de 3 à chaque itération de la boucle extérieure, ce qui permet d'ajuster les coordonnées horizontales pour la création des rectangles et des lignes noires.
    



def event(touche): # qui est appelée en réponse aux événements de touche dans l'application
    global grille,textCase,cases # Cette ligne déclare les variables grille, textCase et cases comme variables globales, ce qui permet d'accéder et de modifier ces variables à l'intérieur de la fonction
    toucheK = touche.keysym # Cette ligne récupère la touche pressée à partir de l'objet touche passé en argument de la fonction.
    if toucheK in "123456789": #Cette ligne vérifie si la touche pressée est un chiffre entre 1 et 9. Si c’est le cas, le bloc de code suivant est exécuté
        eff = False # Cette ligne initialise une variable locale nommée eff à False. Cette variable sert à indiquer si une case de texte a été effacée ou non
        if interface.type(interface.find_closest(touche.x,touche.y)[0]) == "text" and interface.itemcget(interface.find_closest(touche.x,touche.y)[0],"tags") != "i current":# Cette ligne vérifie si l’élément le plus proche du pointeur de la souris est de type texte et si son tag n’est pas “i current”. Si c’est le cas, le bloc de code suivant est exécuté
            interface.delete(interface.find_closest(touche.x,touche.y)[0])#Cette ligne supprime l’élément de texte le plus proche du pointeur de la souris
            eff = True#Cette ligne met à jour la variable eff à True pour indiquer qu’une case de texte a été effacée
        for i in range(9):# Cette ligne commence une boucle for qui itère sur les valeurs de i allant de 0 à 8. Cette boucle sert à parcourir les lignes d’une grille de 9x9 cases
            for j in range(9):#Cette ligne commence une boucle for imbriquée qui itère sur les valeurs de j allant de 0 à 8. Cette boucle sert à parcourir les colonnes d’une grille de 9x9 cases
                if interface.find_closest(touche.x,touche.y)[0] == cases[i][j]:#Cette ligne vérifie si l’élément le plus proche du pointeur de la souris correspond à la case située à la position (i,j) dans la grille
                    if not eff and not grille[i][j]:# Cette ligne vérifie si la variable eff est False et si la valeur de la case (i,j) dans la grille est nulle. Si c’est le cas, le bloc de code suivant est exécuté
                        grille[i][j] = int(toucheK)# Cette ligne affecte la valeur entière de la touche pressée à la case (i,j) dans la grille
                    if eff:#Cette ligne vérifie si la variable eff est True. Si c’est le cas, le bloc de code suivant est exécuté
                        grille[i][j] = int(toucheK)#grille[i][j] = int(toucheK) Cette ligne affecte la valeur entière de la touche pressée à la case (i,j) dans la grille
                        textCase[i][j] = False#Cette ligne met à jour la valeur de textCase[i][j] à False pour indiquer que la case (i,j) ne contient pas de texte
                    break#Cette ligne interrompt la boucle for imbriquée sur j, car on a trouvé la case correspondant à l’élément le plus proche du pointeur de la souris
            if interface.find_closest(touche.x,touche.y)[0] == cases[i][j]:#Cette ligne vérifie à nouveau si l’élément le plus proche du pointeur de la souris correspond à la case située à la position (i,j) dans la grille
                break#Cette ligne interrompt la boucle for sur i, car on a trouvé la case correspondant à l’élément le plus proche du pointeur de la souris
        affG(i,j,toucheK)#Cette ligne appelle une fonction nommée affG qui prend en argument les valeurs de i, j et toucheK. Cette fonction sert à afficher la valeur de la touche pressée dans la case (i,j) de l’interface graphique
    if toucheK == "Return":#Cette ligne vérifie si la touche pressée est la touche Entrée. Si c’est le cas, le bloc de code suivant est exécuté
        chercher()#Cette ligne appelle une fonction nommée chercher qui sert à résoudre le sudoku1
    if toucheK == "Delete":#Cette ligne vérifie si la touche pressée est la touche Supprimer. Si c’est le cas, le bloc de code suivant est exécuté
        nouv()#Cette ligne appelle une fonction nommée nouv qui sert à générer un nouveau sudoku
    if toucheK == "BackSpace":#Cette ligne vérifie si la touche pressée est la touche Retour arrière. Si c’est le cas, le bloc de code suivant est exécuté
        if interface.type(interface.find_closest(touche.x,touche.y)[0]) == "text" and interface.itemcget(interface.find_closest(touche.x,touche.y)[0],"tags") != "i current":#Cette ligne vérifie si l’élément le plus proche du pointeur de la souris est de type texte et si son tag n’est pas “i current”. Si c’est le cas, le bloc de code suivant est exécuté
            interface.delete(interface.find_closest(touche.x,touche.y)[0])#Cette ligne supprime l’élément de texte le plus proche du pointeur de la souris
            for i in range(9):#Cette ligne commence une boucle for qui itère sur les valeurs de i allant de 0 à 8. Cette boucle sert à parcourir les lignes d’une grille de 9x9 cases
                for j in range(9):#Cette ligne commence une boucle for imbriquée qui itère sur les valeurs de j allant de 0 à 8. Cette boucle sert à parcourir les colonnes d’une grille de 9x9 cases
                    if interface.find_closest(touche.x,touche.y)[0] == cases[i][j]:#Cette ligne vérifie si l’élément le plus proche du pointeur de la souris correspond à la case située à la position (i,j) dans la grille
                        grille[i][j] = 0# 0 Cette ligne affecte la valeur nulle à la case (i,j) dans la grille
                        textCase[i][j] = False#Cette ligne met à jour la valeur de textCase[i][j] à False pour indiquer que la case (i,j) ne contient pas de texte
                        break#Cette ligne interrompt la boucle for imbriquée sur j, car on a trouvé la case correspondant à l’élément le plus proche du pointeur de la souris
                if interface.find_closest(touche.x,touche.y)[0] == cases[i][j]:#Cette ligne vérifie à nouveau si l’élément le plus proche du pointeur de la souris correspond à la case située à la position (i,j) dans la grille
                    break#Cette ligne interrompt la boucle for sur i, car on a trouvé la case correspondant à l’élément le plus proche du pointeur de la souris
    




def affG(x=-1,y=-1,nb=-1):#Cette ligne définit une fonction nommée affG qui prend trois arguments optionnels nommés x, y et nb. Cette fonction sert à afficher la valeur de la touche pressée dans la case (x,y) de l’interface graphique
    global textCase,cases# Cette ligne déclare les variables textCase et cases comme variables globales, ce qui permet d’accéder et de modifier ces variables à l’intérieur de la fonction
    if (x,y) == (-1,-1):# Cette ligne vérifie si les arguments x et y ont leurs valeurs par défaut (-1,-1). Si c’est le cas, le bloc de code suivant est exécuté
        for x in range(9):#Cette ligne commence une boucle for qui itère sur les valeurs de x allant de 0 à 8. Cette boucle sert à parcourir les lignes d’une grille de 9x9 cases
            for y in range(9):#Cette ligne commence une boucle for imbriquée qui itère sur les valeurs de y allant de 0 à 8. Cette boucle sert à parcourir les colonnes d’une grille de 9x9 cases
                if not textCase[x][y]:#Cette ligne vérifie si la valeur de textCase[x][y] est False. Si c’est le cas, le bloc de code suivant est exécuté
                    interface.create_text((interface.coords(cases[x][y])[0]+interface.coords(cases[x][y])[2])//2,(interface.coords(cases[x][y])[1]+interface.coords(cases[x][y])[3])//2,anchor="center",text=str(grille[x][y]),font=("Helvetica","16","bold"),fill="#0f0fa0",tags="case")#Cette ligne crée un élément de texte dans l’interface graphique, dont les coordonnées sont le centre de la case (x,y), dont le texte est la valeur de la case (x,y) dans la grille, dont la police est Helvetica en gras et de taille 16, dont la couleur est un bleu foncé et dont le tag est "case"
    else:#Cette ligne indique le début du bloc de code alternatif si la condition (x,y) == (-1,-1) est fausse
        if not textCase[x][y]:# Cette ligne vérifie si la valeur de textCase[x][y] est False. Si c’est le cas, le bloc de code suivant est exécuté
            textCase[x][y] = True#True Cette ligne met à jour la valeur de textCase[x][y] à True pour indiquer que la case (x,y) contient du texte
            interface.create_text((interface.coords(cases[x][y])[0]+interface.coords(cases[x][y])[2])//2,(interface.coords(cases[x][y])[1]+interface.coords(cases[x][y])[3])//2,anchor="center",text=nb,font=("Helvetica","16","bold"),tags="case")#Cette ligne crée un élément de texte dans l’interface graphique, dont les coordonnées sont le centre de la case (x,y), dont le texte est la valeur de l’argument nb, dont la police est Helvetica en gras et de taille 16 et dont le tag est "case"
    


fenetre.bind("<Key>",event)#Cette ligne lie l’événement “<Key>” (pression d’une touche) à la fonction event définie précédemment. Ainsi, chaque fois qu’une touche est pressée dans la fenêtre, la fonction event est appelée avec l’objet touche comme argument






                                        # Moteur de resolution  ::       Cette ligne est un commentaire qui indique le début d’une section du code qui sert à résoudre le sudoku
    






def nouv():#Cette ligne définit une fonction nommée nouv qui ne prend aucun argument. Cette fonction sert à générer un nouveau sudoku
    global grille,grilleFinie,textCase#Cette ligne déclare les variables grille, grilleFinie et textCase comme variables globales, ce qui permet d’accéder et de modifier ces variables à l’intérieur de la fonction.
    grille = [[0]*9 for n in range(9)]#Cette ligne crée une liste de listes qui représente une grille de 9x9 cases, toutes initialisées à 0
    grilleFinie = [[False]*9 for n in range(9)]#Cette ligne crée une liste de listes qui représente une grille de 9x9 booléens, tous initialisés à False. Cette grille sert à indiquer si une case est remplie ou non
    textCase = [[False]*9 for n in range(9)]#Cette ligne crée une liste de listes qui représente une grille de 9x9 booléens, tous initialisés à False. Cette grille sert à indiquer si une case contient du texte ou non
    interface.delete("case")# Cette ligne supprime tous les éléments de texte ayant le tag “case” dans l’interface graphique
    



def solutions(l,c,ites):# Définition de la fonction solutions avec les paramètres l, c et ites
    global grille,grilleFinie# Déclaration de variables globales grille et grilleFinie
    verifier()# Appel de la fonction verifier()
    
    # Détermination des indices de ligne et de colonne pour la sous-grille 3x3 contenant la cellule
    lc = l in [0,1,2] and [0,1,2] or l in [3,4,5] and [3,4,5] or l in [6,7,8] and [6,7,8]
    cc = c in [0,1,2] and [0,1,2] or c in [3,4,5] and [3,4,5] or c in [6,7,8] and [6,7,8]
    
    # Methode de recherche : Inclusion
    
    if not grilleFinie[l][c]:# Si la cellule (l,c) n'est pas encore remplie
        if not ites:# Si ites est False
            grille[l][c] = [1,2,3,4,5,6,7,8,9]#Initialisation des valeurs possibles pour la cellule 
        for k in range(9):
             # Suppression des valeurs déjà présentes dans la même ligne ou colonne que la cellule (l,c)
            if grilleFinie[l][k] and grille[l][k] in grille[l][c] and k != c:
                grille[l][c].remove(grille[l][k])
            if grilleFinie[k][c] and grille[k][c] in grille[l][c] and k != l:
                grille[l][c].remove(grille[k][c])
        for i in lc:
            for j in cc:
                # Suppression des valeurs déjà présentes dans la même sous-grille 3x3 que la cellule (l,c)
                if grilleFinie[i][j] and grille[i][j] in grille[l][c] and (i,j) != (l,c):
                    grille[l][c].remove(grille[i][j])
        verifier(l,c)# Appel de la fonction verifier() avec les arguments l et c
        
    # Methode de recherche : Exclusion (ap 1 iteration)
    
    if not grilleFinie[l][c] and ites:# Si la cellule (l,c) n'est pas encore remplie et ites est True
        for nb in grille[l][c]:# Pour chaque valeur possible pour la cellule (l,c)
            compteur = [0,0,0]# Initialisation d'un compteur pour chaque direction (ligne, colonne, sous-grille)
            for k in range(9):
                 # Comptage du nombre de cellules non remplies dans la même ligne ou colonne que la cellule (l,c) qui contiennent la valeur nb
                if not grilleFinie[l][k] and k != c:
                    for n in grille[l][k]:
                        compteur[0] += int(n == nb)
                if not grilleFinie[k][c] and k != l:
                    for n in grille[k][c]:
                        compteur[1] += int(n == nb)
            for i in lc:
                for j in cc:
                     # Comptage du nombre de cellules non remplies dans la même sous-grille 3x3 que la cellule (l,c) qui contiennent la valeur nb
                    if not grilleFinie[i][j] and (i,j) != (l,c):
                        for n in grille[i][j]:
                            compteur[2] += int(n == nb)
            if compteur[0] == 0 or compteur[1] == 0 or compteur[2] == 0: # Si aucune cellule non remplie dans une direction ne contient la valeur nb
                grilleFinie[l][c] = True # La cellule (l,c) est remplie
                grille[l][c] = nb   # La valeur de la cellule (l,c) est définie à nb
                for k in range(9):
                     # Suppression de la valeur nb des cellules non remplies dans la même ligne ou colonne que la cellule (l,c)
                    if not grilleFinie[l][k] and grille[l][c] in grille[l][k] and k != c:
                        grille[l][k].remove(grille[l][c])
                    if not grilleFinie[k][c] and grille[l][c] in grille[k][c] and k != l:
                        grille[k][c].remove(grille[l][c])
                for i in lc:
                    for j in cc:
                         # Suppression de la valeur nb des cellules non remplies dans la même sous-grille 3x3 que la cellule (l,c)
                        if not grilleFinie[i][j] and grille[l][c] in grille[i][j] and (i,j) != (l,c):
                            grille[i][j].remove(grille[l][c])
                break
                
    # Methode de recherche : Paires exclusives
    
    if not grilleFinie[l][c] and ites and len(grille[l][c]) == 2:# Si la cellule (l,c) n'est pas encore remplie, ites est True et il y a exactement 2 valeurs possibles pour la cellule (l,c)
        existe = [False,False,False]# Initialisation d'un indicateur d'existence pour chaque direction (ligne, colonne, sous-grille)
        for k in range(9):
            # Vérification de l'existence d'une autre cellule non remplie dans la même ligne ou colonne que la cellule (l,c) avec les mêmes 2 valeurs possibles
            if not grilleFinie[l][k] and grille[l][k] == grille[l][c] and k != c:
                existe[0] = True
            if not grilleFinie[k][c] and grille[k][c] == grille[l][c] and k != l:
                existe[1] = True
        for i in lc:
            for j in cc:
                # Vérification de l'existence d'une autre cellule non remplie dans la même sous-grille 3x3 que la cellule (l,c) avec les mêmes 2 valeurs possibles
                if not grilleFinie[i][j] and grille[i][j] == grille[l][c] and (i,j) != (l,c):
                    existe[2] = True
        if existe[0]:# Si une autre cellule non remplie dans la même ligne que la cellule (l,c) a les mêmes 2 valeurs possibles
            for k in range(9):
                # Suppression des 2 valeurs possibles des autres cellules non remplies dans la même ligne que la cellule (l,c)
                if not grilleFinie[l][k] and grille[l][k] != grille[l][c]:
                    for n in grille[l][k]:
                        if n in grille[l][c]:
                            grille[l][k].remove(n)
        if existe[1]:
            # Si une autre cellule non remplie dans la même colonne que la cellule (l,c) a les mêmes 2 valeurs possibles
            for k in range(9):
                if not grilleFinie[k][c] and grille[k][c] != grille[l][c]:
                    for n in grille[k][c]:
                        if n in grille[l][c]:
                            grille[k][c].remove(n)
        if existe[2]:
            # Si une autre cellule non remplie dans la même sous-grille 3x3 que la cellule (l,c) a les mêmes 2 valeurs possibles
            for i in lc:
                for j in cc:
                    # Suppression des 2 valeurs possibles des autres cellules non remplies dans la même sous-grille 3x3 que la cellule (l,c)
                    if not grilleFinie[i][j] and grille[i][j] != grille[l][c]:
                        for n in grille[i][j]:
                            if n in grille[l][c]:
                                grille[i][j].remove(n)
            
    # Methode de recherche : Triplets exculsifs (hors triplet induit)
            
    if not grilleFinie[l][c] and ites and len(grille[l][c]) == 3:# Si la cellule (l,c) n'est pas encore remplie, ites est True et il y a exactement 3 valeurs possibles pour la cellule (l,c)
        existe = [[],[],[]]# Initialisation d'une liste d'existence pour chaque direction (ligne, colonne, sous-grille)
        decompo = [[grille[l][c][0],grille[l][c][1]],[grille[l][c][1],grille[l][c][2]],[grille[l][c][0],grille[l][c][2]]]# Décomposition des 3 valeurs possibles en 3 paires de 2 valeurs
        for k in range(9):
            # Vérification de l'existence d'autres cellules non remplies dans la même ligne ou colonne que la cellule (l,c) avec les mêmes 3 valeurs possibles ou une paire de 2 valeurs possibles
            if not grilleFinie[l][k] and k != c and (grille[l][k] == grille[l][c] or grille[l][k] in decompo):
                existe[0].append(grille[l][k])
            if not grilleFinie[k][c] and k != l and (grille[k][c] == grille[l][c] or grille[k][c] in decompo):
                existe[1].append(grille[k][c])
        for i in lc:
            for j in cc:
                # Vérification de l'existence d'autres cellules non remplies dans la même sous-grille 3x3 que la cellule (l,c) avec les mêmes 3 valeurs possibles ou une paire de 2 valeurs possibles
                if not grilleFinie[i][j] and (i,j) != (l,c) and (grille[i][j] == grille[l][c] or grille[i][j] in decompo):
                    existe[2].append(grille[i][j])
        for k in range(3):
            triplet = []
            if len(existe[k]) == 2:# Si exactement 2 autres cellules non remplies dans une direction ont les mêmes 3 valeurs possibles ou une paire de 2 valeurs possibles
                for i in [0,1]:
                    for n in existe[k][i]:
                        if n not in triplet:
                            triplet.append(n)
                if triplet != grille[l][c]: # Si les 3 valeurs possibles ne sont pas les mêmes que celles de la cellule (l,c)
                    existe[k] = False
            else:
                existe[k] = False
        if existe[0]:# Si d'autres cellules non remplies dans la même ligne que la cellule (l,c) ont les mêmes 3 valeurs possibles ou une paire de 2 valeurs possibles
            for k in range(9):
                # Si d'autres cellules non remplies dans la même ligne que la cellule (l,c) ont les mêmes 3 valeurs possibles ou une paire de 2 valeurs possibles
                if not grilleFinie[l][k] and grille[l][k] != grille[l][c] and grille[l][k] not in existe[0]:
                    for n in grille[l][k]:
                        if n in grille[l][c]:
                            grille[l][k].remove(n)
        if existe[1]: # Si d'autres cellules non remplies dans la même colonne que la cellule (l,c) ont les mêmes 3 valeurs possibles ou une paire de 2 valeurs possibles
            for k in range(9):
                # Suppression des 3 valeurs possibles des autres cellules non remplies dans la même colonne que la cellule (l,c)
                if not grilleFinie[k][c] and grille[k][c] != grille[l][c] and grille[k][c] not in existe[1]:
                    for n in grille[k][c]:
                        if n in grille[l][c]:
                            grille[k][c].remove(n)
        if existe[2]:  # Si d'autres cellules non remplies dans la même sous-grille 3x3 que la cellule (l,c) ont les mêmes 3 valeurs possibles ou une paire de 2 valeurs possibles
            for i in lc:
                for j in cc:
                     # Suppression des 3 valeurs possibles des autres cellules non remplies dans la même sous-grille 3x3 que la cellule (l,c)
                    if not grilleFinie[i][j] and grille[i][j] != grille[l][c] and grille[i][j] not in existe[2]:
                        for n in grille[i][j]:
                            if n in grille[l][c]:
                                grille[i][j].remove(n)
            
        





def verifier(l=0,c=0):# Définition de la fonction verifier avec les paramètres l et c ayant des valeurs par défaut de 0
    global grille,grilleFinie# Déclaration de variables globales grille et grilleFinie
    if not l and not c:# Si l et c sont tous les deux égaux à 0
        for i in range(9):
            for j in range(9):
                 # Si la cellule (i,j) contient une liste de valeurs possibles
                if type(grille[i][j]) is list:
                     # Si la liste ne contient qu'une seule valeur possible et que cette valeur est différente de 0
                    if len(grille[i][j]) == 1 and grille[i][j][0]:
                        grilleFinie[i][j] = True# La cellule (i,j) est remplie
                        grille[i][j] = grille[i][j][0]# La valeur de la cellule (i,j) est définie à la seule valeur possible
                else: # Si la cellule (i,j) ne contient pas une liste de valeurs possibles
                    if grille[i][j] != 0:# Si la valeur de la cellule (i,j) est différente de 0
                        grilleFinie[i][j] = True # La cellule (i,j) est remplie
    else:# Si l ou c sont différents de 0
        if type(grille[l][c]) is list:# Si la cellule (l,c) contient une liste de valeurs possibles
            if len(grille[l][c]) == 1 and grille[l][c][0]: # Si la liste ne contient qu'une seule valeur possible et que cette valeur est différente de 0
                grilleFinie[l][c] = True# La cellule (l,c) est remplie
                grille[l][c] = grille[l][c][0]# La valeur de la cellule (l,c) est définie à la seule valeur possible
                






def chercher(ee=0,ite=0): # Définition de la fonction chercher avec les paramètres ee et ite ayant des valeurs par défaut de 0
    global grilleFinie,grille# Déclaration de variables globales grilleFinie et grille
    iterations = 0# Initialisation du compteur d'itérations
    grilleTest = [[0]*9 for n in range(9)]# Initialisation d'une grille de test
    grilleBack = [[0]*9 for n in range(9)]# Initialisation d'une grille de sauvegarde
    cellBack = [0,0,9,[]]# Initialisation d'une cellule de sauvegarde
    if ee:# Si ee est différent de 0
        print(ite,"iter"+"s"*(ite!=1))# Affichage du nombre d'itérations
    print(" "*(ee-1)+"|"*(ee!=0)+"_ couche",ee,end=" => ")# Affichage de la couche courante
    while "solution non determinee":# Boucle infinie
        grilleTest = copie(grille)# Copie de la grille dans la grille de test
        for i in range(9):
            for j in range(9):
                solutions(i,j,iterations)# Appel de la fonction solutions pour chaque cellule (i,j) avec le compteur d'itérations en argument
        for i in range(9):
            for j in range(9):
                if grille[i][j] == []:# Si la cellule (i,j) ne contient aucune valeur possible
                    return False # Retourne False (solution non trouvée)
        if grilleFinie == [[True]*9 for n in range(9)]: # Si toutes les cellules sont remplies
            print(iterations,"iter"+"s"*(iterations!=1)) # Affichage du nombre d'itérations
            affG() # Appel de la fonction affG()
            return True # Retourne True (solution trouvée)
        if grilleTest == grille:  # Si la grille n'a pas changé depuis la dernière itération
            grilleBack = copie(grille) # Copie de la grille dans la grille de sauvegarde
            for i in range(9):
                for j in range(9):
                    # Recherche de la cellule non remplie avec le moins de valeurs possibles

                    if not grilleFinie[i][j] and cellBack[2] > len(grille[i][j]):
                        cellBack = [i,j,len(grille[i][j]),grille[i][j]]
            for n in cellBack[3]: # Pour chaque valeur possible pour la cellule trouvée précédemment
                grille[cellBack[0]][cellBack[1]] = n # Définition de la valeur de la cellule à n
                if chercher(ee+1,iterations): # Appel récursif de la fonction chercher avec ee+1 et iterations en arguments
                    return True # Si une solution est trouvée, retourne True (solution trouvée)
                else:
                    grilleFinie = [[False]*9 for n in range(9)]  # Réinitialisation de la grilleFinie à False pour toutes les cellules
                    grille = copie(grilleBack)  # Restauration de la grille à partir de la grille de sauvegarde
                    verifier() # Appel de la fonction verifier()
            return False   # Retourne False (solution non trouvée)
        else:
            iterations += 1 # Incrémentation du compteur d'itérations
    





    
def copie(l):  # Définition de la fonction copie avec le paramètre l
    re = [[0]*9 for n in range(9)]  # Initialisation d'une nouvelle grille de 9x9 remplie de 0
    for i in range(9):
        for j in range(9):
            re[i][j] = l[i][j] # Copie des valeurs de la grille l dans la nouvelle grille
    return re  # Retourne la nouvelle grille
    
nouv()
fenetre.mainloop()