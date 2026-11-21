---
title: [Q806] 大表上的 Django 迁移策略
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q806 · 大表上的 Django 迁移策略

> 难度:★★★★ | 标签:Django, 迁移, 在线 DDL

**问**:给亿级订单表加一列,Django migrate 直接跑会发生什么?正确流程是什么?

**答**:加列本身多数库是元数据操作,但**带默认值/非空约束**可能触发表重写长时间锁表(MySQL 尤甚);加索引、改列类型同理。策略:expand-migrate-contract——先加可空列(无默认值)的轻量迁移 → 代码双写、历史数据**分批回填**(按主键范围循环) → 校验后加约束/删旧列。MySQL 用 pt-osc/gh-ost 在线改表;PG 11+ 加常量默认值列是 O(1),但要小心 NOT NULL+DEFAULT 组合。原则:**迁移脚本与代码版本解耦,每步可回滚**。

```python
# file: code/03_Web后端开发/q806_online_ddl.py

def plan_add_column(big_table: str, column: str) -> list:
    return [
        f"迁移A: {big_table} 加可空列 {column} 不带默认值, 秒级完成",
        f"代码双写: 新写入同时填旧字段与 {column}",
        f"回填: 按主键分批 UPDATE 历史行, 控制每批速率",
        f"迁移B: 数据对齐后收紧约束, 观察一个发布周期",
        f"迁移C: 移除旧字段与双写代码",
    ]

for step in plan_add_column("orders", "status_v2"):
    print(step)
```

**追问**:
- 怎么预估一条 DDL 的风险?——看表行数、存储引擎对在线 DDL 的支持、是否触发表重建,预发用同量级数据演练。
- Django 迁移锁和业务锁冲突怎么办?——低峰执行、设置 lock_timeout 快速失败重试,避免排队雪崩。
