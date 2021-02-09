from evaluatexpression import evaluate

test_expression = ['( 1 + 2 )','( 1 + ( 2 * 3 ) )','( ( 1 * 2 ) + 3 )','( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )']
counter=0
for count in test_expression:
    print()
    counter=counter+1
    print('We are now in example number',counter, 'that has an expression of ',count)
    test_expression=count.split()
    result=(evaluate(test_expression))
    if(result.is_integer()==True):
        result=int(result)
    print('Result will be :',result)
    print()

