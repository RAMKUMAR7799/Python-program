num = int(input("Enter lower range : "))  
num1 = int(input("Enter upper range : "))  
  
for n in range(num,num1 + 1):  
   sum = 0  
   A = n  
   while A > 0:  
       D = A % 10  
       sum = sum + D ** 3  
       A = A // 10  
  
   if n == sum:  
       print(n)    
