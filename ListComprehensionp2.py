
def a_comprehension():
    """This functions finds abc where a^2+b^2=c^2 and a,b,c are less than 100.It then prints them"""
    x= [(a,b,c) for a in range(1,101) for b in range(1,101) for c in range(1,101) if a**2+b**2==c**2]
    print(x)
    
def b_comprehension():
    """This function gets the strings that have more than 5 characters and 
    put the integer number in front of it"""
    list=['one', 'seven', 'three', 'two', 'ten']
    x= [(len(list[s]),list[s].upper()) for s in range(len(list)) if len(list[s])>3]
    print(x)

def c_comprehension():
    """This function takes a list of names and switches the last name for the first"""
    list=["Jules Verne", "Alexandre Dumas", "Maurice Druon"]
    x= [a + ", " + b for a,b in [y.split()[::-1] for y in list]]
    print(x)
    
def concatenate(a,*b):
    """Join b's with a in the middle then return the string """
    x=[a.join(b)]
    return(x)
    
    
a_comprehension()
b_comprehension()
c_comprehension()
x=concatenate(':','one', 'two','three')
print(x)