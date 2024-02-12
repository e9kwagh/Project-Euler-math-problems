"""1000-digit Fibonacci
"""


def answer():
    """digits"""
    return fibonacci_index(1000)


def large_digits(a, b):
    """largets"""
    a, b = str(a), str(b)
    result = []
    carry = 0

    diff = len(a) - len(b)
    if diff > 0:
        b = "0" * diff + b
    elif diff < 0:
        a = "0" * abs(diff) + a

    for i in range(len(a) - 1, -1, -1):
        digit_a = int(a[i])
        digit_b = int(b[i])

        total = digit_a + digit_b + carry
        result_digit = total % 10
        carry = total // 10

        result.insert(0, str(result_digit))

    if carry > 0:
        result.insert(0, str(carry))

    final_result = "".join(result)
    return int(final_result)


def fibonacci_index(length):
    """finonaic"""
    first_num, second_num = 1, 1
    current_index = 2
    while True:
        first_num, second_num = second_num, large_digits(first_num, second_num)
        current_index += 1

        if len(str(second_num)) == length:
            return current_index


def solver(length: int):
    """solver"""
    return fibonacci_index(length)


if __name__ == "__main__":
    print("answer of math025 = ", answer())
    print(solver(3))
