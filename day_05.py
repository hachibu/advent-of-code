from collections import Counter
from itertools import combinations


def parse_input_text(file):
    updates = []
    rules = set()

    with open(file) as f:
        for line in f.read().splitlines():
            if line.find("|") > -1:
                rule = tuple(map(int, line.split("|")))
                rules.add(rule)
            elif line.find(",") > -1:
                update = list(map(int, line.split(",")))
                updates.append(update)

    return (updates, rules)


def is_update_valid(update, rules):
    for a, b in rules:
        if a not in update or b not in update:
            continue
        i, j = update.index(a), update.index(b)
        if i > j:
            return False
    return True


def main():
    updates, rules = parse_input_text("input/day_05.txt")
    ans = 0
    invalid_updates = []

    for u in updates:
        is_valid = True
        for a, b in combinations(u, 2):
            if (a, b) in rules:
                if u.index(a) > u.index(b):
                    is_valid = False
            if (b, a) in rules:
                if u.index(b) > u.index(a):
                    is_valid = False
        if is_valid:
            ans += u[len(u) // 2]
        else:
            invalid_updates.append(u)

    assert ans == 6498

    ans = 0

    for u in invalid_updates:
        while not is_update_valid(u, rules):
            for a, b in rules:
                if a not in u or b not in u:
                    continue
                i, j = u.index(a), u.index(b)
                if i > j:
                    u[j], u[i] = u[i], u[j]
        ans += u[len(u) // 2]

    assert ans == 5017


if __name__ == "__main__":
    main()
