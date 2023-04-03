from tools import *

def solve(s:list, t:list):
    sol= []
    l= ['']
    while l:
        temp= l.pop()
        if is_subsequence(temp, s) and is_subsequence(temp, t) and is_valid(temp):
            sol.append(temp)
        
        if len(temp) <= 2*len(s+t) -1:
            l.append(temp + '(')
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