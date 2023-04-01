from first_solve import is_subsequence


def create_matrix(s,t,n,m):
    dp= [["" for j in range(m+1)] for i in range(n+1) ] #create the nXm matrix

    for i in range(1,len(dp)):
        dp[i][0]=s[0:i]

    for i in range(1,len(dp[0])):
        dp[0][i]=t[0:i]
    return dp


def get_n_to_balanced(a):
    neq=0
    pos=0
    for i in a:
        if(i=="("):
            pos+=1
        else: 
            if(pos):
                pos-=1
            else:
                neq+=1
    return neq+pos
            

def min_sequence(a,b):    
    if((len(a)+get_n_to_balanced(a))>(len(b)+get_n_to_balanced(b))):
        return b
    return a

def get_better_chain(ct,cs,t,s):
    if is_subsequence(cs,ct) or is_subsequence(cs,t):
        return cs
    if is_subsequence(ct,cs) or is_subsequence(ct,s):
        return ct
    cs = cs+t[len(t)-1]
    ct = ct + s[len(s)-1]
    return min_sequence(cs,ct) 



def spies_dp(s,t):
    n=len(s)
    m=len(t)
    dp=create_matrix(s,t,n,m)
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            dp[i][j] = get_better_chain(dp[i-1][j], dp[i][j-1],dp[0][j],dp[i][0])
    return dp[len(dp)-1][ len(dp[0])-1]
            

# s="(()("
# t= ")))"

# a=spies_dp(s,t)
# print(a,len(a))

