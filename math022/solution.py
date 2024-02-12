"""
Name Scores
"""

 
def answer():
    """answer()"""
    return solver("0022_names.txt")



def solver(filename="0022_names.txt"):
    """solver()"""

    with open(filename,"r", encoding="utf-8") as f:
        data = f.read()

    data = data.replace('"', "").replace("\n", "")
    data = sorted(data.split(","))
    check = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    word = 0

    for index, value in enumerate(data, 1):
        num = 0
        for i in value:
            num += check.get(str(i.lower()))
        word += num * index

    return word


if __name__ == "__main__":
    print(solver())
    print(answer())
