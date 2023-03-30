
from generator import generate_n
from LCS import LCS
from first_solve import solve
from brute_force import *


def get_balance(l,a,b):
    balance=0
    balanced=""
    for i in l:
        if balance:
            balance-=1
            balanced+=i
        else:            
            balanced+= i + a if i == b else i
    return balanced


def greedy(s,t,a="(",b=")"):
    balance=0
    i_s=0
    i_t=0
    selected=""
    solution=""
    while True:
        if(i_s==len(s) and i_t==len(t)):
            return solution
        if(i_s==len(s)):
            solution += t[i_t:len(t)-1]
            return get_balance(solution,a,b)
        if(i_t==len(t)):
            solution += s[i_t:len(s)-1]
            return get_balance(solution,a,b)

        if not balance:
            selected = a
            i_s+= 1 if s[i_s]==a else 0
            i_t+= 1 if t[i_t]==a else 0
        elif(s[i_s]==t[i_t]): #equals options and balance > 0 we choose b
            selected = s[i_s]          
            i_s+=1
            i_t+=1
        elif(balance): #diferents options and balance > 0 we choose b
            selected = b
            if s[i_s] == b : i_s += 1
            else: i_t += 1
        else:  #diferents options and balance == 0 we choose a
            selected=a
            if s[i_s] == a : i_s += 1
            else: i_t += 1
        solution+=selected
        balance += 1 if selected == a else -1
        


def comprobate(lcs, sols:list):
    for sol in sols:
        if(not lcs in sol):
            return False
    return True



# a = generate_n(1,5,10,"(",")")
# for i in a:
#     l1=i[0]
#     l2=i[1]
#     lcs=LCS(l1,l2)
#     solve_i="".join(brute_force_algorithm(l1,l2))
#     print([comprobate(lcs,j) for j in solve_i])

print("aaa",greedy("())((","(()()("))
