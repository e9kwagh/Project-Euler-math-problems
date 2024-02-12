"""math037"""


def is_prime(n):
    """prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def answer():
    """answer"""
    primes = []
    number = 10
    while len(primes) < 11:
        if is_prime(number):
            number_str = str(number)

            left_side = all(
                is_prime(int(number_str[i:])) for i in range(len(number_str))
            )

            right_side = all(
                is_prime(int(number_str[: i + 1])) for i in range(len(number_str))
            )

            if left_side and right_side:
                primes.append(number)

        number += 1

    return sum(primes)


if __name__ == "__main__":
    print("Question no. : Math037 :")
    print("Answer of math037 = ", answer())
