from generator import generate_n
from first_solve import solve as solve1
from second_solve import solve as solve2

from time import time

def same_solution(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    return True


def test(method, times:int, min_len:int, max_len:int):
    gen = generate_n(times, min_len, max_len)
    
    print('generated  ', gen)
    for i in range(times):
        
        t= time()
        real_solves:list = solve1(gen[i][0], gen[i][1])
        print('brute force time', time()- t)
        t= time()
        test_solve= method(gen[i][0], gen[i][1])
        print('test time', time()- t)

        if same_solution(test_solve, real_solves):
            print(f"Solution = {test_solve} that is CORRECT")
        else:
            print(f"Solution = {test_solve} that is INCORRECT")



test(solve2, 1, 10,11)
        


