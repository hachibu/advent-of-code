from itertools import chain, zip_longest


def int_split(s, sep=None):
    return [int(n) for n in (s.split(sep) if sep else s.split())]


def interleave(a, b):
    return [x for x in chain(*zip_longest(a, b)) if x is not None]
