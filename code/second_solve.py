from tools import *

def solve(s:list, t:list):
    sol= []
    l= ['']
    while l:
        temp= l.pop()
        if is_subsequence(temp, s) and is_subsequence(temp, t) and raw_balance(temp) == 0:
            sol.append(temp)
        
        if len(temp) <= 2*len(s+t) -1:
            if (temp + '(').count('(') <= (len(s+t) + 1)/2:
                l.append(temp + '(')

            if raw_balance(temp + ')') >= 0:
                l.append(temp + ')')
    
    s= sol[0]
    solution= []
    for i in sol:
        if len(s) > len(i):
            s= i
            solution= []
        if len(s) == len(i):
            solution.append(i)
    
    return solution