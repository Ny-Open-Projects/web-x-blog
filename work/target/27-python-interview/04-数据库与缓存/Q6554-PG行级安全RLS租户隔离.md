---
title: [Q6554] PG 行级安全 RLS：多租户隔离的数据库层防线
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6554 · PG 行级安全 RLS：多租户隔离的数据库层防线

难度：P7 | 标签：PostgreSQL、RLS、多租户、纵深防御

**问**：SaaS 平台出现"A 租户看到 B 租户账单"的事故，根因是新写的报表 SQL 忘了带 `tenant_id = ?`。为什么"应用层自觉加 WHERE"守不住？PG 的行级安全（RLS）怎么把租户过滤变成数据库层强制？

**答**：
- **结论**：应用层 WHERE 是"自觉"，遗漏一个查询就漏数据；RLS 把租户谓词放进策略（`CREATE POLICY t ON invoice USING (tenant = current_setting('app.tenant_id'))`），数据库在执行计划层自动叠加过滤——应用裸写 `SELECT * FROM invoice` 也只能拿到本租户的行。纵深防御的关键配套：应用账号必须是非超级用户（超级用户 BYPASSRLS）、连接池借出时 `SET app.tenant_id`（或每事务设置）、唯一索引带上租户列（否则 A 租户先插 id=1，B 租户再插直接撞唯一约束）。
- **取舍**：RLS 有代价——谓词叠加让部分执行计划变差（计划器多一列过滤），跨租户的运营查询要走 BYPASSRLS 专用账号并全量审计；`SET` 级别的租户上下文在连接池里必须配归还复位，否则下一个借走连接的请求带着上个租户的身份跑（连接归还会话污染是 RLS 落地最常见的次生事故）。
- **实战**：落地清单：① 全部业务表建 POLICY，migration 里加"新表必须有 RLS"的检查；② 会话变量用 `SET LOCAL`（事务级）避免池污染，或配 `reset_on_return`；③ 写一条对抗测试：用 app 账号裸查每张表，断言拿不到别的租户的行——把"忘了 WHERE"变成 CI 里的红灯。

```python
"""行级安全（RLS）思想模拟：租户过滤下沉到数据库层，应用忘写 WHERE 也漏不了。"""
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE invoice (id INTEGER PRIMARY KEY, tenant TEXT, amount REAL)")
db.executemany("INSERT INTO invoice VALUES (?,?,?)", [
    (1, "t_a", 100.0), (2, "t_a", 250.0), (3, "t_b", 80.0), (4, "t_c", 60.0)])
db.commit()

# 模拟 RLS 策略表：表 -> 租户列
# （PG 里是 CREATE POLICY ... USING (tenant = current_setting('app.tenant_id'))）
POLICY = {"invoice": "tenant"}

class RlsSession:
    """持有租户上下文的会话：所有查询自动叠加租户谓词（USING 子句）。"""

    def __init__(self, conn: sqlite3.Connection, tenant: str, bypass: bool = False):
        self.conn, self.tenant, self.bypass = conn, tenant, bypass

    def query(self, sql: str, params: tuple = ()) -> list:
        if self.bypass:                    # 超级用户/迁移进程：BYPASSRLS
            return self.conn.execute(sql, params).fetchall()
        table = sql.split("FROM")[1].split()[0].strip().rstrip(";")
        col = POLICY.get(table)
        if col is None:                    # 没有策略的表维持原样
            return self.conn.execute(sql, params).fetchall()
        glued = f" WHERE {col} = ?" if "WHERE" not in sql.upper() else f" AND {col} = ?"
        return self.conn.execute(sql + glued, params + (self.tenant,)).fetchall()

# 应用代码"忘了"写租户条件：RLS 层兜住，绝不超过本租户的数据
s = RlsSession(db, "t_a")
print("应用裸写 SELECT * FROM invoice ->", s.query("SELECT id, amount FROM invoice"))

# 直连迁移/DBA 账号：显式 BYPASSRLS，看到全量
admin = RlsSession(db, "t_a", bypass=True)
print("BYPASSRLS 会话同一条 SQL ->", admin.query("SELECT id, amount FROM invoice"))

print("落地纪律：应用账号必须非超级用户；连接池借出时设置租户上下文并归还复位；"
      "唯一索引带上租户列，否则跨租户写入会撞唯一约束")
```

**追问链**：
1. 追问一层：为什么唯一索引必须带租户列？——全局唯一索引会把"每个租户各自从 1 开始编号"的语义变成全表唯一；A 租户插 `(1, t_a)` 后 B 租户插 `(1, t_b)` 直接失败。用 `(tenant, id)` 复合唯一，或全局发号器。
2. 追问二层：连接池归还不复位会出什么事故？——上个请求 `SET app.tenant_id='t_a'` 后归还，下个请求借到同一连接却没设置，继续以 t_a 的身份查自己的数据——表现为"偶尔串租户且不可复现"。所以必须 `SET LOCAL`（事务结束自动还原）或配 `reset_on_return` 复位会话变量。

**背诵要点**：
1. RLS 把租户过滤从"应用自觉"变成"数据库强制"，遗漏 WHERE 不再漏数据。
2. 三配套：应用账号非超级用户、租户上下文事务级设置（或归还复位）、唯一索引带租户列。
3. 对抗测试进 CI：app 账号裸查断言拿不到他租户数据。

**复盘追问**：
1. RLS 上线后某接口计划变慢了，怎么定位与缓解？（看执行计划里策略谓词是否阻断索引；给 tenant 列建前导索引或按租户分区，让谓词能下推到分区裁剪）
2. 为什么运营后台的"跨租户查询"不能直接用应用账号开 BYPASSRLS？（BYpassRLS 是账号级开关，开了就全量穿透；应单设专用账号、逐查询审计、限定白名单语句）
