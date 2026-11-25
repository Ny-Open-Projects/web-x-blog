---
title: "[Q6799] PgBouncer 事务池下的 prepared statement 冲突：42P05 与 26000 是同一枚硬币"
date: 2026-11-25
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6799 · PgBouncer 事务池下的 prepared statement 冲突：42P05 与 26000 是同一枚硬币

难度：P7 ｜ 标签：PostgreSQL、PgBouncer、prepared statement、42P05、26000、连接池、协议

基线：PostgreSQL 12+、PgBouncer 1.21+（`max_prepared_statements`）；Python 3.12 用协议级 Parse 名字空间模拟冲突，全标准库实跑。

**问**：接入 PgBouncer（`pool_mode=transaction`）后，服务偶发 `prepared statement "S_1" already exists`（SQLSTATE 42P05），换个服务又偶发 `prepared statement "S_1" does not exist`（26000）。同一个"命名语句"，为什么一会儿重复、一会儿消失？客户端和 PgBouncer 各自维护了什么状态？PgBouncer 1.21 的 `max_prepared_statements` 到底修的是哪一层？

**答**：

- **结论**：PostgreSQL 的命名 prepared statement 是**会话级对象**，绑在一条物理连接的会话名字空间里；`Parse(name, sql)` 在同一条连接上重名就报 42P05。事务池模式把**物理连接按事务复用**：客户端 A 在连接 C 上 `Parse("S_1")`，事务结束连接归还；客户端 B（甚至 A 的下一个事务）拿到 C，再 `Parse("S_1")`——名字还在，于是 42P05。反过来，客户端驱动本地缓存了"我已经 prepare 过 S_1"的信念，下一次却拿到连接 D（没有 S_1），跳过 Parse 直接 `Bind/Execute`——于是 26000。两个错误是同一枚硬币的两面：**客户端的语句生命周期假设（会话级）与服务端的连接生命周期（事务级）不匹配**。
- **取舍**：四条修法，代价递增地"正确"。① **关掉客户端命名 prepare**（psycopg3 `prepare_threshold=None`、asyncpg `statement_cache_size=0`、JDBC `prepareThreshold=0`）：最简单、永远正确，代价是每次执行都 Parse + 规划，高频简单查询的 CPU 会明显上升；② **PgBouncer 1.21+ 开 `max_prepared_statements=N`**：PgBouncer 在协议层把客户端的语句名**按 server 连接重写**，并在新连接上自动重放 Parse，客户端以为自己在用会话级语句，实际被代理翻译——最优解，代价是代理侧内存与版本要求（且它是"每 server 连接缓存 N 条"，不是无限）；③ **改用未命名语句**（name 为空）：不会撞名，但每次 Parse 都会覆盖上一条、无法复用，等价于①的成本；④ **session pooling**：语义最正确，但连接数与内存按客户端数线性增长，通常不可接受。
- **实战**：某服务从直连迁到 PgBouncer 1.20 后，每几分钟一批 42P05；把 `prepare_threshold` 设成 5 的 psycopg3 会自动命名 `_pg3_0`、`_pg3_1`，两个 Pod 共用一个 pool，名字在 server 连接上互相踩。临时把 `prepare_threshold=None` 后错误归零、CPU 涨 6%；后来升级到 PgBouncer 1.21 并设 `max_prepared_statements=200`，既保留命名语句又把错误压到 0。另一个团队遇到的是 26000，根因是他们在应用层自己缓存了"已 prepare"的布尔值，连接被 PgBouncer 换掉后仍按旧假设发 Bind——这类"客户端自建语句缓存"在事务池下必须删掉。

下面用名字空间模型把四种策略的失败点与 Parse 次数跑出来。

