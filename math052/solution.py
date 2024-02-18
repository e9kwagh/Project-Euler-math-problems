"""
math052
"""


def answer():
    """answer"""
    for i in range(10, 10000000):
        if all(
            sorted(str(i * multiplyer)) == sorted(str(i)) for multiplyer in range(1, 6)
        ):
            return i
    return None


if __name__ == "__main__":
    print("Answer of math052 =", answer())
