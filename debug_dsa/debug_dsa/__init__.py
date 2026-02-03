import debug_dsa.two_pointers
import sys

tp = debug_dsa.two_pointers.p
tpprint = tp


def p(*args, **kwargs):
    kwargs.update({"file": sys.stderr})
    print(*args, **kwargs)
