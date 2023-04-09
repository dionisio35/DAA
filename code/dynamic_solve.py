import numpy as np


def balanced(l: list):
    n= 0
    b= 0
    for i in l:
        if i == '(':
            n+=1
        if i == ')':
            if n == 0:
                b+=1
            else:
                n-=1
    return n + b

def f(l):
    return len(l) + balanced(l)


def balance(l):
    open=0
    close=0
    for i in l:
        if i == '(':
            close+=1
        if i == ')':
            if close == 0:
                open+=1
            else:
                close-=1

    new_l=l
    for _ in range(open):
        new_l= '(' + new_l
    for _ in range(close):
        new_l = new_l + ')'
    return new_l



def is_subsequence(l: list, subl: list):
    pos=0
    for i in l:
        if i == subl[pos]:
            pos+=1
        if pos == len(subl):
            return True
    return False



def set_balance(s: set, new: str) -> set:
    if not s.issubset({}):
        temp= s.pop()
        if f(temp) == f(new):
            s.add(temp)
            s.add(new)
        elif f(temp) > f(new):
            s= {new}
        else:
            s.add(temp)
        return s
    return {new}



def solve_fast(s:list, t:list):
    dp= {(0, 0): {s[0]}} if s[0] == t[0] else {(0, 0): {'()'}}

    for s_pos in range(len(s)):
        for t_pos in range(len(t)):

            if s_pos + 1 < len(s) and t_pos + 1 < len(t) and dp.get((s_pos + 1, t_pos + 1)) == None:
                dp[(s_pos + 1, t_pos + 1)]= set()
            if s_pos + 1 < len(s) and dp.get((s_pos + 1, t_pos)) == None:
                dp[(s_pos + 1, t_pos)]= set()
            if t_pos + 1 < len(t) and dp.get((s_pos, t_pos + 1)) == None:
                dp[(s_pos, t_pos + 1)]= set()
            
            for l in dp[(s_pos, t_pos)]:
                
                # diagonal case
                if s_pos + 1 < len(s) and t_pos + 1 < len(t):
                    if s[s_pos + 1] == t[t_pos + 1]:
                        dp[(s_pos + 1, t_pos + 1)] = set_balance(dp[(s_pos + 1, t_pos + 1)], l + s[s_pos + 1])
                    # else:
                    #     dp[(s_pos + 1, t_pos + 1)] = set_balance(dp[(s_pos + 1, t_pos + 1)], l + '()')
                
                    else:
                        if is_subsequence(l + '(', t[:t_pos + 2]) and is_subsequence(l + '(', s[:s_pos + 2]):
                            dp[(s_pos + 1, t_pos + 1)] = set_balance(dp[(s_pos + 1, t_pos + 1)], l + '(')

                        elif is_subsequence(l + ')', t[:t_pos + 2]) and is_subsequence(l + ')', s[:s_pos + 2]):
                            dp[(s_pos + 1, t_pos + 1)] = set_balance(dp[(s_pos + 1, t_pos + 1)], l + ')')

                        else:
                            dp[(s_pos + 1, t_pos + 1)] = set_balance(dp[(s_pos + 1, t_pos + 1)], l + '()')
                    
                # horizontal case
                if s_pos + 1 < len(s):
                    if is_subsequence(l, s[:s_pos + 2]):
                        dp[(s_pos + 1, t_pos)] = set_balance(dp[(s_pos + 1, t_pos)], l)

                    else:
                        dp[(s_pos + 1, t_pos)] = set_balance(dp[(s_pos + 1, t_pos)], l + s[s_pos + 1])
                
                # vertical case
                if t_pos + 1 < len(t):
                    if is_subsequence(l, t[:t_pos + 2]):
                        dp[(s_pos, t_pos + 1)] = set_balance(dp[(s_pos, t_pos + 1)], l)

                    else:
                        dp[(s_pos, t_pos + 1)] = set_balance(dp[(s_pos, t_pos + 1)], l + t[t_pos + 1])
    
    # print ('dp', dp)
    # print('l', dp[(len(s)-1, len(t)-1)])

    return [balance(x) for x in dp[(len(s)-1, len(t)-1)]]


def fast(s:list, t:list):
    dp= {(-1, -1): {''}}

    for s_pos in range(-1, len(s)):
        for t_pos in range(-1, len(t)):

            if s_pos + 1 < len(s) and t_pos + 1 < len(t) and dp.get((s_pos + 1, t_pos + 1)) == None:
                dp[(s_pos + 1, t_pos + 1)]= set()
            if s_pos + 1 < len(s) and dp.get((s_pos + 1, t_pos)) == None:
                dp[(s_pos + 1, t_pos)]= set()
            if t_pos + 1 < len(t) and dp.get((s_pos, t_pos + 1)) == None:
                dp[(s_pos, t_pos + 1)]= set()
            
            for l in dp[(s_pos, t_pos)]:
                
                # diagonal case
                if s_pos + 1 < len(s) and t_pos + 1 < len(t):
                    if s[s_pos + 1] == t[t_pos + 1]:
                        dp[(s_pos + 1, t_pos + 1)] = set_balance(dp[(s_pos + 1, t_pos + 1)], l + s[s_pos + 1])
                
                    else:
                        if is_subsequence(l + '(', t[:t_pos + 2]) and is_subsequence(l + '(', s[:s_pos + 2]):
                            dp[(s_pos + 1, t_pos + 1)] = set_balance(dp[(s_pos + 1, t_pos + 1)], l + '(')

                        elif is_subsequence(l + ')', t[:t_pos + 2]) and is_subsequence(l + ')', s[:s_pos + 2]):
                            dp[(s_pos + 1, t_pos + 1)] = set_balance(dp[(s_pos + 1, t_pos + 1)], l + ')')

                        else:
                            dp[(s_pos + 1, t_pos + 1)] = set_balance(dp[(s_pos + 1, t_pos + 1)], l + '()')
                    
                # horizontal case
                if s_pos + 1 < len(s):
                    if is_subsequence(l, s[:s_pos + 2]):
                        dp[(s_pos + 1, t_pos)] = set_balance(dp[(s_pos + 1, t_pos)], l)

                    else:
                        dp[(s_pos + 1, t_pos)] = set_balance(dp[(s_pos + 1, t_pos)], l + s[s_pos + 1])
                
                # vertical case
                if t_pos + 1 < len(t):
                    if is_subsequence(l, t[:t_pos + 2]):
                        dp[(s_pos, t_pos + 1)] = set_balance(dp[(s_pos, t_pos + 1)], l)

                    else:
                        dp[(s_pos, t_pos + 1)] = set_balance(dp[(s_pos, t_pos + 1)], l + t[t_pos + 1])
    
    print ('dp', dp)
    return [balance(x) for x in dp[(len(s)-1, len(t)-1)]]



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






