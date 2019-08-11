import string as m
m=input()
m=m.lower()
a=0
alpha='abcdefghijklmnopqrstuvwxyz'
for i in alpha:
  if i not in m:
    a=1
if(a==1):
  print("no")
else:
  print("yes")
