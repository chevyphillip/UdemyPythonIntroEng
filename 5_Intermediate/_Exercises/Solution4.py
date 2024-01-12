"""Exercise 4:
1.)
Write a function that takes an integer number "n" as an input.
The function returns a list with all power of twos (2^n)
from 0 to n-1. Use a list comprehension.
2.)
Write a function that takes the resulting list from 1.) as
an input. Iterate over all values of the list and print
the current index and the current value in each iteration.
"""


def exercise1(n: int) -> list[int]:
    return [2**i for i in range(n)]


def exercise2(lst: list) -> None:
    for idx, val in enumerate(lst):
        print(idx, val)


def main() -> None:
    n = 5
    lst = exercise1(n)
    print(lst)

    exercise2(lst)


if __name__ == "__main__":
    main()
