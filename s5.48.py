n=int(input())
l=[]
sum=0
for i in input().split():
    sum=sum+int(i)
    sum=sum/n
    print(int(sum))
