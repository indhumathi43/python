num=int(input("Enter a number:"))
k=0
for i in range(2,num//2):
    if(num%i)==0:
        k=k+1
if(k<=0):
    print("Yes")
else:
    print("No")
