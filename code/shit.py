
def fast_solve(s, t):
    dp= dict()

    ps= []
    l=''
    for i in s:
        l= l + i
        ps.append(l)
    pt= []
    l=''
    for i in t:
        l= l + i
        pt.append(l)
    
    l=''
    for i in range(len(s)):
        
        if i+1 < len(s) and is_subsequence(l, ps[i+1]):
            l=l
        else:
            if s[i] == t[i]:
                l= l + s[i]
            else:
                if i+1 < len(s) and s[i+1] != t[i+1]:
                    l = l + ')('
                else:
                    l= l + '()'
        dp[i] = l

        if is_subsequence(dp[i], s) and is_subsequence(dp[i], t):
            print(dp)
            return balance(dp[i])
    print(dp)
    return balance(dp[len(s)-1])



def fast_bf(s, t):
    dp= {0: ['']}
    for i in range(len(s)):
        dp[i+1] = []
        for l in dp[i]:

            if i+1 < len(s) and is_subsequence(l, s[:i+1]) and is_subsequence(l, t[:i+1]):
                dp[i+1].append(l)
            
            elif s[i] == t[i]:
                dp[i+1].append(l + s[i])
            
            else:
                if i+1 < len(s) and is_subsequence(l+'(', t[:i+2]) and is_subsequence(l+'(', s[:i+2]):
                    dp[i+1].append(l + '(')
                elif i+1 < len(s) and is_subsequence(l + ')', t[:i+2]) and is_subsequence(l+'(', s[:i+2]):
                    dp[i+1].append(l + ')')
                else:
                    dp[i+1].append(l + '()')
                    dp[i+1].append(l + ')(')

    print(dp)
    print(dp[(len(s))])
    
    l=[dp[(len(s))][0]]
    for i in dp[(len(s))]:
        if len(l[0]) + balanced(l[0]) > len(i) + balanced(i):
            l = [i]
        elif len(l[0]) + balanced(l[0]) == len(i) + balanced(i):
            l.append(i)
    return [balance(x) for x in l][0]



def sol(dp: dict, s, t):
    for i in dp:
        if is_subsequence(i, s) and is_subsequence(i, t):
            return balance(i)
    return balance(dp[(len(s)-1, len(t)-1)])



def matrix(d):
    max_s=0
    max_t=0
    for i in list(d):
        if max_s < i[0]:
            max_s= i[0]
        if max_t < i[1]:
            max_t= i[1]

    m=[]
    for s in range(max_s+1):
        temp=[]
        for t in range(max_t+1):
            temp.append(d[(t,s)])
        m.append(temp)
    print(np.array(m))




def solve(s:list, t:list):
    ps= []
    l=''
    for i in s:
        l= l + i
        ps.append(l)
    pt= []
    l=''
    for i in t:
        l= l + i
        pt.append(l)

    dp= dict()
    if s[0] == t[0]:
        dp[(0, 0)] = s[0]
    else:
        dp[(0, 0)] = '()'

    for s_pos in range(len(s)):
        for t_pos in range(len(t)):

            # diagonal case
            if s_pos + 1 < len(s) and t_pos + 1 < len(t):
                
                if s[s_pos + 1] == t[t_pos + 1]:
                    new= dp[(s_pos, t_pos)] + s[s_pos + 1]

                    if dp.get((s_pos + 1, t_pos + 1)) == None:
                        dp[(s_pos + 1, t_pos + 1)]= new
                    
                    else:
                        current= dp[(s_pos+1, t_pos+1)]
                        dp[(s_pos + 1, t_pos + 1)]= (
                            new
                            if len(new) + balanced(new) <= len(current) + balanced(current)
                            else current
                        )
            
                if s[s_pos + 1] != t[t_pos + 1]:
                    new= dp[(s_pos, t_pos)] + '()'

                    if dp.get((s_pos + 1, t_pos + 1)) == None:
                        dp[(s_pos + 1, t_pos + 1)]= new
                    
                    else:
                        current= dp[(s_pos+1, t_pos+1)]
                        dp[(s_pos + 1, t_pos + 1)]= (
                            new
                            if len(new) + balanced(new) <= len(current) + balanced(current)
                            else current
                        )
                                    
            # horizontal case
            if s_pos+1 < len(s):
                if is_subsequence(dp[(s_pos, t_pos)], ps[s_pos+1]):
                    new= dp[(s_pos, t_pos)]
                else:
                    new= dp[(s_pos, t_pos)] + s[s_pos + 1]

                if dp.get((s_pos + 1, t_pos)) == None:
                    dp[(s_pos + 1, t_pos)]= new

                else:
                    current= dp[(s_pos + 1, t_pos)]
                    dp[(s_pos+1, t_pos)]= (
                        new
                        if len(new) + balanced(new) <= len(current) + balanced(current)
                        else current
                    )
            
            # vertical case
            if t_pos+1 < len(t):
                if is_subsequence(dp[(s_pos, t_pos)], pt[t_pos+1]):
                    new= dp[(s_pos, t_pos)]
                else:
                    new= dp[(s_pos, t_pos)] + t[t_pos + 1]

                if dp.get((s_pos, t_pos + 1)) == None:            
                    dp[(s_pos, t_pos + 1)]= new
                
                else:
                    current= dp[(s_pos, t_pos + 1)]
                    dp[(s_pos, t_pos + 1)]= (
                            new
                            if len(new) + balanced(new) <= len(current) + balanced(current)
                            else current
                        )
    
    matrix(dp)
    return balance(dp[(len(s)-1, len(t)-1)])
    # return sol(dp, s, t)