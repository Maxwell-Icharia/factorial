def factorial(number):
	n = 1
	while number >= 1:
		n = n * number
		number = number - 1
	return n