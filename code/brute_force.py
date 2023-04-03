from tools import *

def generate_all_balanced_len_n(n, mem):
    """generate all the sequences balanced of lenth n"""
    n_list=[]
    for c in mem[n-1]:
        n_list.append(c + "(")
        n_list.append(c + ")")
    return n_list

def solved(elems, s, t):
    solv=[]
    for i in elems:
        if(is_subsequence(i, s) and is_subsequence(i, t) and is_valid(i)):
            solv.append(i)
    return solv

def brute_force_algorithm(s:str, t:str):
    """generate all solutions"""
    mem=[[""]]
    for i in range(1, 2*(len(s) + len(t))):
        mem.append(generate_all_balanced_len_n(i, mem))
        solutions_n=solved(mem[i], s, t)
        if(len(solutions_n)):
            return solutions_n