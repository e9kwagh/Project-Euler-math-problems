"math055"

def is_palindrome(num):
    """is_palindrome
    """
    return str(num) == str(num)[::-1]

def reverse(num):
    """
    def reverse(num):

    """
    return num + int(str(num)[::-1])
    

def is_lychrel(num, max_iterations=50):
    """"
    is_palindrome
    """
    for _ in range(50):
        num = reverse(num)
        if is_palindrome(num):
            return False 
    return True  
   
def answer():
    """
    answer
    """
    count = 0
    for num in range(1, 10000):
        if is_lychrel(num):
            count += 1
    return count

if __name__ == "__main__":
       print("Answer of math055 =", answer())

