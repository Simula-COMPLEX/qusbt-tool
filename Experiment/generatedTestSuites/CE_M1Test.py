import unittest
import sys
sys.path.append("D:\WXY\QuSBT_Exp\CE")
from testing import execute_quantum_program

class CE_M1Test(unittest.TestCase):

	def test_CE_M1_537(self):
		#Input: 1000011001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 537, "CE_M1", 400))

	def test_CE_M1_984(self):
		#Input: 1111011000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 984, "CE_M1", 400))

	def test_CE_M1_511(self):
		#Input: 0111111111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 511, "CE_M1", 400))

	def test_CE_M1_519(self):
		#Input: 1000000111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 519, "CE_M1", 400))

	def test_CE_M1_149(self):
		#Input: 0010010101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 149, "CE_M1", 400))

	def test_CE_M1_48(self):
		#Input: 0000110000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 48, "CE_M1", 400))

	def test_CE_M1_799(self):
		#Input: 1100011111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 799, "CE_M1", 400))

	def test_CE_M1_710(self):
		#Input: 1011000110
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 710, "CE_M1", 400))

	def test_CE_M1_1002(self):
		#Input: 1111101010
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 1002, "CE_M1", 400))

	def test_CE_M1_707(self):
		#Input: 1011000011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 707, "CE_M1", 400))

	def test_CE_M1_699(self):
		#Input: 1010111011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 699, "CE_M1", 400))

	def test_CE_M1_681(self):
		#Input: 1010101001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 681, "CE_M1", 400))

	def test_CE_M1_317(self):
		#Input: 0100111101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 317, "CE_M1", 400))

	def test_CE_M1_1010(self):
		#Input: 1111110010
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 1010, "CE_M1", 400))

	def test_CE_M1_164(self):
		#Input: 0010100100
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 164, "CE_M1", 400))

	def test_CE_M1_244(self):
		#Input: 0011110100
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 244, "CE_M1", 400))

	def test_CE_M1_61(self):
		#Input: 0000111101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 61, "CE_M1", 400))

	def test_CE_M1_720(self):
		#Input: 1011010000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 720, "CE_M1", 400))

	def test_CE_M1_452(self):
		#Input: 0111000100
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 452, "CE_M1", 400))

	def test_CE_M1_175(self):
		#Input: 0010101111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 175, "CE_M1", 400))

	def test_CE_M1_373(self):
		#Input: 0101110101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 373, "CE_M1", 400))

	def test_CE_M1_915(self):
		#Input: 1110010011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 915, "CE_M1", 400))

	def test_CE_M1_878(self):
		#Input: 1101101110
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 878, "CE_M1", 400))

	def test_CE_M1_27(self):
		#Input: 0000011011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 27, "CE_M1", 400))

	def test_CE_M1_379(self):
		#Input: 0101111011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 379, "CE_M1", 400))

	def test_CE_M1_38(self):
		#Input: 0000100110
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 38, "CE_M1", 400))

	def test_CE_M1_395(self):
		#Input: 0110001011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 395, "CE_M1", 400))

	def test_CE_M1_979(self):
		#Input: 1111010011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 979, "CE_M1", 400))

	def test_CE_M1_340(self):
		#Input: 0101010100
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 340, "CE_M1", 400))

	def test_CE_M1_736(self):
		#Input: 1011100000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 736, "CE_M1", 400))

	def test_CE_M1_371(self):
		#Input: 0101110011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 371, "CE_M1", 400))

	def test_CE_M1_253(self):
		#Input: 0011111101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 253, "CE_M1", 400))

	def test_CE_M1_356(self):
		#Input: 0101100100
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 356, "CE_M1", 400))

	def test_CE_M1_760(self):
		#Input: 1011111000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 760, "CE_M1", 400))

	def test_CE_M1_716(self):
		#Input: 1011001100
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 716, "CE_M1", 400))

	def test_CE_M1_765(self):
		#Input: 1011111101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 765, "CE_M1", 400))

	def test_CE_M1_342(self):
		#Input: 0101010110
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 342, "CE_M1", 400))

	def test_CE_M1_279(self):
		#Input: 0100010111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 279, "CE_M1", 400))

	def test_CE_M1_365(self):
		#Input: 0101101101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 365, "CE_M1", 400))

	def test_CE_M1_326(self):
		#Input: 0101000110
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 326, "CE_M1", 400))

	def test_CE_M1_138(self):
		#Input: 0010001010
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 138, "CE_M1", 400))

	def test_CE_M1_1002(self):
		#Input: 1111101010
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 1002, "CE_M1", 400))

	def test_CE_M1_473(self):
		#Input: 0111011001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 473, "CE_M1", 400))

	def test_CE_M1_701(self):
		#Input: 1010111101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 701, "CE_M1", 400))

	def test_CE_M1_66(self):
		#Input: 0001000010
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 66, "CE_M1", 400))

	def test_CE_M1_640(self):
		#Input: 1010000000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 640, "CE_M1", 400))

	def test_CE_M1_987(self):
		#Input: 1111011011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 987, "CE_M1", 400))

	def test_CE_M1_728(self):
		#Input: 1011011000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 728, "CE_M1", 400))

	def test_CE_M1_424(self):
		#Input: 0110101000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 424, "CE_M1", 400))

	def test_CE_M1_610(self):
		#Input: 1001100010
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 610, "CE_M1", 400))

	def test_CE_M1_361(self):
		#Input: 0101101001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 361, "CE_M1", 400))

	def test_CE_M1_428(self):
		#Input: 0110101100
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 428, "CE_M1", 400))

if __name__ == '__main__':
	unittest.main()