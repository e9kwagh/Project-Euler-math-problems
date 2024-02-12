"""math030"""


def sum_of_digit_powers(num, power):
    return sum(int(digit) ** power for digit in str(num))


def solver(power):
    upper_limit = 10 ** (power + 1)
    result = sum(
        num for num in range(10, upper_limit) if num == sum_of_digit_powers(num, power)
    )

    return result


def answer():
    return sum(num for num in range(10, 10**6) if num == sum_of_digit_powers(num, 5))


if __name__ == "__main__":
    print("Math030")
    print("answer of math030 = ", answer())
    print("solver(4) =", solver(4))
