"""solver"""


def answer():
    """answer"""
    return solver(100)


def solver(n):
    """solver"""
    number = "1"
    for i in range(2, n + 1):
        rev, carry = "", 0
        for num in number[::-1]:
            prod = (int(num) * i) + carry
            carry = prod // 10
            end = prod % 10
            rev = str(end) + rev
        if carry:
            rev = str(carry) + rev
        number = rev
    return sum(map(int, number))


if __name__ == "__main__":
    print(solver(100))
    print("answer of math020 = ", answer())
