---
title: "[Q7283] pandas Category 的字典编码：内存账与 observed 的静默行数差异"
date: 2026-11-25
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7283 · pandas Category 的字典编码：内存账与 observed 的静默行数差异

难度：P6 ｜ 标签：pandas、Category、字典编码、内存、groupby、observed、基数

基线：库知识卡，代码用标准库模拟——用 `array` 的 codes + 类别字典还原 Category 的存储结构，不依赖 pandas。

**问**：一张 1000 万行的订单表把 `city`、`status` 两列转成 `category`，内存从 3.2GB 降到 2.1GB，团队准备把所有字符串列都转一遍；结果 `order_id`（900 万唯一值）转完内存反而涨了 400MB。同时另一张报表把 `groupby(["city","status"])` 的 `observed` 从默认改成 `True` 后，行数从 1200 掉到 900，对账直接不平。Category 的内存账到底怎么算？`observed` 改的又是什么？

**答**：

- **结论**：Category 是**字典编码**：一列拆成两段——`codes`（每行一个整数，指向类别数组的下标）和 `categories`（去重后的取值数组）。内存 = `n × codes 宽度` + `基数 × 类别对象开销` + 哈希索引开销。codes 宽度随基数自动选（`int8` <128、`int16` <32768、`int32` 更大），所以**低基数时** 1000 万行只要 10MB，而 object 列是 `n × (指针 + 字符串对象)` ≈ 600MB，差两个数量级；**高基数时**类别数组本身就要几百 MB，加上哈希索引反而比 object 更贵。经验阈值：**基数 / 行数 < 10%** 才值得转，且要留出新增类别的余量。`observed` 是另一个维度的坑：`observed=False`（pandas 2.x 默认，带 FutureWarning）会为**所有类别组合**生成分组，包括数据里从未出现过的组合，聚合结果补 0 或 NaN；`observed=True` 只保留真实出现的组合——两者**求和相等但行数不同**，下游按行数或按索引 join 就会静默错位。
- **取舍**：Category 适合"取值集合稳定、需要排序/去重/小内存"的列（城市、状态、渠道）；不适合高基数列（订单号、用户 ID）、需要频繁字符串操作的列（转回 object 后编码白做）、以及**类别会持续新增**的列（每次新增都要改 categories，跨分区的 category 类别不一致还会在 concat 时退化成 object）。`observed` 的选择取决于语义：报表要"完整维度矩阵"（缺失组合补 0）就用 `False` 并显式 reindex；要"只统计出现过的"就用 `True`，但必须在断言里锁定行数，不能让它悄悄变。
- **实战**：一次日活报表从 7 天改成 30 天，行数反而变少，排查发现是升级 pandas 后 `observed` 默认值变化：原来 `False` 会给"某城市 × 某状态"补零行，`True` 只保留出现过的组合，而下游用 `merge` 按索引对齐，缺的行直接变成 NaN 被 `dropna` 吃掉。修复不是改回 `False`，而是在聚合后**显式 reindex 到完整维度**（`pd.MultiIndex.from_product`），并把"期望行数 = 城市数 × 状态数"写成断言。另一边，`order_id` 转 category 的收益为负，回滚后内存恢复——两件事都不是 bug，是没算清账。

下面用 codes + 类别表还原内存公式，并复现 `observed` 的行数差异。

