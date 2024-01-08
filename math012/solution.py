""" this is the solver function """

def answer():
    """answer function gives the answer"""
    return solver(500)



def check_factors(num):
    """check factors"""
    limit = int(num**0.5)
    li = [i for i in range(1, limit + 1) if num % i == 0]
    return li


def solver(n):
    """solver"""
    check = n // 2
    count = 1
    add = 0

    while True:
        add += count
        count += 1
        factors = check_factors(add)
        if len(factors) >= check:
            break

    return add


if __name__ == "__main__":
    print(solver(500))
    print(answer())