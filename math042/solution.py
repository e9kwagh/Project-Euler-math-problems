"""math042"""
import os


def is_triangle_number(n):
    """triangle number."""
    discriminant = 1 + 8 * n
    root = int((discriminant**0.5 - 1) / 2)
    return root * (root + 1) // 2 == n


def word_value(word):
    """word"""
    return sum(ord(char) - ord("A") + 1 for char in word)


def answer():
    """answer()"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "words.txt")

    with open(file_path, "r", encoding="utf-8") as file:
        words = file.read().replace('"', "").split(",")

    count = 0
    for word in words:
        if is_triangle_number(word_value(word)):
            count += 1
    return count


if __name__ == "__main__":
    print("Problem no : math042")
    print("Answer of math042= ", answer())
