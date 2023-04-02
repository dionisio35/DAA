from first_solve import is_subsequence
from brute_force import brute_force_algorithm
from second_solve import solve
from dp import *



def create_matrix(s,t,n,m):
    dp= [[[] for j in range(m+1)] for i in range(n+1) ] #create the nXm matrix
    for i in range(1,len(dp)):
        dp[i][0]=[s[0:i]]
    for i in range(1,len(dp[0])):
        dp[0][i]=[t[0:i]]
    # print(dp)
    return dp


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




def min_sequences(possibles_sequences,a,b):    
    m=10e31
    sequences:set=set()
    for i in possibles_sequences:
        ni0,ni1=get_n_to_balanced(i,a,b)
        mi=len(i)+ ni0+ni1

        if mi < m:
            sequences=set()
            sequences.add(i)
            m=mi

        elif mi == m:
            sequences.add(i)
 
    return list(sequences)

def get_better_chains(ct,cs,t,s,a,b):
    possibles_sequences=[]
    # if is_subsequence(ct,s) and is_subsequence(cs,t):
    #     possibles_sequences.append(min_sequence([cs,ct],a,b))
    for csi in cs:
            if is_subsequence(csi,t):
                possibles_sequences.append(csi)
            possibles_sequences.append(csi + t[len(t)-1])

    for cti in ct:
        if is_subsequence(cti,s):
            possibles_sequences.append(cti)    
        possibles_sequences.append(cti + s[len(s)-1])
    return min_sequences(possibles_sequences,a,b) 

def get_min(sol): 
    min=10e31
    solution=""
    for i in sol:
        if len(i) < min:
            min=len(i)
            solution=i
    return solution



def dp2(s,t,a="(",b=")"):
    n=len(s)
    m=len(t)
    balance=0
    dp=create_matrix(s,t,n,m)
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            # if(i==3 and j==4):
                # print("here")
            dp[i][j] = get_better_chains(dp[i-1][j], dp[i][j-1],dp[0][j][0],dp[i][0][0],a,b)
    # print(np.array(dp)) 
    # print(dp[1])
    solutions = get_balanced_chains(dp[len(dp)-1][ len(dp[0])-1],a,b)
    return get_min(solutions)




s="(()("
t= ")))"

# s=")((()(("      
# t="))(((((()"

# s="()((" 
# t="())("


# s="())("
# t=")((("

# s="(()("
# t=")((("


# s="()())" 
# t="(()))"


from time import time

t1=time()
a=dp2(s,t)
t2=time()
b=brute_force_algorithm(s,t)
t="(()))"
t3=time()
# c=solve(s,t)
# t4=time()

print("dp2",a,len(a),t2-t1)
print("brute_force_algorithm",b,len(b[0]),t3-t2)
# print("solve",c,len(c[0]),t4-t3)

