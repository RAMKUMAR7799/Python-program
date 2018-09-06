import re
st = input("Enter the string:")
rs = re.sub('[\w]+' ,'', st)
print(len(rs))
