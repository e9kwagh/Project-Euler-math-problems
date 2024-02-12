"""math033"""


def gcd(a, b):
    """gcd"""
    while b:
        a, b = b, a % b
    return a


def simplify_fraction(num, deno):
    """simplify"""
    common_divisor = gcd(num, deno)
    s_num = num // common_divisor
    s_den = deno // common_divisor
    return s_num, s_den


def find_fractions():
    """fractions"""
    curious_fractions = []

    for num in range(10, 100):
        for deno  in range(num + 1, 100):
            num_str = str(num)
            den_str = str(deno)

            if num_str[0] != num_str[1] and den_str[0] != den_str[1]:
                if num_str[1] == den_str[0] and den_str[1] != "0":
                    simplified_fraction = simplify_fraction(num, deno)
                    if (int(num_str[0]), int(den_str[1])) == simplified_fraction:
                        curious_fractions.append((num, deno))

    return curious_fractions


def product_of_fractions(fractions):
    """product"""
    result_numerator = 1
    result_denominator = 1
    for num, deno in fractions:
        result_numerator *= num
        result_denominator *= deno

    # common_divisor = gcd(result_numerator, result_denominator)
    simplified_result = simplify_fraction(result_numerator, result_denominator)

    return simplified_result[1]


def answer():
    """answer"""
    curious_fractions = find_fractions()
    return product_of_fractions(curious_fractions)


if __name__ == "__main__":
    print("Math033")
    print("answer/solver = ", answer())
