import unittest
import sys
sys.path.append("D:\WXY\QuSBT_Exp\IQ")
from testing import execute_quantum_program

class IQ_M1Test(unittest.TestCase):

	def test_IQ_M1_491(self):
		#Input: 0111101011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 491, "IQ_M1", 102400))

	def test_IQ_M1_829(self):
		#Input: 1100111101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 829, "IQ_M1", 102400))

	def test_IQ_M1_755(self):
		#Input: 1011110011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 755, "IQ_M1", 102400))

	def test_IQ_M1_763(self):
		#Input: 1011111011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 763, "IQ_M1", 102400))

	def test_IQ_M1_621(self):
		#Input: 1001101101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 621, "IQ_M1", 102400))

	def test_IQ_M1_971(self):
		#Input: 1111001011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 971, "IQ_M1", 102400))

	def test_IQ_M1_595(self):
		#Input: 1001010011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 595, "IQ_M1", 102400))

	def test_IQ_M1_939(self):
		#Input: 1110101011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 939, "IQ_M1", 102400))

	def test_IQ_M1_809(self):
		#Input: 1100101001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 809, "IQ_M1", 102400))

	def test_IQ_M1_473(self):
		#Input: 0111011001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 473, "IQ_M1", 102400))

	def test_IQ_M1_442(self):
		#Input: 0110111010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 442, "IQ_M1", 102400))

	def test_IQ_M1_542(self):
		#Input: 1000011110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 542, "IQ_M1", 102400))

	def test_IQ_M1_127(self):
		#Input: 0001111111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 127, "IQ_M1", 102400))

	def test_IQ_M1_720(self):
		#Input: 1011010000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 720, "IQ_M1", 102400))

	def test_IQ_M1_768(self):
		#Input: 1100000000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 768, "IQ_M1", 102400))

	def test_IQ_M1_257(self):
		#Input: 0100000001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 257, "IQ_M1", 102400))

	def test_IQ_M1_957(self):
		#Input: 1110111101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 957, "IQ_M1", 102400))

	def test_IQ_M1_137(self):
		#Input: 0010001001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 137, "IQ_M1", 102400))

	def test_IQ_M1_732(self):
		#Input: 1011011100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 732, "IQ_M1", 102400))

	def test_IQ_M1_318(self):
		#Input: 0100111110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 318, "IQ_M1", 102400))

	def test_IQ_M1_520(self):
		#Input: 1000001000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 520, "IQ_M1", 102400))

	def test_IQ_M1_395(self):
		#Input: 0110001011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 395, "IQ_M1", 102400))

	def test_IQ_M1_3(self):
		#Input: 0000000011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 3, "IQ_M1", 102400))

	def test_IQ_M1_10(self):
		#Input: 0000001010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 10, "IQ_M1", 102400))

	def test_IQ_M1_359(self):
		#Input: 0101100111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 359, "IQ_M1", 102400))

	def test_IQ_M1_666(self):
		#Input: 1010011010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 666, "IQ_M1", 102400))

	def test_IQ_M1_318(self):
		#Input: 0100111110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 318, "IQ_M1", 102400))

	def test_IQ_M1_289(self):
		#Input: 0100100001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 289, "IQ_M1", 102400))

	def test_IQ_M1_676(self):
		#Input: 1010100100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 676, "IQ_M1", 102400))

	def test_IQ_M1_734(self):
		#Input: 1011011110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 734, "IQ_M1", 102400))

	def test_IQ_M1_255(self):
		#Input: 0011111111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 255, "IQ_M1", 102400))

	def test_IQ_M1_447(self):
		#Input: 0110111111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 447, "IQ_M1", 102400))

	def test_IQ_M1_853(self):
		#Input: 1101010101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 853, "IQ_M1", 102400))

	def test_IQ_M1_149(self):
		#Input: 0010010101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 149, "IQ_M1", 102400))

	def test_IQ_M1_901(self):
		#Input: 1110000101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 901, "IQ_M1", 102400))

	def test_IQ_M1_301(self):
		#Input: 0100101101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 301, "IQ_M1", 102400))

	def test_IQ_M1_509(self):
		#Input: 0111111101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 509, "IQ_M1", 102400))

	def test_IQ_M1_169(self):
		#Input: 0010101001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 169, "IQ_M1", 102400))

	def test_IQ_M1_783(self):
		#Input: 1100001111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 783, "IQ_M1", 102400))

	def test_IQ_M1_655(self):
		#Input: 1010001111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 655, "IQ_M1", 102400))

	def test_IQ_M1_362(self):
		#Input: 0101101010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 362, "IQ_M1", 102400))

	def test_IQ_M1_649(self):
		#Input: 1010001001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 649, "IQ_M1", 102400))

	def test_IQ_M1_863(self):
		#Input: 1101011111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 863, "IQ_M1", 102400))

	def test_IQ_M1_40(self):
		#Input: 0000101000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 40, "IQ_M1", 102400))

	def test_IQ_M1_619(self):
		#Input: 1001101011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 619, "IQ_M1", 102400))

	def test_IQ_M1_485(self):
		#Input: 0111100101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 485, "IQ_M1", 102400))

	def test_IQ_M1_697(self):
		#Input: 1010111001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 697, "IQ_M1", 102400))

	def test_IQ_M1_70(self):
		#Input: 0001000110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 70, "IQ_M1", 102400))

	def test_IQ_M1_580(self):
		#Input: 1001000100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 580, "IQ_M1", 102400))

	def test_IQ_M1_756(self):
		#Input: 1011110100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 756, "IQ_M1", 102400))

	def test_IQ_M1_266(self):
		#Input: 0100001010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 266, "IQ_M1", 102400))

	def test_IQ_M1_135(self):
		#Input: 0010000111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 135, "IQ_M1", 102400))

if __name__ == '__main__':
	unittest.main()