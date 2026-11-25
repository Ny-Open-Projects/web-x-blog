---
title: "[Q7284] merge 的 many_to_many 膨胀：行数守恒断言与去重键设计"
date: 2026-11-25
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7284 · merge 的 many_to_many 膨胀：行数守恒断言与去重键设计

难度：P6 ｜ 标签：pandas、merge、笛卡尔膨胀、行数守恒、去重键、validate

基线：库知识卡，代码用标准库模拟——用 Counter 预计算 fanout 并做嵌套连接，不依赖 pandas。

**问**：订单宽表 `merge` 商品维表后，行数从 120 万涨到 380 万，GMV 汇总跟着翻了三倍；但 `merge(..., validate="many_to_one")` 没报错，因为商品维表里同一个 `sku` 确实有多条版本记录，`many_to_many` 在"语法"上是合法的。这种膨胀怎么在上线前发现？"去重键"应该怎么设计——按 `sku` 取最新一条就够了吗？

**答**：

- **结论**：`merge` 的行数不是"左表行数"，而是 **Σ over keys（左表该键行数 × 右表该键行数）**，再按 `how` 决定是否保留未匹配行。所以膨胀系数可以在 merge **之前**算出来：对两边各做一次 `groupby(key).size()`，按 key 对齐相乘求和，就是精确的期望行数。把这个值和 `len(result)` 对比，就是**行数守恒断言**——它能抓住 `validate` 抓不到的 many_to_many（validate 只校验"声明的是一对一/多对一"，而 many_to_many 本来就是合法的）。去重键的设计要点是：**先定义"一行代表什么"**。如果业务语义是"每个订单一行"，那右表必须先聚合成每个 `sku` 一行，聚合键要包含"版本选择规则"（取最新 `valid_from`、取有效期内、取优先级最高），而不是简单 `drop_duplicates("sku")`——后者保留哪一条取决于文件顺序，是不可复现的。
- **取舍**：三条路。① **右表预聚合到 1:1**（`sort_values(valid_from).groupby(sku).tail(1)`）：merge 前就把粒度对齐，最稳，代价是一次排序/聚合；② **先展开再去重**：merge 后按业务键 `drop_duplicates(keep="last")`，看似省事，但膨胀已经发生——内存峰值、聚合口径、中间指标都已经被污染，只适合小表；③ **保留多版本、显式 explode**：如果业务确实要"订单 × 商品版本"的明细，那就接受膨胀，但必须把膨胀系数写进断言与容量估算，并确认下游所有聚合都按正确的键去重（比如 GMV 要按 `order_id` 去重求和，不能直接 `sum`）。
- **实战**：一次大促前的宽表刷新，商品维表因为价格变更保留了 3 个版本/ sku，订单表 join 后行数 ×3，GMV 报表直接翻倍，直到财务对账才发现。复盘加了两道闸：① merge 前用 `groupby.size()` 算 fanout，超过 1.2 就告警；② merge 后 `assert len(result) == expected`，并把 `expected` 打进日志。去重键最终定为 `(sku, 价格生效时间 <= 下单时间)` 取最近一条——不是"最新版本"，因为历史订单要用下单时刻有效的价格，用最新版本会把历史 GMV 算成新价。

下面用 Counter 预计算 fanout，复现 3 倍膨胀，再用"版本去重键"把粒度拉回 1:1。

