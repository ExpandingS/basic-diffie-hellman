#!/usr/bin/env python3

#Basic Diffie Hellman
import random, numpy, sys, argparse


if "-h" in sys.argv or "--help" in sys.argv:
    print("Usage:")
    print("./Diffie_Hellman.py")
    print("./Diffie_Hellman.py XOR")
    print()
    print("XOR option replaces (mod) with ^, and outputs how often it works.")
    exit() 
if "XOR" in sys.argv:
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
            print(str(worked/ran*100)+"%")
        else:
            print(worked)


