import unittest
import sys
sys.path.append("D:\WXY\QuSBT_Exp\AS")
from testing import execute_quantum_program

class AS_M1Test(unittest.TestCase):

	def test_AS_M1_65(self):
		#Input: 0001000001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 65, "AS_M1", 400))

	def test_AS_M1_255(self):
		#Input: 0011111111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 255, "AS_M1", 400))

	def test_AS_M1_364(self):
		#Input: 0101101100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 364, "AS_M1", 400))

	def test_AS_M1_684(self):
		#Input: 1010101100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 684, "AS_M1", 400))

	def test_AS_M1_247(self):
		#Input: 0011110111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 247, "AS_M1", 400))

	def test_AS_M1_8(self):
		#Input: 0000001000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 8, "AS_M1", 400))

	def test_AS_M1_890(self):
		#Input: 1101111010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 890, "AS_M1", 400))

	def test_AS_M1_284(self):
		#Input: 0100011100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 284, "AS_M1", 400))

	def test_AS_M1_528(self):
		#Input: 1000010000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 528, "AS_M1", 400))

	def test_AS_M1_998(self):
		#Input: 1111100110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 998, "AS_M1", 400))

	def test_AS_M1_104(self):
		#Input: 0001101000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 104, "AS_M1", 400))

	def test_AS_M1_339(self):
		#Input: 0101010011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 339, "AS_M1", 400))

	def test_AS_M1_31(self):
		#Input: 0000011111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 31, "AS_M1", 400))

	def test_AS_M1_318(self):
		#Input: 0100111110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 318, "AS_M1", 400))

	def test_AS_M1_887(self):
		#Input: 1101110111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 887, "AS_M1", 400))

	def test_AS_M1_541(self):
		#Input: 1000011101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 541, "AS_M1", 400))

	def test_AS_M1_237(self):
		#Input: 0011101101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 237, "AS_M1", 400))

	def test_AS_M1_770(self):
		#Input: 1100000010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 770, "AS_M1", 400))

	def test_AS_M1_71(self):
		#Input: 0001000111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 71, "AS_M1", 400))

	def test_AS_M1_285(self):
		#Input: 0100011101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 285, "AS_M1", 400))

	def test_AS_M1_200(self):
		#Input: 0011001000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 200, "AS_M1", 400))

	def test_AS_M1_529(self):
		#Input: 1000010001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 529, "AS_M1", 400))

	def test_AS_M1_647(self):
		#Input: 1010000111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 647, "AS_M1", 400))

	def test_AS_M1_257(self):
		#Input: 0100000001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 257, "AS_M1", 400))

	def test_AS_M1_973(self):
		#Input: 1111001101
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 973, "AS_M1", 400))

	def test_AS_M1_233(self):
		#Input: 0011101001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 233, "AS_M1", 400))

	def test_AS_M1_9(self):
		#Input: 0000001001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 9, "AS_M1", 400))

	def test_AS_M1_376(self):
		#Input: 0101111000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 376, "AS_M1", 400))

	def test_AS_M1_73(self):
		#Input: 0001001001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 73, "AS_M1", 400))

	def test_AS_M1_214(self):
		#Input: 0011010110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 214, "AS_M1", 400))

	def test_AS_M1_228(self):
		#Input: 0011100100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 228, "AS_M1", 400))

	def test_AS_M1_219(self):
		#Input: 0011011011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 219, "AS_M1", 400))

	def test_AS_M1_744(self):
		#Input: 1011101000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 744, "AS_M1", 400))

	def test_AS_M1_123(self):
		#Input: 0001111011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 123, "AS_M1", 400))

	def test_AS_M1_67(self):
		#Input: 0001000011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 67, "AS_M1", 400))

	def test_AS_M1_651(self):
		#Input: 1010001011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 651, "AS_M1", 400))

	def test_AS_M1_863(self):
		#Input: 1101011111
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 863, "AS_M1", 400))

	def test_AS_M1_662(self):
		#Input: 1010010110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 662, "AS_M1", 400))

	def test_AS_M1_978(self):
		#Input: 1111010010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 978, "AS_M1", 400))

	def test_AS_M1_218(self):
		#Input: 0011011010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 218, "AS_M1", 400))

	def test_AS_M1_76(self):
		#Input: 0001001100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 76, "AS_M1", 400))

	def test_AS_M1_764(self):
		#Input: 1011111100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 764, "AS_M1", 400))

	def test_AS_M1_482(self):
		#Input: 0111100010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 482, "AS_M1", 400))

	def test_AS_M1_354(self):
		#Input: 0101100010
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 354, "AS_M1", 400))

	def test_AS_M1_377(self):
		#Input: 0101111001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 377, "AS_M1", 400))

	def test_AS_M1_680(self):
		#Input: 1010101000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 680, "AS_M1", 400))

	def test_AS_M1_500(self):
		#Input: 0111110100
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 500, "AS_M1", 400))

	def test_AS_M1_390(self):
		#Input: 0110000110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 390, "AS_M1", 400))

	def test_AS_M1_955(self):
		#Input: 1110111011
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 955, "AS_M1", 400))

	def test_AS_M1_313(self):
		#Input: 0100111001
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 313, "AS_M1", 400))

	def test_AS_M1_368(self):
		#Input: 0101110000
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 368, "AS_M1", 400))

	def test_AS_M1_30(self):
		#Input: 0000011110
		print(execute_quantum_program([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 12, 30, "AS_M1", 400))

if __name__ == '__main__':
	unittest.main()