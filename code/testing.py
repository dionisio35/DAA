from generator import generate_n

from brute_force import brute_force_algorithm
from dynamic_solve import solve_fast, fast
from dp2 import dp2

from time import time
from colorama import init, Fore
import argparse
from argparse import Namespace


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


def test(method, times:int, min_len:int, max_len:int, seed:int=None):
    init()
    if seed:
        generated_cases = generate_n(times, min_len, max_len, seed=seed)
    else:
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Spies")
    parser.add_argument('-m', help="Method to test", type=str, default='dp2', choices=['dp2', 'fast', 'solve_fast'])
    parser.add_argument('-l', help="Max string", type=int)
    parser.add_argument('-r', help="Min and max range of string", type=int, nargs=2)
    parser.add_argument('-s', help="Seed", type=int, default=None)
    parser.add_argument('-t', help="Times to run", type=int, default=1)
    args: Namespace = parser.parse_args()

    if args.m == 'dp2':
        method = dp2
    elif args.m == 'fast':
        method = fast
    elif args.m == 'solve_fast':
        method = solve_fast

    if args.l:
        test(method, args.t, args.l, args.l, args.s)
    elif args.r:
        test(method, args.t, args.r[0], args.r[1], args.s)
    else:
        test(method, args.t, 1, 10, args.s)