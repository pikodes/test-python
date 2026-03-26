new_caractere=list()
caractere=input("donner une phrase courte: ")
bomber=caractere
print(caractere.lower())
print(caractere.upper())
print(caractere.strip())
print(caractere.capitalize())
for a in caractere:
      if a== "a":
            x=caractere.count("a")
            caractere=caractere.replace("a","@",x)
            print()
      if a=="e":
            x=caractere.count("e")
            caractere=caractere.replace("e","&",x)





print(new_caractere)
pairs = [x for x in range(11) if x % 2 == 0] 





