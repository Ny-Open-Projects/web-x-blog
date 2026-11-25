---
title: [Q6700] psycopg2 到 psycopg3 迁移破坏点
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6700 · psycopg2 到 psycopg3 迁移破坏点

难度：P6 ｜ 标签：版本演进、驱动迁移、PostgreSQL、psycopg3

基线：Python 3.9+；psycopg[binary] 3.1+；SQLAlchemy 2.0（`postgresql+psycopg` dialect）。

**问**：团队把 PostgreSQL 驱动从 psycopg2 换到 psycopg3，pip 装完能 import，为什么还是会在生产炸？哪些接口语义变了？

**答**：
- **结论**：psycopg3 是纯 Python 实现配 Rust libpq 绑定（或纯 Python 连接），API 兼容是"故意不完全"的。高频破坏点：
  1. **占位符**：psycopg2 用 `%s`（pyformat），psycopg3 客户端绑定改用 `%(name)s`（dict）或服务端绑定 `$1`，位置参数混用直接报错；
  2. **游标/连接类路径**：`psycopg2.extras.RealDictCursor`、`execute_values` 没了——3.x 用 `cursor(row_factory=dict_row)` 与 `cur.executemany(..., returning=?)`/COPY 替代，`execute_values` 的高性能批量插入在 3.x 走 `executemany` 内部 pipeline 或 COPY；
  3. **事务语义**：3.x 连接默认自动开启事务但**不再需要显式 commit 才能读**的隐式行为有变化，`connection.commit()`/`rollback()` + 上下文管理器语义与 2.x 的 `with conn:` 不同（3.x 的 `with conn:` 退出即提交/回滚且连接不关闭，2.x 亦如此，但 `with cur:` 3.x 会关闭游标）；
  4. **通知/等待**：`select.select()` 手写等待改为 `conn.notifies()` 迭代器；
  5. **SQLAlchemy**：dialect 从 `postgresql+psycopg2` 换成 `postgresql+psycopg`，URL 不换会走不到新驱动。
- **取舍**：升级动机：3.x 原生 async、pipeline 模式（批量往返省 RTT）、类型适配器体系更现代；老项目若没有 async/性能诉求，psycopg2 仍在维护，"为了新而新"不值得冒迁移风险。
- **实战**：迁移策略——先统一数据访问层（SQL 全走仓储函数，不裸拼 execute）→ 占位符批量替换 + 单测覆盖每种语句类型 → SQLAlchemy URL/dialect 切换灰度 → 关注 `array` 与 `json` 类型适配器的注册方式变化。

```python
# psycopg3 关键差异演示：无库时给出降级说明（依赖：psycopg[binary] 3.1+）。
try:
    import psycopg
    from psycopg.rows import dict_row
    HAVE_PS3 = True
except ImportError:
    HAVE_PS3 = False
    print("降级提示: pip install 'psycopg[binary]>=3.1' 后重试；"
          "以下为等价 psycopg2 写法对照。")

if HAVE_PS3:
    DSN = "dbname=test user=postgres host=localhost"
    # 3.x：dict 行工厂替代 psycopg2.extras.RealDictCursor
    with psycopg.connect(DSN, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            # 3.x 具名占位符 %(name)s；2.x 的 %s 位置绑定不再等价
            cur.execute("SELECT %(x)s AS v", {"x": 1})
            print(cur.fetchone())
    # with conn 退出即提交/回滚，连接保持打开：显式 close 才关
else:
    print("psycopg2 对照: cur.execute('SELECT %s AS v', (1,)) + RealDictCursor")
```

**追问**：
- 一层：psycopg3 的 pipeline 模式解决什么问题？→ 提示：把多条语句攒在一个网络往返，跨机房高 RTT 下批量写收益最大。
- 二层：为什么 3.x 的 COPY 通道常用来替代 execute_values？→ 提示：COPY 是流式二进制协议，百万行导入比逐条 INSERT 快一个数量级，但要处理错误粒度（整批失败）。
- 三层：SQLAlchemy 里 async 引擎切换要注意什么？→ 提示：`create_async_engine("postgresql+psycopg")`，连接串不能复用同步驱动，事件钩子在 async 侧也要换 async 版本。

**背诵要点**：
1. 破坏点四件套：占位符语义（%s→%(name)s/$1）、RealDictCursor→row_factory、execute_values→executemany/COPY、SQLAlchemy dialect 名换成 postgresql+psycopg。
2. psycopg3 动机：原生 async、pipeline 攒批省 RTT、现代类型适配器；无此诉求不必激进升级。
3. with conn 退出提交/回滚但连接不关；COPY 快但错误粒度是整批。

**复盘追问**：
1. 为什么"能 import"不等于"迁移完成"？提示：占位符和行工厂在特定代码路径才触发，需要按语句类型做全路径单测。
2. 如果存量代码里散落着上千个裸 execute，怎么迁？提示：先建数据访问层收敛入口，再机械替换，禁止边散写边迁。
