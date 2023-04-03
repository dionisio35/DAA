

def is_subsequence(l: list, subl: list):
    pos=0
    for i in l:
        if i == subl[pos]:
            pos+=1
        if pos == len(subl):
            return True
    return False

def is_valid(l: list):
    n= 0
    for i in l:
        if n < 0:
            return False
        if i == '(':
            n+=1
        if i == ')':
            n-=1
    return n == 0

def raw_balance(l: list):
    n= 0
    if not l:
        return -1
    
    for i in l:
        if n < 0:
            return -1
        if i == '(':
            n+=1
        if i == ')':
            n-=1
    return n



