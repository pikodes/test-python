tampon=int(input("donnez moi un nombre N "))
print("vous voulez sa table de mutiplication((mu) ou la somme des nbres de 1 à N(som)")
N=input("")
q=tampon+1
if N=="mu":
      for i in range (1,11):
            print(f"{i}","x",tampon,"=",i*tampon, sep=" ")
else:
      for i in range (1,tampon):
            tampon=tampon+i
      print(f"{tampon}")      