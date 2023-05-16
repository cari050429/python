#Drawing a leaf
#Base X Conversion 
#Binomial Coefficient 
#with testif case

from turtle import *


def draw_branch(length, level):
  if level==0:
      return
  else:
      forward(length)
      draw_branch(length/2,level-1)
      backward(length*1/3)
      left(60)
      draw_branch(length/3,level-1)
      right(120)
      draw_branch(length/3,level-1)
      left(60)
      backward(length*2/3)

def Cnk_m(n,k):
    Cnk_dict={}
    Cnk_dict[(n,0)]=1
    Cnk_dict[(n,n)]=1
   
    if (n,k) not in Cnk_dict:
      Cnk_dict[(n,k)] = (Cnk_m((n-1),(k-1))+Cnk_m((n-1),k))
    return Cnk_dict[(n,k)]
       
def make_pairs(list_a,list_b):
    if len(list_a)==1 or len(list_b)==1:
        c=[(list_a.pop(0),list_b.pop(0))]
        return c
    
    if len(list_a)==0 or len(list_b)==0:
        return []

    else:
        a=list_a.pop(0)
        b=list_b.pop(0)
        return [(a,b)] + make_pairs(list_a,list_b)
    
def strB(n,base=10):
    past_9='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x=(n%base)
    if n<base:
        return past_9[n]
    else:
        return str(strB(n//base,base))+ str(past_9[x])

x=strB(123,16)
print(x)
    
def testif(b,testname):
    if b:
        print(testname+ " Success")
    else:
        print(testname + " Fail")
    
        

testif(Cnk_m(13,2)==78, 'base_test')
testif(Cnk_m(15,3)==455, 'base_test')
testif(Cnk_m(20,3)==1140, 'base_test')
testif(Cnk_m(4,2)==6, 'base_test')

testif(make_pairs([1,2,3,4],[5,6,7,8])==[(1,5),(2,6),(3,7),(4,8)], 'base_test')
testif(make_pairs([1,2,3],[5,6,7,8])==[(1,5),(2,6),(3,7)], 'base_test')
testif(make_pairs([1,2,3,4],[])==[], 'base_test')
testif(make_pairs([],[5,6,7,8])==[], 'base_test')
testif(make_pairs([1,2,3,4],[1,2])==[(1,1),(2,2)], 'base_test')

testif(strB(138,2)=='10001010', 'base_test')
testif(strB(15,16)=='F', 'base_test')
testif(strB(109,8)=='155', 'base_test')
testif(strB(523,20)=='163', 'base_test')

clearscreen()
delay(0)
left(90)
draw_branch(160,6)
