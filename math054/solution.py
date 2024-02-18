"""math054"""


def answer():
    """answer()"""
    for i in range(10, 10000000):
        check = all(
            sorted(str(i * multiplyer)) == sorted(str(i)) for multiplyer in range(1, 6)
        )
        if check:
            return i
    return None


if __name__ == "__main__":
    print("Answer of math054 =", answer())
