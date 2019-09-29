a=1
while a<101:
	if a%7 and (a%10-7) and (a//10-7):
		print(a)
	a=a+1