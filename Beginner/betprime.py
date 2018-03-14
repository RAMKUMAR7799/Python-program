num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
for num in range(num1,num2):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