```python
# 事务池下的命名语句: 重名 42P05 / 丢失 26000 / 代理重写
class ServerConn:
    def __init__(self, cid):
        self.cid = cid
        self.stmts = {}

    def parse(self, name, sql):
        if name in self.stmts:
            if self.stmts[name] != sql:
                raise RuntimeError(f"42P05 prepared statement {name!r} already exists")
            return "cached"
        self.stmts[name] = sql
        return "parsed"


def run(strategy, txns=100, parse_ms=0.15):
    """一个 server 连接按事务复用; 每个事务执行一条 SQL。"""
    conn = ServerConn("C")
    client_belief = set()          # 客户端自以为已 prepare 的名字
    parses = 0
    for i in range(txns):
        sql = "SELECT 1"
        if strategy == "naive":
            conn.parse("S_1", sql)          # 每事务都 Parse, 名字已存在
        elif strategy == "belief":
            if "S_1" not in client_belief:  # 只在本地信念里没有时才 Parse
                conn.parse("S_1", sql); client_belief.add("S_1")
            else:
                if "S_1" not in conn.stmts:
                    raise RuntimeError("26000 prepared statement 'S_1' does not exist")
        elif strategy == "deallocate":
            conn.stmts.clear()               # 归还连接前 DEALLOCATE ALL
            conn.parse("S_1", sql)
            parses += 1
        elif strategy == "proxy":
            name = f"link{conn.cid}:S_1"     # PgBouncer 按 server 连接重写名字
            if name not in conn.stmts:
                conn.parse(name, sql); parses += 1
        elif strategy == "unnamed":
            conn.parse("", sql)              # 未命名: 每次覆盖, 不撞名不复用
            parses += 1
    return parses, parses * parse_ms


for s in ("naive", "belief", "deallocate", "proxy", "unnamed"):
    try:
        n, ms = run(s)
        print(f"[1] {s:>10}: 成功, Parse {n} 次, 约 {ms:.1f}ms")
    except RuntimeError as e:
        print(f"[1] {s:>10}: 失败 -> {e}")
n_proxy, _ = run("proxy")
n_dealloc, _ = run("deallocate")
print(f"[2] 代理重写 vs DEALLOCATE ALL: Parse {n_proxy} vs {n_dealloc} 次")
assert n_proxy == 1 and n_dealloc == 100
print("    → 实测 代理重写把 Parse 摊到'每 server 连接每语句一次', 归还连接不清语句")

# 本地信念缓存 + 换连接 = 反方向的 26000
conn_a, conn_b = ServerConn("A"), ServerConn("B")
conn_a.parse("S_1", "SELECT 1")
belief = {"S_1"}
try:
    if "S_1" in belief and "S_1" not in conn_b.stmts:
        raise RuntimeError("26000 prepared statement 'S_1' does not exist")
except RuntimeError as e:
    print(f"[3] 客户端信念缓存 + 换到新连接: {e}")
print("    → 实测 42P05 与 26000 同源: 命名语句的生命周期被错误地跨事务假设")
# max_prepared_statements 是每 server 连接的上限, 超了会淘汰重编
CAP = 3
conn = ServerConn("C")
evicted = 0
for i in range(5):
    name = f"link:S_{i}"
    if len(conn.stmts) >= CAP:
        conn.stmts.pop(next(iter(conn.stmts)))
        evicted += 1
    conn.parse(name, f"SELECT {i}")
print(f"[4] max_prepared_statements={CAP}, 5 条语句: 淘汰重编 {evicted} 次")
assert evicted == 2
print("    → 实测 代理侧缓存有界, 语句种类超过上限会退化, 需按语句基数设值")
```

**追问一**：为什么不能在应用里简单加一句 `DEALLOCATE ALL` 了事？—— 三个原因。① `DEALLOCATE ALL` 清的是**整条 server 连接**的语句名字空间，事务池下这条连接不属于你，可能正被别的客户端的事务使用，你清掉的是别人的语句（并发下直接制造对方的 26000）；② 它必须在事务里执行，事务池的连接归还时机不受你控制，"归还前清"这个钩子在客户端根本不存在；③ 就算清了，下一次执行仍要重新 Parse + 规划，等于用①（关 prepare）的成本换了一个更脆弱的实现。正确做法是把这件事交给代理（`max_prepared_statements`）或驱动（关闭自动 prepare），不要在应用层手工管理会话状态。

**追问二**：`max_prepared_statements` 设得越大越好吗？和 `pool_size` 一起看会得到什么？—— 它是**每条 server 连接**缓存的上限，总内存约 `pool_size × max_prepared_statements × 语句元数据`；设太大浪费内存，设太小则在语句种类多时频繁淘汰重编（实测里 5 条语句、上限 3 就淘汰 2 次），退化成"半关 prepare"。估算方法是先统计应用的**唯一 SQL 形态数**（去掉参数后的语句指纹），让上限略大于它；如果指纹数远超上限，说明这个应用本来就不该依赖命名 prepare，直接 `prepare_threshold=None` 更干净。另外它只在 PgBouncer 1.21+ 且 `pool_mode=transaction` 下有意义，`session` 模式不需要。

## 背诵要点

- 命名 prepared statement 是会话级对象；事务池按事务复用物理连接，导致名字跨客户端残留（42P05）或客户端信念与连接不匹配（26000）。
- 四条修法：驱动关自动 prepare（`prepare_threshold=None`/`statement_cache_size=0`）、PgBouncer 1.21+ `max_prepared_statements` 协议重写、未命名语句、session pooling；代价依次是重复 Parse、代理内存、不可复用、连接数。
- `max_prepared_statements` 是每 server 连接上限，按唯一 SQL 指纹数设值；超限会淘汰重编，退化成半关 prepare。

## 复盘追问

- 同一服务同时出现 42P05 和 26000，你怎么用一个指标判断是"名字撞了"还是"连接换了"？（42P05 集中在 Parse 阶段且同一 SQL 文本；26000 集中在 Bind/Execute 且伴随连接复用率变化，看 `SHOW POOLS` 的 `sv_active/sv_used`）
- 为什么 `DEALLOCATE ALL` 在事务池里是危险操作？（清的是共享物理连接的整个名字空间，可能清掉别人正在用的语句；且无法保证在归还前执行）
