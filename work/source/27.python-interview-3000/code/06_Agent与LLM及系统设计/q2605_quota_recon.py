"""Q2605 配额结算的对账:流水累加对不上结算单要能定位差异。

月末对账三方口径:用量流水按租户累加、结算单按租户累加,先按
结算单号去重再比差值;差值非零要能指出是哪个租户差多少,漏单
与重复单都能当场定位。
"""
from collections import defaultdict

LEDGER = [  # 用量流水: 租户, tokens, 事件号
    ("t1", 100, "e1"), ("t1", 250, "e2"), ("t2", 80, "e3"), ("t3", 40, "e4"),
]
SETTLE = [  # 结算单: 租户, tokens, 单号(t1 少结 50, s3 重复出现)
    ("t1", 300, "s1"), ("t2", 80, "s2"), ("t3", 40, "s3"), ("t3", 40, "s3"),
]


def reconcile(ledger, settle):
    usage = defaultdict(int)
    for t, tok, _ in ledger:
        usage[t] += tok
    billed = defaultdict(int)
    seen = set()
    dup = []
    for t, tok, sid in settle:
        if sid in seen:
            dup.append(sid)
            continue
        seen.add(sid)
        billed[t] += tok
    diffs = {}
    for t in sorted(set(usage) | set(billed)):
        d = billed[t] - usage.get(t, 0)
        if d != 0:
            diffs[t] = d
    return dict(usage), dict(billed), diffs, dup


def main():
    usage, billed, diffs, dup = reconcile(LEDGER, SETTLE)
    assert usage == {"t1": 350, "t2": 80, "t3": 40}, usage
    assert billed == {"t1": 300, "t2": 80, "t3": 40}, billed
    assert diffs == {"t1": -50}, diffs
    assert dup == ["s3"], dup
    ledger2 = [e for e in LEDGER if e[2] != "e3"]   # 流水丢一条
    _, _, diffs2, _ = reconcile(ledger2, SETTLE)
    assert diffs2 == {"t1": -50, "t2": 80}, diffs2
    print("用量:", usage)
    print("结算:", billed)
    print("差异:", diffs, "→ t1 少结 50 tokens 需补账")
    print("重复结算单:", dup, "已按单号去重")
    print("流水漏单场景差异:", diffs2, "→ t2 少记 80 可当场定位")


if __name__ == "__main__":
    main()
