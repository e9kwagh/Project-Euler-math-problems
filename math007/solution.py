"""Write a function, solver() to find the nth prime number?"""


def answer():
    """answer function"""
    return solver(10001)


def solver(n: int = 10001):
    """solver function"""
    counter, prime, i = 1, 0, 2
    while counter <= n:
        square = int(i**0.5)
        flag = True
        for sqr in range(2, square + 1):
            if i % sqr == 0:
                flag = False
                i += 1
                break
        if flag:
            counter += 1
            prime = i
            i += 1

    return prime


if __name__ == "__main__":
    print(solver(10001))
    print("answer of math007 = ", answer())
