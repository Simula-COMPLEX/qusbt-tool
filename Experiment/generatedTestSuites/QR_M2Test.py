import unittest
import sys
sys.path.append("D:\WXY\QuSBT_Exp\QR")
from testing import execute_quantum_program

class QR_M2Test(unittest.TestCase):

	def test_QR_M2_429(self):
		#Input: 110101101
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 429, "QR_M2", 200))

	def test_QR_M2_59(self):
		#Input: 000111011
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 59, "QR_M2", 200))

	def test_QR_M2_412(self):
		#Input: 110011100
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 412, "QR_M2", 200))

	def test_QR_M2_467(self):
		#Input: 111010011
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 467, "QR_M2", 200))

	def test_QR_M2_260(self):
		#Input: 100000100
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 260, "QR_M2", 200))

	def test_QR_M2_268(self):
		#Input: 100001100
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 268, "QR_M2", 200))

	def test_QR_M2_48(self):
		#Input: 000110000
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 48, "QR_M2", 200))

	def test_QR_M2_426(self):
		#Input: 110101010
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 426, "QR_M2", 200))

	def test_QR_M2_217(self):
		#Input: 011011001
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 217, "QR_M2", 200))

	def test_QR_M2_73(self):
		#Input: 001001001
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 73, "QR_M2", 200))

	def test_QR_M2_284(self):
		#Input: 100011100
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 284, "QR_M2", 200))

	def test_QR_M2_423(self):
		#Input: 110100111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 423, "QR_M2", 200))

	def test_QR_M2_250(self):
		#Input: 011111010
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 250, "QR_M2", 200))

	def test_QR_M2_266(self):
		#Input: 100001010
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 266, "QR_M2", 200))

	def test_QR_M2_317(self):
		#Input: 100111101
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 317, "QR_M2", 200))

	def test_QR_M2_264(self):
		#Input: 100001000
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 264, "QR_M2", 200))

	def test_QR_M2_82(self):
		#Input: 001010010
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 82, "QR_M2", 200))

	def test_QR_M2_311(self):
		#Input: 100110111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 311, "QR_M2", 200))

	def test_QR_M2_211(self):
		#Input: 011010011
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 211, "QR_M2", 200))

	def test_QR_M2_313(self):
		#Input: 100111001
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 313, "QR_M2", 200))

	def test_QR_M2_488(self):
		#Input: 111101000
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 488, "QR_M2", 200))

	def test_QR_M2_81(self):
		#Input: 001010001
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 81, "QR_M2", 200))

	def test_QR_M2_283(self):
		#Input: 100011011
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 283, "QR_M2", 200))

	def test_QR_M2_217(self):
		#Input: 011011001
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 217, "QR_M2", 200))

	def test_QR_M2_157(self):
		#Input: 010011101
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 157, "QR_M2", 200))

	def test_QR_M2_494(self):
		#Input: 111101110
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 494, "QR_M2", 200))

if __name__ == '__main__':
	unittest.main()