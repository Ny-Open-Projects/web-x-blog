---
title: [Q6549] MySQL 5.7 到 8.0 升级兼容事故复盘：认证插件与排序规则
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6549 · 版本演进：MySQL 5.7 升级 8.0，为什么升级当晚连接全挂？

> 难度:★★★★ | 标签:版本演进, 升级迁移, 事故复盘

**问**：把 MySQL 5.7 原地升级到 8.0 后，应用大面积报 "Authentication plugin 'caching_sha2_password' cannot be loaded" 和字符集错乱。这两个故障的根因是什么？一次合格的 MySQL 大版本升级要提前做哪些兼容审计？

**答**：结论：8.0 的默认值变更制造了两类兼容断层——**认证插件默认从 mysql_native_password 换成 caching_sha2_password**（老驱动/老连接器不支持），**默认字符集从 latin1 换 utf8mb4、默认排序规则从 utf8mb4_general_ci 换 utf8mb4_0900_ai_ci**（新表与旧表 collation 混用导致 JOIN 报 "Illegal mix of collations" 和索引失效）。合格升级 = 事前兼容审计（驱动版本、默认值 diff、保留字、SQL 兼容性）+ 影子库双跑 + 回退预案，而不是直接原地升级。

机理与实战：
- **认证断层**：修复有三层——升级驱动（PyMySQL 1.0+ / mysqlclient 2.x / SQLAlchemy 1.4+，`cryptography` 提供 caching_sha2 的 RSA 支持）；或对存量账号 `ALTER USER ... IDENTIFIED WITH mysql_native_password` 过渡；或连接串加 `ssl` 参数满足 caching_sha2 的安全通道要求。生产做法是"先升驱动再升库"，双跑期两种插件并存。
- **排序规则断层**：5.7 建的表是 general_ci，8.0 新连接默认 0900_ai_ci，混排 JOIN 直接报错。审计用 `information_schema.tables/columns` 扫全库 collation 分布，升级前把目标 collation 写进建表规范或升级后统一转换（转换 = 重建索引，大表要分批）。
- **其他经典断层**：8.0 移除查询缓存与 `GROUP BY` 隐式排序（依赖它排序的业务静默变序）；`utf8` 别名警告；新增保留字（RANK/DENSE_RANK 等）撞列名；`GROUP BY ... ASC` 语法删除。每一条都能单独造成事故，所以升级审计必须是清单制。
- **升级路径选择**：原地升级（停机窗口+快速回滚难）vs 逻辑复制/双跑切换（慢但可回退）——大库首选双跑：8.0 作为从库同步 5.7，验证后按 Q6512 类剧本切流。

