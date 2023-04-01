from first_solve import is_subsequence


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
    return neq+pos
            

def min_sequence(c,v,a,b):    
    if((len(c)+get_n_to_balanced(c,a,b))>(len(v)+get_n_to_balanced(v,a,b))):
        return v
    return c

def get_better_chain(ct,cs,t,s,a,b):
    if is_subsequence(cs,ct) or is_subsequence(cs,t):
        return cs
    if is_subsequence(ct,cs) or is_subsequence(ct,s):
        return ct
    cs = cs+t[len(t)-1]
    ct = ct + s[len(s)-1]
    return min_sequence(cs,ct,a,b) 


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



def spies_dp(s,t,a="(",b=")"):
    n=len(s)
    m=len(t)
    dp=create_matrix(s,t,n,m)
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            dp[i][j] = get_better_chain(dp[i-1][j], dp[i][j-1],dp[0][j],dp[i][0],a,b)
    # return dp[len(dp)-1][ len(dp[0])-1]            
    return get_balance(dp[len(dp)-1][ len(dp[0])-1],a,b)
            

# s="(()("
# t= ")))"

s=")((()(("      
t="))(((((()"


a=spies_dp(s,t)
print(a,len(a))

# print(")"*5)