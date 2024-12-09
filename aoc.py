def int_split(s, sep=None):
    return [int(n) for n in (s.split(sep) if sep else s.split())]
