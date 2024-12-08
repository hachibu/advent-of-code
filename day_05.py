from collections import Counter
from itertools import combinations


def parse_input_text(file):
    updates = []
    update_sep = ","
    rules = set()
    rule_sep = "|"
    with open(file) as f:
        for line in f.read().splitlines():
            if line.find(rule_sep) > -1:
                rules.add(tuple(map(int, line.split(rule_sep))))
            elif line.find(update_sep) > -1:
                updates.append(list(map(int, line.split(update_sep))))
    return (updates, rules)


def main():
    updates, rules = parse_input_text("input/day_05.txt")
    ans = 0
    invalid_updates = []

    for u in updates:
        is_valid = True
        errors = []
        for a, b in combinations(u, 2):
            if (a, b) in rules:
                if u.index(a) > u.index(b):
                    is_valid = False
                    errors.append((a, b))
            if (b, a) in rules:
                if u.index(b) > u.index(a):
                    is_valid = False
                    errors.append((b, a))
        if is_valid:
            ans += u[len(u) // 2]
        else:
            invalid_updates.append((u[:], errors))

    # assert ans == 143
    assert ans == 6498

    ans = 0

    for u, errors in invalid_updates:
        for a, b in errors:
            i, j = u.index(a), u.index(b)
            u[i], u[j] = u[j], u[i]

    for u, _ in invalid_updates:
        ans += u[len(u) // 2]

    print(ans)
    # assert ans == 123
    # 4254 too low


if __name__ == "__main__":
    main()
