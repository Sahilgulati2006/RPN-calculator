# class StackCalc: a class that extends (inherit) the functionalities
#  of the class Stack 

from select import kqueue
from Stack import *
import copy
import numpy as np # if you need sin, just do np.sin, etc.
from Queue import *

class StackCalc(Stack):    
    def __init__(self):        
      super().__init__()
      
  
    def rpnCommand(self,command):
      try:
         
        if command in {'+','-','*','^','/'}:
          self._arithematic(command)
          
        elif command in {'sin','cos','exp','log','abs','sqrt'}:
          self._function(command)
        elif command in {'pi','e'}:
          self._constant(command)
        elif command == 'swap':
          self.swap()
        elif command == 'copy':
          self.copy()
        elif command == 'flush':
          self.flush()
        else:
          return self.push(float(command))   #Try to push a numeric value on to the stack
          
      except ValueError:
        print(f"Invalid command: {command}")    #To handle invalid inputs/commands
         
      
  

    def _arithematic(self,operator):  #method to perform arithematic operations
      if self.getSize() < 2:    #making sure there are atleast two elements
        return
      b = self.pop()
      a = self.pop()
      if operator == '+':
        self.push(a+b)
      elif operator =='-':
        self.push(a-b)
      elif operator =='*':
        self.push(a*b)
      elif operator =='^':
        self.push(a ** b)
      elif operator == '/':
        if b!=0:
          self.push( a/b )
  
  
    def _function(self,function): #Method to perform mathematic and trigonometric operations
      if self.isEmpty():  #To ensure that there is atleast one element in the stack
        return
      a = self.pop()
      if function == 'sin':
        self.push(np.sin(a))
      elif function == 'cos':
        self.push(np.cos(a))
      elif function == 'exp':
        self.push(np.exp(a))
      elif function =='log':
        self.push(np.log(a))
      elif function == 'abs':
        self.push(np.abs(a))
      elif function == 'sqrt':
        self.push(np.sqrt(a))
        
  

    def _constant(self,constant): #Method to push mathematical constants on to the stack
      if constant == 'pi':
        self.push(np.pi)
      elif constant == 'e':
        self.push(np.e)

    @staticmethod
    def postfix2infix(myqueue):
        stack = Stack()
        postfix_elements = []

        temp_queue = copy.deepcopy(myqueue)
        
        while not temp_queue.isEmpty():
            token = temp_queue.dequeue()
            postfix_elements.append(token)
            
            if token in {'+', '-', '*', '/', '^'}:
                if stack.getSize() < 1:
                    return stack.peek()  # Not enough operands
                    
                b = stack.pop()
                a = stack.pop()
                
                new_expr = f"({a} {token} {b})"
                stack.push(new_expr)
            
            elif token in {'sin', 'cos', 'exp', 'log', 'abs', 'sqrt'}:
                if stack.isEmpty():
                    return "Invalid Expression"  # Not enough operands
                    
                a = stack.pop()
                new_expr = f"{token}({a})"
                stack.push(new_expr)
            
            elif token in {'pi', 'e'}:
                if token == 'pi':
                    stack.push('π')
                elif token == 'e':
                    stack.push('e')
            
            else:
                # Directly push numbers or variables
                stack.push(token)
        
        if stack.getSize() != 1:
            return myqueue.peekRear()
        
        infix_expr = stack.peek()
        return infix_expr

    @staticmethod
    def evaluate_postfix(myqueue, x=None):
      stack = Stack()
      temp_queue = copy.deepcopy(myqueue)
        
      while not temp_queue.isEmpty():
          token = temp_queue.dequeue()
            
          if token in {'+', '-', '*', '/', '^'}:
              b = stack.pop()
              a = stack.pop()
              if token == '+':
                  stack.push(a + b)
              elif token == '-':
                  stack.push(a - b)
              elif token == '*':
                  stack.push(a * b)
              elif token == '^':
                  stack.push(a ** b)
              elif token == '/':
                  if b != 0:
                      stack.push(a / b)
                  else:
                      print("Division by zero error")
                      return None
          
          elif token in {'sin', 'cos', 'exp', 'log', 'abs', 'sqrt'}:
              a = stack.pop()
              if token == 'sin':
                  stack.push(np.sin(a))
              elif token == 'cos':
                  stack.push(np.cos(a))
              elif token == 'exp':
                  stack.push(np.exp(a))
              elif token == 'log':
                  stack.push(np.log(a))
              elif token == 'abs':
                  stack.push(np.abs(a))
              elif token == 'sqrt':
                  stack.push(np.sqrt(a))
            
          elif token in {'pi', 'e'}:
              if token == 'pi':
                  stack.push(np.pi)
              elif token == 'e':
                  stack.push(np.e)
          
          else:
              if token == 'x' and x is not None:
                  stack.push(x)
              else:
                  stack.push(float(token))
        
      if stack.getSize() == 1:
        return stack.peek()
      else:
        return "Invalid Expression"
    
    
    
    def plot_expression(self, infix_expr):
       
      import matplotlib.pyplot as plt
      import numpy as np

      try:
        xmin, xmax, nbp = map(float, input("Enter values of xmin, xmax, nbp: ").split()) 
      except ValueError:
        print("Invalid input. Please enter three numerical values separated by spaces.")
        return

      x_values = np.linspace(xmin, xmax, int(nbp))
      y_values = []
       
      for x in x_values:
        y = eval(infix_expr.replace('x', str(x)))
        y_values.append(y)

      plt.plot(x_values, y_values)
      plt.xlabel('x')
      plt.ylabel('y')
      plt.title(f'Plot of {infix_expr}')
      plt.grid(True)
      plt.show()

    