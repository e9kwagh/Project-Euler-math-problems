Review Assignment Due Date
Problem No. 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
Part A

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

Edit the file answer.py and update the function answer() to return the answer.
Part B

Write code for solver.solver() to find all pythogorean triplets whose sum lies between p and q, inclusive, and return a dictionary where the key is the sum and the value is a list of all tuples whose sides add up to the key.

Solve for the range all numbers less than or equal to p if only p is provided

Solve for the range between p and q if p and q are both provided

In [1]: solver(12)
Out[1]: {12: [(3, 4, 5)]}