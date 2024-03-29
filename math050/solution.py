"""
math050
"""
def is_prime(num):
    """is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def answer(limit):
    """answer"""
    prime_numbers = [i for i in range(2, 1000000) if is_prime(i)]
    max_length = 0
    result_prime = 0

    for i in range(len(prime_numbers)):
        for j in range(i + max_length, len(prime_numbers)):
            current_sum = sum(prime_numbers[i:j])
            if current_sum < limit and is_prime(current_sum):
                max_length = j - i
                result_prime = current_sum
            elif current_sum >= limit:
                break

    return result_prime


if __name__ == "__main__":
    print("Problem no 50")
    print("Answer of math050 =", answer(1000000))


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True


# def all_numbers():
#     non_prime = [1]
#     for i in range(3, 1000000):
#         if not is_prime(i):
#             non_prime.append(i)
#     return non_prime


# def factors(num):
#     li = []

#     for i in range(2, int(num**0.5)):
#         if num % i == 0:
#             if is_prime(i):
#                 li.append(i)
#             if num // i != i and is_prime(num // i):
#                 li.append(i)

#     return li

# def answer():
#     return -1
