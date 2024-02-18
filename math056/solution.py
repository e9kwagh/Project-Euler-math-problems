"math056"
 

def sum_of_digits(num):
    """sum_of_digits"""
    num = str(num)[::-1]  
    result = []
    carry = 0

    for digit in num:
        current_sum = int(digit) + carry
        result.append(current_sum % 10)
        carry = current_sum // 10

    while carry:
        result.append(carry % 10)
        carry //= 10

    return sum(result)

   
def answer():
    """
     answer():
    """
    max_digital = 0
    for a in range(1, 100):
        for b in range(1, 100):
            num = a ** b
            current_sum = sum_of_digits(num)
            if current_sum > max_digital:
                max_digital = current_sum
    return max_digital

if __name__ == "__main__":
       print("Answer of math056 =", answer())