```python
# 基线:Python 3.10+;纯标准库,MySQL 大版本升级前的兼容审计扫描器(离线规则)
from __future__ import annotations
import re
from dataclasses import dataclass

RESERVED_8_0 = {"RANK", "DENSE_RANK", "GROUPS", "WINDOW", "LATERAL", "CUME_DIST"}
NEW_DEFAULTS = {"charset": "utf8mb4", "collation": "utf8mb4_0900_ai_ci"}


@dataclass
class AuditFinding:
    level: str      # 阻断/告警
    item: str
    detail: str


def audit(driver_version: str, driver_ok: bool,
          old_collations: set[str], sql_files: list[str]) -> list[AuditFinding]:
    fs: list[AuditFinding] = []
    # 1. 驱动/插件
    if not driver_ok:
        fs.append(AuditFinding("阻断", "auth-plugin",
                    f"{driver_version} 不支持 caching_sha2_password,先升级驱动"))
    # 2. collation 分布
    legacy = old_collations - {NEW_DEFAULTS["collation"]}
    if legacy:
        fs.append(AuditFinding("告警", "collation-mix",
                    f"存量 collation {sorted(legacy)},升级后混排 JOIN 报错,先统一或写入建表规范"))
    # 3. 保留字与隐式排序依赖
    for path in sql_files:
        text = open(path, encoding="utf-8").read()
        for m in re.findall(r"\b(" + "|".join(RESERVED_8_0) + r")\b", text, re.I):
            fs.append(AuditFinding("阻断", "reserved-word", f"{path}: 列名撞 8.0 保留字 {m.upper()}"))
        if re.search(r"GROUP\s+BY\b.{0,200}?\bASC\b", text, re.I | re.S):
            fs.append(AuditFinding("阻断", "groupby-asc", f"{path}: GROUP BY ASC 语法在 8.0 已删除"))
        if re.search(r"\bGROUP\s+BY\b(?!.*\bORDER\s+BY\b)", text, re.I | re.S):
            fs.append(AuditFinding("告警", "groupby-order",
                        f"{path}: 依赖 GROUP BY 隐式排序,8.0 不再保证,需显式 ORDER BY"))
    return fs


def demo() -> None:
    import tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as td:
        sql = Path(td) / "report.sql"
        sql.write_text(
            "SELECT RANK, WINDOW FROM t;\n"
            "SELECT dept, COUNT(*) FROM emp GROUP BY dept ASC;\n"
            "SELECT dept, COUNT(*) FROM emp GROUP BY dept;\n",
            encoding="utf-8")
        fs = audit("PyMySQL 0.9", driver_ok=False,
                   old_collations={"utf8mb4_general_ci"}, sql_files=[str(sql)])
    for f in fs:
        print(f"  [{f.level}] {f.item}: {f.detail}")
    assert any(f.item == "auth-plugin" and f.level == "阻断" for f in fs)
    assert any(f.item == "groupby-asc" for f in fs)
    print("升级审计:驱动/排序规则/保留字/隐式排序 四项清单制 ✅")


if __name__ == "__main__":
    demo()
```

**追问一**：8.0 移除查询缓存后，依赖它的读热点怎么办？
答：查询缓存本来就因为全局锁串行化失效在高并发下是负资产；迁移方案是把"相同 SQL 文本返回相同结果"的热点改到应用侧缓存（Redis/本地缓存 + 显式失效），或依赖 8.0 的 InnoDB buffer pool 与二级缓存。复盘要点：查询缓存的命中与否对业务不可见，升级前要用 `Qcache_hits` 指标评估依赖度。

**追问二**：为什么推荐"双跑切换"而不是原地升级，各自的回退代价是什么？
答：原地升级回退 = 从备份恢复（数据回滚到升级点，分钟级到小时级 RTO 且丢增量写入）；双跑切换回退 = 把流量切回 5.7 主库（8.0 期间写入要反向同步回来，需要短暂停写或接受对账修复）。大库与不可停机业务只能双跑——回退能力决定升级路径，这是版本演进类问题的通用判断框架。

## 背诵要点
- 8.0 两大断层：默认认证插件 caching_sha2_password（先升驱动/过渡 native 插件）与默认 collation utf8mb4_0900_ai_ci（混排 JOIN 报错，先扫全库 collation 分布）。
- 隐性断层清单：查询缓存移除、GROUP BY 隐式排序取消、GROUP BY ASC 语法删除、新保留字（RANK/WINDOW 等）。
- 升级路径由回退代价决定：原地升级回退=备份恢复丢增量；双跑切换回退=切回旧主+反向同步；大库一律双跑+影子验证。

## 复盘追问
- 升级当晚为什么灰度环境没暴露认证插件问题？（提示：灰度环境驱动版本与生产不一致，或灰度账号是手工建的 native 插件账号；升级审计必须包含"环境矩阵×驱动版本×账号插件"全组合验证）
- collation 混用导致 JOIN 索引失效，性能劣化怎么在事前量化？（提示：审计时对涉及跨 collation 的 JOIN 跑 EXPLAIN 对比，记录扫描行数差；性能回归要有升级前后基准集，不能只验证"跑得通"）
