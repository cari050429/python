#Defines a class NVector with many functionalities, also has testifs

#a
class NVector(object):
    def __init__(self,a,*arg):
        self.numbers=[]
        if len(a)==0:
            for x in arg:
                self.numbers.append(x) 
        else:
            for x in a:
                self.numbers.append(x)

    def __len__(self):
        return len(self.numbers)
    
    def __getitem__(self,key):
        return self.numbers[key]
    
    def __setitem__(self,position,value):
        self.numbers[position]=value
        
    def __str__(self):###need to work on this one 
        return str(self.numbers)
    
    def __eq__(self, param):
        if self.numbers == param:
            return self.numbers
        else:
            return False
        
    def __neq__(self,param):###checkkkk
        return not self.list==param 
        
    def __add__(self,vector):
        list=[]
        if type(self.numbers)==type(vector):
            for x in range(len(self.numbers)):
                y=self.numbers[x]+vector[x]
                list.append(y)
            return list
        else:
            for x in range(len(self.numbers)):
                y=self.numbers[x]+vector
                list.append(y)
            return list
        
    def __radd__(self,param):
        return self.__add__(param)
    
    def __mul__(self,vector):
        list=[]
        if type(self.numbers)==type(vector):
            for x in range(len(self.numbers)):
                y=self.numbers[x]*vector[x]
                list.append(y)
            return list
        else:
            for x in range(len(self.list)):
                y=self.numbers[x]*vector
                list.append(y)
            return list
        
    def __rmul__(self,param):
        return self.__mul__(param)
    
    def zeroes(n):
        z=[]
        for x in range(n):
            y=0
            z.append(y)
        return z
    
def testif(b, msgOK="", msgFailed=""):
    """Function used for testing. 
    param b: boolean, normally a tested condition: true if test passed, false 
    otherwise param testname: the test name
    param msgOK: string to be printed if param b==True  ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: "+ "; " + msgOK)
    else:
        print("Failed: "+ "; " + msgFailed)
        return b


vector1=NVector([1,2,3,4])
testif(vector1==[1,2,3,4],"setting works", "setting failed")
testif(len(vector1)==4,"length works", "length failed")
testif(vector1[0]==1, "getitem works", "getitem failed")
vector1[2]=0
testif(vector1[2]==0,"setitem works", "setitem works")
testif(str(vector1)=='[1, 2, 0, 4]',"string works", "string failed" )#ask the teacher 
x=[1,2,0,4]
testif(vector1==x, "equal works", "equal failed")
y=[3,2,0,4]
testif(vector1!=y, "notequal works", "notequal failed")
testif(vector1+x==[2,4,0,8], "add works", "add failed")
testif(x+vector1==[2,4,0,8], "radd works", "radd failed")
testif(vector1*x==[1,4,0,16], "mul works", "mul failed")
testif(x*vector1==[1,4,0,16], "rmul works", "rmul failed")
t=NVector.zeroes(3)
testif(len(t)==3,"zeroes length works","zeroes length does not work")







        