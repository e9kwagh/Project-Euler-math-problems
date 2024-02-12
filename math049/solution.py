"""math047"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def all_numbers():
    non_prime = [1]
    for i in range(3, 1000000):
        if not is_prime(i):
            non_prime.append(i)
    return non_prime


def factors(num):
    li = []

    for i in range(2, int(num**0.5)):
        if num % i == 0:
            if is_prime(i):
                li.append(i)
            if num // i != i and is_prime(num // i):
                li.append(i)

    return li

def answer():
    return -1

if __name__ == "__main__":
    print("Problem no 47")
    print("Answer of math049 = incomplete = ",answer())
