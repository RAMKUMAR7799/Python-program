num=int(input("Enter number:"))
r=num
rev=0
while(num>0):
    p=num%10
    rev=rev*10+p
    num=num//10
if(r==rev):
    print("The number",r,"is a palindrome")
else:
    print("The number",r,"is not a palindrome")
