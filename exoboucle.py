"""
while True: 
      reponse = input("Tapez 'quitter' pour arrêter : ") 
      if reponse == "quitter": 
            break  # on sort de la boucle 
      print(f"Vous avez tapé : {reponse}") 
print("Au revoir !") 

for i in range(10): 
    if i % 2 == 0: 
        continue  
    print(i)      
    """
n=int(input("ecombien de note tu veux entre? "))
som=float(0)
for i in range (n):
      d=int(input("entre une note: "))
      som+=d
print("la moyenne est:", som/n)  

#entier de 1 a 30
for i in range (1,31):
      if i%3==0:
            print("fizz")
      if i%5==0:
            print("buzz") 
      else:
            print(i)     