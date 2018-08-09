def main():
	try:
		r=0
		k=0
		n=input("Enter the string:")
		for i in n:
			if i.isalpha():
				r=r+1
			elif i.isnumeric():
				k=k+1
		if r+k==len(n) and r>0 and k>0:
			print('yes')
		else :
			print('no')
	except:
		print('invalid')
main()
