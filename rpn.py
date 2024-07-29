from StackCalc import *
from Queue import *
from numpy import *  # if you need sin, just do sin, etc.
import matplotlib.pyplot as plt


# Menu
print()
print("===============================================")
print("================= Project 1 ===================")
print("===============================================")
print("|                                             |")
print("|         1-Simple  RPN calculator            |")
print("|         2-Fancy   RPN calculator            |")
print("|         3-Fancier RPN calculator            |")
print("|                                             |")
print("===============================================")
print()
choice=input("Your choice: ")


mystack=StackCalc()
myqueue=Queue()


if choice=="1": #////////////// Simple RPN calculator

    print("Welcome to the simple RPN calculator (enter 'quit' to quit)");
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        prompt=input(">")    
        if prompt=="quit": break

        mystack.rpnCommand(prompt)



if choice=="2": #////////////// Fancy RPN calculator

    print("Welcome to the fancy RPN calculator (enter 'quit' to quit)");
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        if not myqueue.isEmpty(): #Display both postfix and infix
            print("Postfix: "+str(myqueue))
            print("Infix: ",StackCalc.postfix2infix(myqueue))
        prompt=input(">")    
        if prompt=="quit": break
        mystack.rpnCommand(prompt)
        if prompt!="flush":
            myqueue.enqueue(prompt)
        else:
            myqueue.flush()

        



    print("Welcome to the fancier RPN calculator (enter 'quit' to quit)")
    while True:
        print("--------------------------------------------------------------")
        print(mystack)
        
        if not myqueue.isEmpty():
            print("Postfix: " + str(myqueue))
            infix_expr = StackCalc.postfix2infix(myqueue)
            print("Infix:", infix_expr)
            
            

        prompt = input(">")  # Correctly read user input
        
        if prompt == "quit":
            break
        elif prompt == "run":
            if infix_expr is not None:
                if 'x' in str(myqueue):
                
                    x = float(input("Enter the value of x: "))
                    
                else:
                    x = None
                # Replace 'x' with its value in the infix expression and evaluate
                infix_result = eval(infix_expr.replace('x', str(x)))
            elif infix_expr:
                # Evaluate without replacing 'x'
                infix_result = eval(infix_expr)
                
            # Evaluate postfix expression
            postfix_result = StackCalc.evaluate_postfix(myqueue, x)
            
            print("Solution using infix:", infix_result)
            print("Solution using postfix:", postfix_result)
        else:
            mystack.rpnCommand(prompt)
            if prompt != "flush":
                myqueue.enqueue(prompt)
            else:
                myqueue.flush()

    print("Thanks for using the RPN calculator")

if choice == "3":  #////////////// Fancier RPN calculator

    print("Welcome to the fancier RPN calculator (enter 'quit' to quit)")
    infix_expr = None
    while True:
        print("--------------------------------------------------------------")
        print(mystack)
        
        if not myqueue.isEmpty():
            print("Postfix: " + str(myqueue))
            infix_expr = StackCalc.postfix2infix(myqueue)
            print("Infix:", infix_expr)
            

        prompt = input(">")  # Correctly read user input
        
        if prompt == "quit":
            break
        elif prompt == "run":
            if infix_expr and infix_expr != "Invalid Expression":
                
                if 'x' in infix_expr:
                    x = float(input("Enter the value of x: "))
                try:
                    infix_result = eval(infix_expr.replace('x', str(x)))
                    postfix_result = StackCalc.evaluate_postfix(myqueue, x)
                    print("Solution using infix:", infix_result)
                    print("Solution using postfix:", postfix_result)
                except Exception as e:
                    print(f"Error in evaluating expression: {e}")
            else:
                print("Cannot run. The infix expression is invalid.")
        elif prompt == "plot":
            if infix_expr and infix_expr != "Invalid Expression" and 'x' in infix_expr:
                mystack.plot_expression(infix_expr)
            else:
                print("Plotting requires a valid expression containing 'x'")
        else:
            mystack.rpnCommand(prompt)
            if prompt != "flush":
                myqueue.enqueue(prompt)
            else:
                myqueue.flush()

    print("Thanks for using the RPN calculator")
