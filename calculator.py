from ast import parse
import sys
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

# expression = 

def sol_equation(lhs,rhs,variable):
    lhs = parse_expr(lhs)
    rhs = parse_expr(rhs)
    return solve(lhs-rhs)[0]

def sol(expression):
    return parse_expr(expression)


# def calculator(expression):

# expression_list = []
try:

    expression = sys.argv[1]
    if '=' in expression:
        #solve equation
        lhs = expression.split('=')[0]
        rhs = expression.split('=')[1]
        variable =''.join(filter(str.isalpha, expression))[0]
        print(sol_equation(lhs,rhs,variable))
    else:
        print(sol(expression))
    # print(expression)
    # for ele in expression.split(' '):
    #     expression_list.append(ele)
    # print(ast.parse(expression, mode='eval').body)
    # # print('The result is: ' + str(eval(expression)))
except IndexError:
    print('Please enter the expression to evaluate. Missing argument!!!')
    