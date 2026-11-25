---
title: [Q6623] JSONB GIN 索引膨胀拖垮写入的事故复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6623 · JSONB GIN 索引膨胀拖垮写入的事故复盘

难度：P6 ｜ 标签：事故复盘 / PostgreSQL / JSONB

**问**：一张事件表加了 `gin (payload jsonb_path_ops)` 索引用于按 JSON 字段过滤，上线后高峰期 INSERT 延迟从 2ms 涨到 40ms，索引体积比表还大。为什么 JSONB 的 GIN 索引对写入这么贵？怎么治理？

**答**：
- **结论**：GIN（倒排）索引按 JSON 内的**每个键值对**建条目——一个 50 键的 payload 更新要在 GIN 里插入 50 条 pending 条目，写放大 = 键数量级；默认 `fastupdate` 先写 pending list（内存+磁盘），列表超 `gin_pending_list_limit` 后触发**合并刷新**，一批待清理条目集中落盘，表现为周期性的写入毛刺。索引膨胀超过表本身是因为低基数键（几十个固定 key 重复出现）导致 posting list 不断追加。治理次序：① 只索引真正要查的路径——用**表达式索引**（`CREATE INDEX ON t ((payload->>'status'))`）替代全量 GIN，把每行 50 条降到 1 条；② 必须全量 GIN 时用 `jsonb_path_ops`（只索引值哈希，体积小数倍）+ 调 `gin_pending_list_limit`；③ 低频写入大 JSON 的场景考虑降采样：把历史行 payload 压缩或拆到冷表。
- **取舍**：表达式索引 vs 全量 GIN？查询模式收敛（固定几个字段过滤）选表达式索引——代价是新增查询路径要加新索引（DDL 变更）；查询模式发散（任意字段 ad-hoc 查询，如数据平台）才值得付全量 GIN 的写成本。这是"写路径可预测性换读灵活性"的典型取舍，决策依据是查询模式的稳定度而不是索引体积本身。
- **实战**：① 上线前用真实 payload 估算：GIN 条目数 ≈ 每行键数 × 行数，先算账再建索引；② 监控 `gin_pending_list` 长度与 INSERT p99 毛刺的关联，毛刺周期 = pending limit 触发周期；③ alembic 迁移里给 GIN 索引标注"需要 review 查询模式"的注释；④ SQLAlchemy 中把 JSONB 过滤字段收敛成显式列 + 生成列（generated column），让优化器走 btree。

```python
# GIN 写放大账: 条目数=每行键数x行数; 表达式索引把 50:1 降到 1:1
# 基线: Python 3.9+ 标准库
from dataclasses import dataclass


@dataclass
class JsonbIndex:
    rows: float
    keys_per_row: int
    expr_keys: int = 0        # 表达式索引只覆盖固定几列
    ops: str = "jsonb_ops"    # jsonb_path_ops 体积约为 1/3


def gin_entries(i: JsonbIndex) -> float:
    return i.rows * i.keys_per_row * (1 / 3 if i.ops == "jsonb_path_ops" else 1)


def expr_entries(i: JsonbIndex) -> float:
    return i.rows * i.expr_keys


def spike_period_s(i: JsonbIndex, pending_limit_kb: int, entry_b: int = 40) -> float:
    """pending list 触发合并的周期(毛刺周期)。"""
    return pending_limit_kb * 1024 / (gin_entries(i) * entry_b / 86400)


def main() -> None:
    full = JsonbIndex(rows=1e8, keys_per_row=50)
    narrow = JsonbIndex(rows=1e8, keys_per_row=50, expr_keys=3, ops="jsonb_path_ops")
    assert gin_entries(full) == 5e9                    # 50 亿条目 -> 索引比表大
    assert expr_entries(narrow) == 3e8                 # 降 94%
    assert expr_entries(narrow) / gin_entries(full) < 0.07
    # 毛刺周期: pending 越小触发越频繁
    assert spike_period_s(full, 4096) < spike_period_s(full, 65536)
    print(f"full GIN: {gin_entries(full):.1e} entries; "
          f"expr: {expr_entries(narrow):.1e} -> 写放大降一个数量级")
    print("OK: 查询模式收敛用表达式索引, 发散才付全量 GIN 写成本")


if __name__ == "__main__":
    main()
```

**追问 1**：`fastupdate` 和 `gin_pending_list_limit` 的机制是什么？为什么调大 limit 不能消除毛刺只是拉长周期？
→ 一句话提示：pending list 是延迟合并的缓冲，写先入队列、满后批量并入主树；调大只是把毛刺变稀变重（每次合并更久），总合并量不变，根治要降条目数或换索引结构。

**追问 2**：为什么 `jsonb_path_ops` 不能支持 `?`（键存在）查询？
→ 一句话提示：path_ops 只索引值哈希不索引键，键存在性查询没有条目可查；选 ops 前要先审计查询算子集合，算子决定索引参数而不是反过来。

## 背诵要点
- GIN 写放大 ≈ 每行键数量级，pending list 满触发集中合并 = 周期性 INSERT 毛刺；调 limit 只拉长周期不消除。
- 治理优先级：表达式索引（收敛查询）> jsonb_path_ops（体积降数倍）> 调 pending limit > 拆冷表。
- `jsonb_path_ops` 不支持 `?` 键存在查询——先审计查询算子再选索引参数。

## 复盘追问
- 怎么在上线前预判"索引比表大"？提示：条目数 ≈ 行数 × 每行键数，用真实 payload 采样算账，低基数键会撑大 posting list。
- 为什么把 JSONB 过滤字段收敛成 generated column + btree 常常比 GIN 更优？提示：btree 单键条目 1:1、支持范围与排序、写放大恒定，代价是字段集合要提前约定。
