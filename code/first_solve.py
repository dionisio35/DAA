import generator as generator


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
    print(solution)
    return solution
    


# solve('()', '(((')



