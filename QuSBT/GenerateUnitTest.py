import os
import sys

class GenerateUnitTest():

    @staticmethod
    def generateUnitTestClass(quantumProgram, inputID, outputID, num_qubit, inputs, input_str, times, program_folder, ROOT):
        str_list = []
        str_list.append("import unittest\n")
        str_list.append("import sys\n")
        str_list.append("sys.path.append(\""+program_folder+"\")\n")
        str_list.append("from testing import execute_quantum_program\n\nclass ")
        className = quantumProgram + "Test"
        str_list.append(className)
        str_list.append("(unittest.TestCase):\n\n")
        index = 0
        for i in inputs:
            str_list.append("\tdef test_")
            str_list.append(quantumProgram)
            str_list.append("_")
            str_list.append(str(i))
            str_list.append("(self):\n")
            str_list.append("\t\t")
            #execute_quantum_program(inputID, outputID, num_qubit, i, quantumProgram)
            str_list.append("#Input: ")
            str_list.append(input_str[index])
            str_list.append("\n")
            str_list.append("\t\t")
            str_list.append("print(execute_quantum_program(")
            str_list.append(str(inputID))
            str_list.append(", ")
            str_list.append(str(outputID))
            str_list.append(", ")
            str_list.append(str(num_qubit))
            str_list.append(", ")
            str_list.append(str(i))
            str_list.append(", \"")
            str_list.append(quantumProgram)
            str_list.append("\"")
            str_list.append(", ")
            str_list.append(str(times[index]))
            str_list.append("))\n\n")
            index += 1
        str_list.append("if __name__ == '__main__':\n\tunittest.main()")
        output = ''.join(str_list)
        fileName = className + ".py"

        resultFolder = 'generatedTestSuites'
        if not os.path.exists(sys.path[0]+ROOT+resultFolder):
            os.makedirs(sys.path[0]+ROOT+resultFolder)

        f = open(sys.path[0]+ROOT+resultFolder+ROOT+fileName, "w")
        f.write(output)
        f.close()

if __name__ == '__main__':
    GenerateUnitTest.generateUnitTestClass("MyQuantum", 2, 4, 11, [1, 2, 3], [100,200,300])
