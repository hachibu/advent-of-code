from collections import deque
from re import Scanner
import operator


def parse_memory(file):
    memory = []
    with open(file) as f:
        memory.extend(f.read().splitlines())
    return memory


def parse_program(lines):
    programs = []
    for line in lines:
        programs.extend(lex(tokenize(line)))
    return programs


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
        expr = None
        match tokens[i:]:
            case [("id", "do"), ("lparen", _), ("rparen", _), *_]:
                expr = [("id", "do")]
            case [("id", "don't"), ("lparen", _), ("rparen", _), *_]:
                expr = [("id", "don't")]
            case [
                ("id", "mul"),
                ("lparen", _),
                ("num", a),
                ("comma", _),
                ("num", b),
                ("rparen", _),
                *_,
            ]:
                expr = [
                    ("operator", "mul", operator.mul),
                    ("num", a),
                    ("num", b),
                ]
        if expr:
            stmts.append(expr)
    return stmts


def eval(program, version):
    ans = 0
    mul_enabled = True

    for stmt in program:
        match stmt:
            case [("id", "do")]:
                if version > 1:
                    mul_enabled = True
            case [("id", "don't")]:
                if version > 1:
                    mul_enabled = False
            case [("operator", "mul", f), ("num", a), ("num", b)]:
                if version == 1 or mul_enabled:
                    ans += f(a, b)

    return ans


def main():
    memory = parse_memory("input/day_03.txt")
    program = parse_program(memory)

    ans = eval(program, 1)

    assert ans == 192767529

    ans = eval(program, 2)

    assert ans == 104083373


if __name__ == "__main__":
    main()
