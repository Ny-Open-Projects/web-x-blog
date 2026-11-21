---
title: [Q932] Alembic 迁移: revision 链与 upgrade/downgrade
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q932 · Alembic 迁移: revision 链与 upgrade/downgrade

> 难度:★★★☆ | 标签:Alembic, 迁移

**问**:Alembic 的工作流是怎样的?upgrade 与 downgrade 怎么写才可靠?

**答**:流程:alembic init 建目录与 env.py(绑定 Base.metadata 与引擎)、alembic revision --autogenerate 对比模型与库差异生成迁移脚本、alembic upgrade head 应用到最新。每个脚本有 revision id 与 down_revision,形成单向链,alembic current 查当前版本。可靠性要点:autogenerate 只是草稿,人工审查(它识别不了列类型细节变更、数据迁移)、downgrade 必须真的可回滚或标记不可逆、迁移与代码同仓库同版本发布、升级前备份。数据回填(新列填默认值)与 DDL 分开:先加可空列、分批回填、再加约束,这是零停机的基本功。

```python
# file: code/04_数据库与缓存/q932_alembic_flow.py
"""演示迁移脚本的 revision 链结构与 upgrade/downgrade 对称性"""
MIGRATIONS = {
    "a1": {"down": None, "up": "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)"},
    "b2": {"down": "a1", "up": "ALTER TABLE users ADD COLUMN age INT",
           "downgrade": "ALTER TABLE users DROP COLUMN age"},
}

def current(rev):
    return rev

def upgrade(conn, target):
    rev = current(None)
    for rid, m in MIGRATIONS.items():
        if rev is None or _after(rid, rev):
            conn.execute(m["up"]) if isinstance(m["up"], str) else None
            rev = rid
        if rid == target:
            break
    return rev

def _after(rid, rev):
    return rev is None or MIGRATIONS[rid]["down"] == rev or True

if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect(":memory:")
    head = upgrade(conn, "b2")
    print("升级到:", head)
    print("结构:", conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'").fetchall())
    print("Alembic 真实流程: init -> autogenerate -> 人工审查 -> upgrade head")
    print("downgrade 与 upgrade 必须成对编写并演练")
```

**追问**:
- autogenerate 漏掉了什么?——表/列重命名(被识别为删+建)、数据迁移、函数索引细节,这些都要手写 op.execute 并人工审查。
- 多人并行生成迁移冲突怎么办?——两条链分叉时用 alembic merge 生成合并 revision,规范上约定短周期合并避免长期分叉。

---
