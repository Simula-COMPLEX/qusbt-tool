from search_method import Search
import time
import os
import configparser
import shutil
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])

if sys.platform.startswith('win32'):
    ROOT='\\'
elif sys.platform.startswith('linux'):
    ROOT='/'
elif sys.platform.startswith('darwin'):
    ROOT='/'
def user_input():
    print('\n')
    text1 = "1. Check the template of the configuration file.(.ini file)"
    print(text1)
    print("\n")
    text2 = "2. Check the example of the configuration file.(.ini file)"
    print(text2)
    print('\n')
    text3 = "3. Upload your configuration.(.ini file)"
    print(text3)
    print('\n')
    text4 = "4. Exit."
    print(text4)
    print('\n')
    print("Your choice?[1/2/3/4]",end=' ')
    user_choice = input()
    print('\n')
    return user_choice

def template_file():
    print("The template is shown below:")
    program = '''
[program]
root= 
;(Required)
;Description: The absolute root of your quantum program file.
num_qubit= 
;(Required)
;Description: The total number of qubit of your quantum program.
inputID= 
;(Required)
;Description: The IDs of input qubits.
;Format: A non-repeating sequence separated by commas.
outputID= 
;(Required)
;Description: The IDs of output qubits which are the qubits to be measured.
;Format: A non-repeating sequence separated by commas.
    '''
    qusbt_configuration = '''
[qusbt_configuration]
beta=
;(Optional)
;Description: The percentage of possible inputs as the number of test cases in a test suite.
M=
;(Optional)
;Description: The number of test cases in a test suite.
;Attention: You should use either 'beta' or 'M'. We use 'beta' as 0.05 by default.
'''
    GA_parameter = '''
[GA_parameter]
population_size= 
;(Optional) 
;Description: The population size in GA, population_size=10 by default.
offspring_population_size= 
;(Optional)
;Description: The offspring population size in GA, offspring_population_size=10 by default.
max_evaluations=
;(Optional)
;Description: The maximum evaluations in GA, max_evaluations=500 by default.
mutation_probability=
;(Optional)
;Description: mutation probability in GA, mutation_probability=1.0/M, 'M' is the size of a test suite by default.
mutation_distribution_index=
;(Optional)
;Description: mutation distribution in GA, mutation_distribution_index=20 by default.
crossover_probability=
;(Optional)
;Description: crossover probability in GA, crossover_probability=0.9 by default.
crossover_distribution_index=
;(Optional)
;Description: crossover probability in GA, crossover_distribution_index=20 by default.
'''
    program_specification = '''
[program_specification]
;Description: The program specification.
;Format:input string (binary),output string (binary)=probability
;Example:
;00,1=0.5
;00,0=0.5
;01,1=0.5
;01,0=0.5
;or
;0-,-=0.5
;Attention: '-' can refer to both '0' and '1'.
'''
    print(program)
    print(qusbt_configuration)
    print(GA_parameter)
    print(program_specification)
    print('\n')

def example_file():
    print("The example is shown below:")
    example = '''
[program]
root=C:\IQ.py
num_qubit=10
inputID=0,1,2,3,4,5,6,7,8,9
outputID=0,1,2,3,4,5,6,7,8,9

[qusbt_configuration]
beta=0.05
confidence_level=0.01

[GA_parameter]
population_size=10
offspring_population_size=10
max_evaluations=500  

[program_specification]
----------,----------=0.0009765625
'''
    print(example)

def dec2bin(value, n):
    a = 1
    list = []
    while a > 0:
        a, b = divmod(value, 2)
        list.append(str(b))
        value = a
    s = ""
    for i in range(len(list) - 1, -1, -1):
        s += str(list[i])
    s = s.zfill(n)
    return s

