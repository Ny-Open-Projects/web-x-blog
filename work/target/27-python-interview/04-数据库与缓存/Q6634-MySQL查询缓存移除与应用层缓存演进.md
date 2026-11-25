---
title: [Q6634] MySQL 查询缓存移除的演进史与应用层缓存的替代设计
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6634 · MySQL 查询缓存移除的演进与应用层缓存替代

难度：P6 ｜ 标签：版本演进 / MySQL / 缓存

**问**：MySQL 5.7 里 `query_cache` 还是被默认提及的功能，8.0 直接整块移除。官方为什么砍掉它？它被移除后，"SQL 级结果缓存"这个需求在 MySQL 生态和应用侧分别怎么补？

**答**：
- **结论**：query cache 的死因是**全局锁 + 写失效**：任何一张表只要有写入，引用该表的所有缓存条目全部失效，且加锁互斥使高并发写场景下缓存本身成为串行化点——多核扩展性为负，官方测得开启后吞吐反而下降，8.0（2018）整体移除（哈希表、锁、`query_cache_*` 变量全部删除）。生态替代分三层：① 服务端官方补位：MySQL 没有重做 SQL 缓存，但 InnoDB buffer pool 管数据页缓存（这是它一直的分工——缓存数据页不缓存结果集）；② 代理层：ProxySQL 的 query cache、RDS 代理缓存，在应用与 DB 之间按 SQL 指纹缓存结果，可控 TTL；③ 应用层（主流答案）：Python 侧 dogpile.cache / redis-py + 装饰器，把失效粒度从"表级全局"收敛到"业务 key 级"，并配上双删/版本号（Q6593、Q6507）。演进启示：**DB 引擎不该做应用感知的结果缓存**，失效语义必须由掌握业务的人控制。
- **取舍**：应用层缓存换来的代价是缓存-DB 双写一致性负担（整套双删/订阅 binlog 体系都是为它服务的）；代理层缓存配置简单但失效粒度仍是 SQL 级、带 TTL 容忍脏读。选型：读多写少且能容忍秒级脏读 → 代理层 TTL 最省事；一致性敏感 → 应用层 key 级失效；只是想挡重复相同的 SELECT → 先看是不是该合并调用或加本进程 memoize。
- **实战**：① 升级 5.7→8.0 时（Q6549）检查代码里残留 `query_cache_*` 会话变量，连接即报错；② 应用层缓存 key 必须带"数据版本/更新时间"成分，避免靠 TTL 硬扛；③ 监控从"缓存命中率"升级为"失效风暴率"——单次写操作引发的失效条目数才是新体系的健康指标。

```python
# query cache 失效模型: 表级失效放大 + 全局锁串行化 vs key 级应用缓存
# 基线: Python 3.9+ 标准库
from collections import Counter


def invalidation_storm(entries_per_table: dict[str, int],
                        writes_per_table: dict[str, int]) -> int:
    """表级失效: 一次写失效该表全部条目。"""
    return sum(entries_per_table[t] * w
               for t, w in writes_per_table.items())


def app_cache_storm(entries: int, writes: int) -> int:
    """key 级失效: 只失效被写的 key。"""
    return entries * writes if False else writes  # 每写只失效 1 条


def main() -> None:
    # 100 表, 每表缓存 200 条结果, 热表每秒 50 写
    entries = {f"t{i}": 200 for i in range(100)}
    writes = {"t7": 50, "t3": 30}
    storm = invalidation_storm(entries, writes)
    assert storm == 200 * 80                       # 16000 条/秒失效
    assert app_cache_storm(80, 80) == 80           # key 级: 写多少失效多少
    ratio = storm / app_cache_storm(80, 80)
    assert ratio >= 100                            # 放大 200 倍量级
    print(f"表级失效 {storm} 条/s vs key级 {80} 条/s (放大 x{ratio:.0f})")
    print("OK: 全局锁+写失效 => 8.0 移除; 应用层缓存把失效粒度收敛到 key")


if __name__ == "__main__":
    main()
```

**追问 1**：ProxySQL 这类代理缓存的失效为什么天然不如应用层精准？
→ 一句话提示：代理只能按 SQL 文本/指纹匹配，不知道业务上"哪个 key 变了"，只能靠 TTL 过期容忍脏读，或者保守地大范围失效。

**追问 2**：buffer pool 和 query cache 的分工差别说明什么设计原则？
→ 一句话提示：页缓存对上层透明、失效天然跟随 B-tree 页更新，无语义问题；结果集缓存耦合了"业务可见性"，失效语义只有应用能定义——所以缓存放在离语义最近的层。

## 背诵要点
- query cache 死因：表级写失效放大 + 全局锁串行化，多核吞吐为负；8.0 整块移除（含全部 query_cache_* 变量）。
- 三层替代：InnoDB buffer pool（页级）/ 代理层 TTL 缓存 / 应用层 key 级缓存（主流，失效粒度收敛 100 倍量级）。
- 新健康指标：单次写触发的失效条目数（失效风暴率），而非单纯命中率。

## 复盘追问
- 为什么"能容忍脏读"是代理层缓存的前提？提示：代理无业务失效能力，只能 TTL 兜底，脏读窗口 = TTL；一致性敏感必须上应用层失效。
- 5.7→8.0 升级时 query cache 相关的兼容检查清单有哪些？提示：my.cnf 变量、连接里 SET query_cache_type、以及依赖 SQL 缓存兜底性能的隐藏假设要重新压测。
