"""特征测试:固化现状 -> 重构 -> 新旧实现输出一致。"""

INPUTS = [0, 1, 59, 60, 61, 89, 90, 91, 100, 105, -5]


def grade_legacy(score):
    """遗留实现:怪癖是 105 与负数也不报错,按边界硬算。"""
    if score < 60:
        return "F"
    return "ABCDF"[(100 - score) // 10] if score <= 100 else "A+"


def grade_refactored(score):
    """重构版:结构更清晰,但行为必须与 legacy 完全一致。"""
    if score < 60:
        return "F"
    if score > 100:
        return "A+"
    return "ABCDF"[(100 - score) // 10]


if __name__ == "__main__":
    golden = {s: grade_legacy(s) for s in INPUTS}   # 第一步:固化现状
    print("固化的怪癖:", {k: v for k, v in golden.items() if k in (105, -5)})

    mismatches = [(s, golden[s], grade_refactored(s))
                  for s in INPUTS if grade_refactored(s) != golden[s]]
    print("重构后与现状不一致的输入:", mismatches, "(应为空,守护通过)")
