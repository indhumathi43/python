a=input("Enter letter:")
a=a.lower()
if(a.islower() and len(a)==1):
if(a in vowel):
print("VOWEL")
else:
print("CONSONANT")
else:
print("INVALID")
