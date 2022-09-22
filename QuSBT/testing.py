from qiskit import (
    #IBMQ,
    QuantumCircuit,
    QuantumRegister,
    ClassicalRegister,
    execute,
    Aer,
)

import collections

import importlib

import numpy as np
import rpy2.robjects as robjects
import os
import pandas as pd
import time
import swap


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


def wrong_output(i, right_output):
    set_output = set(right_output)
    if i not in set_output:
        return True  # existing wrong output
    return False

def execute_quantum_program(inputID, outputID, num_qubit, i, module_name, times): #module_name is the name of the quantum program file
    q = QuantumRegister(num_qubit)
    c = ClassicalRegister(len(outputID))
    qc = QuantumCircuit(q, c)
    i = dec2bin(i, len(inputID)) # Turning one integer into binary number
    for j in range(len(inputID)):
        if i[len(inputID) - 1 - j] == '1':
            qc.x(inputID[j])
    module = importlib.import_module(module_name)
    run_method = getattr(module,"run")
    run_method(qc)
    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=times).result().get_counts(qc)
    return result

def check_WOO(i, o, valid_inputs, valid_outputs):
    flag = False
    for k in range(len(valid_inputs)):
        if valid_inputs[k] == i and valid_outputs[k] == o:
            flag = True
    if flag == False:
        return False
    return True


def process_bar(percent, start_str='', end_str='', total_length=0):
    bar = ''.join(['#'] * int(percent * total_length)) + ''
    bar = '\r' + start_str + bar.ljust(total_length) + ' {:0>4.1f}%|'.format(percent*100) + end_str
    print(bar, end='', flush=True)

def calculate_fail_number_GA(input, config_dic, solution_sheet, log_sheet):
    count_fail = 0  # the number that fails the test
    pvalue = []
    global f
    valid_input = config_dic['valid_input']
    valid_output = config_dic['valid_output']
    pt = config_dic['p']
    inputs_str = []
    test_results = []


    for i in input:  # fix
        flag_wrong = False  # have wrong outputs
        fre = []  # counts of expected outputs
        p = []  # possibility of expected outputs
        outputs = []

        count_times = 0
        right_output = []
        i_str = dec2bin(i, len(config_dic['inputID']))
        inputs_str.append(i_str)
        for j in range(len(valid_input)):
            if valid_input[j] == i_str and pt[j] > 0: # finding valid outputs and probability of the input
                right_output.append(valid_output[j])
                p.append(pt[j])
                outputs.append(valid_output[j])
                count_times += 1

        # calculate outputs

        ##
        start = time.time()
        temp = execute_quantum_program(config_dic['inputID'], config_dic['outputID'], config_dic['num_qubit'], i, config_dic['module_name'], count_times*100)
        end = time.time()

        exe_time = solution_sheet['B4'].value + end - start

        solution_sheet['B4'] = exe_time

        # judge wrong outputs
        for key in list(temp.keys()):
            if key not in right_output:
                flag_wrong = True


        # chi test
        if flag_wrong == False:  # no wrong output
            if count_times == 1:  # only one output
                pvalue.append(1)
            else:
                for j_s in outputs:
                    if j_s in temp:
                        fre.append(temp[j_s])
                    else:
                        fre.append(0)
                p = np.array(p)
                fre = np.array(fre)
                p = robjects.FloatVector(p)
                fre = robjects.FloatVector(fre)
                robjects.r('''
                    chitest<-function(observed,theoretical){
                        test_result <- chisq.test(x = observed,p = theoretical)
                        pvalue = test_result$p.value
                        return (pvalue)
                    }''')
                t = robjects.r['chitest'](fre, p)
                pvalue.append(t[0])
        else:
            pvalue.append(0)

        if pvalue[-1] < 0.01:
            count_fail += 1
            if flag_wrong == False:
                test_result = 'wodf'
            else:
                test_result = 'uof'
        else:
            test_result = 'pass'
        test_results.append(test_result)


    count_fail_list = [count_fail]
    count_fail = np.array(count_fail_list)


    inputs_str.insert(0,'value of inputs')
    test_results.insert(0,'test results')
    count_fail_list.insert(0,'number of failing inputs')
    log_sheet.append(inputs_str)
    log_sheet.append(test_results)
    log_sheet.append(count_fail_list)
    process_bar((log_sheet.max_row / 3) / config_dic['max_evaluations'], start_str='', end_str='100%', total_length=30)

    return count_fail

