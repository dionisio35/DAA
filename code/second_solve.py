

def is_subsequence(l: list, subl: list):
    '''...'''
    pos=0
    for i in l:
        if i == subl[pos]:
            pos+=1
        if pos == len(subl):
            return True
    return False

def is_valid(l: list):
    '''...'''
    n= 0
    if not l:
        return -1
    
    for i in l:
        if n < 0:
            return -1
        if i == 'e':
            n+=1
        if i == 'r':
            n-=1
    return n




def solve(s:list, t:list):
    '''...'''
    sol= []
    l= ['']
    while l:
        temp= l.pop()
        if is_subsequence(temp, s) and is_subsequence(temp, t) and is_valid(temp) == 0:
            sol.append(temp)
        
        if len(temp) <= 2*len(s+t) -1:
            if (temp + 'e').count('e') <= (len(s+t) + 1)/2:
                l.append(temp + 'e')

            if is_valid(temp + 'r') >= 0:
                l.append(temp + 'r')
    
    s= sol[0]
    solution= []
    for i in sol:
        if len(s) > len(i):
            s= i
            solution= []
        if len(s) == len(i):
            solution.append(i)
    
    return solution