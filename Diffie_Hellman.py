#Basic Diffie Hellman
import random, numpy, sys


if len(sys.argv) == 1:
    print("Usage:")
    print("Diffie_Hellman.py n OR Diffie_Hellman.py XOR")
    print("n is for usual diffie-hellman, XOR is for replacing (mod) wth XOR, and returning the times it worked as a percentage.")
    exit() 

if sys.argv[1] == "XOR":
    XOR=True
else:
    XOR=False

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
        self.secret = random.randrange(3,p-1)
        if XOR:
            self.Pkey = int((g^self.secret) % p)
        else:
            self.Pkey = int((g**self.secret) % p)

    def recieve(self,b):
        self.s = (b**self.secret) % p


def run():
    global worked, ran
    ran+=1
    initialise()
    c1 = client()
    c2 = client()
    c1.recieve(c2.Pkey)
    c2.recieve(c1.Pkey)
    if c1.s == c2.s:
        worked+=1
        return True
    else:
        return False

if __name__ == "__main__":
    worked=0
    ran = 0
    while True:
        run()
        if XOR:
            print(worked/ran*100)
        else:
            print(worked)


