import numpy as np


def main() -> None:
    vec = np.array([1, 2, 3, 4, 5])
    print(np.max(vec))
    print(np.min(vec))
    print(np.median(vec))
    print(np.mean(vec))
    print(vec.shape)

    matrix = np.array([[1, 2], [3, 4]])
    print(np.max(matrix))
    print(np.min(matrix))
    print(np.max(matrix, axis=0))  # column wise
    print(np.min(matrix, axis=0))  # column wise
    print(np.max(matrix, axis=1))  # row wise
    print(np.min(matrix, axis=1))  # row wise
    print(np.median(matrix))
    print(np.mean(matrix))
    print(matrix.shape)


if __name__ == "__main__":
    main()
