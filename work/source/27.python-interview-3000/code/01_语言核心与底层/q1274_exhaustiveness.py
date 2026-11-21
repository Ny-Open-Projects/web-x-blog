from __future__ import annotations

import sys

Mode = str        # 实际应为 Literal["fast", "safe", "off"]


def handle(mode: Mode) -> str:
    if mode == "fast":
        return "F"
    elif mode == "safe":
        return "S"
    elif mode == "off":
        return "O"
    else:
        # 3.11+: assert_never(mode);这里用运行时兜底保持 3.9 可运行
        raise AssertionError("unhandled mode: %r" % (mode,))


if __name__ == "__main__":
    print("python:", sys.version.split()[0])
    for m in ("fast", "safe", "off"):
        print(m, "->", handle(m))
    try:
        handle("turbo")
    except AssertionError as e:
        print("unhandled:", e)
    if sys.version_info >= (3, 11):
        print("3.11+: typing.assert_never 让漏分支变成静态错误")
