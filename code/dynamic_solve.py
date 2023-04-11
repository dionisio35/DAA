def dp_solution(s:str, t:str):
    dp = generate_matrix(s, t)
    sol = generate_solution(s, t, dp)
    return sol


def generate_matrix(s:str, t:str):
    dp= {(0, 0): {0: 0}}

    for s_pos in range(len(s) + 1):
        for t_pos in range(len(t) + 1):
            for balance, lenght in zip(dp[(s_pos, t_pos)].keys(), dp[(s_pos, t_pos)].values()):
                
                # generate next dictionaries
                if s_pos < len(s) and t_pos < len(t) and dp.get((s_pos + 1, t_pos + 1)) == None:
                    dp[(s_pos + 1, t_pos + 1)]= dict()
                if s_pos < len(s) and dp.get((s_pos + 1, t_pos)) == None:
                    dp[(s_pos + 1, t_pos)]= dict()
                if t_pos < len(t) and dp.get((s_pos, t_pos + 1)) == None:
                    dp[(s_pos, t_pos + 1)]= dict()
                
                # diagonal case
                if s_pos < len(s) and t_pos < len(t) and s[s_pos] == t[t_pos]:
                    
                    current = balance + 1 if s[s_pos] == '(' else balance -1
                    if current >= 0:
                        if dp[(s_pos + 1, t_pos + 1)].get(current) is not None:
                            dp[(s_pos + 1, t_pos + 1)][current] = min(dp[(s_pos + 1, t_pos + 1)][current], dp[(s_pos, t_pos)][balance] + 1)
                        else:
                            dp[(s_pos + 1, t_pos + 1)][current] = dp[(s_pos, t_pos)][balance] + 1
                    else:
                        if dp[(s_pos + 1, t_pos + 1)].get(balance) is not None:
                            dp[(s_pos + 1, t_pos + 1)][balance] = min(dp[(s_pos + 1, t_pos + 1)][balance], dp[(s_pos, t_pos)][balance] + 2)
                        else:
                            dp[(s_pos + 1, t_pos + 1)][balance] = dp[(s_pos, t_pos)][balance] + 2

                # horizontal case
                if s_pos  < len(s):
                    current = balance + 1 if s[s_pos] == '(' else balance -1
                    if current >= 0:
                        if dp[(s_pos + 1, t_pos)].get(current) is not None:
                            dp[(s_pos + 1, t_pos)][current] = min(dp[(s_pos + 1, t_pos)][current], dp[(s_pos, t_pos)][balance] + 1)
                        else:
                            dp[(s_pos + 1, t_pos)][current] = dp[(s_pos, t_pos)][balance] + 1
                    else:
                        if dp[(s_pos + 1, t_pos)].get(balance) is not None:
                            dp[(s_pos + 1, t_pos)][balance] = min(dp[(s_pos + 1, t_pos)][balance], dp[(s_pos, t_pos)][balance] + 2)
                        else:
                            dp[(s_pos + 1, t_pos)][balance] = dp[(s_pos, t_pos)][balance] + 2
                

                # vertical case
                if t_pos  < len(t):
                    current = balance + 1 if t[t_pos] == '(' else balance -1
                    if current >= 0:
                        if dp[(s_pos, t_pos + 1)].get(current) is not None:
                            dp[(s_pos, t_pos + 1)][current] = min(dp[(s_pos, t_pos + 1)][current], dp[(s_pos, t_pos)][balance] + 1)
                        else:
                            dp[(s_pos, t_pos + 1)][current] = dp[(s_pos, t_pos)][balance] + 1
                    else:
                        if dp[(s_pos, t_pos + 1)].get(balance) is not None:
                            dp[(s_pos, t_pos + 1)][balance] = min(dp[(s_pos, t_pos + 1)][balance], dp[(s_pos, t_pos)][balance] + 2)
                        else:
                            dp[(s_pos, t_pos + 1)][balance] = dp[(s_pos, t_pos)][balance] + 2

    return dp



def generate_solution(s: str, t: str, dp):
    balance= sorted(list(dp[(len(s), len(t))].keys()))[0]
    solution= ')' * balance
    s_pos = len(s)
    t_pos = len(t)

    while s_pos > 0 or t_pos > 0:
        
        # diagonal case
        if s_pos>0 and t_pos>0 and s[s_pos-1] == t[t_pos-1]:
            
            current= 1 if s[s_pos - 1] == '(' else -1
            if (dp[(s_pos, t_pos)].get(balance) is not None
                and dp[(s_pos-1, t_pos-1)].get(balance-current) is not None
                and dp[(s_pos, t_pos)].get(balance) == dp[(s_pos-1, t_pos-1)].get(balance-current) + 1):

                solution+= s[s_pos - 1]
                balance -= current
                s_pos-=1
                t_pos-=1
                continue
            
            elif (balance == 0
                  and s[s_pos-1] == ')'
                  and dp[(s_pos-1, t_pos-1)].get(balance) is not None
                  and dp[(s_pos, t_pos)].get(balance) is not None
                  and dp[(s_pos-1, t_pos-1)].get(balance) + 2 == dp[(s_pos, t_pos)].get(balance)):
                
                solution+=')('
                s_pos-=1
                t_pos-=1
                continue
        
        # horizontal case
        if s_pos>0:

            current= 1 if s[s_pos - 1] == '(' else -1
            if (dp[(s_pos, t_pos)].get(balance) is not None
                and dp[(s_pos-1, t_pos)].get(balance-current) is not None
                and dp[(s_pos, t_pos)].get(balance) == dp[(s_pos-1, t_pos)].get(balance-current) + 1):

                solution+= s[s_pos - 1]
                balance -= current
                s_pos-=1
                continue
            elif (balance == 0
                  and s[s_pos-1] == ')'
                  and dp[(s_pos-1, t_pos)].get(balance) is not None
                  and dp[(s_pos, t_pos)].get(balance) is not None
                  and dp[(s_pos-1, t_pos)].get(balance) + 2 == dp[(s_pos, t_pos)].get(balance)):
                
                solution+=')('
                s_pos-=1
                continue
        
        # vertical case
        if t_pos>0:

            current= 1 if t[t_pos - 1] == '(' else -1
            if (dp[(s_pos, t_pos)].get(balance) is not None
                and dp[(s_pos, t_pos-1)].get(balance-current) is not None
                and dp[(s_pos, t_pos)].get(balance) == dp[(s_pos, t_pos-1)].get(balance-current) + 1):

                solution+= t[t_pos - 1]
                balance -= current
                t_pos-=1
                continue
            
            elif (balance == 0
                  and t[t_pos-1] == ')'
                  and dp[(s_pos, t_pos-1)].get(balance) is not None
                  and dp[(s_pos, t_pos)].get(balance) is not None
                  and dp[(s_pos, t_pos-1)].get(balance) + 2 == dp[(s_pos, t_pos)].get(balance)):
                
                solution+=')('
                t_pos-=1
                continue
    
    return ''.join([i for i in reversed(solution)])

