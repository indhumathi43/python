class space:
   def __init__(self):
    self.s=str(input())
    l=len(self.s)
    count=0
    for i in range(0,l-1): 
      if(self.s[i]==' '):
         count+=1
         print(count)
sp=space()
