"""math035"""


def is_prime():
    """is_prime()"""
    prime_no = {2: True}

    for num in range(3, 1000000, 2):
        flag = False
        sqr = int(num**0.5)
        for i in range(2, sqr + 1):
            if num % i == 0:
                flag = True
                break
        if flag == False:
            prime_no[num] = True
    return prime_no


def rotations(num):
    """roatations"""
    num_str = str(num)
    rotations_list = []
    for _ in range(len(num_str)):
        num_str = num_str[1:] + num_str[0]
        rotations_list.append(int(num_str))
    return rotations_list


def primes_count(start, limit):
    """prime_count"""
    prime_no = is_prime()
    circular_primes = []

    for num in range(start, limit):
        if num in prime_no and (
            num == 2 or all(prime_no.get(rotated, False) for rotated in rotations(num))
        ):
            circular_primes.append(num)

    return len(circular_primes)


def solver(p, q):
    """solver()"""
    return primes_count(p, q)


def answer():
    """answer()"""
    return solver(2, 1000000)


if __name__ == "__main__":
    print("Question no Math035")
    print("Answer of math035 = ", answer())
    print("solver() =", solver(2, 1000000))
