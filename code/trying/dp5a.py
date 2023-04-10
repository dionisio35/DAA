import numpy as np



def create_matrix(s,t,n,m):
    dp= [[ dict()  for j in range(m+1)] for i in range(n+1) ] #create the nXm matrix
    dp[0][0][0]=0
    return dp



def dp5(s,t,a="(",b=")"):
    n=len(s)
    m=len(t)
    dp=create_matrix(s,t,n,m)
    for i in range(len(dp)):
        for j in range(len(dp[0])):            
            for k in dp[i][j].keys():
                #i+1,j+1,k
                if i+1<=n and j+1<=m:
                    if s[i] == t[i]:
                        if s[i]==")": 
                            if k > 0:
                                dp[i+1][j+1][k-1] = min(dp[i][j][k]+1 ,dp[i+1][j+1][k-1] if dp[i+1][j+1].get(k-1) else 2e31)
                            else:
                                dp[i+1][j+1][k] = min(dp[i][j][k]+2 ,dp[i+1][j+1][k] if dp[i+1][j+1].get(k) else 2e31)
                        else:
                            dp[i+1][j+1][k+1] = min(dp[i][j][k]+1, dp[i+1][j+1][k+1] if dp[i+1][j+1].get(k+1) else 2e31)
                    else:
                        dp[i+1][j+1][k] = min(dp[i][j][k]+2, dp[i+1][j+1][k] if dp[i+1][j+1].get(k) else 2e31)
                #i+1,j,k
                if i+1<=n:
                    if s[i]==")":
                        if k>0:
                            dp[i+1][j][k-1] = min(dp[i][j][k]+1, dp[i+1][j][k-1] if dp[i+1][j].get(k-1) else 2e31)
                        else:
                            dp[i+1][j][k] = min(dp[i][j][k]+2, dp[i+1][j][k] if dp[i+1][j].get(k) else 2e31)
                    else:
                        dp[i+1][j][k+1] = min(dp[i][j][k]+1, dp[i+1][j][k+1] if dp[i+1][j].get(k+1) else 2e31)
                #i,j+1,k
                if j+1<=m:
                    if t[j]==")":
                        if k > 0:
                            dp[i][j+1][k-1] = min(dp[i][j][k]+1, dp[i][j+1][k-1] if dp[i][j+1].get(k-1) else 2e31)
                        else:
                            dp[i][j+1][k] = min(dp[i][j][k]+2, dp[i][j+1][k] if dp[i][j+1].get(k) else 2e31)
                    else:
                        dp[i][j+1][k+1] = min(dp[i][j][k]+1, dp[i][j+1][k+1] if dp[i][j+1].get(k+1) else 2e31)
    
    printy(dp)
    return lookback(s,t , dp)

def printy(dp):               
    for i in range(len(dp)):
        for j in range(len(dp[i])):

            print(i,j,dp[i][j])
    print(np.array(dp))



def lookback(s: str, t:str, dp):
    balance= sorted(list(dp[len(s)][len(t)].keys()))[0]
    solution= ')' * balance
    s_pos = len(s)
    t_pos = len(t)

    while s_pos > 0 or t_pos > 0:
        
        if s_pos>0 and t_pos>0 and s[s_pos-1]==t[t_pos-1]:
            
            current= 1 if s[s_pos - 1] == '(' else -1
            if (dp[s_pos][t_pos].get(balance) != None
                and dp[s_pos-1][t_pos-1].get(balance-current) != None
                and dp[s_pos][t_pos].get(balance) == dp[s_pos-1][t_pos-1].get(balance-current) + 1):

                solution+= s[s_pos - 1]
                balance -= current
                s_pos-=1
                t_pos-=1
                continue
            
            elif (balance == 0
                  and s[s_pos-1] == ')'
                  and dp[s_pos-1][t_pos-1].get(balance) != None
                  and dp[s_pos][t_pos].get(balance) != None
                  and dp[s_pos-1][t_pos-1].get(balance) + 2 == dp[s_pos][t_pos].get(balance)):
                
                solution+=')('
                s_pos-=1
                t_pos-=1
                continue
        
        if s_pos>0:

            current= 1 if s[s_pos - 1] == '(' else -1
            if (dp[s_pos][t_pos].get(balance) != None
                and dp[s_pos-1][t_pos].get(balance-current) != None
                and dp[s_pos][t_pos].get(balance) == dp[s_pos-1][t_pos].get(balance-current) + 1):

                solution+= s[s_pos - 1]
                balance -= current
                s_pos-=1
                continue
            elif (balance == 0
                  and s[s_pos-1] == ')'
                  and dp[s_pos-1][t_pos].get(balance) != None
                  and dp[s_pos][t_pos].get(balance) != None
                  and dp[s_pos-1][t_pos].get(balance) + 2 == dp[s_pos][t_pos].get(balance)):
                
                solution+=')('
                s_pos-=1
                continue
        
        if t_pos>0:

            current= 1 if t[t_pos - 1] == '(' else -1
            if (dp[s_pos][t_pos].get(balance) != None
                and dp[s_pos][t_pos-1].get(balance-current) != None
                and dp[s_pos][t_pos].get(balance) == dp[s_pos][t_pos-1].get(balance-current) + 1):

                solution+= t[t_pos - 1]
                balance -= current
                t_pos-=1
                continue
            
            elif (balance == 0
                  and t[t_pos-1] == ')'
                  and dp[s_pos][t_pos-1].get(balance) != None
                  and dp[s_pos][t_pos].get(balance) != None
                  and dp[s_pos][t_pos-1].get(balance) + 2 == dp[s_pos][t_pos].get(balance)):
                
                solution+=')('
                t_pos-=1
                continue
    return ''.join([i for i in reversed(solution)])



                
               


s="())("
t=")((("

a=dp5(s,t)
print(a)
