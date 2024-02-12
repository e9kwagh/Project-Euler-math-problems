"""math041"""
def is_pandigital(number_str):
    """pandigital."""
    return sorted(number_str) == [str(i) for i in range(1, len(number_str) + 1)]


def is_prime(num):
    """is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_pandigitals(n):
    """numbers"""
    digits = list("123456789"[:n])
    pandigitals = []

    while True:
        number = int("".join(digits))
        if is_prime(number):
            pandigitals.append(number)

        i = n - 1
        while i > 0 and digits[i - 1] >= digits[i]:
            i -= 1
        if i == 0:
            break

        j = n - 1
        while digits[j] <= digits[i - 1]:
            j -= 1

        digits[i - 1], digits[j] = digits[j], digits[i - 1]

        # Reverse the suffix
        digits[i:] = reversed(digits[i:])

    return pandigitals


def answer():
    """answer."""
    largest = 0

    for n in range(1, 10):
        pandigitals = generate_pandigitals(n)
        largest_prime = max(pandigitals, default=0)
        largest = max(largest, largest_prime)

    return largest


if __name__ == "__main__":
    print("Problem no : 41")
    print("answer():", answer())
