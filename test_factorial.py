import unittest, factorial

from factorial import *

class TestFactorial(unittest.TestCase):
	def test_is_number(self):
		self.assertIsinstance(factorial(8), int)

if __name__ == '__main__':
	unittest.main()