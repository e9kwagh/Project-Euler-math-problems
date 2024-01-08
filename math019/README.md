# Problem No. 19

## Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.
 
1 Jan 1900 was a Monday.<br>
Thirty days has September,<br>
April, June and November.<br>
All the rest have thirty-one,<br>
Saving February alone,<br>
Which has twenty-eight, rain or shine.<br>
And on leap years, twenty-nine.<br>
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

## Part A

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Edit the file `answer.py` and update the function `answer()` to return the answer.

## Part B

Generalize the solution in Part A by taking two dates and counting the number of Sundays between both dates, inclusive.

Note that it is important that you take `from` and `to` as python date or datetime and not a string, int, or some other new format that is other than date or datetime.

Edit the file `solver.py` and update the function `solver()` with your generalized solution.

```python
solver(from: datetime.date, to: datetime.date)
```
