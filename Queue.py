# As seen in class with few more methods provided to you. (code is not commented)
class Queue:
    #constructor
    def __init__(self,maxSize=50): #default
        self.__maxSize=maxSize
        self.__queue=[None]*maxSize  #private
        self.__rear=-1 
        self.__front=0
        self.__nbitems=0

    #methods
    def size(self):        #return queue size
        return self.__nbitems
    def isEmpty(self):  #check if empty
        return self.__nbitems==0      
    def isFull(self):      #check if full
        return self.__nbitems==self.__maxSize

    def peekFront(self): #peek the front item
        if self.isEmpty(): return None
        return self.__queue[self.__front]

    def peekRear(self): #peek the rear item
        if self.isEmpty(): return None
        return self.__queue[self.__rear]

    def enqueue(self, item):   #insert rear item
        if not self.isFull():
          if self.__rear==self.__maxSize-1: self.__rear=-1
          self.__rear+=1
          self.__queue[self.__rear]=item
          self.__nbitems+=1
        else:
          print("queue is full!")  #optional

    def dequeue(self):           #remove front item
        if self.isEmpty(): return None
        temp=self.__queue[self.__front]
        self.__front=(self.__front+1)%self.__maxSize
        self.__nbitems-=1
        return temp

    def __str__(self):
        q=""
        temp=self.__front
        for i in range(self.__nbitems):
            q=q+str(self.peekFront())+" "
            self.__front=(self.__front+1)%self.__maxSize
        self.__front=temp
        return q
    
    def flush(self):
        self.__rear=-1 
        self.__front=0
        self.__nbitems=0
        
    def find(self,item):
        found=False
        temp=self.__front
        for i in range(self.__nbitems):
            if item in self.peekFront():
                found=True
                break
            self.__front=(self.__front+1)%self.__maxSize
        self.__front=temp
        return found