def expand_ps(ps,inputID,outputID):#check and expand
    flag = True
    for i in range(len(ps)):
        pair = ps[i][0].split(',')
        if len(pair[0]) != len(inputID) or len(pair[1]) != len(outputID):

            flag = False
            break
        for j in range(len(inputID)):
            if ps[i][0][j] != '0' and ps[i][0][j] != '1' and ps[i][0][j] != '-':
                flag = False
        for j in range(len(inputID)+1, len(inputID) + len(outputID) + 1):
            if ps[i][0][j] != '0' and ps[i][0][j] != '1' and ps[i][0][j] != '-':
                flag = False
    if flag == False:
        print("Error: The format of the program specification is wrong.")
        print("Example: 00-1,01=0.5")
        end_running()
    else:
        l = len(inputID) + len(outputID) + 1
        length_origin = len(ps)
        items = []
        ps_new = []

        for i in range(length_origin):
            if ps[i][0].find('-',0,len(ps[i][0])) != -1:
                mark = []
                item = ps[i]
                items.append(item)
                for j in range(l):
                    if ps[i][0][j] == '-':
                        mark.append(j)
                for j in range(pow(2,len(mark))):
                    t=dec2bin(j,len(mark))
                    temp = list(item[0])
                    for k in range(len(mark)):
                        temp[mark[k]] = t[k]
                    temp = ''.join(temp)
                    temp_item = (temp,item[1])
                    ps_new.append(temp_item)
        if len(items) == 0:
            return ps
        else:
            for i in range(len(items)):
                ps.remove(items[i])
            ps += ps_new
            return ps

def check_configuration_file(config):
    if config.has_section('program') == False:
        print("Error: QuSBT cannot find section 'program' in this configuration file.")
        end_running()
    else:
        if config.has_option('program', 'root') == False:
            print("Error: QuSBT cannot find the root of the quantum program file.")
            end_running()
        if config.has_option('program', 'num_qubit') == False:
            print("Error: QuSBT cannot find the number of qubits of the program.")
            end_running()
        if config.has_option('program', 'inputID') == False:
            print("Error: QuSBT cannot find the input IDs of the program.")
            end_running()
        if config.has_option('program', 'outputID') == False:
            print("Error: QuSBT cannot find the output IDs of the program.")
            end_running()

    if config.has_section('program_specification') == False:
        print("Error: QuSBT cannot find section 'program_spacification' in this configuration file.")
        end_running()



def check_unique(l):
    return len(l) == len(set(l))

def check_unique_pair(ps):
    pair = []
    for i in range(len(ps)):
        pair.append(ps[i][0])
    return len(pair) == len(set(pair))

def check_inputID_outputID(num_qubit, inputID, outputID):
    if check_unique(inputID) == False:
        print("Wrong format of 'inputID'.")
        end_running()
    if check_unique(outputID) == False:
        print("Wrong format of 'outputID'.")
        end_running()
    try:
        inputID = [int(i) for i in inputID]
    except:
        print("Wrong format of 'inputID'.")
        end_running()
    try:
        outputID = [int(i) for i in outputID]
    except:
        print("Wrong format of 'outputID'.")
        end_running()
    inputID.sort()
    outputID.sort()

    if int(inputID[-1]) > num_qubit - 1:#the last one
        print("Wrong input IDs")
        end_running()
    if int(inputID[-1]) > num_qubit - 1:
        print("Wrong output IDs")
        end_running()

    return inputID, outputID

def check_bin(bin_str, n):
    if len(bin_str) != n:
        print("Error: The format of the program specification is wrong.")
        end_running()
   # print("check bin: "+str(bin_str))
    for i in range(len(bin_str)):
        if bin_str[i] != '0' and bin_str[i] != '1':
            print("Error: The format of the program specification is wrong.")
            end_running()

def input_group(valid_input):
    index = [] #unique input index
    index_flag = valid_input[0]
    index.append(0)
    for i in range(1,len(valid_input)):
        if valid_input[i] != index_flag:
            index.append(i)
            index_flag = valid_input[i]
    return index

