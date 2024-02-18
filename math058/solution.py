"""
math058
"""
def is_prime(n):
    """
    is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def answer(ratio):
    """
    answer
    """
    side_length, count_primes, count_num, current_num, increment = 1, 0, 1, 1, 2
    # prime = [ i for i in range(2,1000000) if is_prime(i)]
    while True:
        for _ in range(4):
            current_num += increment
            count_num += 1
            if is_prime(current_num):
                count_primes += 1
        increment += 2
        side_length += 2
        if count_primes / count_num < ratio:
            return side_length


if __name__ == "__main__":
    print("Answer of math058 =", answer(0.1))


# ned to mke this faster !!!!!!
