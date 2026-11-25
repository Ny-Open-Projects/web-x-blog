---
title: "[Q7235] downcast 到 int8 静默回绕：200 变成 -56，报表金额出现负值"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7235 · downcast 到 int8 静默回绕：200 变成 -56，报表金额出现负值

难度：P6 ｜ 标签：pandas、dtype、downcast、溢出

基线：Python 3.12 + `ctypes`（`c_int8` 与 numpy 的溢出行为一致：截断补码，不回绕报错）。

**问**：几千万行的明细表为了省内存，按列做了 `df["qty"] = pd.to_numeric(df["qty"], downcast="integer")`，又对类别列 `astype("int8")` 做编码。上线后汇总报表出现"负销量"，个别渠道的件数是 -56、-128。原始数据里根本没有负数，也没有空值。钱和数量都对不上，但代码没报任何 warning。为什么？

**答**：
- **结论**：**numpy/pandas 的整型转换是 C 语义的截断，不检查范围**：把 200 塞进 `int8`（范围 -128~127）得到 `200 - 256 = -56`；把 300 塞进去得到 44；把 -129 塞进去得到 127。`astype("int8")`、`downcast="integer"`、`array.astype(np.int8)` 全都是静默的。更隐蔽的是 `downcast="integer"` 会按列的 min/max 选"能装下的最小类型"——它看的是**当前这批数据的范围**，一旦后续批次出现更大的值（或数据被拼接、被重新计算），就会溢出。这也是"离线跑没事、上线就出负值"的典型来源。
- **取舍**：① 省内存优先用 **category**（类别数远小于行数时收益最大）或 `int32`（覆盖 ±21 亿，绝大多数计数够用），不要一上来就 int8/int16；② 必须 downcast 时先做范围断言（`min >= iinfo.min and max <= iinfo.max`），越界就拒绝并告警；③ 用 `pd.to_numeric(..., downcast="unsigned")` 前想清楚负值语义（销量退货会有负数，unsigned 会变巨大正数）；④ 用 `nullable` 的 `Int8`/`Int32`（大写 I）保留缺失值，避免 `NaN` 把整列推回 float64。
- **实战**：① 在 ETL 的 schema 层声明每列的合法范围，落盘前校验；② 单测构造边界值（127/128/-128/-129）跑一遍 downcast；③ 监控"负数计数"指标，出现即报警——这是溢出最直接的症状；④ Parquet/Arrow 落盘时 schema 固定为 int32/int64，别让读取时再自动推断。

```python
"""int8 截断：200 -> -56，且 sum 完全错掉。"""
import ctypes


def to_int8(v: int) -> int:
    """与 numpy 的 astype(np.int8) 一致：截断到低 8 位再按补码解释。"""
    return ctypes.c_int8(v).value


LIMITS = {"int8": (-128, 127), "int16": (-32768, 32767), "int32": (-2**31, 2**31 - 1)}


def safe_downcast(values: list[int], dtype: str) -> list[int]:
    lo, hi = LIMITS[dtype]
    bad = [v for v in values if not (lo <= v <= hi)]
    if bad:
        raise ValueError(f"{dtype} 越界: {bad[:5]}（范围 {lo}~{hi}）")
    return [to_int8(v) if dtype == "int8" else v for v in values]


def to_numeric_downcast(values: list[int | None]) -> tuple[str, list[float]]:
    """模拟 pd.to_numeric(downcast='integer')：有 NaN 就退回 float64。"""
    if any(v is None for v in values):
        return "float64", [float("nan") if v is None else float(v) for v in values]
    return "int32", [int(v) for v in values]


if __name__ == "__main__":
    qty = [100, 120, 127, 128, 200, 300]
    down = [to_int8(v) for v in qty]
    print("原始:", qty, "sum =", sum(qty))
    print("int8:", down, "sum =", sum(down), "-> 汇总直接错")
    print("边界: -129 ->", to_int8(-129), "| 128 ->", to_int8(128),
          "| 255 ->", to_int8(255))

    print("\n带范围校验的 downcast:")
    try:
        safe_downcast(qty, "int8")
    except ValueError as e:
        print(" ", e)
    ok = safe_downcast([0, 100, 127], "int8")
    print("  合法批次:", ok)

    print("\n有缺失值时 downcast 退化:")
    dtype, vals = to_numeric_downcast([1, None, 3])
    print("  dtype =", dtype, "values =", vals, "-> 4 字节/值，白省")

    rows = 100_000_000
    print(f"\n{rows:,} 行：int64->int32 省 {rows * 4 / 1024**2:.0f} MiB；"
          f"int64->int8 省 {rows * 7 / 1024**2:.0f} MiB")
    print("结论：downcast 必须前置范围校验；省内存首选 category / int32")
```

**追问一**：为什么 `pandas` 不做溢出检查？加检查的代价有多大？

→ 解析：`astype`/`downcast` 走的是 numpy 的 C 循环，逐元素做范围判断会引入分支与额外的比较指令，向量化路径会慢一个量级；而对"用户明确要求窄类型"的调用，pandas 的契约就是"按 C 语义转换"。折中做法是先用向量化的 min/max（O(n) 但常数极小）判断整列范围，再决定是否转换——比逐元素检查便宜得多，也足够安全。真正危险的是"按当前批次推断类型"，因为类型是**跨批次契约**，不该由数据样本决定。

**追问二**：`int8` 编码类别（`cat.codes`）安全吗？

→ 解析：`cat.codes` 的取值范围是 `[-1, len(categories)-1]`（-1 表示缺失），只要类别数 ≤ 128 就安全；超过 127 个类别还硬塞 int8 就会溢出，且溢出发生在编码后的下游计算里，很难回溯。更稳的是用 `int16`（3 万类别）或直接保留 category dtype——后者还带类别名映射，调试友好。另外**不同批次各自 `factorize` 的 code 不对应**（第 1 批 "A"=0，第 2 批 "A"=3），跨批合并必须传同一份 categories，否则 code 混用会算出完全错误的分组。
