n=int(input("Enter number:"))
k=int(input("Enter exponent value:"))
p=1
for i in range(1,k+1):
    p=p*n
    print("Result of {0} power {1}={2}".format(n,k,p))
