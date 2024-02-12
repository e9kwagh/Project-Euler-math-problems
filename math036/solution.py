"""math036"""


def is_palindromic(number):
    """check"""
    number_str = str(number)
    return number_str == number_str[::-1]


def to_binary(number):
    """binary"""
    binary_digits = []
    while number > 0:
        binary_digits.append(str(number % 2))
        number = number // 2
    binary_digits.reverse()
    return "".join(binary_digits)


def convert_base2(number):
    """base2"""
    binary = to_binary(number)
    return is_palindromic(binary)


def answer():
    """answer"""
    limit = 1000000
    total_sum = 0
    for number in range(1, limit):
        if is_palindromic(number) and convert_base2(number):
            total_sum += number
    return total_sum


if __name__ == "__main__":
    print("Question no  = Math036")
    print("answer() =", answer())
