a = int(input('what is your current attitude - '))
if(a >= 10000):
	print('Go around !!')
elif(a  <10000):
	if(a==1000):
		print('Land the plane ')
	elif(a>1000):
		print('Land the plane by bringing it to 1000ft ')
	else:
		print('Given attitude is invalid')