def check_full_ps(valid_input, p):
    index = input_group(valid_input)
    p_sum = 0
    for i in range(len(index)):
        start = index[i]
        if i == len(index) - 1:
            end = len(valid_input)
        else:
            end = index[i+1]
        for j in range(start,end):
            p_sum += p[j]
        if p_sum != 1:
            print("Error: This is not a complete program specification.")
            end_running()
        else:
            p_sum = 0

def end_running():
    exit()

if __name__ == '__main__':
    # warnings.filterwarnings('ignore')
    print("".center(60,"="))
    print('\n')
    print("Welcome to QuSBT".center(60))
    print('\n')
    print("".center(60,"="))
    user_choice = user_input()
    while user_choice != '3' and user_choice != '4':
        if user_choice != '1' and user_choice != '2' and user_choice != '4':
            print("Error: Please type in '1', '2', '3' or '4'.")
            user_choice = user_input()
        elif user_choice == '1':
            template_file()
            user_choice = user_input()
        elif user_choice == '2':
            example_file()
            user_choice = user_input()
    if user_choice == '3':
        print("please enter the root of your configuration file.(.ini file)")

        #get configuration file
        root_con_string = input()
        root_con = root_con_string
        START = time.time()

        if os.path.isfile(root_con) == True:
            config = configparser.ConfigParser(allow_no_value=True)
            config.read(root_con, encoding='utf-8')
        else:
            print("Error: QuSBT cannot find the configuration file.")
            end_running()

        check_configuration_file(config)

        # get quantum program
        root = config.get('program', 'root')
        if os.path.isfile(root) != True:
            print("Error: QuSBT cannot find the quantum program file.")
            end_running()

        root_list = root.split(ROOT)
        program_file = root_list[len(root_list) - 1]
        program_folder = root_list[:len(root_list) - 1]
        program_folder = ROOT.join(str(i) for i in program_folder)
        sys.path.append(program_folder)
        # print(program_file.split('.')[0])
        module_name = program_file.split('.')[0]

        # get inputID, outputID and numner of qubits
        try:
            num_qubit = int(config.get('program', 'num_qubit'))
        except:
            print("Error: The data type of 'num_qubit' should be an Integer")
            end_running()
        inputID_o = config.get('program', 'inputID').split(',')
        outputID_o = config.get('program', 'outputID').split(',')
        inputID, outputID = check_inputID_outputID(num_qubit, inputID_o, outputID_o)

        population_size = 10
        offspring_population_size = 10
        max_evaluations = 500
        if config.get('GA_parameter', 'population_size') != None:
            try:
                population_size = int(config.get('GA_parameter', 'population_size'))
            except:
                print("Error: The data type of 'population_size' should be an Integer")
                end_running()
        if config.get('GA_parameter', 'offspring_population_size') != None:
            try:
                offspring_population_size = int(config.get('GA_parameter', 'offspring_population_size'))
            except:
                print("Error: The data type of 'off_population_size' should be an Integer")
                end_running()

        if config.get('GA_parameter', 'max_evaluations') != None:
            try:
                max_evaluations = int(config.get('GA_parameter', 'max_evaluations'))
            except:
                print("Error: The data type of 'max_evaluations' should be an Integer")
                end_running()

        if os.path.isfile(root) != True:
            print("Error: QuSBT cannot find the quantum program file.")
            end_running()

        M_flag = False
        beta = 0
        if config.has_option('qusbt_configuration','M') == True:
            M_flag == True
            try:
                M = int(config.get('qusbt_configuration','M'))
            except:
                print("Error: The data type of 'M' should be an Integer.")
                end_running()
            if config.has_option('qusbt_configuration', 'beta') == True:
                print("Error: You should use either 'M' or 'beta'.")
                end_running()
        elif config.has_option('qusbt_configuration','beta') == True:
            try:
                beta = float(config.get('qusbt_configuration','beta'))
            except:
                print("Error: The data type of 'beta' should be a Float.")
                end_running()
        else:
            beta = 0.05

        confidence_level = 0.01
        if config.has_option('qusbt_configuration', 'confidence_level') == True:
            try:
                confidence_level = float(config.get('qusbt_configuration', 'confidence_level'))
            except:
                print("Error: The data type of 'confidence_level' should be a Float.")
                end_running()

        mutation_probability_flag = False
        if config.has_option('GA_configuration', 'mutation_probability') == True:
            mutation_probability_flag = True
            try:
                mutation_probability = float(config.get('GA_configuration', 'crossover_probability'))
            except:
                print("Error: The data type of 'mutation_probability' should be a Float.")
                end_running()
            if mutation_probability >= 1:
                print("Error: The value of 'mutation_probability' should be a Float smaller than 1.0.")
                end_running()

        mutation_distribution_index = 20
        if config.has_option('GA_configuration', 'mutation_distribution_index') == True:
            try:
                mutation_distribution_index = int(config.get('GA_configuration', 'mutation_distribution_index'))
            except:
                print("Error: The data type of 'mutation_distribution_index' should be an Integer.")
                end_running()

        crossover_distribution_index = 20
        if config.has_option('GA_configuration', 'crossover_distribution_index') == True:
            try:
                crossover_distribution_index = int(config.get('GA_configuration', 'crossover_distribution_index'))
            except:
                print("Error: The data type of 'crossover_distribution_index' should be an Integer.")
                end_running()

        crossover_probability = 0.9
        if config.has_option('GA_configuration', 'crossover_probability') == True:
            try:
                crossover_probability = float(config.get('GA_configuration', 'crossover_probability'))
            except:
                print("Error: The data type of 'crossover_probability' should be a Float.")
                end_running()
            if crossover_probability >= 1:
                print("Error: The value of 'crossover_probability' should be a Float smaller than 1.0.")
                end_running()


        #PS
        valid_input = []
        valid_output = []
        p = []
        ps = config.items('program_specification')
        ps = expand_ps(ps, inputID, outputID)

        # print(ps)
        #print("origin:"+str(ps))
        if check_unique_pair(ps) == False:
            print("There are duplicate input-output pairs in the program specification.")
            end_running()
        #sort PS according to input and output
        ps.sort(key=lambda x:x[0])
        #print("new:"+str(ps))
        for i in range(len(ps)):
            valid_input_item = ps[i][0][:len(inputID)]
            valid_output_item = ps[i][0][len(inputID)+1:]
            check_bin(valid_input_item,len(inputID))
            check_bin(valid_output_item,len(outputID))
            valid_input.append(valid_input_item)
            valid_output.append(valid_output_item)
            p.append(float(ps[i][1]))
        check_full_ps(valid_input, p)

        config_dic = {}
        config_dic['program_folder'] = program_folder
        config_dic['root'] = root_con_string
        config_dic['module_name'] = module_name
        config_dic['num_qubit'] = num_qubit
        config_dic['inputID'] = inputID
        config_dic['outputID'] = outputID
        if M_flag == True:
            config_dic['M'] = M
        else:
            config_dic['beta'] = beta
        config_dic['confidence_level'] = confidence_level
        config_dic['population_size'] = population_size
        config_dic['offspring_population_size'] = offspring_population_size
        config_dic['max_evaluations'] = max_evaluations
        config_dic['valid_input'] = valid_input
        config_dic['valid_output'] = valid_output
        config_dic['p'] = p
        config_dic['crossover_probability'] = crossover_probability
        config_dic['crossover_distribution_index'] = crossover_distribution_index
        if mutation_probability_flag == True:
            config_dic['mutation_probability'] = mutation_probability
        config_dic['mutation_distribution_index'] = mutation_distribution_index
        Search.search(config_dic)
        # Search.search(root, module_name, alg, len(inputID), beta)
        END = time.time()
        T1 = END-START

    elif user_choice == '4':
        print("Exit :D")
