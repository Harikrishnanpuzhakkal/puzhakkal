charhk=str(input())
vowel=("a","e","i","o","u")
if(charhk>="a"and charhk<="z" or charhk>="A" and charhk<="Z"):
  if charhk in vowel:
    print("Vowel")
  else:
    print("Consonant")  
else:
  print("invalid") 
