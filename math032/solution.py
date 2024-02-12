"""
Pandigital Products
"""


def is_pan(multiplicand, multiplier, product):
    """is_pan"""
    con_str = str(multiplicand) + str(multiplier) + str(product)
    return "".join(sorted(con_str)) == "123456789"


def answer():
    """solver()"""
    pan_products = set()

    for multiplicand in range(1, 10000):
        for multiplier in range(1, int(10000 / multiplicand) + 1):
            product = multiplicand * multiplier
            if product >= 10000:
                break

            if is_pan(multiplicand, multiplier, product):
                pan_products.add(product)

    return sum(pan_products)


if __name__ == "__main__":
    print("Question no 32")
    print("Answer of math032 = ", answer())
