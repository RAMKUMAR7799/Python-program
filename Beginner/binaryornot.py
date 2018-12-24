n=str(input(""))
flag=0
for i in n:
  if int(i) not in range(0,2):
    flag=1
    break
if flag>0:
  print("no")
else:
  print("yes")
