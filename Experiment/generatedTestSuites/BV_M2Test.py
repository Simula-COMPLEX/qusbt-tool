import unittest
import sys
sys.path.append("D:\WXY\QuSBT_Exp\BV")
from testing import execute_quantum_program

class BV_M2Test(unittest.TestCase):

	def test_BV_M2_683(self):
		#Input: 1010101011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 683, "BV_M2", 100))

	def test_BV_M2_49(self):
		#Input: 0000110001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 49, "BV_M2", 100))

	def test_BV_M2_988(self):
		#Input: 1111011100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 988, "BV_M2", 100))

	def test_BV_M2_41(self):
		#Input: 0000101001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 41, "BV_M2", 100))

	def test_BV_M2_565(self):
		#Input: 1000110101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 565, "BV_M2", 100))

	def test_BV_M2_790(self):
		#Input: 1100010110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 790, "BV_M2", 100))

	def test_BV_M2_699(self):
		#Input: 1010111011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 699, "BV_M2", 100))

	def test_BV_M2_241(self):
		#Input: 0011110001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 241, "BV_M2", 100))

	def test_BV_M2_504(self):
		#Input: 0111111000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 504, "BV_M2", 100))

	def test_BV_M2_280(self):
		#Input: 0100011000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 280, "BV_M2", 100))

	def test_BV_M2_739(self):
		#Input: 1011100011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 739, "BV_M2", 100))

	def test_BV_M2_416(self):
		#Input: 0110100000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 416, "BV_M2", 100))

	def test_BV_M2_399(self):
		#Input: 0110001111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 399, "BV_M2", 100))

	def test_BV_M2_613(self):
		#Input: 1001100101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 613, "BV_M2", 100))

	def test_BV_M2_189(self):
		#Input: 0010111101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 189, "BV_M2", 100))

	def test_BV_M2_1002(self):
		#Input: 1111101010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 1002, "BV_M2", 100))

	def test_BV_M2_958(self):
		#Input: 1110111110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 958, "BV_M2", 100))

	def test_BV_M2_498(self):
		#Input: 0111110010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 498, "BV_M2", 100))

	def test_BV_M2_894(self):
		#Input: 1101111110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 894, "BV_M2", 100))

	def test_BV_M2_755(self):
		#Input: 1011110011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 755, "BV_M2", 100))

	def test_BV_M2_434(self):
		#Input: 0110110010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 434, "BV_M2", 100))

	def test_BV_M2_693(self):
		#Input: 1010110101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 693, "BV_M2", 100))

	def test_BV_M2_583(self):
		#Input: 1001000111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 583, "BV_M2", 100))

	def test_BV_M2_117(self):
		#Input: 0001110101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 117, "BV_M2", 100))

	def test_BV_M2_492(self):
		#Input: 0111101100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 492, "BV_M2", 100))

	def test_BV_M2_810(self):
		#Input: 1100101010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 810, "BV_M2", 100))

	def test_BV_M2_814(self):
		#Input: 1100101110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 814, "BV_M2", 100))

	def test_BV_M2_138(self):
		#Input: 0010001010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 138, "BV_M2", 100))

	def test_BV_M2_434(self):
		#Input: 0110110010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 434, "BV_M2", 100))

	def test_BV_M2_241(self):
		#Input: 0011110001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 241, "BV_M2", 100))

	def test_BV_M2_561(self):
		#Input: 1000110001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 561, "BV_M2", 100))

	def test_BV_M2_127(self):
		#Input: 0001111111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 127, "BV_M2", 100))

	def test_BV_M2_872(self):
		#Input: 1101101000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 872, "BV_M2", 100))

	def test_BV_M2_378(self):
		#Input: 0101111010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 378, "BV_M2", 100))

	def test_BV_M2_830(self):
		#Input: 1100111110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 830, "BV_M2", 100))

	def test_BV_M2_880(self):
		#Input: 1101110000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 880, "BV_M2", 100))

	def test_BV_M2_725(self):
		#Input: 1011010101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 725, "BV_M2", 100))

	def test_BV_M2_292(self):
		#Input: 0100100100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 292, "BV_M2", 100))

	def test_BV_M2_737(self):
		#Input: 1011100001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 737, "BV_M2", 100))

	def test_BV_M2_876(self):
		#Input: 1101101100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 876, "BV_M2", 100))

	def test_BV_M2_161(self):
		#Input: 0010100001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 161, "BV_M2", 100))

	def test_BV_M2_101(self):
		#Input: 0001100101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 101, "BV_M2", 100))

	def test_BV_M2_304(self):
		#Input: 0100110000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 304, "BV_M2", 100))

	def test_BV_M2_894(self):
		#Input: 1101111110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 894, "BV_M2", 100))

	def test_BV_M2_303(self):
		#Input: 0100101111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 303, "BV_M2", 100))

	def test_BV_M2_379(self):
		#Input: 0101111011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 379, "BV_M2", 100))

	def test_BV_M2_737(self):
		#Input: 1011100001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 737, "BV_M2", 100))

	def test_BV_M2_175(self):
		#Input: 0010101111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 175, "BV_M2", 100))

	def test_BV_M2_622(self):
		#Input: 1001101110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 622, "BV_M2", 100))

	def test_BV_M2_569(self):
		#Input: 1000111001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 569, "BV_M2", 100))

	def test_BV_M2_540(self):
		#Input: 1000011100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 540, "BV_M2", 100))

	def test_BV_M2_450(self):
		#Input: 0111000010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20, 450, "BV_M2", 100))

if __name__ == '__main__':
	unittest.main()