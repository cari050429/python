#Random Number Generator using an iterator and generator
class RndSeq():
    def __init__(self,x,n):
        self.n=n
        self.x=x
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n<0: 
            while True:
                self.x=((22695477*self.x)+1)%pow(2,32)
                return self.x
        elif self.n==0: 
            raise Exception("Stopiteration")
        else:
            self.x=((22695477*self.x)+1)%pow(2,32)
            self.n=self.n-1
            return self.x

def rnd_gen(x,n):
    if n>=0:
        for z in range(n):
           x=((22695477*x)+1)%pow(2,32)
           yield(x)
    if n<0:
        while True: 
            x=((22695477*x)+1)%pow(2,32)
            yield(x)
            

x=RndSeq(1,10)
for i in range(10): 
    print(next(x))

y=rnd_gen(1,10)
for i in range(10): 
    print(next(y))



