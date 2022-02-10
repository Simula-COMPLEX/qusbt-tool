import numpy as np
from jmetal.core.problem import IntegerProblem
from jmetal.core.solution import IntegerSolution

from testing import calculate_fail_number_GA

import math


class TestingProblem(IntegerProblem):
    def __init__(self, config_dic, solution_sheet, log_sheet):
        super(IntegerProblem).__init__()

        n = len(config_dic['inputID'])
        if 'M' in config_dic.keys():
            self.number_of_variables = config_dic['M']
        else:
            self.number_of_variables = math.ceil(pow(2, n) * config_dic['beta'])
        self.number_of_objectives = 1
        self.number_of_constraints = 0


        self.obj_directions = [self.MINIMIZE]

        self.lower_bound = self.number_of_variables * [0]

        self.upper_bound = self.number_of_variables * [pow(2,n)-1]

        self.config_dic = config_dic
        self.solution_sheet = solution_sheet
        self.log_sheet = log_sheet


    def evaluate(self, solution: IntegerSolution) -> IntegerSolution:
        variables = np.array(solution.variables)
        p = calculate_fail_number_GA(variables, self.config_dic, self.solution_sheet, self.log_sheet)
        # the value is negated because we want to maximize "p" using a minimization problem
        solution.objectives[0] = -p
        return solution

    def get_name(self) -> str:
        return 'TestingProblem'
