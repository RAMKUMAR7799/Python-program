ngk=15
print('sum from 1-15 :'+str(ngk*(ngk+1)//2))
st=15
eo=45
sum=0
for i in range(st,eo+1):
	if i%2==0:
		continue
	sum+=i
print('sum of odd number from 15-45(included) :'+str(sum))
