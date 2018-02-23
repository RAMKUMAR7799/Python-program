num1=int(input("Enter your number"))
num2=int(input("Enter your number"))
num3=int(input("Enter your number"))
if(num1>=num2 and num1>=num3):
  print(num1,"is greatest number")
elif(num2>=num1 and num2>=num3):
  print(num2,"is greatest number")
else:
  print(num3,"is greatest number")
