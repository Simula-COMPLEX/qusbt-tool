import unittest
import sys
sys.path.append("D:\WXY\QuSBT_Exp\CE")
from testing import execute_quantum_program

class CE_M2Test(unittest.TestCase):

	def test_CE_M2_257(self):
		#Input: 0100000001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 257, "CE_M2", 400))

	def test_CE_M2_999(self):
		#Input: 1111100111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 999, "CE_M2", 400))

	def test_CE_M2_215(self):
		#Input: 0011010111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 215, "CE_M2", 400))

	def test_CE_M2_297(self):
		#Input: 0100101001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 297, "CE_M2", 400))

	def test_CE_M2_239(self):
		#Input: 0011101111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 239, "CE_M2", 400))

	def test_CE_M2_259(self):
		#Input: 0100000011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 259, "CE_M2", 400))

	def test_CE_M2_992(self):
		#Input: 1111100000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 992, "CE_M2", 400))

	def test_CE_M2_521(self):
		#Input: 1000001001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 521, "CE_M2", 400))

	def test_CE_M2_451(self):
		#Input: 0111000011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 451, "CE_M2", 400))

	def test_CE_M2_857(self):
		#Input: 1101011001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 857, "CE_M2", 400))

	def test_CE_M2_893(self):
		#Input: 1101111101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 893, "CE_M2", 400))

	def test_CE_M2_987(self):
		#Input: 1111011011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 987, "CE_M2", 400))

	def test_CE_M2_146(self):
		#Input: 0010010010
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 146, "CE_M2", 400))

	def test_CE_M2_910(self):
		#Input: 1110001110
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 910, "CE_M2", 400))

	def test_CE_M2_999(self):
		#Input: 1111100111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 999, "CE_M2", 400))

	def test_CE_M2_3(self):
		#Input: 0000000011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 3, "CE_M2", 400))

	def test_CE_M2_757(self):
		#Input: 1011110101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 757, "CE_M2", 400))

	def test_CE_M2_522(self):
		#Input: 1000001010
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 522, "CE_M2", 400))

	def test_CE_M2_904(self):
		#Input: 1110001000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 904, "CE_M2", 400))

	def test_CE_M2_507(self):
		#Input: 0111111011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 507, "CE_M2", 400))

	def test_CE_M2_297(self):
		#Input: 0100101001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 297, "CE_M2", 400))

	def test_CE_M2_154(self):
		#Input: 0010011010
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 154, "CE_M2", 400))

	def test_CE_M2_109(self):
		#Input: 0001101101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 109, "CE_M2", 400))

	def test_CE_M2_956(self):
		#Input: 1110111100
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 956, "CE_M2", 400))

	def test_CE_M2_369(self):
		#Input: 0101110001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 369, "CE_M2", 400))

	def test_CE_M2_776(self):
		#Input: 1100001000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 776, "CE_M2", 400))

	def test_CE_M2_867(self):
		#Input: 1101100011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 867, "CE_M2", 400))

	def test_CE_M2_1010(self):
		#Input: 1111110010
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 1010, "CE_M2", 400))

	def test_CE_M2_749(self):
		#Input: 1011101101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 749, "CE_M2", 400))

	def test_CE_M2_856(self):
		#Input: 1101011000
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 856, "CE_M2", 400))

	def test_CE_M2_452(self):
		#Input: 0111000100
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 452, "CE_M2", 400))

	def test_CE_M2_1005(self):
		#Input: 1111101101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 1005, "CE_M2", 400))

	def test_CE_M2_987(self):
		#Input: 1111011011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 987, "CE_M2", 400))

	def test_CE_M2_241(self):
		#Input: 0011110001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 241, "CE_M2", 400))

	def test_CE_M2_787(self):
		#Input: 1100010011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 787, "CE_M2", 400))

	def test_CE_M2_73(self):
		#Input: 0001001001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 73, "CE_M2", 400))

	def test_CE_M2_17(self):
		#Input: 0000010001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 17, "CE_M2", 400))

	def test_CE_M2_629(self):
		#Input: 1001110101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 629, "CE_M2", 400))

	def test_CE_M2_993(self):
		#Input: 1111100001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 993, "CE_M2", 400))

	def test_CE_M2_6(self):
		#Input: 0000000110
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 6, "CE_M2", 400))

	def test_CE_M2_231(self):
		#Input: 0011100111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 231, "CE_M2", 400))

	def test_CE_M2_857(self):
		#Input: 1101011001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 857, "CE_M2", 400))

	def test_CE_M2_852(self):
		#Input: 1101010100
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 852, "CE_M2", 400))

	def test_CE_M2_995(self):
		#Input: 1111100011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 995, "CE_M2", 400))

	def test_CE_M2_161(self):
		#Input: 0010100001
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 161, "CE_M2", 400))

	def test_CE_M2_450(self):
		#Input: 0111000010
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 450, "CE_M2", 400))

	def test_CE_M2_437(self):
		#Input: 0110110101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 437, "CE_M2", 400))

	def test_CE_M2_885(self):
		#Input: 1101110101
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 885, "CE_M2", 400))

	def test_CE_M2_627(self):
		#Input: 1001110011
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 627, "CE_M2", 400))

	def test_CE_M2_806(self):
		#Input: 1100100110
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 806, "CE_M2", 400))

	def test_CE_M2_415(self):
		#Input: 0110011111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 415, "CE_M2", 400))

	def test_CE_M2_279(self):
		#Input: 0100010111
		print(execute_quantum_program([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14, 279, "CE_M2", 400))

if __name__ == '__main__':
	unittest.main()