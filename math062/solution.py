"""math062"""


def answer():
    """
    answer()
    """
    no_itrations = 5
    cube_dict = {}
    cube_root = 1

    while True:
        cube = cube_root**3
        digits = "".join(sorted(str(cube)))

        if digits not in cube_dict:
            cube_dict[digits] = [cube]
        else:
            cube_dict[digits].append(cube)

            if len(cube_dict[digits]) == no_itrations:
                return min(cube_dict[digits])

        cube_root += 1


if __name__ == "__main__":
    print("Answer of math062  =", answer())
