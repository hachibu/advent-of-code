from collections import Counter
from itertools import pairwise, combinations
from aoc import int_split


def parse_reports(file):
    reports = []
    with open(file) as f:
        for line in f.read().splitlines():
            reports.append(int_split(line))
    return reports


def count_by_sign(nums: list[int]) -> Counter:
    c = Counter()
    for n in nums:
        if n == 0:
            c["0"] += 1
        elif n < 0:
            c["-"] += 1
        else:
            c["+"] += 1
    return c


def is_safe(report) -> bool:
    diff = [a - b for a, b in pairwise(report)]
    c = count_by_sign(diff)

    all_incr = c["-"] == len(diff)
    all_decr = c["+"] == len(diff)
    all_grad = all(0 < abs(n) < 4 for n in diff)

    return (all_incr or all_decr) and all_grad


def main():
    reports = parse_reports("input/day_02.txt")
    num_safe = 0
    unsafe_reports = []

    for r in reports:
        if is_safe(r):
            num_safe += 1
        else:
            unsafe_reports.append(r)

    assert num_safe == 379

    for r in unsafe_reports:
        for c in combinations(r, len(r) - 1):
            if is_safe(c):
                num_safe += 1
                break

    assert num_safe == 430


if __name__ == "__main__":
    main()
