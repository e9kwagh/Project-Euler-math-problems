"""math47"""


def is_prime(num):
    """prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_count(num):
    """prime_count"""
    factors_count = 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0 and is_prime(i):
            factors_count += 1
            while num % i == 0:
                num //= i
    if num > 1:
        factors_count += 1
    return factors_count


def find_integers(consecutive_count, target_factors_count):
    """find_intergers"""
    current_count = 0
    num = 2
    while True:
        if prime_count(num) == target_factors_count:
            current_count += 1
            if current_count == consecutive_count:
                return num - consecutive_count + 1
        else:
            current_count = 0
        num += 1


def answer():
    """answer()"""
    consecutive_count = 4
    target_factors_count = 4
    result = find_integers(consecutive_count, target_factors_count)
    return result


if __name__ == "__main__":
    print("Answer of math047 = ", answer())
