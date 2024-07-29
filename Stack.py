#class Stack - the main class for Stack seen in lecture 5. 
# Reminder: stack is a private variable
# To complete: *  __str__ method must be included that displays the stack in reverse
# order from the bottom to the top (with index 0 at the bottom)
#             * swap method: two swap the top with top-1 item
#             * copy method: duplicate the top item
#             * flush method: to empty the stack

class Stack:
    #constructor
    def __init__(self):
        self.__stack = []  # create private stack
    #methods
    def pop(self):  #pop the item
        if self.isEmpty(): return None
        return self.__stack.pop()

    def peek(self): #peek the item (no removal)
        if self.isEmpty(): return None
        return self.__stack[len(self.__stack)-1]

    def push(self, item): #push the item
        self.__stack.append(item)

    def getSize(self):           #return stack size
        return len(self.__stack)

    def isEmpty(self): #check if stack empty
        return self.getSize()==0
    
    def __str__(self):
        output = []
        for i in range(len(self.__stack)):
            value = self.__stack[i]
            output.append(F"{i} \t {value}")  #formatting the string with index and value seperated by a tab
        return "\n".join(output)
        
       #complete
    def swap(self):
        if len(self.__stack) < 2:
            return "To swap, atleast two elements are required in the stack"
        else : self.__stack[-1],self.__stack[-2] = self.__stack[-2],self.__stack[-1] #Swaps the top and top-1 element of the stack

    def copy(self):
        if len(self.__stack) < 1:
            return "error: atleast one element is required for this method"
        else:
            top = self.__stack[-1] 
            self.__stack.append(top) #the top item of the original stack is copied as the new element in the stack
            return self.__stack
        
    def flush(self):
        self.__stack.clear() #clears the stack



################################
################################

def main():
    mystack=Stack()
    for i in range(1,4): mystack.push(i*10)
    
    print("test __str__")
    print(mystack)

    print("test swap")
    mystack.swap()
    print(mystack)

    print("test copy")
    mystack.copy()
    print(mystack)

    print("test flush")
    mystack.flush()
    mystack.push(11)
    print(mystack)
    

## call the main function if this file is directly executed
if __name__=="__main__":
    main()
