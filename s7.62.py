import re
d=input()
if re.findall("[a-zA-Z2-9]",d):
   print("No")
else:
   print("Yes")
