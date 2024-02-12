# Problem No. 26

## Reciprocal Cycles

A unit fraction contains $1$ in the numerator. 

The decimal representation of the unit fractions with denominators $2$ to $10$ are given:

$$\begin{align}
1/2 &amp;= 0.5\\
1/3 &amp;=0.(3)\\
1/4 &amp;=0.25\\
1/5 &amp;= 0.2\\
1/6 &amp;= 0.1(6)\\
1/7 &amp;= 0.(142857)\\
1/8 &amp;= 0.125\\
1/9 &amp;= 0.(1)\\
1/10 &amp;= 0.1
\end{align}$$

Where $0.1(6)$ means $0.166666\cdots$, and has a $1$-digit recurring cycle. It can be seen that $1/7$ has a $6$-digit recurring cycle.</p>

## Part A

Find the value of $d \lt 1000$ for which $1/d$ contains the longest recurring cycle in its decimal fraction part.

Update the function `answer()` in `solution.py` with your solution.

## Part B

Generalize the solution in Part A to find the value of $d \lt n$ for which $1/n$ contains all the digits in the provided list in the recurring cycle in its decimal fraction part.

For example: `solver(1000, [124578]) = 7`

Update the function `solver()` in `solution.py` with your generalized solution.

## Instructions

Create a new directory in your math problem repo (math) called `math026`

Copy README.md and solution.py into `math026`

Share your solution by updating `answer()` and `solver()` in solution.py.

```
math026
├── README.md
└── solution.py
``` 
