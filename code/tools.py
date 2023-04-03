

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

def is_balanced(l: list):
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


def get_balanced_chains(input,a,b):
    result :set = set()
    for l in input:
        balance=0
        balanced=""
        for i in l:
            if(i==a):
                balanced+=i
                balance+=1
            else:
                if balance:
                    balance-=1
                    balanced+=i
                else:   
                    balanced+= a+i
        balanced += balance*b
        result.add(balanced)
    return list(result)

def get_n_to_balanced(s,a,b):
    neq=0
    pos=0
    for i in s:
        if(i==a):
            pos+=1
        else: 
            if(pos):
                pos-=1
            else:
                neq+=1
    return pos,neq