def factorial(number):
	if number == int:
		n = 1
		while number >= 1:
			n = n * number
			number = number - 1
		return n
	else:
		return 'Invalid input'