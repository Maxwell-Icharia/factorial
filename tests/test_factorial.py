import unittest

from main.factorial import factorial

class TestFactorial(unittest.TestCase):
	def test_is_number(self):
		self.assertTrue(factorial(8), int)
	def test_length(self):
		self.assertTrue(factorial(-1))
		self.assertTrue(factorial(0))

if __name__ == '__main__':
	unittest.main()