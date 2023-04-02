# from first_solve import solve as solve1
# from second_solve import solve as solve2
from generator import generate_n
from brute_force import brute_force_algorithm

import sys
from time import time
from colorama import init, Fore


def same_solution(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    return True

def error(solution):
    print('===================================')
    print()
    print('Fail:')
    print(solution, 'is not a solution')
    print()
    print('===================================')


def test(method, times:int, min_len:int, max_len:int):
    init()
    gen = generate_n(times, min_len, max_len)
    
    count_errors=0
    time_bf=0
    time_best=0
    for i in range(times):
        
        t= time()
        bf_solves = brute_force_algorithm(gen[i][0], gen[i][1])
        time_bf+= time()- t

        t= time()
        test_solve= method(gen[i][0], gen[i][1])
        time_best+= time()- t

        if isinstance(test_solve, list):
            if not same_solution(test_solve, bf_solves):
                count_errors+=1
                error(test_solve)
                
        else:
            if test_solve not in bf_solves:
                count_errors+=1
                error(test_solve)

    print()
    print(Fore.BLUE + 'Ran {} tests in {:.2f} seconds'.format(times, time_best+time_bf))
    print(Fore.CYAN + 'Brute force time: {:.2f} seconds'.format(time_bf))
    print(Fore.CYAN + 'Test method time: {:.2f} seconds'.format(time_best))
    print()

    if count_errors == 0:
        print(Fore.GREEN + 'OK')
    else:
        print(Fore.RED + 'FAILED(failures={})'.format(count_errors))
    print()
    

if __name__ == '__main__':
    times = int(sys.argv[1])
    min = int(sys.argv[2])
    max = int(sys.argv[3])
    test(brute_force_algorithm, times, min, max)