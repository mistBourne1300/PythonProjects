import graphviz
from sympy import isprime
import numpy as np

def replace(string, index, char):
    return string[:index] + char + string[index+1:]

def prime_sieve(N = 100000):
    """Yield all primes that are less than or equal to N."""
    numbers = np.arange(2,N+1)
    while len(numbers)>0:
        num_zero = numbers[0]
        mask = numbers % num_zero != 0
        numbers = numbers[mask]
        yield num_zero

def digitally_similar_primes(maximum = 1000):
    DIGITS = ['0','1','2','3','4','5','6','7','8','9']
    dot = graphviz.Graph("Prime Connections", "Digits are Forever", strict=True)
    for p in prime_sieve(maximum):
        prime = str(p)
        for i in range(len(prime)):
            for d in DIGITS:
                new_str = replace(prime,i,d)
                new_int = int(new_str)
                if new_int != p and isprime(new_int):
                    dot.edge(prime, str(new_int))
                    print(f'{prime} >> {new_int}')
    
    return dot

    

if __name__ == "__main__":
    import os
    maximum = int(input("enter maximum: "))
    dot = digitally_similar_primes(maximum)
    file = open(f"prime_graphs_source/{maximum}.txt", 'w+')
    file.write(dot.source)
    file.close()
    os.system(f"dot -Tjpg prime_graphs_source/{maximum}.txt >> prime_graphs/{maximum}.jpg")