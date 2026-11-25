---
title: "[Q7300] groupby.first 不是第一行：它取的是第一个非空值"
date: 2026-11-25
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7300 · groupby.first 不是第一行：它取的是第一个非空值

难度：P7 ｜ 标签：pandas、groupby、first、nth、缺失值、去重取首条

基线：库知识库外知识卡，用纯 Python 分组列表模拟 `groupby.first()/last()/nth(0)` 的"跳过空值"与"按位置取"差异。

**问**：订单有多条支付流水，想取"第一笔支付的渠道"：`orders.groupby("order_id")["channel"].first()`。上线后发现 3.2 万单的渠道取到了第二笔甚至第三笔，因为第一笔的 `channel` 是空的（老网关没回填）。同一批数据用 `head(1)` 又是对的。`first()` 不是"第一行"吗？它和 `nth(0)`、`head(1)` 到底差在哪？`last()` 也有同样的问题吗？

**答**：

- **结论**：`groupby.first()`/`last()` 的语义是**"第一个/最后一个非空值"**，不是"第一行/最后一行"——它们默认 `skipna=True`，跳过 `NaN`。很多人只记得“first”，忘了这个默认值，把它当成“第一行”。`nth(0)` 按**位置**取组内第 0 行，保留空值；`head(1)` 也是按位置取每组前一行。所以只要首行/末行有缺失，`first()/last()` 就会"向前/向后借"一个值，看起来像取错了行。这个差异在"取首条快照""取最后一次状态"的场景里非常致命。
- **取舍**：① `nth(0)`：按位置、保留 NaN，最符合"第一行"直觉，但要求组内顺序已确定（先 `sort_values`）；② `head(1)`：返回 DataFrame，适合保留整行，但多列一起取时要注意对齐；③ `drop_duplicates(subset=..., keep="first")`：按业务键去重取首条，语义最清楚，适合"每单一条"；④ `first()`：只在"明确要第一个非空值"时用，比如"取首个可用联系人"，不是"取首行"。
- **实战**：① 取首条/末条前先显式排序（`sort_values(["order_id","paid_at"])`），不要依赖文件原始顺序；② 用 `nth(0)`/`drop_duplicates` 代替 `first()`，并在注释里写清"按位置"；③ 断言：`result["channel"].isna().sum()` 应与"首行缺失的组数"一致，不能被 `first()` 悄悄填平；④ 对"最后一次状态"用 `last()` 同样要小心，末行缺失会取到更早的值。

下面模拟两组订单：第一组首行渠道为空、第二组末行为空，对比 `first/last/nth` 的结果。

```python
# groupby.first/last 跳过空值; nth(0)/head(1) 按位置取, 保留空值
GROUPS = {
    "o1": [None, "wx", "ali"],      # 首行渠道缺失
    "o2": ["card", None, "wx"],     # 中间缺失, 末行有值
    "o3": ["card", None, None],     # 末行缺失
}


def first_skipna(values):
    for v in values:
        if v is not None:
            return v
    return None


def last_skipna(values):
    for v in reversed(values):
        if v is not None:
            return v
    return None


def nth0(values):
    return values[0]


def last_pos(values):
    return values[-1]


print(f"[1] o1 first={first_skipna(GROUPS['o1'])}, nth(0)={nth0(GROUPS['o1'])}")
print(f"[2] o3 last={last_skipna(GROUPS['o3'])}, 位置末行={last_pos(GROUPS['o3'])}")
assert first_skipna(GROUPS["o1"]) == "wx"
assert nth0(GROUPS["o1"]) is None
assert last_skipna(GROUPS["o3"]) == "card"
assert last_pos(GROUPS["o3"]) is None
print("    → 实测 first/last 会跨过空行取值, 与'第一行/最后一行'不是一回事")

# 全组都为空时, first 返回 None, 不会报错
assert first_skipna([None, None]) is None
assert last_skipna([None, None]) is None

# 业务口径: 每单第一笔支付渠道, 应该按 paid_at 排序后取位置 0
def first_by_position(records):
    ordered = sorted(records, key=lambda r: r["paid_at"])
    return ordered[0]["channel"]


records = [
    {"order_id": "o1", "paid_at": "2026-11-01T10:00", "channel": None},
    {"order_id": "o1", "paid_at": "2026-11-01T10:05", "channel": "wx"},
]
print(f"[3] 按 paid_at 排序取第一笔: channel={first_by_position(records)}")
assert first_by_position(records) is None

# 修复后对账: 取首条保留空值, 缺失数应等于'首行缺失的组数'
fixed = {k: nth0(v) for k, v in GROUPS.items()}
missing = sum(1 for v in fixed.values() if v is None)
print(f"[4] nth(0) 结果={fixed}, 缺失组数={missing}")
assert missing == 1          # 只有 o1 的首行本身缺失
print("    → 实测 缺失是数据事实, 不是 bug; 用 first 填平反而掩盖了首行缺失")
```

**追问一**：`first(skipna=False)` 不就等于第一行了吗？—— 语义上接近，但仍有坑：它要求组内顺序已确定（先排序），而且老版本/部分封装不暴露 `skipna` 参数；更稳妥的是 `nth(0)`/`head(1)`/`drop_duplicates`，语义一眼可见。`first` 的设计意图是“聚合出第一个可用值”（类似 SQL 的 `FIRST_VALUE ... IGNORE NULLS`），不是“取首行”。

**追问二**：`last()` 在"取最后一次状态"时一定对吗？—— 不一定。如果最后一行的状态字段为空（比如只更新了备注），`last()` 会取到更早的状态，而位置末行是空。业务上要明确"最后一次**有值**的状态"还是"最后一行的状态"；前者用 `last()`，后者用 `nth(-1)`，两者在缺失场景下结果不同。

## 背诵要点

- `groupby.first()/last()` 取**第一个/最后一个非空值**，跳过 NaN；`nth(0)`/`head(1)` 按位置取，保留空值。
- `first()` 默认 `skipna=True`；要"第一行"用 `nth(0)`/`head(1)`/`drop_duplicates(keep="first")`，并先显式排序（新版可 `first(skipna=False)`，但语义仍不如按位置直观）。
- 取首条后统计缺失组数，缺失是数据事实；用 `first` 填平会掩盖"首行缺失"。

## 复盘追问

- `groupby.agg("first")` 与 `groupby.first()` 行为一致吗？多列聚合时哪些列会被跳过？
- 如果业务要"第一笔非空渠道"，但"第一笔"和"第一个非空"都有人理解，怎么在指标口径里写清楚？
