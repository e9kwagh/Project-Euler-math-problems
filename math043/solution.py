"""math043"""


def sub_property(num_str):
    """property"""
    divisors = [2, 3, 5, 7, 11, 13, 17]

    for i in range(1, 8):
        substring = int(num_str[i : i + 3])
        if substring % divisors[i - 1] != 0:
            return False

    return True


def generate_numbers():
    """generate"""
    digits = list("0123456789")
    pandigital_sum = [0]

    def generate(current, remaining):
        if not remaining:
            num_str = "".join(current)
            if sub_property(num_str):
                pandigital_sum[0] += int(num_str)
        else:
            for i in range(len(remaining)):
                generate(current + [remaining[i]], remaining[:i] + remaining[i + 1 :])

    generate([], digits)
    return pandigital_sum[0]


def answer():
    """answer()"""
    return generate_numbers()


if __name__ == "__main__":
    print("Problem no math043")
    print("Answer of math043 = ", answer())
