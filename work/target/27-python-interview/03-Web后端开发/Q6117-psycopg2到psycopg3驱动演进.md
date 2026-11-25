---
title: [Q6117] psycopg2 到 psycopg3 的驱动演进
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6117 · psycopg2 → psycopg3 的驱动演进

> 难度:★★★★☆ | 标签:版本演进, PostgreSQL, 驱动

**问**:SQLAlchemy 2.0 时代选 `psycopg2` 还是 `psycopg[binary]`？psycopg3（2022+）相对 psycopg2 改了哪些架构层的东西——连接、参数绑定、COPY、异步？迁移事故常出在哪？

**答**:结论：psycopg3 不是 psycopg2 的升级，是**纯 Python 实现 + C 可选加速**的重新设计（psycopg2 是 libpq 的 C 绑定），四个架构级变化：a) **客户端/服务端两套参数绑定**：psycopg2 全走服务端绑定（libpq `PQexecParams`），psycopg3 默认**客户端绑定**（Python 侧拼查询，`ClientCursor`），显式 `ServerCursor`/`conn.cursor(cursor_factory=psycopg.ServerCursor)` 才走服务端——客户端绑定带来 psycopg 风格的 `%s` 增强类型映射与 JSON 快路径，但**占位符语义差异**是迁移事故第一爆点（服务端绑定不支持某些 Python 类型直接内插）；b) **异步一等公民**：`psycopg.AsyncConnection`/`AsyncCursor` 原生 asyncio API，psycopg2 从未有（2.x 的 async 扩展被官方标记废弃）；c) **COPY 大幅强化**：`copy` 上下文管理器 + 流式读写器，批量导入从"手工转义"变成生成器协议；d) **适配器体系重构**：`Dumpers/Loaders` 分层，自定义类型适配比 psycopg2 的 `register_adapter` 干净。部署差异：psycopg3 纯 Python 包 `psycopg`（可 `psycopg[binary]` 带 bundled libpq），psycopg2 必须装系统 libpq（`psycopg2-binary` wheel 有 ABI 坑）。迁移方法：先在测试环境把 Cursor 换 `ServerCursor` 对齐旧语义，跑全量 SQL 回归；对 `%s` 占位符类型逐个过 dumper；SQLAlchemy 侧 URL 从 `postgresql+psycopg2://` 换 `postgresql+psycopg://`。

```python
# 基线: psycopg[binary]>=3.1（演示环境无 PG 时走降级路径）；对照 psycopg2>=2.9
try:
    import psycopg
    print("psycopg3:", psycopg.__version__)
except ImportError:
    print("缺 psycopg[binary]>=3.1 — pip install 'psycopg[binary]'")
    raise SystemExit(0)

# 1) 两套绑定：默认 ClientCursor（客户端绑定）vs ServerCursor（服务端绑定，对齐 psycopg2）
print("默认 cursor:", psycopg.Cursor)                 # 客户端绑定
print("服务端绑定:", psycopg.ServerCursor)            # 迁移对齐项

# 2) 连接上下文与事务语义：commit 时机显式化（psycopg3 的自动提交策略更严格）
conn_kwargs = dict(
    host="localhost", port=5432, dbname="app", user="u", password="p",
    autocommit=False,                  # psycopg3: 显式管理，无隐式 commit
)
print("事务姿势: with conn.transaction(): ...  （嵌套事务映射 SAVEPOINT）")

# 3) COPY 流式导入（psycopg3 的杀手锏，psycopg2 手工 copy_expert）
def gen_rows(n):
    for i in range(n):
        yield (i, f"name-{i}")

# 伪代码形态（无 DB 时不执行）：
#   with conn.cursor() as cur:
#       with cur.copy("COPY t (id, name) FROM STDIN") as cp:
#           for row in gen_rows(1_000_000):
#               cp.write_row(row)
print("COPY: write_row 生成器流式导入，峰值内存 O(批)")

# 4) 异步 API 形态（psycopg2 无对应物）
async_code = (
    "async with psycopg.AsyncConnection.connect(...) as aconn:\n"
    "    async with aconn.cursor() as acur:\n"
    "        await acur.execute('SELECT 1')\n"
    "        row = await acur.fetchone()"
)
print("AsyncConnection/AsyncCursor 是一等公民:")
print(async_code)

# 5) 迁移爆点清单
for item in [
    "占位符语义: 默认 ClientCursor 改变 %s 的类型适配，需 ServerCursor 对齐旧行为",
    "DateTime/JSON 适配器体系重构: register_adapter 换 Dumper 注册",
    "notice/noise 处理 API 变化: conn.add_notice_handler",
    "SQLAlchemy URL: postgresql+psycopg2:// -> postgresql+psycopg://",
    "psycopg2-binary 的 libpq ABI 坑不再存在（binary 轮子由 psycopg 官方发布）",
]:
    print(" -", item)
```

**追问一层**:客户端绑定与服务端绑定在 SQL 注入防护上等价吗？什么场景必须坚持服务端绑定（PREPARE 复用、批量 execute_values 类优化）？
**追二层**:psycopg3 的 `Pipeline`（批量管道，libpq pipeline mode）对"每请求多次小查询"的往返账能省多少（对照 Q6043 连接复用成本账）？

**背诵要点**
- psycopg3 = 纯 Python + 可选 C 加速；默认客户端绑定（ClientCursor），`ServerCursor` 对齐 psycopg2 服务端绑定语义。
- 异步 API（AsyncConnection/AsyncCursor）与强化 COPY 是两大新能力；SQLAlchemy URL 换 `+psycopg`。
- 迁移爆点集中在占位符类型适配与适配器体系；`with conn.transaction()` 显式管理事务与 SAVEPOINT。

**复盘追问**
- 迁移后部分查询变慢 30%，怎么定位是不是"客户端绑定丢了服务端 prepare 复用"？提示：pg_stat_statements 对比 plan cache 命中与 `ServerCursor` 灰度对照。
- 异步视图里用了同步 psycopg3 连接，事件循环被阻塞的表现是什么（对照 Q6006 桥接线程池耗尽）？提示：要么 AsyncConnection，要么 to_thread 包装同步调用。
