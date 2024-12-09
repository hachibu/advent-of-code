from itertools import chain
import numpy as np


def parse_matrix(file):
    m = []
    with open(file) as f:
        for line in f.read().splitlines():
            m.append(list(line))
    return np.array(m)


def rows(a):
    for row in a:
        for i in range(len(row)):
            yield row[i:]


def cols(a):
    for col in a.T:
        for i in range(len(col)):
            yield col[i:]


def diags(a):
    n, m = a.shape
    for i in range(1 - n, m):
        main_diag = a.diagonal(i)
        for j in range(len(main_diag)):
            yield main_diag[j:]

        anti_diag = np.fliplr(a).diagonal(i)
        for j in range(len(anti_diag)):
            yield anti_diag[j:]


def submatricies(a, shape):
    h, w = a.shape
    for i in range(h):
        for j in range(w):
            yield a[i : i + shape[0], j : j + shape[1]]


def contains_xmas(a) -> bool:
    match list(a):
        case ["X", "M", "A", "S", *_]:
            return True
        case ["S", "A", "M", "X", *_]:
            return True
    return False


def contains_mas(a) -> bool:
    match list(a):
        case ["M", "A", "S"]:
            return True
        case ["S", "A", "M"]:
            return True
    return False


def main():
    m = parse_matrix("input/day_04.txt")

    ans = 0

    for a in chain(rows(m), cols(m), diags(m)):
        if contains_xmas(a):
            ans += 1

    assert ans == 2557

    ans = 0

    for sm in submatricies(m, shape=(3, 3)):
        main_diag = sm.diagonal()
        anti_diag = np.fliplr(sm).diagonal()

        if contains_mas(main_diag) and contains_mas(anti_diag):
            ans += 1

    assert ans == 1854


if __name__ == "__main__":
    main()
