from evaluatexpression import evaluate
test_expression = input("Please enter expression seperated by paranthesis :")
test_expression=test_expression.split()
result=(evaluate(test_expression))
if(result.is_integer()==True):
    result=int(result)
print(result)