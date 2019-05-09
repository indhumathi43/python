string=input()
count=0
for i in string:
  if i.isspace()!=True:
      count+=1
      print(count)
