num=int(input("Enter number:"))
temp=num
rev=0
while temp!=0:
   rev=(rev*10)+(temp%10)
   temp=temp//10
if num==rev:
   print("Palindrome")
else:
   print("Not palindrome")
