---
title: "[Q6735] jsonb 往返：Decimal 变 float、NaN 写不进去、时间戳变字符串"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6735 · jsonb 往返：Decimal 变 float、NaN 写不进去、时间戳变字符串

难度：P6 ｜ 标签：PostgreSQL、jsonb、Decimal、序列化边界

基线：Python 3.12；`json.dumps(default=..., allow_nan=False)`；psycopg 把 jsonb 解析成 dict。

**问**：把订单快照 `json.dumps({"amount": Decimal("19.90"), "ts": datetime.now(), "rate": float("nan")})` 写进 PG 的 `jsonb` 列：不加 `default=` 直接 `TypeError`；加了 `default=str` 金额变成字符串 `"19.90"`、时间戳变成 `"2026-11-24 10:00:00.123456"`；不加 `default` 而只开 `allow_nan` 则写入报错 `invalid input syntax for type json`。jsonb 不是"存 JSON"吗，为什么类型全变了？

**答**：
- **结论**：JSON 只有 string/number/bool/null/array/object 六种类型，**没有 Decimal、没有 datetime、没有 NaN**。`json.dumps` 遇到 Decimal/datetime 抛 `TypeError`（除非给了 `default`）；`NaN` 被默认的 `allow_nan=True` 写成裸字面量 `NaN`，而 PG 的 jsonb 解析器只接受严格 JSON → 语法错误。读回来时 JSON number 被 psycopg 解析成 Python `float`，`19.90` 的十进制语义丢失。
- **取舍**：jsonb 灵活、可 GIN 索引、可 `@>` 查询，但代价是**类型系统退化到 JSON 那套**。金额要么存字符串（`"19.90"`，读侧 `Decimal(...)`），要么存整数最小单位（`1990` 分，最稳，还能直接比大小）；时间统一 ISO8601 带时区字符串；缺失/NaN 一律用 `null`。要范围查询的字段抽成独立列，别塞 jsonb。
- **实战**：① 出站统一 `json.dumps(payload, default=encoder, allow_nan=False)`，encoder 只处理已知类型，未知类型继续抛错（fail-fast）；② 金额、汇率用整数分/基点；③ 读侧做 schema 校验（pydantic/dataclass）而不是直接信任 dict；④ 契约测试断言 `Decimal("19.90")` 往返后仍相等。

```python
"""jsonb 出站编码：Decimal→字符串、datetime→ISO8601、NaN 拒绝。"""
import json
from datetime import datetime, timezone
from decimal import Decimal


class JsonbEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)                      # 保留十进制字面量
        if isinstance(o, datetime):
            if o.tzinfo is None:
                raise TypeError("naive datetime 不允许出站，先补时区")
            return o.isoformat()
        return super().default(o)              # 未知类型继续报错


def strict_loads(text: str):
    """模拟 PG jsonb / JS JSON.parse：拒绝 NaN、Infinity。"""

    def reject(token: str):
        raise ValueError(f"非法 JSON 常量: {token}")

    return json.loads(text, parse_constant=reject)


if __name__ == "__main__":
    payload = {
        "amount": Decimal("19.90"),
        "ts": datetime(2026, 11, 24, 10, 0, tzinfo=timezone.utc),
        "rate": 0.0735,
        "cnt": 3,
    }

    text = json.dumps(payload, cls=JsonbEncoder, allow_nan=False)
    print("编码结果:", text)

    back = strict_loads(text)
    print("读回 amount:", back["amount"], type(back["amount"]).__name__)
    print("金额用 Decimal 还原:", Decimal(back["amount"]) == Decimal("19.90"))

    # 1) 默认编码器直接失败
    try:
        json.dumps({"amount": Decimal("19.90")})
    except TypeError as e:
        print("默认编码器:", e)

    # 2) NaN 能骗过 Python，但骗不过 jsonb
    try:
        json.dumps({"rate": float("nan")}, allow_nan=False)
    except ValueError as e:
        print("allow_nan=False:", e)
    loose = json.dumps({"rate": float("nan")})
    try:
        strict_loads(loose)
    except ValueError as e:
        print("严格解析:", e, "-> PG jsonb 同样拒绝")

    # 3) naive datetime 必须当场炸，而不是被 str() 糊过去
    try:
        json.dumps({"ts": datetime(2026, 11, 24)}, cls=JsonbEncoder)
    except TypeError as e:
        print("naive:", e)

    # 4) 金额存整数分最稳
    cents = int(Decimal("19.90") * 100)
    print("整数分:", cents, "-> 无精度损失、可直接比较与聚合")
```

**追问一**：`json` 列和 `jsonb` 列怎么选？
→ 解析：`json` 存原始文本、保留空白与重复 key、写入快但每次查询都要重新解析；`jsonb` 存解析后的二进制、去重 key、可建 GIN 索引、支持 `?`/`@>`/`jsonb_path_query`。要查询或索引选 `jsonb`，只做归档日志可以选 `json` 省转换开销。

**追问二**：为什么 `default=str` 是"看起来能用"的坏解？
→ 解析：它把 Decimal、datetime、UUID、甚至自定义对象都降级成字符串，读侧无法区分"本来就是字符串"和"被降级"，金额会静默变成字符串比较（`"9.9" > "19.9"` 为 True），时间格式也随 `str()` 实现漂移。要显式类型映射表，让未知类型直接失败。
