#Quadratic Equation 
#A main while loop which the user 
#enters value for coefficients a,b and c and 
#the function returns one solution if b^2-4ac=0
#it returns no solution if b^2-4ac<0
#returns two solutions if b^2-4ac>0

import math
import matplotlib.pyplot as plt
import numpy as np
while True:
    a=(input("Give a number for a:"))
    if a =='':
        break  
    b=float(input("Give a number for b:"))
    c=float(input("Give a number for c:"))
    a=float(a)
    if ((b**2)-4*a*c)<0:
        print("No real solutions\t")
        x=np.linspace((-b/(2*a))-2,(-b/(2*a))+2,num=150)
        plt.scatter(x,(a*(x*x)+b*x+c))
    elif (b**2)-(4*a*c)== 0:
        solution = (-b+(math.sqrt((b**2)-4*a*c)))/2*a
        print("One Solution:",solution,"\t")
        x=np.linspace(solution-2,solution+2,num=150)
        plt.scatter(x,(a*(x*x)+b*x+c))
    else:
        solution2=(-b+(math.sqrt((b**2)-4*a*c)))/2*a
        solution3=(-b-(math.sqrt((b**2)-4*a*c)))/2*a
        print("two solutions:{} and {}".format(solution2, solution3))
        x=np.linspace(solution3-2,solution2+2,num=150)
        plt.scatter(x,(a*(x*x)+b*x+c))
     
    
        

