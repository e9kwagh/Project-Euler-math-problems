# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def con_prime(primes):
#     for i in range(len(primes)):
#         for j in range(i + 1, len(primes)):
#             if not is_prime(int(str(primes[i]) + str(primes[j]))) or \
#                not is_prime(int(str(primes[j]) + str(primes[i]))):
#                 return False
#     return True

# def answer():
#     prime = []
#     num = 2
#     while len(prime) < 5:
#         if is_prime(num) and con_prime(prime + [num]):
#             prime.append(num)
#         num += 1
#     return sum(prime)

# if __name__ == "__main__":

#     print("answer to math060 = ",answer() )


"""math060"""


def is_prime(n):
    """
    Check prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def answer():
    """answer"""
    # prime_no = [i for i in range(2, 10000000) if is_prime(int(i))]
    prime_no = {i: i for i in range(673, 10000000) if is_prime(int(i))}

    def con_prime(num, i):
        concat1 = int(str(num) + str(i))
        concat2 = int(str(i) + str(num))
        if prime_no[concat1] == concat1 and prime_no[concat2] == concat2:
            return True
        return False

    li = [3, 7, 109, 673]
    for num in prime_no:
        if all(con_prime(num, i) for i in li):
            li.append(num)
            return sum(li)


if __name__ == "__main__":
    print("Answer of math060  is taking way to long ")
    print("Answer of math060 is taking way to long  =", answer())


# def is_prime(n):
#     """
#     Check if a number is prime
#     """
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def is_concatenation_prime(p1, p2):
#     """
#     Check if concatenation of two primes is prime
#     """
#     concat1 = int(str(p1) + str(p2))
#     concat2 = int(str(p2) + str(p1))
#     return is_prime(concat1) and is_prime(concat2)

# def find_set_of_five_primes():
#     primes = [2]  # Initialize with 2, as we are excluding even numbers
#     num = 3
#     while True:
#         if all(is_concatenation_prime(num, prime) for prime in primes):
#             primes.append(num)
#             if len(primes) == 5:
#                 return primes
#         num += 2  # Skipping even numbers

# if __name__ == "__main__":
#     primes_set = find_set_of_five_primes()
#     print("Lowest sum for a set of five primes:", sum(primes_set))


# def is_prime(n):
#     """
#     is prime
#     """
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def answer():
#     """
#     answer
#     """
#     check_prime = [3, 7, 109, 673]
#     primes = [i for i in range(673, 100000) if is_prime(int(i))]

#     for num in primes:
#         flag = False
#         for i in check_prime:
#             pair1 = int(str(num) + str(i))
#             pair2 = int(str(i) + str(num))
#             if  (is_prime(pair1) and is_prime(pair2)):
#                 flag = True
#                 break
#         if flag:
#             return sum(check_prime) + num

# if __name__ == "__main__":
#     print("Answer of math059 is wrong =", answer())


# def is_prime(n):
#     """
#     Check if a number is prime
#     """
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def is_concatenation_prime(p1, p2):
#     """
#     Check if concatenation of two primes is prime
#     """
#     concat1 = int(str(p1) + str(p2))
#     concat2 = int(str(p2) + str(p1))
#     return is_prime(concat1) and is_prime(concat2)

# def find_set_of_five_primes():
#     primes = [2]
#     num = 3
#     while len(primes) < 5:
#         if all(is_concatenation_prime(num, prime) for prime in primes):
#             primes.append(num)
#         num += 2
#     return primes

# if __name__ == "__main__":
#     primes_set = find_set_of_five_primes()
#     print("Lowest sum for a set of five primes:", sum(primes_set))
