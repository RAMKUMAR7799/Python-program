a=int(input(""))
if a>1:
  for i in range(2,a):
    if a%i==0:
      print("NO")
      break
  else:
    print("Yes")
else:
  print("NO")
