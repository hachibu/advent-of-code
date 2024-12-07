from collections import deque
from re import Scanner


def parse_input_text(file):
    memory = []
    with open(file) as f:
        memory.extend(f.read().splitlines())
    return memory


def tokenize(line):
    scanner = Scanner(
        [
            (r"[0-9]+", lambda _, t: ("num", int(t))),
            (r"[a-z]+'*[a-z]*", lambda _, t: ("id", t)),
            (r"[(]", lambda _, t: ("lparen", t)),
            (r"[)]", lambda _, t: ("rparen", t)),
            (r"[,]", lambda _, t: ("comma", t)),
            (r"[^a-z0-9]", lambda _, t: ("invalid", t)),
        ]
    )
    tokens, remainder = scanner.scan(line)
    if len(remainder) > 0:
        raise "unparsed input remaining"
    return tokens


def lex(tokens):
    stmts = []
    for i in range(len(tokens)):
        match tokens[i:]:
            case [
                ("id", id),
                ("lparen", _),
                ("num", a),
                ("comma", _),
                ("num", b),
                ("rparen", _),
                *_,
            ]:
                expr = [
                    ("id", id),
                    ("num", a),
                    ("num", b),
                ]
                stmts.append(expr)
    return stmts


def parse_program(lines):
    program = []
    for line in lines:
        program.extend(lex(tokenize(line)))
    return program


def main():
    input_text = parse_input_text("input/day_03.txt")
    ans = 0

    for stmt in parse_program(input_text):
        match stmt:
            case [("id", "mul"), ("num", a), ("num", b)]:
                ans += a * b

    assert ans == 192767529


if __name__ == "__main__":
    main()
