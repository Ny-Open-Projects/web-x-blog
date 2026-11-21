from __future__ import annotations

import sys
from dataclasses import dataclass


@dataclass
class V1:
    x: int
    y: int = 0


if __name__ == "__main__":
    print("python:", sys.version.split()[0])
    v = V1(3)
    print("basic:", v, "| has __dict__:", hasattr(v, "__dict__"))
    if sys.version_info >= (3, 10):
        @dataclass(slots=True, kw_only=True)
        class V2:
            x: int
            y: int = 0

        w = V2(x=3)                     # 全部字段必须按关键字
        print("slots instance has __dict__:", hasattr(w, "__dict__"))
        try:
            V2(3)
        except TypeError as e:
            print("positional rejected:", e)
    else:
        print("slots=True 与 kw_only 是 3.10 引入的 dataclass 参数")
