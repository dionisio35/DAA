
from tools import *
from dp3 import *
from brute_force import *

def dp4(s,t,a="(",b=")"):
    n = len(s)
    m = len(t)    
    if n>m:
        t=t+s[m:n]
    elif m>n:
        s=s+t[n:m]
    n=max(n,m)
    dp = [set() for i in range(n+1)]
    dp[0].add("")
    for i in range(n):  
        for k in dp[i]: 
            ss1=is_subsequence(k, s[0:i+1])
            ss2=is_subsequence(k, t[0:i+1])
            if  ss1 and ss2:   
                dp[i+1].add(k)
            if ss1:
                dp[i+1].add(k+t[i])
            if ss2:
                dp[i+1].add(k+s[i])            
            if s[i]==t[i]:  
                dp[i+1].add(k+s[i])
            else:            
                dp[i+1].add(k+s[i]+t[i])
                dp[i+1].add(k+t[i]+s[i])
        print(i+1,dp[i+1])
    solutions = get_balanced_chains(dp[n],a,b)
    return get_min(solutions)


    
s="())("
t=")((("

# s="(()("
# t=")((("


# s="()())" 
# t="(()))"


s="()(("
t= "))()"


from time import time

t1=time()
a=dp4(s,t)
t2=time()
b=brute_force_algorithm(s,t)
t3=time()
# c=solve(s,t)
# t4=time()

print("dp4",a,len(a),t2-t1)
print("brute_force_algorithm",b,len(b[0]),t3-t2)
# print("solve",c,len(c[0]),t4-t3)
    







