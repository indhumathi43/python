string=input()
s=0
for i in string:
    if not(i.isalpha() or i.isdigit() or i==""):
        s+=1
        print(s)
