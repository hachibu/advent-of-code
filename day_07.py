from aoc import int_split, interleave
from itertools import combinations_with_replacement, permutations
from operator import add, mul
from collections import Counter, deque
from functools import cache
import time


def parse_equations(file):
    equations = []

    with open(file) as f:
        for line in f.read().splitlines():
            v, *nums = int_split(line.replace(":", ""), " ")
            equations.append((v, nums))

    return equations


def cat(a, b):
    return int(str(a) + str(b))


@cache
def enumerate_solutions(n):
    operators = set()

    for c in combinations_with_replacement([add, mul, cat], n):
        for p in permutations(c):
            operators.add(p)

    return operators


def main():
    equations = parse_equations("input/day_07.txt")

    total = 0

    for target, nums in equations:
        solution_found = False

        for solution in enumerate_solutions(len(nums) - 1):
            queue = deque(interleave(nums, solution))
            solution_too_big = False

            while queue:
                if len(queue) >= 3:
                    n = queue.popleft()
                    f = queue.popleft()
                    m = queue.popleft()
                    v = f(n, m)
                    if v > target:
                        solution_too_big = True
                        break
                    queue.appendleft(v)
                else:
                    n = queue.popleft()
                    if n == target:
                        solution_found = True
                        break

            if solution_too_big:
                continue

            if solution_found:
                break

        if solution_found:
            total += target

    assert total == 227615740238334


if __name__ == "__main__":
    main()
