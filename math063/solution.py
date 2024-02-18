"""math063"""


def answer():
    """answer()"""
    count = 0
    for n in range(1, 10):
        i = 1
        while i <= len(str(n**i)):
            if i == len(str(n**i)):
                count += 1
            i += 1
    return count


if __name__ == "__main__":
    print("Answer of math063  =", answer())
