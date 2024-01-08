"""Write a function in python that returns the largest prime factor of a given number.
    Edit the file solver.py to update the function solver to
    return the answer when called as in the below example.
"""
def answer():
    """answer function""" 
    return solver(600851475143)



def solver(value =600851475143):
    """This is the solver """
    n = value
    square = int(n**0.5)
    arr = [i for i in range(1, square + 1) if n % i == 0]

    mirror = []
    for i in arr:
        val = n // i
        mirror.append(val)

    total = mirror + arr
    prime_list = []

    for i in total:
        flag = True
        sqr = int(i**0.5)
        for a in range(2, sqr + 1):
            if i % a == 0:
                flag = False
                break

        if flag:
            prime_list.append(i)

    if prime_list:
        final = max(prime_list)
    else:
        final = n
    return final

if __name__ == "__main__":
    print(solver(600851475143))
    print(answer())