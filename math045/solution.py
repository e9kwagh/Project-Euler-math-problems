"""math045"""


def is_pentagonal(num):
    n = int((1 + (1 + 24 * num) ** 0.5) / 6)
    return n * (3 * n - 1) // 2 == num


def is_hexagonal(num):
    n = int((1 + (1 + 8 * num) ** 0.5) / 4)
    return n * (2 * n - 1) == num


def answer():
    triangle_number = 286
    while True:
        current_triangle = triangle_number * (triangle_number + 1) // 2
        if is_pentagonal(current_triangle) and is_hexagonal(current_triangle):
            return current_triangle
        triangle_number += 1


if __name__ == "__main__":
    print("Problem no math045")
    print("Answer of math045 = ", answer())
