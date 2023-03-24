#idea de generar todas las cadenas de tamanno de la mayor de las secuencias a el doble de la suma de varios tamannos 
#y quedarse con las de menor tamanno 
def generate_all_balanced_len_n(n):
    """generate all the sequences balanced of lenth n"""
    ...

def brute_force_algorithm(s:str,t:str):
    """generate all solutions"""
    for i in range(max(len(s),len(t)),2*(len(s)+len(t))):
        generate_all_balanced_len_n(i)
