[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6-YZO1RR)
# Problem No. 14

## Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

$n \to n/2$ ($n$ is even)

$n \to 3n + 1$ ($n$ is odd)

Using the rule above and starting with 13, we generate the following sequence:

```math
13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.
```

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

## Part A

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Edit the file answer.py and update the function `answer()` to return the answer.

## Part B

Write a function in python that returns 
- `None` if neither p nor q are defined
- the number which returns the longest collatz sequence such that the number is between (a) 1 and `p` if only `p` is defined and (b) `p` and `q` if both `p` and `q` are defined 

```python
solver(p: int = None, q: int = None)
```

## References

[Project Euler Problem 14](https://projecteuler.net/problem=14)

[Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)

[The Simple Math Problem We Still Can’t Solve](https://www.quantamagazine.org/why-mathematicians-still-cant-solve-the-collatz-conjecture-20200922/)
