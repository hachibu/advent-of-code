from itertools import chain
import numpy as np


def parse_input_text(file):
    m = []
    with open(file) as f:
        for line in f.read().splitlines():
            m.append(list(line))
    return np.array(m)


def count_xmas(a):
    n = 0
    match list(a):
        case ["X", "M", "A", "S", *_]:
            n += 1
        case ["S", "A", "M", "X", *_]:
            n += 1
    return n


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
        xs = a.diagonal(i)
        for j in range(len(xs)):
            yield xs[j:]

        ys = np.fliplr(a).diagonal(i)
        for j in range(len(ys)):
            yield ys[j:]


def main():
    a = parse_input_text("input/day_04.txt")

    ans = 0

    for arr in chain(rows(a), cols(a), diags(a)):
        ans += count_xmas(arr)

    assert ans == 2557


if __name__ == "__main__":
    main()
