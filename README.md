# Python Lab 1 – Getting Started

Introductory Python programs written for the first lab of a programming course.
Each program reads its input from the keyboard and prints the result.

## Programs

| File | Problem |
|------|---------|
| `sum.py` | Computes the sum of two numbers entered by the user. |
| `factorial.py` | Computes the product of the first *n* natural numbers (n!). |
| `zero.py` | Counts the zeros at the end of n! (e.g. n = 10 → 2 zeros). |
| `perfect.py` | Checks whether a number is perfect, i.e. equal to the sum of its divisors smaller than itself (e.g. 6 = 1 + 2 + 3). |

## How the solutions work

**zero.py** – does not compute n! at all. Every trailing zero comes from a factor 10 = 2 × 5,
and factors of 2 are always more frequent than factors of 5, so the program only counts
the factors of 5: n/5 + n/25 + n/125 + ... For n = 150 this gives 30 + 6 + 1 = 37 zeros.
This works instantly even for very large n.

**perfect.py** – looks for divisors only up to √n and adds them in pairs (i and n/i),
so it stays fast for large numbers. The case n = 1 is handled separately.

## Example

```
Enter a number : 150
The number of zeros in the product of the first 150 natural numbers is equal to 37
```

```
Enter a number : 28
28 is a perfect number
```

## How to run

Requires Python 3.6 or newer.

```
python zero.py
```

Or open the file in IDLE and press **F5** (Run Module).
