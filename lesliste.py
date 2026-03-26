liste_debut=[]
liste2=list()
liste3=[1,2,"maman",8.9,"django"]
print(liste3)
print(len(liste3))
print(len(liste2))
print(len("bonjour"), end=" "), print(len([1,2,3]))
print(liste3[2])
print(liste3[-1])

# Créer la liste des nombres pairs de 0 à 10 
pairs = [x for x in range(11) if x % 2 == 0] 
print(pairs)   # [0, 2, 4, 6, 8, 10] 

# Créer la liste [1, 4, 9, 16, 25] (les carrés de 1 à 5) 
carres = [x**2 for x in range(1, 6)] 
print(carres)   # [1, 4, 9, 16, 25] 
 
# Équivalent sans compréhension (plus long) : 
carres = [] 
for x in range(1, 6): 
    carres.append(x**2) 
