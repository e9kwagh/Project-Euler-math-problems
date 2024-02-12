"""math046"""

def is_prime(num):
    """check"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(limit):
    """prime"""
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]

def answer():
    """answer"""
    limit = 10000
    prime_list = primes(limit)
    
    for odd_composite in range(9, limit, 2):
        if not is_prime(odd_composite):
            if not any((odd_composite - prime) // 2 == int(((odd_composite - prime) // 2)**0.5)**2
                        for prime in prime_list if prime < odd_composite):
                return odd_composite

if __name__ == "__main__":
    print("Problem no 46")
    print("answer =:", answer())
