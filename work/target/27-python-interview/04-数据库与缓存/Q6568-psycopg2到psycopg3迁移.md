---
title: "[Q6568] psycopg2 到 psycopg3 迁移与 PG 版本升级配合"
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6568 · psycopg2 到 psycopg3 迁移与 PG 版本升级配合

难度：P6 ｜ 标签：PostgreSQL / psycopg3 / 版本演进 / 驱动

**问**：团队计划 PG 14 → PG 17 升级，同时把驱动从 psycopg2 换到 psycopg3。为什么这两个升级要捆绑做？迁移中有哪些真实破坏点？

**答**：

**结论**：捆绑的理由是 psycopg3 才有对 PG 新特性的完整适配（服务端绑定参数配合更好的计划缓存、pipeline 模式摊薄网络 RTT、原生 COPY 增强、二进制协议），且 psycopg2 已进入维护模式、对新 PG 类型（如 PG 16+ 的改进）适配慢。迁移破坏点集中在四处：① 参数占位符从 `%s` 仍是 `%s`，但 psycopg3 默认客户端绑定改为可切服务端绑定（`cursor_factory=psycopg.ServerCursor`），执行计划行为可能变化；② 事务/连接管理重构：`conn.transaction()` 上下文与 psycopg2 的 `begin/commit` 手工流不同，嵌套事务语义（savepoint）更明确；③ `execute_values` 没了，批量写改用 `executemany`（服务端模式）或 COPY；④ 类型适配体系重写，自定义 adapter 注册方式从 `register_type` 变为 `TypeDumper`/`Dumper` 类。

**取舍**：不要在 PG 升级当周做驱动迁移——两件事各自都可能引入回归，混在一起无法归因。正确顺序：先 psycopg2 跑通 PG 17（psycopg2 兼容 PG 17 基本协议），稳定后单独排期驱动迁移，每步都有独立对拍与回滚。反方向（先迁驱动后升库）也可以，但必须串行。

**实战**：迁移面最大的代码是"数据导入/导出"与"批量写"：psycopg2 的 `execute_values` hack 在 psycopg3 里用 `executemany` + pipeline 或 `copy` 替代，性能口径要重测。连接池从 `psycopg2.pool`/第三方（如 `pgbouncer` 配合）切到 `psycopg_pool`。Python 侧写一个适配层：把"开连接、开事务、批量写"封到单一模块，迁移时只改模块内部，业务代码零改动——这也是能不能快速回滚的关键。

```python
# 驱动适配层：业务代码只依赖本模块，psycopg2/3 可切换（标准库模拟演示）
# 仅标准库，Python 3.9+；真实项目 psycopg3>=3.1 / psycopg2>=2.9
from __future__ import annotations

from typing import Any, Callable


class DBFacade:
    """把连接/事务/批量写收口，驱动差异不外泄。"""

    def __init__(self, driver: str) -> None:
        assert driver in ("psycopg2", "psycopg3")
        self.driver = driver
        self.log: list[str] = []

    def bulk_insert(self, table: str, rows: list[dict]) -> int:
        if not rows:
            return 0
        cols = list(rows[0])
        if self.driver == "psycopg2":
            # psycopg2: execute_values 拼 VALUES 元组
            self.log.append(f"executE_values {table} x{len(rows)}")
        else:
            # psycopg3: executemany + pipeline 或 COPY
            if len(rows) > 1000:
                self.log.append(f"copy {table} x{len(rows)}")
            else:
                self.log.append(f"executemany(pipeline) {table} x{len(rows)}")
        return len(rows)

    def run_in_tx(self, fn: Callable[[], Any]) -> Any:
        # psycopg2: 手工 set_session/commit；psycopg3: conn.transaction()
        self.log.append(f"tx[{self.driver}]")
        try:
            return fn()
        except Exception:
            self.log.append("rollback")
            raise
        else:
            self.log.append("commit")


def main() -> None:
    rows = [{"uid": i, "score": i * 2} for i in range(5000)]
    for drv in ("psycopg2", "psycopg3"):
        db = DBFacade(drv)
        n = db.run_in_tx(lambda: db.bulk_insert("scores", rows))
        assert n == 5000
    print(db.log)
    # psycopg3 大批量应走 COPY 路径
    assert any("copy scores x5000" in s for s in db.log)
    print("结论：适配层收口后，迁移只改 Facade，业务零改动、可独立回滚")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：psycopg3 的服务端绑定和客户端绑定对执行计划有什么影响？——客户端绑定（默认）参数值内联进 SQL 文本，每次都是"新 SQL"，配合通用计划可能走错；服务端绑定走 PREPARE/EXECUTE，PG 17 的通用计划启发式介入更积极，对简单点查更快、对倾斜分布可能更差——切换后必须重跑慢查询回归。
- 追问 1.1：pipeline 模式省的是什么？——把 N 次往返压成批量发送，省的是网络 RTT 而非服务器工作量；跨区高 RTT 链路收益巨大（10 次往返 100ms → 1 次），但出错时错误归因到具体语句更复杂（pipeline 内某条失败不影响已发语句，需按序处理结果）。
- 追问 2：为什么"PG 升级与驱动迁移不能同周"？——两个变量叠加后回归无法归因：行为差异可能来自 PG 优化器变化、驱动绑定方式、或两者交互；串行化后每步有独立基线，出问题能 5 分钟定位是哪一层。

**背诵要点**：

1. psycopg3 核心差异：服务端绑定可选、pipeline 摊 RTT、COPY/`executemany` 替代 `execute_values`、类型适配改为 Dumper 类体系。
2. 升级与迁移必须串行不能同周，各自独立基线、独立对拍、独立回滚。
3. 适配层收口（连接/事务/批量写单模块）是快速迁移与回滚的前提；大批量写优先 COPY 路径。

**复盘追问**：

1. 迁移后发现某复杂报表查询计划劣化，你会先怀疑服务端绑定还是 PG 17 优化器变化？怎么验证？
2. `executemany` 改造后写入吞吐不升反降，可能的三个原因？
