import os


def run_files():
    start = 1
    end = 65

    li = []

    for i in range(start, end + 1):
        if i <= 9:
            li.append("math00" + str(i))

        if i > 9:
            li.append("math0" + str(i))

    for i in li:
        val = os.path.join(i, "solution.py")

        # print(val)

        os.system("python " + val)


if __name__ == "__main__":
    run_files()


# path = sorted(os.listdir())
# print(path)
# for i in path:
#     path = os.path.join(i, "solution.py")
#     print(path)
#     if "math" in path:
#         os.system("python3 " + path)
#         print()


# import os

# def run_files():
#    y
#     path = os.listdir(os.getcwd())

#
#     for i in sorted(path):
#
#         val = os.path.join(os.getcwd(), i, "solution.py")

#
#         python_executable = r'C:\Python39\python.exe'  # Adjust the path if needed

#
#         os.system(f'{python_executable} {val}')

# if __name__ == "__main__":
#     # Run the script when executed
#     run_files()
