---
title: [Q6574] PostgreSQL 17 升级要点与 Python 侧适配
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6574 · PostgreSQL 17 升级要点与 Python 侧适配

难度：P6/P7 ｜ 标签：PostgreSQL / 版本演进 / 升级

**问**：团队要从 PG 15 升到 17，作为 Python 应用负责人，升级前你要梳理哪些破坏点与收益？怎么安排灰度？

**答**：
- **结论**：PG 17 对 Python 应用最有感的点：① 逻辑复制的改进（pg_upgrade 保留 subscription、pg_createsubscriber 快速搭建逻辑副本）让"逻辑复制滚动升级"更顺；② vacuum 内存重构（基于 TID 的 radix tree，不再受 maintenance_work_mem 一把锁内存限制）降低长表 vacuum 抖动；③ MERGE 能力扩展、`RETURNING` 支持 MERGE/旧数据；④ 客户端认证层面 `scram-sha-256` 全面默认，`md5` 逐渐边缘化。
- **取舍**：升级路径二选一：`pg_upgrade`（停机窗口小但要双倍磁盘）vs 逻辑复制（可回退但要处理序列、DDL、大对象不复制）。Python 侧真正的破坏点常不在 PG 本身而在驱动链：psycopg2 (2.9) 对 PG 17 无兼容问题，但项目若在迁移 psycopg3（psycopg 3.2+），注意其 server-side binding 默认化对某些动态 SQL 拼接的影响。
- **实战**：灰度顺序：先在 staging 用生产快照 + `pg_upgrade --check` 演练 → 应用跑全量回归与 EXPLAIN 对拍（计划翻转监控，参考统计信息卡）→ 生产按"逻辑副本 → 切读 → 切写"三步走，应用侧只改连接串即可回退。

```python
# 升级前后 SQL/驱动行为对拍清单的机检脚本（纯标准库）
# 基线：Python 3.9+

import re

# 应用代码中升级敏感的模式
RISKS = [
    (r"\bmd5\b", "认证方式 md5 已边缘化，确认服务端 pg_hba 使用 scram-sha-256"),
    (r"FOR\s+UPDATE\s+SKIP\s+LOCKED", "PG17 正常支持，但确认 advisory/queue 场景回归"),
    (r"\bMERGE\b", "PG15 语法子集，PG17 扩展了 RETURNING/WHEN NOT MATCHED BY SOURCE，可简化 SQL"),
    (r"pg_dump|pg_upgrade", "检查 CI 中工具版本必须 >= 服务端大版本"),
]


def scan(sql_files: dict[str, str]) -> list[str]:
    findings = []
    for name, text in sql_files.items():
        for pat, msg in RISKS:
            if re.search(pat, text, re.I):
                findings.append(f"{name}: {msg}")
    return findings


def main() -> None:
    files = {
        "db/auth.py": "conn = psycopg2.connect(..., password_md5='abc')",
        "repo/orders.py": "MERGE INTO stock USING ... RETURNING old.price",
        "ci/backup.sh": "pg_dump --version=15 target",
    }
    for f in scan(files):
        print("[risk]", f)
    assert any("md5" in f for f in scan(files))


if __name__ == "__main__":
    main()
```

**追问 1**：为什么说"Python 侧破坏点常在驱动链而不是 PG 本身"？
→ 一句话提示：PG 保持了很宽的 wire protocol 兼容，真正翻车的是驱动行为差异（如 psycopg3 的 server-side binding、asyncpg 的类型编解码缓存）和工具版本错配（旧 pg_dump 连新 server）。

**追问 2**：逻辑复制升级时，序列（sequence）为什么是坑？
→ 一句话提示：序列状态不随逻辑复制同步，切换瞬间自增主键可能从旧值重发，必须切换前 `setval` 对齐或在应用侧改用号段/雪花 ID。

## 背诵要点
- PG17 关键词：pg_createsubscriber 快速逻辑副本、vacuum 内存 radix tree、MERGE RETURNING、scram-sha-256 默认。
- 升级路径取舍：pg_upgrade 停机短/磁盘翻倍；逻辑复制可回退/序列与大对象不复制。
- Python 侧风险扫描三件套：认证方式、驱动行为（psycopg3 binding）、CI 工具版本 ≥ 服务端大版本。

## 复盘追问
- 升级灰度中如何防止"计划翻转"放大为故障？提示：逻辑副本期对 top SQL 做 EXPLAIN 对拍，读流量先灰度 1%。
- 为什么 pg_upgrade 要求双倍磁盘？提示：新集群要完整拷贝数据文件，可用 --link 硬链接省空间但牺牲回退灵活性。
