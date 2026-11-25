---
title: "[Q7205] explode 的行数放大与空列表变 NaN"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7205 · explode 的行数放大与空列表变 NaN

难度：P6 ｜ 标签：pandas、explode、行数放大、缺失值

基线：Python 3.12；pandas 2.x `explode` 语义；纯 Python 模拟展开行为。

**问**：订单表的 `items` 列存商品列表，`df.explode("items")` 后做商品维度汇总：总金额比原表多了一截（3 个商品的订单被计了 3 次），清理空商品后又少了一截（空购物车订单不见了）。`explode` 到底怎么处理空列表、None 和多元素列表？

**答**：
- **结论**：`explode` 把列表的**每个元素展开成一行**，行数 = 各列表长度之和；**空列表和 None 不会丢行，而是展开成一行 NaN**（这是 pandas 的明确语义）。所以：多元素列表 → 金额被重复计数；空列表/None → 变成 `item=NaN` 的行，如果下游 `dropna(subset=["item"])` 就会把整张订单丢掉。两个方向的误差同时存在，合计自然对不上。
- **取舍**：`explode` 适合"一行一元素"的明细分析。要保留空列表订单，就别在下游无条件 `dropna`，或者先把空列表归一成 `["__EMPTY__"]` 哨兵；要避免金额重复，订单级金额在**展开前**按订单算，展开只用于商品级指标。反过来统计"商品数"时又必须对订单去重。
- **实战**：① 展开前后记 `len(df)` 与订单号 `nunique`：行数应等于 `sum(max(len(x),1))`；② 空列表显式标记，不要靠 `dropna` 隐式处理；③ 指标分层：订单金额展开前算，商品金额展开后算；④ 大列表 explode 会放大内存，先估算总元素数再决定分块。

```python
def explode_rows(orders: list[dict]) -> list[dict]:
    """空列表/None 展开成一行 item=None，与 pandas explode 语义一致。"""
    out = []
    for order in orders:
        items = order.get("items")
        if not items:                       # [] 或 None：保留一行 NaN
            out.append({"order_id": order["order_id"], "item": None,
                        "amount": order["amount"]})
            continue
        for item in items:
            out.append({"order_id": order["order_id"], "item": item,
                        "amount": order["amount"]})
    return out


if __name__ == "__main__":
    orders = [
        {"order_id": 1, "amount": 100, "items": ["A", "B", "C"]},
        {"order_id": 2, "amount": 50, "items": []},
        {"order_id": 3, "amount": 80, "items": None},
        {"order_id": 4, "amount": 30, "items": ["A"]},
    ]
    rows = explode_rows(orders)
    print("原订单数:", len(orders), "展开行数:", len(rows))
    print("直接 sum:", sum(r["amount"] for r in rows), "（重复计数）")
    cleaned = [r for r in rows if r["item"] is not None]
    print("dropna 后 sum:", sum(r["amount"] for r in cleaned), "（丢了空购物车）")
    print("按订单去重 sum:", sum(o["amount"] for o in orders))
    print("结论：explode 既放大行数，也把空列表变成 NaN 行")
```

**追问一**：为什么"先 explode 再按订单去重金额"不一定对？
→ 解析：去重能消掉多商品订单的重复金额，但空列表订单已经变成 `item=NaN` 的行；如果之前做过 `dropna`，去重也找不回来。而且同一订单的不同商品金额不同时，去重保留哪一条是随机的。正确做法是金额在展开前按订单算。

**追问二**：`explode` 和 `merge` 造成的行数放大有什么共同点和区别？
→ 解析：共同点是"一行变多行"，都会让 `sum`/`count` 翻倍；区别是 `explode` 由列表长度决定、可预测（空列表固定 1 行 NaN），`merge` 由键的重复度决定、往往在关联时才暴露（多对多）。两者都要在操作前后核对行数与主键唯一性。
