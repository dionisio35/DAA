import numpy as np



def create_matrix(s,t,n,m):
    dp= [["" for j in range(m+1)] for i in range(n+1) ] #create the nXm matrix

    for i in range(1,len(dp)):
        dp[i][0]=s[0:i]

    for i in range(1,len(dp[0])):
        dp[0][i]=t[0:i]
    # return np.array(dp)
    return dp

def is_subsequence(l: list, subl: list):
    '''...'''
    pos=0
    for i in l:
        if i == subl[pos]:
            pos+=1
        if pos == len(subl):
            return True
    return False

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
    # print(ct,cs,t,s)
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
    # dp = [[""]*m for _ in range(n)] #create the nXm matrix
    dp=create_matrix(s,t,n,m)
    # print(dp)
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            #se puede hacer la matriz lara i = 0 o j = 0 desde aqui    
            if(i==2 and j==3):
                print("here")
            a = get_better_chain(dp[i-1][j], dp[i][j-1],dp[0][j],dp[i][0])
            print(a)
            dp[i][j] = a
            print(i,j,dp[i][j])
    print(dp)
    return dp[len(dp)-1][ len(dp[0])-1]
            

# def spies_dp(s,t):
#     n=len(s)
#     m=len(t)
#     # dp = [[""]*m for _ in range(n)] #create the nXm matrix
#     dp=create_matrix(s,t,n,m)
#     # print(dp)
#     for i in range(1,dp.shape[0]):
#         for j in range(1,dp.shape[1]):
#             #se puede hacer la matriz lara i = 0 o j = 0 desde aqui    
#             if(i==2 and j==3):
#                 print("here")
#             a = get_better_chain(dp[i-1,j], dp[i,j-1],dp[0,j],dp[i,0])
#             print(a)
#             dp[i,j] = a
#             print(i,j,dp[i,j])
#     print(dp)
#     return dp[dp.shape[0]-1, dp.shape[1]-1]
            

# s="pepepe"
# t="jajajaja"

s="(()("
t= ")))"

a=spies_dp(s,t)
print(a,len(a))



# m=len(t)
# n=len(s)
# dp= [["" for j in range(m+1)] for i in range(n+1) ] #create the nXm matrix

# for i in range(1,len(dp)):
#     dp[i][0]=s[i-1]

# for i in range(1,len(dp[0])):
#     dp[0][i]=t[i-1]
# dp=np.array(dp)


# print(dp)
# print(dp)
# print(dp[0,1])
# dp[5][3]=3
# print(dp)
# dp=np.arange((len(s)+1)*(len(t)+1)).reshape(len(t)+1,len(s)+1)
# print(dp)
# print(dp.size,dp.shape)
