from tools import *
from dp import *


def create_matrix(s,t,n,m):
    dp= [[[] for j in range(m+1)] for i in range(n+1) ] #create the nXm matrix
    dp[0][0]=[("",0)]
    return dp

def get_min(l):
    minm=2e31
    chain=""
    for c in l:
        temp=c[0]+")"*c[1]
        if len(temp)<minm:
            minm=len(temp)
            chain=temp
    return chain

def is_subsequence(l: list, subl: list):
    if len(subl)==0:
        return False
    pos=0
    for i in l:
        if i == subl[pos]:
            pos+=1
        if pos == len(subl):
            return True
    return False




def dp3(s,t,a="(",b=")"):
    n=len(s)
    m=len(t)
    dp=create_matrix(s,t,n,m)
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            for chain in dp[i][j]:
                if i+1<=n and j+1<=m:
                    
                    if is_subsequence(chain[0],s[0:i-1]) and is_subsequence(chain[0],t[0:j-1]):
                        dp[i+1][j+1].append((chain[0],chain[1]))

                    if s[i-1] == t[i-1]:
                        if s[i-1]==")":
                            if chain[1] > 0:
                                dp[i+1][j+1].append((chain[0]+")",chain[1]-1))
                            else:
                                dp[i+1][j+1].append((chain[0]+"()",0))
                        else:
                            dp[i+1][j+1].append((chain[0]+"(",chain[1]+1))
                    else:
                        dp[i+1][j+1].append((chain[0]+"()",chain[1]))
                        if chain[1]>0:
                            dp[i+1][j+1].append((chain[0]+")(",chain[1]))

                if i+1<=n:
                    if is_subsequence(chain[0],s[0:i-1]) :
                        dp[i+1][j].append((chain[0],chain[1]))

                    if s[i-1]==")":
                        if chain[1]>0:
                            dp[i+1][j].append((chain[0]+")",chain[1]-1))
                        else:
                            dp[i+1][j].append((chain[0]+"()",0))
                    else:
                        dp[i+1][j].append((chain[0]+"(",chain[1]+1))
                
                if j+1<=m:
                    if is_subsequence(chain[0],t[0:j-1]):
                        dp[i][j+1].append((chain[0],chain[1]))
                    if t[j-1]==")":
                        if chain[1]>0:
                            dp[i][j+1].append((chain[0]+")",chain[1]-1))
                        else:
                            dp[i][j+1].append((chain[0]+"()",0))
                    else:
                        dp[i][j+1].append((chain[0]+"(",chain[1]+1))

    return get_min(dp[n][m])
