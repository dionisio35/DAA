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
                    if s[i-1] == t[i-1]:
                        if s[i-1]==")": 
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
                    if s[i-1]==")":
                        if k>0:
                            dp[i+1][j][k-1] = min(dp[i][j][k]+1, dp[i+1][j][k-1] if dp[i+1][j].get(k-1) else 2e31)
                        else:
                            dp[i+1][j][k] = min(dp[i][j][k]+2, dp[i+1][j][k] if dp[i+1][j].get(k) else 2e31)
                    else:
                        dp[i+1][j][k+1] = min(dp[i][j][k]+1, dp[i+1][j][k+1] if dp[i+1][j].get(k+1) else 2e31)

                #i,j+1,k
                if j+1<=m:
                    if t[j-1]==")":
                        if k > 0:
                            dp[i][j+1][k-1] = min(dp[i][j][k]+1, dp[i][j+1][k-1] if dp[i][j+1].get(k-1) else 2e31)
                        else:
                            dp[i][j+1][k] = min(dp[i][j][k]+2, dp[i][j+1][k] if dp[i][j+1].get(k) else 2e31)
                    else:
                        dp[i][j+1][k+1] = min(dp[i][j][k]+1, dp[i][j+1][k+1] if dp[i][j+1].get(k+1) else 2e31)


     ########################################################               
    for i in range(len(dp)):
        for j in range(len(dp[i])):

            print(i,j,dp[i][j])
    print(np.array(dp))


                
               


s="())("
t=")((("

a=dp5(s,t)

