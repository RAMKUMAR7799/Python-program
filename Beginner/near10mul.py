import math
num=int(input("Enter Value"))
if num<10: print("10")
else:
    l=len(str(num))
    num+=5
    num=num/(10**(l-1))
    print(math.floor(n)*(10**(l-1)))
