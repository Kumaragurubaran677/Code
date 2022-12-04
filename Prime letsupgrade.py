def prime_number():
	n = int(input('Enter 1 to check prime number or not - (or) -Enter 0 to check prime numbers of first 100 : '))
	if n==0:
	
		print ("The Prime Numbers of First 100 Numbers ")  
		for num in range (1, 100 + 1):  
		    if num > 1:  
		        for i in range (2, num):  
		            if (num % i) == 0:  
		                break  
		        else:  
	 	           print (num)
	elif n==1:
		a=int(input('Enter the number : '))
		flag = 0
		for i in range(2,a):
			if a%i==0:
				flag = 1
				break
		if flag == 1:
			print('Not Prime')
		else:
			print("Prime")
print(prime_number())