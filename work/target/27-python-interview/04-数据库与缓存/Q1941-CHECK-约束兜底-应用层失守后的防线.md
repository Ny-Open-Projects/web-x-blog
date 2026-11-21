---
title: [Q1941] CHECK 约束兜底: 应用层失守后的防线
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1941 · CHECK 约束兜底: 应用层失守后的防线

> 难度:★★☆☆ | 标签:约束, 数据完整性

**问**:应用层已经有参数校验了, 数据库还有必要建 CHECK 约束吗?

**答**:有必要, 因为应用层校验一定会被绕过:运维手工修数、脚本直连、旧版本服务、第三方数据导入都绕过你的校验代码。CHECK 是写路径上最后一道闸, 本文件演示负金额、非法状态、跨列组合条件都被数据库直接拒绝。两个关键细节:CHECK 表达式结果是 UNKNOWN 时视为通过, 也就是说 NULL 不违反 CHECK, 要挡 NULL 必须显式加 NOT NULL;CHECK 只在建表或重建表时可靠修改, SQLite 不支持 ALTER 加 CHECK, 改约束要走重建表流程。最佳实践是应用层给友好报错, 数据库层给硬保证, 两层各司其职。

```python
# file: code/04_数据库与缓存/q1941_check_constraint.py
"""CHECK 约束兜底: 应用层校验失守后的数据库防线"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE orders(
    id INTEGER PRIMARY KEY,
    amount INTEGER NOT NULL CHECK (amount > 0),
    status TEXT NOT NULL CHECK (status IN ('created', 'paid', 'void')),
    CHECK (status <> 'paid' OR amount > 0)
)""")

def try_insert(label, args):
    try:
        conn.execute("INSERT INTO orders(amount, status) VALUES(?,?)", args)
        print(f"{label} -> 写入成功")
    except sqlite3.IntegrityError as e:
        print(f"{label} -> 被数据库拒绝: {e}")

try_insert("合法行", (100, "paid"))
try_insert("负金额", (-5, "paid"))
try_insert("非法状态", (10, "shipped"))
try_insert("零金额 created", (0, "created"))
print("库内行数 ->", conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0], " 坏数据全部被挡")

# CHECK 对 UNKNOWN 放行: NULL 不违反 CHECK 但会撞上 NOT NULL
try_insert("amount 为 NULL", (None, "created"))
conn.execute("CREATE TABLE t(x INTEGER CHECK (x > 0))")
try:
    conn.execute("INSERT INTO t VALUES(NULL)")
    print("纯 CHECK 列写 NULL -> 成功: UNKNOWN 不是 FALSE CHECK 放行 要挡 NULL 必须加 NOT NULL")
except sqlite3.IntegrityError:
    print("纯 CHECK 列写 NULL -> 被拒")
print("结论: 应用层校验会被脚本 直连 绕过 CHECK 是最后防线 且必须与 NOT NULL 配套覆盖 NULL 通道")
```

**追问**:
- CHECK 能引用其他表或时间函数吗?—— 不能, CHECK 只能引用当前行的列与确定性函数, 跨表一致性要靠外键或应用层。
- 批量导入时 CHECK 会不会拖慢写入?—— 表达式求值开销极小, 真正的成本是被拒绝的行需要处理, 建议导入前先做同口径的预检。

---
