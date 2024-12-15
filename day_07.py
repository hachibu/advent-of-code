from aoc import int_split, interleave
from itertools import combinations_with_replacement, permutations
from operator import add, mul


def parse_equations(file):
    equations = []

    with open(file) as f:
        for line in f.read().splitlines():
            v, *nums = int_split(line.replace(":", ""), " ")
            equations.append((v, nums))

    return equations


def enumerate_operator_combinations(nums):
    operators = set()
    for c in combinations_with_replacement([add, mul], len(nums) - 1):
        for p in permutations(c):
            operators.add(p)
    return operators


def main():
    equations = parse_equations("input/day_07.txt")

    total_calibration_result = 0

    for target, nums in equations:
        solution_found = False
        operator_combinations = enumerate_operator_combinations(nums)

        for oc in operator_combinations:
            equation = interleave(nums, oc)
            stack = []

            for x in equation:
                if len(stack) == 3:
                    b = stack.pop()
                    o = stack.pop()
                    a = stack.pop()
                    v = o(a, b)
                    if v > target:
                        break
                    stack.append(v)
                stack.append(x)

            if len(stack) == 3:
                a, o, b = stack
                v = o(a, b)
                if v == target:
                    solution_found = True
                    break

        if solution_found:
            total_calibration_result += target

    assert total_calibration_result == 3749
    print(total_calibration_result)


if __name__ == "__main__":
    main()
