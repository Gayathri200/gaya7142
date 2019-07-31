ch=str(input())
c=len(ch)
for i in range(0,c):
  s=ch[i]
  if (s>='a' and s<='z'):
   print(s.upper(),end="")
  elif(s>='A'and s<='z'):
   print(s.lower(),end="")    
