a=[]
n=int(input("Enter the elements:"))
for i in range(1,n+1):
  b=int(input("Enter element:"))
  a.append(b)
  a.sort()
print("Minimum element is:",*a[:1])
