q=int(input())
x=map(int,input().split())
a=list(x)
s=len(a)
if(s==q):
  for i in range(0,s):
    if(a[i]==i):
      print(i,end=" ")
