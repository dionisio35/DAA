from generator import generate_n
from brute_force import brute_force_algorithm

import sys
from time import time
from colorama import init, Fore
from dp import spies_dp
from dp2 import dp2
# from gpt import menor_cadena_balanceada


def same_solution(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    return True

def error(solution, s1, s2, solutions):
    print('===================================')
    print()
    print(Fore.RED +  'Fail:', Fore.RESET)
    print('{} is not a solution of {}, {}'.format(solution, s1, s2))
    print('Expected: {}'.format(solutions))
    print()
    print('===================================')


def test(method, times:int, min_len:int, max_len:int):
    init()
    generated_cases = generate_n(times, min_len, max_len)
    
    count_errors=0
    time_bf=0
    time_best=0
    for case in generated_cases:
        
        t= time()
        bf_solves = brute_force_algorithm(case[0], case[1])
        time_bf+= time()- t

        t= time()
        test_solve= method(case[0], case[1])
        time_best+= time()- t

        if isinstance(test_solve, list):
            if not same_solution(test_solve, bf_solves):
                count_errors+=1
                error(test_solve, case[0], case[1], bf_solves)
                
        else:
            if test_solve not in bf_solves:
                count_errors+=1
                error(test_solve, case[0], case[1], bf_solves)

    print()
    print(Fore.BLUE + 'Ran {} tests in {:.2f} seconds'.format(times, time_best+time_bf))
    print('Brute force time: {:.2f} seconds'.format(time_bf))
    print('Test method time: {:.2f} seconds'.format(time_best), Fore.RESET)
    print()

    if count_errors == 0:
        print(Fore.GREEN + 'OK', Fore.RESET)
    else:
        print(Fore.RED + 'FAILED(failures={})'.format(count_errors), Fore.RESET)
    print()
    
import argparse

if __name__ == '__main__':
    times = int(sys.argv[1])
    try:
        min = int(sys.argv[2])
        max = int(sys.argv[3])
        # test(spies_dp, times, min, max)
        test(dp2, times, min, max)


    except IndexError:
        n = int(sys.argv[2])
        # test(spies_dp, times, n, n)
        test(dp2, times, n, n)



    # parser = argparse.ArgumentParser("simple_example")
    # parser.add_argument("counter", help="An integer will be increased by 1 and printed.", type=int)
    # args = parser.parse_args()
    # print(args.counter + 1)