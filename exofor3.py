mot=input("donne moi un mot ")
a=int(0)
for lettre in  mot:
     if lettre=="a":
          a+=1
print(a,"fois la lettre a")     

matrice = [ 
    [1, 2, 3],   # ligne 0 
    [4, 5, 6],   # ligne 1 
    [7, 8, 9]    # ligne 2 
] 
 
# Accès : matrice[ligne][colonne] 
print(matrice[0][0])  # 1 — ligne 0, colonne 0 
print(matrice[1][2])  # 6 — ligne 1, colonne 2 
print(matrice[2][1]) 
for ligne in matrice: 
    for element in ligne: 
        print(element, end=" ")   # affiche sur la même ligne 
    print() 

