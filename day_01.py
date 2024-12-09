from collections import Counter
from aoc import int_split


def parse_cols(file):
    cols = [[], []]
    with open(file) as f:
        for line in f.read().splitlines():
            id_1, id_2 = int_split(line)
            cols[0].append(id_1)
            cols[1].append(id_2)
    return cols


def distance(col_1, col_2):
    n = 0
    for id_1, id_2 in zip(sorted(col_1), sorted(col_2)):
        n += abs(id_1 - id_2)
    return n


def similarity(col_1, col_2):
    n = 0
    c = Counter(col_2)
    for id_1 in set(col_1):
        n += id_1 * c[id_1]
    return n


def main():
    col_1, col_2 = parse_cols("input/day_01.txt")

    assert distance(col_1, col_2) == 1882714
    assert similarity(col_1, col_2) == 19437052


if __name__ == "__main__":
    main()
