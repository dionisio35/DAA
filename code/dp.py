from first_solve import is_subsequence
from brute_force import brute_force_algorithm
from second_solve import solve

def create_matrix(s,t,n,m):
    dp= [["" for j in range(m+1)] for i in range(n+1) ] #create the nXm matrix
    for i in range(1,len(dp)):
        dp[i][0]=s[0:i]
    for i in range(1,len(dp[0])):
        dp[0][i]=t[0:i]
    return dp


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
            

def get_balance(l,a,b):    
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
    return balanced


 

# def min_sequence(possibles_sequences,a,b):    
#     m=10e31
#     s=""
#     for i in possibles_sequences:
#         temp=len(i)+get_n_to_balanced(i,a,b)
#         if temp < m:
#             m=temp
#             s=i
#     return s
    

# def min_sequence(possibles_sequences,a,b):    
#     m=10e31
#     s=""
#     for i in possibles_sequences:
#         i=get_balance(i,a,b)
#         if len(i) < m:
#             m=len(i)
#             s=i
#     return s
    

def min_sequence(possibles_sequences,a,b):    
    m=10e31
    n=(10e31,10e31)
    s=""
    for i in possibles_sequences:
        mi=len(i)
        ni0,ni1=get_n_to_balanced(i,a,b)
        if (mi + ni0+ni1) < (m + n[0]+n[1]):
            m=mi
            n=(ni0,ni1)
            s=i
        elif (mi + ni0+ni1) == (m + n[0]+n[1]):
            if (ni0+ni1) < (n[0]+n[1]):                
                m = mi
                n = (ni0,ni1)
                s = i          
            elif (ni0+ni1) == (n[0]+n[1]):
                if ni0>n[0]:
                    m = mi
                    n = (ni0,ni1)
                    s = i   
    return s



def get_better_chain(ct,cs,t,s,a,b):
    possibles_sequences=[]
    if is_subsequence(ct,s) and is_subsequence(cs,t):
        possibles_sequences.append(min_sequence([cs,ct],a,b))
    elif is_subsequence(cs,t):
        possibles_sequences.append(cs)
    elif is_subsequence(ct,s):
        possibles_sequences.append(ct)
    possibles_sequences.append(cs+t[len(t)-1])
    possibles_sequences.append(ct + s[len(s)-1])
    return min_sequence(possibles_sequences,a,b) 


import numpy as np

def spies_dp(s,t,a="(",b=")"):
    n=len(s)
    m=len(t)
    dp=create_matrix(s,t,n,m)
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            # if(i==3 and j==4):
                # print("here")
            dp[i][j] = get_better_chain(dp[i-1][j], dp[i][j-1],dp[0][j],dp[i][0],a,b)
    print(np.array(dp))      
    return get_balance(dp[len(dp)-1][ len(dp[0])-1],a,b)
            



s="(()("
t= ")))"

s=")((()(("      
t="))(((((()"

s="()((" 
t="())("


s="())("
t=")((("

s="(()("
t=")((("


s="()())" 
t="(()))"


from time import time

# t1=time()
# a=spies_dp(s,t)
# t2=time()
# b=brute_force_algorithm(s,t)
# t3=time()
# c=solve(s,t)
# t4=time()

# print("spies_dp",a,len(a),t2-t1)
# print("brute_force_algorithm",b,len(b[0]),t3-t2)
# print("solve",c,len(c[0]),t4-t3)

