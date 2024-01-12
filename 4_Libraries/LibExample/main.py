from math_lib import list_max
from math_lib import list_min


def main() -> None:
    list1 = [-2, 1, 2, -10, 22, -10]
    print(list_max(list1))
    print(list_min(list1))
    list2 = [-20, 123, 112, -10, 22, -120]
    print(list_max(list2))
    print(list_min(list2))


if __name__ == "__main__":
    main()
