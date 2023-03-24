from generator import generate_n
from first_solve import solve


def test(method:function, times:int, min_len:int,max_len:int):
    gen = generate_n(times,min_len,max_len)
    for i in range(times):
        real_solves:list = solve(gen[i][0],gen[i][1])
        test_solve=method(gen[i][0],gen[i][1])
        if(real_solves.__contains__(test_solve)):
            print(f"Solution = {test_solve} that is CORRECT")
        else:
            print(f"Solution = {test_solve} that is INCORRECT")




        


