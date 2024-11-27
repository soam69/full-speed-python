class Person:
    def __init__(self,n,a):                                     # This is a constructor for the calss Person
        self.name = n                                           # name and age are variables that are being declared 
        self.age = a                                            # and initialized together
    
    def greet(self):                                            # You have to write "self" to make a method in class 
        print ("Hello %s Welcome to my code" % self.name)       # Yes you can write %s in python also
    def get_age(self):
        print ("The age of %s is %d" %(self.name,self.age))

stu1 = Person("Soham",20)
stu1.greet()
stu1.get_age()
