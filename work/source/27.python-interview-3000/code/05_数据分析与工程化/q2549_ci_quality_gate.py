"""CI 中的数据质量门禁: error 拦合并 warn 只留痕"""

import sys

CHECKS = [
    ("row_count", "error", lambda d: (d["rows"] > 0, f"rows={d['rows']}")),
    ("unique_key", "error", lambda d: (len(d["ids"]) == len(set(d["ids"])), "主键唯一")),
    ("null_ratio", "error", lambda d: (d["nulls"] / max(d["rows"], 1) < 0.1,
                                       f"空值率 {d['nulls'] / max(d['rows'], 1):.0%}")),
    ("freshness", "warn", lambda d: (d["age_hours"] <= 24, f"数据龄 {d['age_hours']}h")),
]


def gate(data):
    errors, warns, lines = 0, 0, []
    for name, severity, fn in CHECKS:
        ok, msg = fn(data)
        tag = "PASS" if ok else severity.upper()
        lines.append(f"[{tag}] {name}: {msg}")
        if not ok and severity == "error":
            errors += 1
        elif not ok:
            warns += 1
    code = 1 if errors else 0
    lines.append(f"门禁结论: error={errors} warn={warns} -> 退出码 {code}"
                 + ("(拦截合并)" if code else "(放行)"))
    return code, lines


if __name__ == "__main__":
    good = {"rows": 500, "ids": list(range(500)), "nulls": 10, "age_hours": 3}
    bad = {"rows": 500, "ids": list(range(499)) + [0], "nulls": 120, "age_hours": 3}
    for name, data in [("正常样本", good), ("异常样本", bad)]:
        code, lines = gate(data)
        print(f"-- {name} --")
        print("\n".join("  " + l for l in lines))
        assert code == (0 if name == "正常样本" else 1)
        if code:
            sys.exit = sys.exit          # CI 场景下非零码直接拦截, 演示中仅断言
    print("要点: 门禁分 error/warn 两级, error 卡合并, warn 进报告; 退出码是 CI 唯一通用的语言")
