from random import randint
import random

def generate_n(n:int, min:int, max:int, a="(", b=")", seed=None):
    cases=[]
    if seed:
        random.seed(seed)
    
    for _ in range(n):
        len1 = randint(min, max)
        len2 = randint(min, max)

        cases.append((generate_string(len1, a, b), generate_string(len2, a, b)))
    return cases

def generate_string(len:int, a="(", b=")"):
    word= ""

    for _ in range(len):
        rnd=randint(0, 1)
        
        if(rnd):
            word+=a
        else:
            word+=b
    return word