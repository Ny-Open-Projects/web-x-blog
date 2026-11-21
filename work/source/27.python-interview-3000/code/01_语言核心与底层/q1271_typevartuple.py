from __future__ import annotations

import sys


def widths_of(*rows: tuple) -> list:
    return [len(r) for r in rows]


if __name__ == "__main__":
    print("python:", sys.version.split()[0])
    if sys.version_info >= (3, 11):
        from typing import TypeVarTuple, Unpack   # PEP 646
        Ts = TypeVarTuple("Ts")
        print("3.11+: tuple[Unpack[Ts]] 可表达异构可变元组")
    else:
        print("3.10-: 只有 Tuple[T, ...] 的同构近似")
    print(widths_of((1, 2), ("a",), (True, False, None)))
