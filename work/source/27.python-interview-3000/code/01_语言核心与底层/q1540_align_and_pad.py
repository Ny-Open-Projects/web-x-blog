
ROWS = [
    ("q1526", 3, 0.874),
    ("q1528", 4, 23.5),
    ("q1540", 2, 6.125),
]


def render_table(rows):
    header = f"{'id':<8}{'level':>7}{'score':>10}"
    lines = [header, "-" * len(header)]
    for qid, level, score in rows:
        lines.append(f"{qid:<8}{level:>7}{score:>10.3f}")
    return "\n".join(lines)


if __name__ == "__main__":
    print(render_table(ROWS))

    # 补零:位数对齐的排序键(不补零字典序会乱)
    parts = [("part", 1), ("part", 23), ("part", 4)]
    keys = [f"{name}-{num:04d}" for name, num in parts]
    print("sorted keys:", sorted(keys))

    # 方法族与 format 的等价关系
    s = "py"
    print(s.ljust(6, "."), "|", f"{s:.<6}")
    print(s.rjust(6, "_"), "|", f"{s:_>6}")
    print(s.center(7, "*"), "|", f"{s:*^7}")

    # 数字补零符号感知 vs 字符串 zfill
    print("format zero:", f"{-3.5:08.2f}")
    print("zfill      :", "-3.5".zfill(8), "|", "42".zfill(5))
