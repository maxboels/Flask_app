from CheckIfoperandisnumber import is_operand
from EvaluationFunction import evaluate
from Datapreprocessing import preprocess

x=input("Please Enter expression to be evaluated :")
print(x)
x=preprocess(x)
result=evaluate(x)
print(result)
