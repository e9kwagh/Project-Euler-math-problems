"""math038"""


def is_pan(number_str):
    """pandigital"""
    return len(number_str) == 9 and set(number_str) == set("123456789")


def answer():
    """anser()"""
    largest = 0

    for multiplicand in range(1, 10000):
        product = str(multiplicand)
        multiplier = 2

        while len(product) < 9:
            product += str(multiplicand * multiplier)
            multiplier += 1

        if is_pan(product):
            pandigital_num = int(product)
            if pandigital_num > largest:
                largest = pandigital_num

    return largest


if __name__ == "__main__":
    print("qustion no. : math038")
    print("Answer of math038 = ", answer())
