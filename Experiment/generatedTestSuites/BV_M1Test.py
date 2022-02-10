import unittest
import sys
sys.path.append("D:\WXY\QuSBT_Exp\BV")
from testing import execute_quantum_program

class BV_M1Test(unittest.TestCase):

	def test_BV_M1_630(self):
		#Input: 1001110110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 630, "BV_M1", 100))

	def test_BV_M1_367(self):
		#Input: 0101101111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 367, "BV_M1", 100))

	def test_BV_M1_251(self):
		#Input: 0011111011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 251, "BV_M1", 100))

	def test_BV_M1_227(self):
		#Input: 0011100011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 227, "BV_M1", 100))

	def test_BV_M1_757(self):
		#Input: 1011110101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 757, "BV_M1", 100))

	def test_BV_M1_380(self):
		#Input: 0101111100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 380, "BV_M1", 100))

	def test_BV_M1_490(self):
		#Input: 0111101010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 490, "BV_M1", 100))

	def test_BV_M1_239(self):
		#Input: 0011101111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 239, "BV_M1", 100))

	def test_BV_M1_437(self):
		#Input: 0110110101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 437, "BV_M1", 100))

	def test_BV_M1_502(self):
		#Input: 0111110110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 502, "BV_M1", 100))

	def test_BV_M1_635(self):
		#Input: 1001111011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 635, "BV_M1", 100))

	def test_BV_M1_487(self):
		#Input: 0111100111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 487, "BV_M1", 100))

	def test_BV_M1_236(self):
		#Input: 0011101100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 236, "BV_M1", 100))

	def test_BV_M1_895(self):
		#Input: 1101111111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 895, "BV_M1", 100))

	def test_BV_M1_373(self):
		#Input: 0101110101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 373, "BV_M1", 100))

	def test_BV_M1_248(self):
		#Input: 0011111000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 248, "BV_M1", 100))

	def test_BV_M1_357(self):
		#Input: 0101100101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 357, "BV_M1", 100))

	def test_BV_M1_374(self):
		#Input: 0101110110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 374, "BV_M1", 100))

	def test_BV_M1_603(self):
		#Input: 1001011011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 603, "BV_M1", 100))

	def test_BV_M1_780(self):
		#Input: 1100001100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 780, "BV_M1", 100))

	def test_BV_M1_210(self):
		#Input: 0011010010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 210, "BV_M1", 100))

	def test_BV_M1_610(self):
		#Input: 1001100010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 610, "BV_M1", 100))

	def test_BV_M1_489(self):
		#Input: 0111101001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 489, "BV_M1", 100))

	def test_BV_M1_304(self):
		#Input: 0100110000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 304, "BV_M1", 100))

	def test_BV_M1_1003(self):
		#Input: 1111101011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 1003, "BV_M1", 100))

	def test_BV_M1_292(self):
		#Input: 0100100100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 292, "BV_M1", 100))

	def test_BV_M1_692(self):
		#Input: 1010110100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 692, "BV_M1", 100))

	def test_BV_M1_111(self):
		#Input: 0001101111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 111, "BV_M1", 100))

	def test_BV_M1_747(self):
		#Input: 1011101011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 747, "BV_M1", 100))

	def test_BV_M1_975(self):
		#Input: 1111001111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 975, "BV_M1", 100))

	def test_BV_M1_253(self):
		#Input: 0011111101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 253, "BV_M1", 100))

	def test_BV_M1_1020(self):
		#Input: 1111111100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 1020, "BV_M1", 100))

	def test_BV_M1_103(self):
		#Input: 0001100111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 103, "BV_M1", 100))

	def test_BV_M1_870(self):
		#Input: 1101100110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 870, "BV_M1", 100))

	def test_BV_M1_97(self):
		#Input: 0001100001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 97, "BV_M1", 100))

	def test_BV_M1_254(self):
		#Input: 0011111110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 254, "BV_M1", 100))

	def test_BV_M1_112(self):
		#Input: 0001110000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 112, "BV_M1", 100))

	def test_BV_M1_245(self):
		#Input: 0011110101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 245, "BV_M1", 100))

	def test_BV_M1_827(self):
		#Input: 1100111011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 827, "BV_M1", 100))

	def test_BV_M1_120(self):
		#Input: 0001111000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 120, "BV_M1", 100))

	def test_BV_M1_996(self):
		#Input: 1111100100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 996, "BV_M1", 100))

	def test_BV_M1_638(self):
		#Input: 1001111110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 638, "BV_M1", 100))

	def test_BV_M1_11(self):
		#Input: 0000001011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 11, "BV_M1", 100))

	def test_BV_M1_239(self):
		#Input: 0011101111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 239, "BV_M1", 100))

	def test_BV_M1_1015(self):
		#Input: 1111110111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 1015, "BV_M1", 100))

	def test_BV_M1_43(self):
		#Input: 0000101011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 43, "BV_M1", 100))

	def test_BV_M1_103(self):
		#Input: 0001100111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 103, "BV_M1", 100))

	def test_BV_M1_355(self):
		#Input: 0101100011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 355, "BV_M1", 100))

	def test_BV_M1_577(self):
		#Input: 1001000001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 577, "BV_M1", 100))

	def test_BV_M1_117(self):
		#Input: 0001110101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 117, "BV_M1", 100))

	def test_BV_M1_160(self):
		#Input: 0010100000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 160, "BV_M1", 100))

	def test_BV_M1_996(self):
		#Input: 1111100100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 996, "BV_M1", 100))

if __name__ == '__main__':
	unittest.main()