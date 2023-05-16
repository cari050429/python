#Input a positive integer to find the Pythagorean Triples

def find_Pythagorean(value):
    c=2
    value_list=[]
    while c<=value:
        for a in range(1,c):
            for b in range(1,c):
                if (a**2)+(b**2)==(c**2):
                    makingitatuple=(a,b,c)
                    value_list.append(makingitatuple)
                    break
        c+=1
    return value_list
        
                    
        
    
    
value = int(input("Input a positive integer to find the Pythagorean triples:"))
if value>=0:
    real_values=find_Pythagorean(value)
    print("""The combination of Pythagorean triples where a,b,c<= {} is:
{}""".format(value,real_values))
else: 
    print("Number inserted was not a positive integer")

