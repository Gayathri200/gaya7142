q=int(input())
x=map(int,input().split())
a=list(x)
num=sorted(a)
s=len(num)
if(s==q):
  while(s>0):
   s=s-1
   print(num[s],end="")
