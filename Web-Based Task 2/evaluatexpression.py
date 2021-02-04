from Applyoperation import applyOp
from FindOperatorPrecedence import precedence
def evaluate(tokens):
    values = []
    ops = []
    i = 0
    while i < len(tokens):
        #Check the token if it is whitespace move one
        if tokens[i] == ' ':
            i += 1
            continue
        #append paranthesis to beginning of operand
        elif tokens[i] == '(':
            ops.append(tokens[i])
        #Check if it is a digit
        elif tokens[i].isdigit():
            val = 0
            while (i < len(tokens) and  tokens[i].isdigit()):
                val = (val * 10) + float(tokens[i])
                i += 1
            values.append(val)
            i-=1
        #check in case of closing paranthesis
        elif tokens[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(applyOp(val1, val2, op))
            ops.pop()
        else:
            #perform operation in while loop
            while (len(ops) != 0 and
                precedence(ops[-1]) >=
                   precedence(tokens[i])):    
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(applyOp(val1, val2, op))
            ops.append(tokens[i])
        i += 1
    #Perform operation on the final output
    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()    
        values.append(applyOp(val1, val2, op))
    return values[-1]