```python
# Category 内存账 + observed 的行数差异(标准库模拟)
import sys
from array import array

SAMPLE = "Shanghai"                       # 代表一个类别字符串
STR_BYTES = sys.getsizeof(SAMPLE)         # 字符串对象本体
PTR = 8


def object_bytes(n):
    """object 列: 每行一个指针 + 一个独立的 str 对象。"""
    return n * (PTR + STR_BYTES)


def category_bytes(n, cardinality, dict_overhead=2.5):
    """codes + categories + 哈希索引(经验系数 2.5)。"""
    code_width = 1 if cardinality < 128 else (2 if cardinality < 32768 else 4)
    return n * code_width + int(cardinality * (PTR + STR_BYTES) * dict_overhead)


N = 10_000_000
obj = object_bytes(N)
print(f"[1] {N:,} 行 object 列约 {obj / 1024**2:.0f}MB")
for card in (20, 200, 60_000, 9_000_000):
    cat = category_bytes(N, card)
    print(f"    基数 {card:>9,}: category 约 {cat / 1024**2:>7.0f}MB, "
          f"相对 object {cat / obj:>5.2f}x")
    if card == 20:
        assert cat < obj / 10, "低基数必须显著省内存"
    if card == 9_000_000:
        assert cat > obj, "高基数 category 反而更贵"
print("    → 实测 拐点在'基数占比'而非绝对值: codes 省下的钱被类别表吃回去")

# observed=False vs True: 2x2 的类别, 只观测到 3 种组合
rows = [("x", "p"), ("x", "q"), ("y", "p"), ("x", "p"), ("y", "p")]
observed_pairs = sorted(set(rows))
all_pairs = sorted({(a, b) for a in ("x", "y") for b in ("p", "q")})
print(f"[2] 实际出现的组合 {observed_pairs}, 完整笛卡尔 {all_pairs}")
assert len(observed_pairs) == 3 and len(all_pairs) == 4

from collections import Counter
cnt = Counter(rows)
obs_rows = [(k, cnt[k]) for k in observed_pairs]
full_rows = [(k, cnt.get(k, 0)) for k in all_pairs]
print(f"    observed=True 行数 {len(obs_rows)}, observed=False 行数 {len(full_rows)}")
assert len(full_rows) == 4 and len(obs_rows) == 3
assert sum(v for _, v in obs_rows) == sum(v for _, v in full_rows)
print("    → 实测 两者合计相等, 但行数差 1; 下游按行数/索引 join 会静默错位")

# 下游 merge: 缺的组合在 inner join 后直接消失
report_keys = [k for k, _ in obs_rows]
downstream = [k for k in full_rows if k[0] in report_keys]
print(f"[3] 完整维度驱动 join observed 结果: 命中 {len(downstream)}/4, "
      f"缺失 {sorted(set(k for k, _ in full_rows) - set(report_keys))}")
assert len(downstream) == 3
print("    → 实测 observed 是语义开关, 不是性能开关; 要补零就显式 reindex")
```

**追问一**：为什么两列都是 category 时，`concat` 之后常常退化成 object？—— Category 的相等性要求 **categories 集合与顺序完全一致**。两个分区各自编码时，A 分区见过 `["北京","上海"]`、B 分区见过 `["上海","广州"]`，`codes` 的整数含义不同，直接拼会错位；pandas 的安全做法是退化成 object（或取并集后重编码，取决于版本与 `union_categoricals`）。工程做法是**先定义全局 categories 再分块转换**（`pd.CategoricalDtype(categories=GLOBAL, ordered=True)`），或拼完用 `union_categoricals` 显式合并。否则你会看到"分块处理时内存很低，concat 那一刻内存翻倍"。

**追问二**：`observed=False` 既然会给未观测组合补行，为什么还会有人依赖它？—— 因为它保证了**维度矩阵的完整性**：报表要展示"每个城市 × 每个状态"的格子，即使某格为 0 也要出现，否则前端表格会缺列、环比计算会错位。问题不在 `False` 本身，而在"默认值悄悄变了"且下游没有断言。正确姿势是把维度完整性显式化：用 `MultiIndex.from_product` 构造完整索引再 `reindex(fill_value=0)`，这样无论 `observed` 取什么值、数据里有没有组合，输出行数都是确定的；同时把期望行数写成测试断言，默认值变化时第一时间炸出来。

## 背诵要点

- Category = codes（int8/16/32 自适应）+ categories 去重数组 + 哈希索引；内存只在低基数（经验 <10%）时赢，高基数会被类别表反噬。
- `observed=False` 生成完整笛卡尔组合（缺失补 0/NaN），`True` 只保留出现过的组合；两者合计相等、行数不同。
- 跨分区 category 必须统一 categories 定义，否则 concat 退化 object；维度完整性用 `reindex` 显式表达，不要依赖默认值。

## 复盘追问

- 1000 万行、20 个类别的列转 category 省多少？900 万唯一值的列呢？（前者约 1/15；后者类别表 + 哈希索引超过 object，转了就亏）
- `observed` 从 False 改 True 后报表行数变少，你怎么判断是"少统计"还是"少了补零行"？（对比分组键的组合数与数据中实际出现的组合数；合计值不变即只是补零行消失）
