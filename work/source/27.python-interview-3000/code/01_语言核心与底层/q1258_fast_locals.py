import dis
import sys


def sample(a, b):
    c = a + b
    d = c * 2
    return d


if __name__ == "__main__":
    print("co_varnames:", sample.__code__.co_varnames)
    print("co_nlocals :", sample.__code__.co_nlocals)
    ops = [i.opname for i in dis.get_instructions(sample)]
    print("opnames    :", ops)

    captured = []
    def probe():
        x = 1
        captured.append(sys._getframe())
        return x
    probe()
    f = captured[0]
    print("f.f_locals is materialized snapshot:", f.f_locals)
    print("修改它不会影响原槽位 — 未定义行为,勿用")
