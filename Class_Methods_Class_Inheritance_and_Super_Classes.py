#Creating Class Methods

class ClassTest:
    def instance_method(self):
        print(f"called instance_method of {self}")
        
    @classmethod
    #uses the class for something and allows you to call a previous instance method
    def class_method(cls):
        print(f"called class_method of {cls}")
        
    @staticmethod
    #no information about the class or object

    def static_method():
        print('called static_method')




#creating a class that allows you to pass the TYPES variable to other fu

class Book:
    TYPES = ('hardcover','paperback')
    
    def __init__(self,name,book_type,weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight+100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)
        
book = Book('Hary Potter', "Hardcover",1500)       
    
#Creation of my own that because why not right

class CoffeeBean():
    TYPES = ('Arabica','Robusta')
    
    def __init__(self,name,bean_type,weight):
        self.name = name
        self.bean_type = bean_type
        self.weight = weight
        
    def __repr__(self):
        return f"Bean {self.name}, {self.bean_type}, weighting {self.weight}g"
    
    @classmethod
    def arabica_bean(cls, name, bean_weight):
        return cls(name, cls.TYPES[0], bean_weight)



#Using Inheritance to pass the variables name and connected_by to the printer class from the device class

class Device:
    def __init__(self,name,connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __repr__(self):
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
             
            
class Printer(Device):
    def __init__(self,name,connected_by,capacity):
        super().__init__(name,connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
            
    def __str__(self):
        return f"{super.__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self,pages):
        if not self.connected:
            print('Your not connected')
        else:
            print(f'Printing {pages} pages')
            self.remaining_pages -= pages


#Creating a Superclass and Subclass because I can 


class Person():

	def __init__(self, name,age):
		self.name = name 
		self.age = age 


	#noting to intialize here, move along
	def display1(self):
		print("This is a superclass")

class Employee(Person):
	#just gonna pass the properties of Person to Employee, nothing to see here
	def display2(self):
		print(f"this is a subclass with name {self.name} and {self.age}")


emp = Employee('Chuck Norris','immortal')

emp.display1()
emp.display2()


#more subclasses
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display1(self):
        print(f'The persons name is {self.name} and their age is {self.age}')
 
#when passing values from one Class to another its important to remember that the Super method overides the init function within a class
#to by pass this you need to ensure that you reference the previous class during your intialization using CLASSNAME.__init__(Variables)        
class Employee(Person):
    
    def __init__(self, emp_name,emp_age,salary):
        self.salary = salary
        Person.__init__(self,emp_name,emp_age)
        
    def display2(self):
        print("salary:", self.salary)
        Person.display1(self)