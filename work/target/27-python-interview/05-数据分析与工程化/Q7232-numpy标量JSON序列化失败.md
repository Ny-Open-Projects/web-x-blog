---
title: "[Q7232] json.dumps 遇到 numpy 标量：TypeError 与 default=str 的两种坏解"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7232 · json.dumps 遇到 numpy 标量：TypeError 与 default=str 的两种坏解

难度：P6 ｜ 标签：pandas、numpy 标量、json、序列化边界

基线：Python 3.12；`json.dumps(..., default=...)`；pandas 2.x 聚合返回 numpy 标量。

**问**：把 DataFrame 聚合结果直接 `json.dumps({"gmv": df["gmv"].sum(), "cnt": df["uid"].count()})` 回传前端，报 `TypeError: Object of type int64 is not JSON serializable`。加 `default=str` 能跑了，但前端收到的 `"cnt": "128"` 是字符串，排序和求和全乱。为什么 pandas 聚合出来不是原生 int？

**答**：
- **结论**：`df.sum()` / `count()` 返回的是 **numpy 标量**（`np.int64` / `np.float64`），不是 Python `int`/`float`。`json` 只认 `int/float/str/bool/None/list/dict`，`np.int64` 不是 `int` 的子类，所以序列化失败。`default=str` 把未知类型一律 `str()`，`np.int64` 变 `"128"`、`Timestamp` 变 `"2026-11-24 00:00:00"`，类型信息全丢；`default=float` 又会把大整数丢精度。
- **取舍**：三条正路：① 出口前逐字段 `int()`/`float()` 强转（最土但最准）；② 自定义 encoder 只处理已知类型（`np.integer`→`int`、`np.floating`→`float`、`np.bool_`→`bool`、`Timestamp`→isoformat），未知类型继续抛错（fail-fast）；③ 用 `orjson`/pydantic 做类型化序列化。关键原则：**不要用 `default=str` 兜底**。
- **实战**：① 统一 `NumpyJSONEncoder` 放在 API 出口；② 契约测试断言 `type(payload["cnt"]) is int`；③ 金额用整数分（`int()` 安全），超过 2^53 的 ID 用字符串；④ 同时 `allow_nan=False` 挡掉 NaN；⑤ 让未知类型抛错，比"生产环境静默变字符串"好排查得多。

```python
"""numpy 标量不可 JSON 序列化：default=str 的三种坏结果与类型化 encoder。"""
import json
from datetime import datetime, timezone


class Int64:
    """模拟 np.int64：不是 int 的子类，json 不认。"""

    def __init__(self, v: int) -> None:
        self.v = v

    def __str__(self) -> str:
        return str(self.v)

    def __int__(self) -> int:
        return self.v

    def __float__(self) -> float:
        return float(self.v)


class Float64:
    def __init__(self, v: float) -> None:
        self.v = v

    def __str__(self) -> str:
        return str(self.v)

    def __float__(self) -> float:
        return self.v


class NumpyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Int64):
            return int(o)
        if isinstance(o, Float64):
            return float(o)
        if isinstance(o, datetime):
            if o.tzinfo is None:
                raise TypeError("naive datetime 不允许出站")
            return o.isoformat()
        return super().default(o)          # 未知类型继续报错，别静默降级


if __name__ == "__main__":
    payload = {
        "gmv": Float64(12345.6),
        "cnt": Int64(128),
        "updated_at": datetime(2026, 11, 24, 10, 0, tzinfo=timezone.utc),
    }

    # 1) 默认编码器：直接失败
    try:
        json.dumps(payload)
    except TypeError as e:
        print("默认:", e)

    # 2) default=str：能跑，但数字变字符串
    loose = json.loads(json.dumps(payload, default=str))
    print("default=str:", loose)
    print("  cnt 类型:", type(loose["cnt"]).__name__,
          "| 前端排序会按字典序: '9' > '128' ->", "9" > "128")

    # 3) default=float：大整数精度丢失
    big = {"uid": Int64(2**53 + 1)}
    print("default=float:", json.dumps(big, default=float),
          "-> 尾数被抹平")

    # 4) 类型化 encoder：类型与精度都保住
    good = json.dumps(payload, cls=NumpyEncoder, allow_nan=False)
    parsed = json.loads(good)
    print("encoder:", good)
    print("  cnt 类型:", type(parsed["cnt"]).__name__,
          "| gmv 类型:", type(parsed["gmv"]).__name__)

    # 5) 未知类型仍然 fail-fast
    class Weird:
        pass

    try:
        json.dumps({"x": Weird()}, cls=NumpyEncoder)
    except TypeError as e:
        print("未知类型:", e)

    print("结论：出口做显式类型映射；default=str 会把数字变成字符串，埋进前端排序")
```

**追问一**：为什么 `int(np.int64(2**53 + 1))` 之后前端还会丢精度？
→ 解析：Python 侧转成 int 没问题，问题在 JSON 文本被 JS 解析时——JS 的 Number 是 IEEE754 双精度，安全整数上限 2^53-1。超过这个范围的 ID 必须以**字符串**形式输出（`str(int(...))`），而不是指望前端"小心处理"。

**追问二**：`json.dumps` 对 `Decimal`、`set`、`bytes` 分别怎么处理？
→ 解析：三者都不可序列化，全部抛 `TypeError`。`Decimal` 要显式转 `str` 或 `float`（金额优先 `str` 保单精度）；`set` 转 `sorted(...)` 保证输出确定性；`bytes` 转 base64 或 hex。都不要交给 `default=str` 自动处理。
