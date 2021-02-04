#Import different modules to be used in our code
from evaluatexpression import evaluate
#Take input from user
test_expression = input("Please enter expression seperated by paranthesis :")
#Split the expression
test_expression=test_expression.split()
#Perform Evaluate function
result=(evaluate(test_expression))
if(result.is_integer()==True):
    result=int(result)
print(result)