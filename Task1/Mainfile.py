#Import different modules to be used in our code
from CheckIfoperandisnumber import is_operand
from EvaluationFunction import evaluate
from Datapreprocessing import preprocess
#Take input from user
x=input("Please Enter expression to be evaluated :")
#Perform preprocess function
x=preprocess(x)
#Perform Evaluate function
result=evaluate(x)
print(result)