```python
# merge fanout 预估 + 行数守恒 + 版本去重键
from collections import Counter

# 左: 9 个订单, sku 各 3 条
left = [{"oid": i, "sku": f"s{i % 3}", "amount": 100 + i} for i in range(9)]
# 右: 每个 sku 3 个价格版本
right = [{"sku": s, "ver": v, "price": 10 * (v + 1)}
         for s in ("s0", "s1", "s2") for v in range(3)]

lc = Counter(r["sku"] for r in left)
rc = Counter(r["sku"] for r in right)
expected = sum(lc[k] * rc.get(k, 0) for k in lc)
print(f"[1] 左 {len(left)} 行, 右 {len(right)} 行, fanout 预估 {expected} 行")
assert expected == 27

merged = [(l, r) for l in left for r in right if l["sku"] == r["sku"]]
print(f"    实际 merge: {len(merged)} 行, 膨胀 {len(merged) / len(left):.1f}x")
assert len(merged) == expected, "行数守恒断言: 实际必须等于 fanout 预估"
print("    → 实测 many_to_many 是合法语法, validate 不会报, 只有行数守恒能抓")

# 直接 sum 金额: 每个订单被重复计 3 次
gmv_bad = sum(l["amount"] for l, _ in merged)
gmv_true = sum(l["amount"] for l in left)
print(f"[2] 直接 sum: {gmv_bad}, 按订单去重后: {gmv_true}, 放大 {gmv_bad / gmv_true:.0f}x")
assert gmv_bad == 3 * gmv_true

# 去重键: 不是"最新版本", 而是"下单时刻生效的版本"
ORDER_TS = 5
prices = {("s0", 0): (1, 10), ("s0", 1): (4, 12), ("s0", 2): (8, 15),
          ("s1", 0): (1, 20), ("s1", 1): (4, 22), ("s1", 2): (8, 25),
          ("s2", 0): (1, 30), ("s2", 1): (4, 32), ("s2", 2): (8, 35)}


def pick(sku, ts):
    """取 valid_from <= ts 的最近一条; 没有则 None。"""
    cands = [(vf, p) for (s, _), (vf, p) in prices.items() if s == sku and vf <= ts]
    return max(cands)[1] if cands else None


dim = {s: pick(s, ORDER_TS) for s in ("s0", "s1", "s2")}
print(f"[3] 下单时刻 {ORDER_TS} 生效价格: {dim}")
assert dim == {"s0": 12, "s1": 22, "s2": 32}

# 1:1 粒度后 merge, 行数守恒
one_to_one = [(l, dim[l["sku"]]) for l in left]
print(f"    去重后 merge: {len(one_to_one)} 行 == 左表 {len(left)} 行")
assert len(one_to_one) == len(left)
latest = {s: prices[(s, 2)][1] for s in ("s0", "s1", "s2")}
print(f"    → 实测 用'最新版本'会得到 {latest}, 与下单时刻价 {dim} 不同; 去重键必须带时间语义")
assert latest != dim
```

**追问一**：`validate="one_to_one"` / `"many_to_one"` 到底校验什么，为什么挡不住这次事故？—— 它校验的是**右表（或两侧）在连接键上是否唯一**，不校验业务语义。`many_to_one` 只要求右表键唯一；本例右表 `sku` 有 3 条，所以会直接抛 `MergeError`——如果真开了 validate，事故其实能挡住。真正挡不住的是 `validate="many_to_many"` 或干脆不传：它接受任意重复，行数照样膨胀。另一个盲区是**多键连接**：只对 `sku` 校验唯一，但业务键是 `(sku, 渠道)`，右表在 `sku` 上唯一、在 `(sku, 渠道)` 上不唯一，validate 通过、结果仍然膨胀。所以 validate 是"声明式契约"，不能替代行数守恒断言。

**追问二**：如果业务确实需要保留多版本明细，怎么保证下游聚合不被重复计数？—— 把"一行代表什么"显式化：输出表加一列 `row_grain`（如 `order × price_version`），所有下游聚合必须先声明粒度，再决定去重键。金额类指标按 `order_id` 去重（`drop_duplicates("order_id")` 后求和，或 `groupby("order_id").amount.first()`），数量类指标要确认是否真的可加（同一订单的多个版本数量是重复的，不能加）。更彻底的做法是**在宽表里就把"下单时刻价格"物化成单值**，多版本只留在维表/审计表，宽表保持 1:1——用存储换正确性，通常比让每个下游都记得去重更划算。

## 背诵要点

- merge 行数 = Σ(左键行数 × 右键行数)，可在 merge 前用两次 `groupby(key).size()` 精确预估；断言 `len(result) == expected`。
- `validate` 只校验声明的键唯一性，`many_to_many` 合法且照样膨胀；多键连接时单键唯一不代表组合唯一。
- 去重键必须带业务时间语义（如下单时刻生效版本），不能 `drop_duplicates` 靠文件顺序；保留多版本时要显式声明粒度并让下游按业务键去重。

## 复盘追问

- merge 后行数从 120 万变 380 万，怎么在跑之前就知道会是 3 倍？（两边按连接键 count，逐键相乘求和；再对比左表行数得到膨胀系数）
- 为什么 `drop_duplicates("sku")` 取到的不一定是"正确的那条"？（无排序时保留顺序依赖输入；正确做法是按 valid_from/优先级显式排序后取，且要结合下单时刻）
