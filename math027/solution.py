"""math027"""


def is_prime(num):
    """is_prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def consecutive_primes(a, b):
    """consecutive_prime"""
    n = 0
    while is_prime(n**2 + a * n + b):
        n += 1
    return n


def answer():
    """answer"""
    max_primes = 0
    result_a, result_b = 0, 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            consecutive_count = consecutive_primes(a, b)
            if consecutive_count > max_primes:
                max_primes = consecutive_count
                result_a, result_b = a, b

    return result_a * result_b


if __name__ == "__main__":
    print("answer of math027 = ", answer())
# -59231
