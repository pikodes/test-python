a=input("entrez votre mot de passe ")
compt=0
if a=="secret123":
      print("deverouiller")
else:
      while a!="secret123":
            print("re-éssayer")
            compt+=1
            a=input("entrez votre mot de passe ")
      print("déverouiller après ",compt," tentatives")      
