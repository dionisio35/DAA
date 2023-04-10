import numpy as np

def create_matrix(s,t,n,m):
    dp= [[ dict()  for j in range(m+1)] for i in range(n+1) ] #create the nXm matrix
    dp[0][0][0]=0

    # if s[0]==t[0] and s[0]=="(":
    #     dp[0][1][1]=1
    #     dp[1][0][1]=1 
    # else: 
    #     dp[0][1][0]=2
    #     dp[1][0][0]=2
    
    for i in range(1,len(dp)):
        for k in dp[i-1][0].keys():
            if s[i-1]==")": 
                if k==0:
                    dp[i][0][k]= dp[i-1][0][k]+2
                else:
                    dp[i][0][k-1]= dp[i-1][0][k]+1
            else:
                dp[i][0][k+1] = dp[i-1][0][k]+1
            
    for j in range(1,len(dp[0])):
        for k in dp[0][j-1].keys():
            if t[j-1]==")": 
                if k==0:
                    dp[0][j][k]= dp[0][j-1][k]+2
                else:
                    dp[0][j][k-1]= dp[0][j-1][k]+1
            else:
                dp[0][j][k+1] = dp[0][j-1][k]+1

    return dp


# def get_k_l(i,j,k,dp,s,t):




def dp5(s,t,a="(",b=")"):
    n=len(s)
    m=len(t)
    dp=create_matrix(s,t,n,m)
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            
            for k in dp[i-1][j-1].keys():                
                if s[i-1] == t[i-1]:
                    if s[i-1]==")": 
                        if k > 0:
                            dp[i][j][k-1] = dp[i-1][j-1][k]+1
                        else:
                            dp[i][j][k] = dp[i-1][j-1][k]+2
                    else:
                        dp[i][j][k+1] = dp[i-1][j-1][k]+1
                else:
                    dp[i][j][k] = dp[i-1][j-1][k]+2
    

            for k in dp[i-1][j].keys():
                if s[i-1]==")":
                    if k>0:
                        dp[i][j][k-1] = dp[i-1][j][k]+1
                    else:
                        dp[i][j][k] = dp[i-1][j][k]+2
                else:
                    dp[i][j][k+1] = dp[i-1][j][k]+1


            for k in dp[i][j-1].keys():
                if t[j-1]==")":
                    if k > 0:
                        dp[i][j][k-1] = dp[i][j-1][k]+1
                    else:
                        dp[i][j][k] = dp[i][j-1][k]+2
                else:
                    dp[i][j][k+1] = dp[i][j-1][k]+1

     ########################################################               
    for i in range(len(dp)):
        for j in range(len(dp[i])):

            print(i,j,dp[i][j])
    print(np.array(dp))


 