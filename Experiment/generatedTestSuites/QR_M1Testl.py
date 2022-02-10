import unittest
import sys
sys.path.append("D:\WXY\QuSBT_Exp\QR")
from testing import execute_quantum_program

class QR_M1Test(unittest.TestCase):

	def test_QR_M1_107(self):
		#Input: 001101011
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 107, "QR_M1", 200))

	def test_QR_M1_503(self):
		#Input: 111110111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 503, "QR_M1", 200))

	def test_QR_M1_470(self):
		#Input: 111010110
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 470, "QR_M1", 200))

	def test_QR_M1_495(self):
		#Input: 111101111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 495, "QR_M1", 200))

	def test_QR_M1_115(self):
		#Input: 001110011
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 115, "QR_M1", 200))

	def test_QR_M1_372(self):
		#Input: 101110100
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 372, "QR_M1", 200))

	def test_QR_M1_391(self):
		#Input: 110000111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 391, "QR_M1", 200))

	def test_QR_M1_150(self):
		#Input: 010010110
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 150, "QR_M1", 200))

	def test_QR_M1_7(self):
		#Input: 000000111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 7, "QR_M1", 200))

	def test_QR_M1_159(self):
		#Input: 010011111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 159, "QR_M1", 200))

	def test_QR_M1_295(self):
		#Input: 100100111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 295, "QR_M1", 200))

	def test_QR_M1_61(self):
		#Input: 000111101
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 61, "QR_M1", 200))

	def test_QR_M1_447(self):
		#Input: 110111111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 447, "QR_M1", 200))

	def test_QR_M1_461(self):
		#Input: 111001101
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 461, "QR_M1", 200))

	def test_QR_M1_275(self):
		#Input: 100010011
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 275, "QR_M1", 200))

	def test_QR_M1_316(self):
		#Input: 100111100
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 316, "QR_M1", 200))

	def test_QR_M1_31(self):
		#Input: 000011111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 31, "QR_M1", 200))

	def test_QR_M1_373(self):
		#Input: 101110101
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 373, "QR_M1", 200))

	def test_QR_M1_119(self):
		#Input: 001110111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 119, "QR_M1", 200))

	def test_QR_M1_453(self):
		#Input: 111000101
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 453, "QR_M1", 200))

	def test_QR_M1_498(self):
		#Input: 111110010
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 498, "QR_M1", 200))

	def test_QR_M1_318(self):
		#Input: 100111110
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 318, "QR_M1", 200))

	def test_QR_M1_449(self):
		#Input: 111000001
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 449, "QR_M1", 200))

	def test_QR_M1_415(self):
		#Input: 110011111
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 415, "QR_M1", 200))

	def test_QR_M1_132(self):
		#Input: 010000100
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 132, "QR_M1", 200))

	def test_QR_M1_424(self):
		#Input: 110101000
		print(execute_quantum_program([4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3], 13, 424, "QR_M1", 200))

if __name__ == '__main__':
	unittest.main()