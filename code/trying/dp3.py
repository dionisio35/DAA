from tools import *
from dp import *


def create_matrix(s,t,n,m):
    dp= [[[] for j in range(m+1)] for i in range(n+1) ] #create the nXm matrix
    for i in range(1,len(dp)):
        dp[i][0]=[s[0:i]]
    for i in range(1,len(dp[0])):
        dp[0][i]=[t[0:i]]
    return dp


def only_positive_bf(chain):
    return chain


def filter_solutions(possibles_sequences):    
    m=10e31
    sequences:set=set()
    for i in possibles_sequences:
        ni=get_n_to_balanced(i,"(",")")
        mi=len(i)+ni[0]+ni[1]
        if mi < m:
            sequences=set()
            sequences.add(i)
            m=mi

        elif mi == m:
            sequences.add(only_positive_bf(i))
 
    return list(sequences)


def get_better_chains(ct,cs,cst,t,s,a,b):
    possibles_sequences:set=set()
    for csi in cs:
            if is_subsequence(csi,t):
                possibles_sequences.add(csi)
            possibles_sequences.add(csi + t[len(t)-1])          

    for cti in ct:
        if is_subsequence(cti,s):
            possibles_sequences.add(cti)    
        possibles_sequences.add(cti + s[len(s)-1])

    for csti in cst:
        if is_subsequence(csti,t) and is_subsequence(csti,s):
            possibles_sequences.add(csti)
        possibles_sequences.add(csti + t[len(t)-1]+s[len(s)-1])

    return filter_solutions(possibles_sequences)



def get_min(sol): 
    min=10e31
    solution=""
    for i in sol:
        if len(i) < min:
            min=len(i)
            solution=i
    return solution



def dp3(s,t,a="(",b=")"):
    n=len(s)
    m=len(t)
    dp=create_matrix(s,t,n,m)
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            dp[i][j] = get_better_chains(dp[i-1][j], dp[i][j-1],dp[i-1][j-1],dp[0][j][0],dp[i][0][0],a,b)
    solutions = get_balanced_chains(dp[len(dp)-1][ len(dp[0])-1],a,b)
    return get_min(solutions)


    