x,y=map(str,input().split())
a=len(x)
b=len(y)
if(a!=b):
  print("no")
else:  
  for i in range(0,a):
    if(x[i]!=y[i]):
      print("no")
      exit()    
  print("yes") 
