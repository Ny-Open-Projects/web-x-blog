---
title: [Q6699] MySQL 5.7 到 8.0 升级破坏点与演练清单
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6699 · MySQL 5.7 到 8.0 升级破坏点与演练清单

难度：P6 ｜ 标签：版本演进、升级迁移、MySQL 8.0、兼容性

基线：MySQL 5.7 → 8.0/8.4；SQLAlchemy 2.0 / PyMySQL 1.1+。

**问**：团队要给一个 5.7 的老库升 8.0，SQL 全量回归跑过了，就敢升吗？8.0 有哪些"测试不容易暴露"的破坏点？升级的正确流程是什么？

**答**：
- **结论**：SQL 回归只是第一层，8.0 的破坏点大多藏在"行为与元数据层"：
  1. **字符集默认值**：`utf8mb4_0900_ai_ci` 替代 `utf8mb4_general_ci`，老表若不统一，跨表 JOIN/UNION 会因 collation 冲突报错或走不了索引；
  2. **认证插件**：默认 `caching_sha2_password`，老驱动/老代理（连接池、ProxySQL 旧版）连不上；
  3. **GROUP BY 隐式排序移除**：5.7 里 `GROUP BY col` 附带排序，8.0 不保证，靠这个排序的报表直接乱序；
  4. **保留字扩充**：`RANK/DENSE_RANK/GROUPS/WINDOW/LATERAL` 成为关键字，老 SQL 里当列名会语法报错；
  5. **查询优化器变化**：8.0 直方图/派生表合并/倒序索引扫描，执行计划可能"变了但没报错"，性能回退；
  6. **移除特性**：query cache 已移除、`NO_AUTO_CREATE_USER` sql_mode 移除——沿用老 my.cnf 直接起不来。
- **取舍**：升级路径两条：原地 `in-place upgrade`（停机短但回滚难，8.0 数据字典不向下兼容）vs 逻辑/复制式升级（新库搭 8.0 从 5.7 主复制——注意 5.7→8.0 原生复制有版本差限制，常用双写/迁移工具），后者可灰度可回滚，代价是迁移窗口与双跑成本。
- **实战**：流程——`mysqlcheck` + `mysqlsh util.checkForServerUpgrade` 预检 → 影子库全量+真实流量回放（用生产 binlog 回放或流量录制）→ 对比执行计划与性能基线 → 应用驱动版本矩阵核对 → 分批切流。

```python
# 升级预检器：对老 SQL/配置做静态扫描（标准库可运行）。
import re

NEW_RESERVED = {"RANK", "DENSE_RANK", "GROUPS", "WINDOW", "LATERAL", "SYSTEM"}
GONE_SETTINGS = ("query_cache_size", "query_cache_type", "NO_AUTO_CREATE_USER")
COLLATION_57 = ("utf8mb4_general_ci", "utf8mb4_unicode_ci")

def scan_upgrade(sql_files: dict[str, str], my_cnf: str) -> list[str]:
    issues = []
    for name, sql in sql_files.items():
        # 粗扫：标识符直接使用新保留字
        for m in re.finditer(
                r'(?i)(?:\b(?:select|from|order\s+by|group\s+by|by)\s+'
                r'|,\s*)`?(' + "|".join(NEW_RESERVED) + r')\b', sql):
            issues.append(f"{name}: 疑似新保留字作列名/别名: {m.group(1).upper()}")
        if re.search(r'(?i)group\s+by\s+\w+\s*(;|$|\s+order)', sql) \
                and not re.search(r'(?i)order\s+by', sql):
            issues.append(f"{name}: GROUP BY 依赖隐式排序，8.0 移除，需补 ORDER BY")
    for s in GONE_SETTINGS:
        if s in my_cnf:
            issues.append(f"my.cnf: 8.0 已移除 {s}，启动会失败")
    for c in COLLATION_57:
        if c in my_cnf:
            issues.append(f"my.cnf: collation {c} 与 8.0 默认 0900 混用需统一")
    return issues or ["预检通过"]

if __name__ == "__main__":
    sqls = {
        "report.sql": "SELECT dept, RANK FROM emp GROUP BY dept;",
        "dash.sql":   "SELECT city, COUNT(*) FROM t GROUP BY city;",
    }
    cnf = "[mysqld]\nquery_cache_size=64M\ncollation_server=utf8mb4_general_ci\n"
    for line in scan_upgrade(sqls, cnf):
        print("-", line)
```

**追问**：
- 一层：为什么"影子库回放"比单测回归更能暴露问题？→ 提示：执行计划回退、锁行为、隐式转换这些要靠真实数据分布和真实流量才显现。
- 二层：5.7 复制到 8.0 会有什么坑？→ 提示：高版本可以读低版本 binlog，反向不行；升级顺序永远"先从库后主库"，且新特性（如 8.0 特有 DDL）不能在混合期使用。

**背诵要点**：
1. 8.0 升级破坏点：collation 0900、caching_sha2_password、GROUP BY 隐式排序移除、新保留字、query cache 移除、执行计划漂移。
2. 升级顺序先从后主；in-place 回滚难，复制式/影子库可灰度可回滚。
3. 预检工具 `mysqlsh util.checkForServerUpgrade` + 真实流量回放对比性能基线，SQL 单测通过不等于能升。

**复盘追问**：
1. 如果升完某个核心报表突然变慢但没报错，怎么定位？提示：对比升级前后的 EXPLAIN/执行计划基线与 8.0 直方图的影响。
2. 驱动矩阵里最容易漏的是什么？提示：中间件与连接池（代理、ORM 方言、云 SDK）对认证插件和字符集的支持。
