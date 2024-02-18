"""math039"""


def answer():
    perimeter_limit = 1000
    max_solutions = 0
    max_solutions_p = 0

    for p in range(1, perimeter_limit + 1):
        solutions = 0

        for a in range(1, p // 3 + 1):
            remaining_perimeter = p - a

            for b in range(a, (remaining_perimeter + 1) // 2):
                c = p - a - b

                if a**2 + b**2 == c**2:
                    solutions += 1

            if solutions > max_solutions:
                max_solutions = solutions
                max_solutions_p = p

    return max_solutions_p


if __name__ == "__main__":
    print("Answer of math039 = ", answer())
