---
title: [Q2939] 完整 DAO 层模板: 连接管理 CRUD 分页一次成型
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2939 · 完整 DAO 层模板: 连接管理 CRUD 分页一次成型

> 难度:★★★☆ | 标签:架构, DAO, 分页

**问**:让你从零写一个模块的数据访问层,连接怎么管、CRUD 怎么放、分页给前端怎么出?给一套能直接用的模板。

**答**:DAO 层的三条纪律:连接由 DAO 自己管理(构造时建、提供 close),SQL 只住在 DAO 里不外漏,出参统一转成 dict 或 DTO 不把 cursor 和 Row 暴露给上层。写路径每个方法一个短事务、随写随提交,语句一律参数化;读路径单查返回 dict 或 None,列表页一次带出 total 与 items,前端好渲染总数。分页要给两套:offset 分页带页码与总数,适合管理后台;keyset 分页用 last_id 做游标,深翻页性能不衰减,适合 Feed 流。模板里的 WHERE 拼接只拼固定字符串片段,条件值全部走占位符,这是 DAO 的安全底线。

```python
# file: code/04_数据库与缓存/q2939_dao_template.py
"""完整 DAO 层模板: 连接管理 CRUD 两种分页一次成型"""
import sqlite3


class UserDao:
    """DAO 三件套: 连接由 DAO 自管, SQL 只住在 DAO 里, 出参全是 dict"""

    DDL = """
    CREATE TABLE IF NOT EXISTS user (
        id     INTEGER PRIMARY KEY,
        name   TEXT NOT NULL,
        age    INTEGER NOT NULL DEFAULT 0,
        status TEXT NOT NULL DEFAULT 'active'
    )
    """

    def __init__(self, dsn=":memory:"):
        self._conn = sqlite3.connect(dsn)
        self._conn.row_factory = sqlite3.Row
        self._conn.executescript(self.DDL)
        self._conn.commit()

    def close(self):
        self._conn.close()

    # ---- 写路径: 每个方法一个短事务, 参数化是铁律 ----
    def insert(self, name, age):
        cur = self._conn.execute(
            "INSERT INTO user(name, age) VALUES(?, ?)", (name, age))
        self._conn.commit()
        return cur.lastrowid

    def update_status(self, uid, status):
        cur = self._conn.execute(
            "UPDATE user SET status=? WHERE id=?", (status, uid))
        self._conn.commit()
        return cur.rowcount == 1

    def delete(self, uid):
        cur = self._conn.execute("DELETE FROM user WHERE id=?", (uid,))
        self._conn.commit()
        return cur.rowcount == 1

    # ---- 读路径: 单查 + 列表页带总数 + 键值分页带游标 ----
    def get(self, uid):
        row = self._conn.execute(
            "SELECT * FROM user WHERE id=?", (uid,)).fetchone()
        return dict(row) if row else None

    def page(self, page=1, size=10, status=None):
        """offset 分页: 数据与总数一起出, 条件只用占位符拼接"""
        where, args = "WHERE 1=1", []
        if status:
            where += " AND status=?"
            args.append(status)
        total = self._conn.execute(
            "SELECT COUNT(*) FROM user " + where, args).fetchone()[0]
        rows = self._conn.execute(
            "SELECT * FROM user " + where + " ORDER BY id LIMIT ? OFFSET ?",
            args + [size, (page - 1) * size]).fetchall()
        return {"total": total, "page": page, "size": size,
                "items": [dict(r) for r in rows]}

    def page_after(self, last_id, size=10):
        """keyset 分页: 翻页稳定, 深页性能不衰减"""
        rows = self._conn.execute(
            "SELECT * FROM user WHERE id>? ORDER BY id LIMIT ?",
            (last_id, size)).fetchall()
        items = [dict(r) for r in rows]
        return {"items": items,
                "next_cursor": items[-1]["id"] if items else None}


if __name__ == "__main__":
    dao = UserDao()
    ids = [dao.insert("u%d" % i, 20 + i % 10) for i in range(1, 24)]
    print("insert 23 rows, last id =", ids[-1])
    print("get(1):", dao.get(1))
    p1 = dao.page(1, 10)
    print("page1: total=%d items=%d" % (p1["total"], len(p1["items"])))
    print("page3 ids:", [u["id"] for u in dao.page(3, 10)["items"]])
    print("page status=active total:", dao.page(1, 5, status="active")["total"])
    kp = dao.page_after(10, 10)
    print("keyset after id=10:", [u["id"] for u in kp["items"]],
          "next_cursor =", kp["next_cursor"])
    assert dao.update_status(1, "frozen")
    assert dao.get(1)["status"] == "frozen"
    assert dao.delete(1)
    assert dao.get(1) is None
    print("CRUD 自检通过")
```

**追问**:
- 跨方法的多个写操作要在一个事务里怎么办?—— DAO 不该吞掉事务边界,提供接收外部连接或用 Unit of Work 的重载,把 commit 决定权交给服务层。
- offset 分页要不要加 ORDER BY?—— 必须加且排序列要稳定,否则数据库不保证顺序,翻页会丢行重行。

---
