a,q=map(int,input().split())
b=map(int,input().split())
d=list(b)
s=len(d)
if(s==a):
  if q in d:
    print("Yes")
  else:
    print("No")  
