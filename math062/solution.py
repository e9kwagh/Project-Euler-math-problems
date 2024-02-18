"""math062"""


def answer():
    """
    answer()
    """
    no_itrations = 5
    cube_dit = {}
    cube_root = 1

    while True:
        cube = cube_root**3
        digits = "".join(sorted(str(cube)))

        if digits not in cube_dit:
            cube_dit[digits] = [cube]
        else:
            cube_dit[digits].append(cube)

            if len(cube_dit[digits]) == no_itrations:
                return min(cube_dit[digits])

        cube_root += 1


if __name__ == "__main__":
    print("Answer of math061  =", answer())
