---
title: "[Q5227] None 混入排序的 TypeError 与混合类型排序策略"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5227 · None 混入排序的 TypeError 与混合类型排序策略

难度：P6 ｜ 标签：排序、None、TypeError、key 函数、cmp_to_key、NULL 语义、混合类型

**问**：`sorted([3, None, 1])` 为什么炸？三种修复方案（key 元组、类型标签、cmp_to_key）分别怎么写、怎么选？数据库 `NULLS FIRST/LAST` 语义在应用层怎么补齐？混合 int/str 的列表怎么排？

**答**：
结论：`sorted` 在元素间直接调 `<`，而 `None` 与任何数比较都抛 `TypeError: '<' not supported between instances of 'NoneType' and 'int'`——数据来自 DB（NULL 列）、上游 JSON（null）时这是常态而非边角。修复三式：①**key 元组**——`key=lambda v: (v is None, v if v is not None else 0)`，利用 False<True 把 None 统一压到末尾（或反写压到开头），None 段内的占位值不影响段间顺序；②**类型标签**——`key=lambda v: (type(v).__name__, v)`，解决 int/str 混排的"比较跨类型崩溃"，代价是排序结果是"按类型分组再各自排"，语义要和业务确认；③**cmp_to_key**（Q2623）——显式写比较函数，None 视为最大/最小一句话说清，语义最直白，代价是 O(n log n) 次回调（Python 层比较慢于 C 层 key）。原则：排序契约里"None 放哪"是业务决定，代码只负责显式表达；数据库有 `NULLS LAST/FIRST` 时尽量下推到 SQL，应用层补齐仅在取回内存后排序的场景。

取舍：a) 数据量大（>10⁵）：key 元组（C 层比较）显著快于 cmp_to_key（每比较一次 Python 回调）；b) 语义复杂（None 按某字段、多级NULL 语义）：cmp_to_key 可读性赢；c) 通用防御：入口把 None 归一化（填默认值/丢弃）往往比在排序处打补丁更对——排序是消费点，数据质量问题应该在上游解决；d) 混合类型排序结果依赖标签选取，评审时必须让业务方确认分组顺序；e) 稳定性：key 值相同的多行按原顺序保留（Q514），分页跨页排序必须补 tie-breaker（唯一键）防止页间抖动，None 段同样需要。

实战：事故形态是"排行榜接口从 DB 拉分数排内存，某批测试数据 score 为 NULL，接口 500；修复为 SQL 下推 `ORDER BY score DESC NULLS LAST`，内存兜底版本用 key 元组，并给分页补 id tie-breaker"。下面演示崩溃点与三式修复。

```python
# None 混入排序的 TypeError 与混合类型排序策略
import functools

print("[1] 直接排序含 None 的列表: '<' not supported between NoneType and int")
try:
    sorted([3, None, 1, 2])
except TypeError as exc:
    print("    TypeError:", exc)

print("[2] 解法一: key 把 None 归一到末尾 (False<True, None 段用占位值)")
data = [3, None, 1, 2, None, 5]
print("    ", sorted(data, key=lambda v: (v is None, v if v is not None else 0)))

print("[3] 解法二: 要 None 排最前, 改元组首项为 0/1:")
print("    ", sorted(data, key=lambda v: (v is not None, v if v is not None else 0)))

print("[4] 混合 int/str 的同型问题: TypeError 不在 key 里发生, 在比较时发生")
mixed = [2, "a", 1, "b"]
try:
    sorted(mixed)
except TypeError as exc:
    print("    TypeError:", exc)
print("    按'类型标签+值'排序:", sorted(mixed, key=lambda v: (type(v).__name__, v)))

print("[5] 解法三: cmp_to_key 显式定义 None 比较规则 (语义最直白)")
def cmp(a, b) -> int:
    if a is None and b is None:
        return 0
    if a is None:
        return 1          # None 视为最大
    if b is None:
        return -1
    return (a > b) - (a < b)

print("    ", sorted(data, key=functools.cmp_to_key(cmp)))
print("[6] 数据库 NULL 排序语义 (NULLS LAST/FIRST) 就是这套规则, API 层要自己补齐")
```

**追问一**：为什么推荐"入口归一化"而不是"排序点打补丁"？—— None 混入是**数据契约破裂**的信号，排序点补丁只救这一次消费，下一次按 None 求和、分组、做索引还是会炸；入口归一（DB 层 COALESCE、反序列化层默认值、校验层拒绝）把契约修复在边界上。排序补丁的合理定位是"最后一道防线"而非主修复：key 元组 + 断言日志（发现 None 就告警上游），既保可用又暴露问题源。两者混用的次序错了，会把数据质量问题永久藏进排序函数里。

**追问二**：分页场景下 None 排序还要注意什么？—— 跨页一致性：排序键不唯一时，同一批数据在不同页间可能因稳定排序假设而重复/丢失，必须补唯一 tie-breaker（主键/游标键，Q1352 的防篡改游标）；None 段让 tie-breaker 更关键——NULL 段内没有可比较的业务值，纯靠第二键排序。还有一致性风险：无 `ORDER BY` 全序的 `LIMIT/OFFSET` 深分页会漂移（Q6053），None 归一规则必须写进排序表达式而不是依赖 DB 默认（不同数据库对 NULL 默认排序位置不同：PostgreSQL 视 NULL 最大、MySQL 视 NULL 最小——同一 SQL 两库行为相反，这正是"应用层补齐语义"的理由）。

## 背诵要点
- None/跨类型比较直接 TypeError；三式修复：key 元组（快）、类型标签（分组语义）、cmp_to_key（语义直白但慢）。
- "None 放哪"是业务契约：优先 SQL 下推 NULLS LAST/FIRST，应用层显式表达，不同 DB 默认相反。
- 分页排序必须补唯一 tie-breaker，NULL 段内无业务值全靠第二键。

## 复盘追问
- 排行榜接口因 NULL score 返回 500，正确修复次序？（上游 COALESCE 归一为第一修复，排序 key 只是防线）
- key 元组方案 `(v is None, v if v is not None else 0)` 为什么能稳定工作？（False<True 分段 + 段内占位值不影响段间序）
