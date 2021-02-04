from CheckIfoperandisnumber import is_operand
from EvaluationFunction import evaluate
from Datapreprocessing import preprocess

#All trial values given for testing
Trial_values=['3','+ 1 2',' + 1 * 2 3','+ * 1 2 3','- / 10 + 1 1 * 1 2','- 0 3','/ 3 2']
counter=0
#For loop that tries out every value and print results
for count in Trial_values:
    print()
    counter=counter+1
    print('We are not in example number',counter, 'that has an expression of ',count)
    x=preprocess(count)
    result=evaluate(x)
    print('Result will be :',result)
    print()
