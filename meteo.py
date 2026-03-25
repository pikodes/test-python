"""nbre=float(input("donnez votre note "))
if nbre==1234:
      print("acces autorisé")
else:
      print("veuillez recommencer")"""

note=float(input("donnez votre note"))
if note>=16:
      print("mention tres bien")
elif note>=14:
      print ("mention bien")
elif note>=12:
      print("mention  assez bien")
elif note>=10:
      print("mention passable")
else:  
      print("insuffisant")                    
