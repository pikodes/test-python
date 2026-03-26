"""liste=[10,20,30,40,50]
print(liste[-5])
print(liste[-1])
print(liste[-3])

#créer une liste vide et y mettre des élements
liste_vide=list()
liste_vide.append("Alice")
liste_vide.append("Bob")
liste_vide.append("Charlie")
print(liste_vide)
"""
#creer, inserer et remplacer des élements dans une liste
listsem=["lundi","mardi","jeudi","jeudi"]
listsem.insert(2,"mercredi")
print(listsem)
listsem[4]="vendredi"
print(listsem)
print(listsem[::-1])
print(listsem[::2])
print(listsem[3:])

list_course=["lait","pain","oeufs","beurre","fromage"]
del list_course[4]
print(list_course)
list_course.remove("lait")
element=list_course.pop(2)
print(list_course)

list_lettres=["a","b","c","d","e","f","g","h"]
print(list_lettres[::2])
print(list_lettres[:])
list_lettres.pop(1)
print(list_lettres[:])
print(list_lettres)



