#Basic Diffie Hellman
import random, numpy
worked=0
#thanks, StackOverflow
def primesfromXtoN(low,high):
    return [x for x in range(low, high)
     if all(x % y != 0 for y in range(low, x))]

LargePrimes = primesfromXtoN(1000,2000)
primes = primesfromXtoN(100,600)

def initialise():
    global primes , LargePrimes , p , g
    p = random.choice(LargePrimes)
    g = random.choice(range(3,p-1))


class client:
    def __init__(self):
        global p , g
        self.secret = random.choice(primes)
        self.Pkey = int((g**self.secret) % p)

    def recieve(self,b):
        self.s = (b**self.secret) % p


def run():
    global worked
    initialise()
    c1 = client()
    c2 = client()
    c1.recieve(c2.Pkey)
    c2.recieve(c1.Pkey)
    if c1.s == c2.s:
        worked+=1
        return True
    else:
        print(p,g,c1.s,c2.s)
        return False

while True:
    print(worked)
    run()


