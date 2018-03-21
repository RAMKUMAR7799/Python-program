from statistics import median
num = int(input('Size of elements : '))
A = list()

for i in range(num) :
  ele  = int(input())
  A.append(ele)
print(median(A))

