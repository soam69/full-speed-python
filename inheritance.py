class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def greet(self):
        print ("Hello %s" %self.name)
    
class minorPerson (Person) :
    def __init__(self,name):
        Person.__init__(self,name,17)
    def greet(self):
        print ("Hello Minor %s" %self.name)

minor = minorPerson("Shivank")
minor.greet()