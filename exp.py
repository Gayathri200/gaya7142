x,y=map(str,input().split())
a=len(x)
b=len(y)
r=0
if(b>=a):
  for i in range(0,a):
    if(x[i]==y[i]):
      r=r+1
  b=b-r
  print(b)
elif(a>=b):
  for i in range(0,b):
    if(x[i]==y[i]):
      r=r+1
  b=b-r
  print(b) 
