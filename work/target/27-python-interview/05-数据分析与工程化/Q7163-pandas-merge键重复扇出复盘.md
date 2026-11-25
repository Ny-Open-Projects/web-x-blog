---
title: [Q7163] pandas-merge键重复扇出复盘
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7163 · pandas merge 后行数暴涨：键重复扇出事故复盘

难度：P6 ｜ 标签：事故复盘、pandas、数据对账
基线：pandas 2.x/3.0（merge 行为一致，validate 参数 2.0+ 语义稳定）。

**问**：一张 10 万行的交易明细 LEFT JOIN 一张 8 万行的用户表后，结果变成 26 万行，下游对账全部失败。事故根因是什么？如何在代码层面让它"炸得早、炸得清楚"？

**答**：**结论**：根因是**右表 join 键不唯一**——用户表里同一 user_id 有多条记录（历史快照、改名未清理、脏数据），merge 按笛卡尔匹配扇出：右表某键出现 k 次，左表该键的每行就变成 k 行。这不是 pandas 的 bug，是关系代数的正确行为；事故的本质是**没有先断言键唯一性**。

**取舍**：三种修复的成本对比：① `merge(..., validate="m:1")`——零成本把断言交给 pandas，键不唯一时直接抛 `MergeError`，让问题在 ETL 第一步爆掉而不是在对账环节爆掉；② 右表先 `drop_duplicates(subset=...)`——快速止血，但**静默丢行**，如果重复行之间数据不同，选 keep 哪条就变成口径决策，必须留痕；③ 语义上本来就是多条的（如订单对多次支付），把 join 目标改成聚合后的子查询（groupby 到 1:1 再 merge）。

**实战**：团队规范是"每个 merge 都带 validate"：`m:1`/`1:1` 断言唯一性、`1:m` 显式声明预期扇出；对账增加一行数守恒断言：merge 前后行数关系 = 预期扇出系数，不满足即 fail-fast。

```python
import pandas as pd

txns = pd.DataFrame({
    "user_id": [1, 1, 2],
    "amount": [100, 200, 300],
})
users = pd.DataFrame({
    "user_id": [1, 1, 2],          # user_id=1 有两条（脏数据/历史快照）
    "name": ["甲-新", "甲-旧", "乙"],
})

# 事故复现：无 validate 的 merge 静默扇出
bad = txns.merge(users, on="user_id", how="left")
print("merge 前:", len(txns), "merge 后:", len(bad))   # 3 -> 4
print(bad)
# user_id=1 的两行各匹配了两次

# 修复 1：validate 断言，让问题在 merge 处爆掉
try:
    txns.merge(users, on="user_id", how="left", validate="m:1")
except pd.errors.MergeError as e:
    print("validate 拦截:", e)

# 修复 2：显式声明业务口径——取"最新一条"再合并（去重口径留痕）
users_latest = (users.sort_values("name")           # 实际按更新时间排
                    .drop_duplicates("user_id", keep="last"))
good = txns.merge(users_latest, on="user_id", how="left", validate="m:1")
assert len(good) == len(txns), "行数守恒断言失败"
print("修复后行数守恒:", len(good))

# 预期扇出的场景：一笔交易对多次支付，显式 1:m 并校验系数
# 注意 1:m 要求左侧键唯一，先收敛到"交易粒度"
pays = pd.DataFrame({"user_id": [1, 1, 2], "pay": [10, 20, 30]})
one_user = txns.drop_duplicates("user_id")
m = one_user.merge(pays, on="user_id", how="left", validate="1:m")
print("1:m 合法扇出:", len(m), "行（1 人 2 笔支付）")
```

**追问 1**：`validate="m:1"` 检查的是哪一侧？开销多大？
提示：检查的是"1"侧（右表）键唯一性，pandas 内部做 `is_unique` 判定，O(n) 且内存开销小，几乎不影响 merge 性能——没有理由不写。

**追问 2**：drop_duplicates 的 keep 选哪条，如何不变成"拍脑袋"？
提示：必须来自业务排序键（更新时间、状态优先级、版本号），并在代码注释与对账规则里写明口径；用 `keep=False` 先统计受影响行数也是灰度手段。

**追问 3**：如果扇出发生在 months 后的新数据（当时没重复），validate 会拖累日常吗？
提示：不会——它就是一次 is_unique 检查；反而要警惕"历史上唯一、新数据里不唯一"的隐性口径漂移，validate 正是这种漂移的门禁。

## 背诵要点
1. merge 行数暴涨 = 右表键不唯一扇出；关系代数正确行为，错在缺唯一性断言。
2. 每个 merge 都带 validate（m:1/1:1），让扇出在 ETL 爆而不是在对账爆。
3. drop_duplicates 是口径决策不是技术动作：keep 依据业务排序键并留痕。

## 复盘追问
1. 你现有 ETL 里有多少个 merge 没有 validate？如果加上，预计哪些会立刻爆？
2. 对账体系的"行数守恒断言"覆盖了 merge、groupby、filter 哪几类变换？缺口在哪？
