#classes allow us to logically group our data(attributes) and functions(methods) to reuse and build upon 
#class is a blueprint for creating instances. Each unique employee would be an instance of the class
import datetime
class Employee:
    pass

emp_1=Employee()
emp_2=Employee()
#each is an instance of the class 

#instance variables contain data that is unique to each instance 
emp_1.first='corey'
emp_1.last="schafer"
emp_1.pay=50000


emp_2.first='sarah'
emp_2.last="perez"
emp_1.pay=60000

print(emp_1.first) #we do classes so that we don't have to initialze each intance variable each time
print(emp_2.first)

class Employees:
    num_of_emps=0
    raise_amount=1.04 #class variable

    def __init__(self,first,last,pay):#initialized/constructor
        #the instance of self is always the first initiliazed
        self.first=first#self.x doesnt need to be the same as first, but it is good to 
        self.last=last
        self.pay=pay
        self.email=first +'.'+'@company.com'
        Employees.num_of_emps+=1 #Employee instead of self because we want all the instances to have the same number of employees

    def fullname(self): #regular method, takes the instance as the first argument
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)#class variable needs to be accessed through an instance 

    @classmethod
    def set_raise_amt(cls,amount):#cls is class variable name, class method is class first
        cls.raise_amount=amount 

    @classmethod
    def from_string(cls,emp_str):#class method used as an alernative constructor
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod #has logical connection with class, but none of the variables, doesnt take instance or class as first argument
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True  
    



emp_3=Employees('Hemi','Yay',80000)#instance of self is passed automatically, emp3 will be self
print(emp_3.first)

print(emp_3.fullname())#need parantheses because it is a method
print(Employees.fullname(emp_3))#top gets transformed to this when it is run in the backend

#class variables are shared for each instance of the class

print(emp_3.pay)
emp_3.apply_raise()
print(emp_3.pay)

print(emp_3.__dict__)#prints employee namespace
Employee.raise_amount=1.05 #changes raise amount for the whole class
emp_3.raise_amount=1.06#changes the raise amount for only the instance of employee 1
#so since class variable can be different between a single instance and the class, putting self on the apply_raise function is important

print(Employees.raise_amount)
print(emp_3.raise_amount)

print(Employees.num_of_emps)

Employees.set_raise_amt(1.08)
print(Employees.raise_amount)

emp_4=Employees.from_string('Hey-HI-3000')
print(emp_4)
print(emp_4.first)

my_date=datetime.date(2023,6,1)
print(Employees.is_workday(my_date))


class Employees_2:
    raise_amount=1.04 #class variable

    def __init__(self,first,last,pay):#initialized/constructor
        #the instance of self is always the first initiliazed
        self.first=first#self.x doesnt need to be the same as first, but it is good to 
        self.last=last
        self.pay=pay
        #self.email=first +'.'+'@company.com'
        Employees.num_of_emps+=1 #Employee instead of self because we want all the instances to have the same number of employees

    @property
    def fullname(self): #regular method, takes the instance as the first argument
        return '{} {}'.format(self.first, self.last)
     
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last
    
    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first=None
        self.last=None

    @property #allows you to continue using the mail as an attribute, the old email attribute was commented out above 
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
    def __repr__(self):#dunder method for a debugging print
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
    
    def __str__(self):#dunder method for printing a string
        return '{}-{}'.format(self.fullname(),self.pay)
    
    def __add__(self,other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname)
    
    
class Developer(Employees_2):#even if empty, will have all instances and methods of employees_2 class 
    #walks up chain of inheritance to find what its looking for
    raise_amount=1.2 #only raise for develoopers, not all employees
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)#passes the ones that you want the employees class to handle
        #Employees_2.__init__(self,first,last,pay) could also be like this 
        self.prog_lang=prog_lang

class Manager(Employees_2):

    def __init__(self,first,last,pay,employees=None):#dunder innit
        super().__init__(first,last,pay)
        if employees is None: 
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp  not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def method_print_emp(self):
        for emp in self.employees:
            print('--->',emp.fullname)

    
dev_1=Developer('Cari','Corrales',140000,'python')
print(dev_1.first)

manager_1=Manager('Hi','Bye',150000,[dev_1])
print(manager_1.first)
manager_1.method_print_emp()

dev_2=Developer('Bye','Hi',100000,'C')
manager_1.add_emp(dev_2)#no brackets because now only one single employee is expected
manager_1.method_print_emp()

#isinstance()#if an object is an instance of a class
print(isinstance(manager_1,Manager))
print(isinstance(manager_1,Developer))

#if a class is an instance of another class
print(issubclass(Developer,Employees_2))

print(1+2)
print('a'+'b')
#addition has different behaviour based on variable type 

print(repr(dev_1))

print(dev_1 + dev_2) #because of the dunder add
#many special methods for arithmetics

print(len(dev_1))

#if we change the first name, the email doesn't update 

dev_1.fullname='Hey Cari'
print(dev_1.fullname)

print(len(dev_1))

del dev_1.fullname#delete dev_1
print(dev_1.fullname)
