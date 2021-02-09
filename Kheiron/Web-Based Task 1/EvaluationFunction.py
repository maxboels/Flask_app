from CheckIfoperandisnumber import is_operand
class operation:
    def __init__(self,o1,o2,sign):
        self.o1 = o1
        self.o2 = o2
        self.sign = sign
    def operation(self):
      if self.sign == '+':
        result = self.o1 + self.o2
        return result
      elif  self.sign == '-':
        result = self.o1 - self.o2
        return result 
      elif  self.sign == '*':
        result =  self.o1 *  self.o2
        return result
      elif  self.sign == '/':
        result =  self.o1 /  self.o2
        return result
#Evaluation
def evaluate(expression): 
    stack = [] 
    # iterate over the string in reverse order 
    for character in expression[::-1]: 
        # push operand to stack 
        if is_operand(character): 
            stack.append(int(character)) 
        else: 
            # pop values from stack can calculate the result 
            # push the result onto the stack again 
            temp_value=[]
            o1 = stack.pop() 
            o2 = stack.pop() 
            P1=operation(o1,o2,character)
            result = P1.operation()
            stack.append(result) 
    return stack.pop() 

