s=input()
a=len(s)
r=0
t=0
for i in range(0,a):
  if(s[i]=="("):
    r=r+1
  elif(s[i]==")"):
    t=t+1  
if(r==t):
  print("yes")
else:
  print("no")    
