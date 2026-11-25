---
title: [Q6610] MySQL 8.0 sql_mode 收紧（ONLY_FULL_GROUP_BY）升级破坏点
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6610 · MySQL 8.0 sql_mode 收紧（ONLY_FULL_GROUP_BY）升级破坏点

难度：P6 ｜ 标签：版本演进 / MySQL 8.0 / 迁移

**问**：从 MySQL 5.7 升 8.0 后，一批跑了两年的 Python 报表任务开始报 `ER_WRONG_FIELD_WITH_GROUP`，另有接口报 `Invalid default value for 'datetime'`。都是 sql_mode 默认值变化惹的祸吗？升级时 sql_mode 应该怎么管？

**答**：
- **结论**：5.7→8.0 默认 sql_mode 变化集中在 `ONLY_FULL_GROUP_BY`（GROUP BY 查询的 SELECT 里出现非聚合、非分组列直接报错）、`STRICT_TRANS_TABLES`（非法值拒绝写入而非截断告警）、`NO_ZERO_DATE/NO_ZERO_IN_DATE`（'0000-00-00' 日期不再合法）。5.7 时这些其实已经默认开启，8.0 没有大改 sql_mode 本身，破坏点更多来自**应用连接串/ORM 覆盖了全局 mode、新库初始化脚本没带旧 mode、以及 8.0 移除的 mode 项（如 NO_AUTO_CREATE_USER）写死在配置里导致启动失败**。datetime 默认值报错通常另有根因：8.0 的 explicit_defaults_for_timestamp 默认开启 + 旧表定义里 '0000-00-00' 默认值在 STRICT 模式下非法。
- **取舍**：管理策略：① **不要靠"全局关掉"续命**——把 ONLY_FULL_GROUP_BY 从全局 mode 里删掉，等于放弃服务端防线，坏查询会在你以为安全的地方产生不确定结果（分组列取值不确定）；正确做法是分治：新代码按严格模式写，遗留 SQL 用 `ANY_VALUE()` 显式声明取值或改成确定聚合；② 全局 mode 用配置管理（8.0 的 `SET PERSIST` 持久化），应用侧连接参数不覆盖全局 mode（SQLAlchemy connect_args 里别塞 sql_mode）；③ 升级预检：mysqldb-auto/升级工具前 grep 全部 SQL 与建表语句，找 GROUP BY 列、'0000-00-00'、被移除的 mode 名。
- **实战**：升级剧本：① 预检脚本扫全库表定义里的 zero date 与 default 值，先在 5.7 开 STRICT 双跑观察；② 报表类报错逐条改：`SELECT dept, ANY_VALUE(col), COUNT(*) ... GROUP BY dept` 或补齐 GROUP BY；③ SQLAlchemy 侧把旧代码里的 `SET SESSION sql_mode` 清掉，统一跟随全局；④ 灰度：升级前把新 sql_mode 在 5.7 从库上开启，跑影子流量收集全部报错清单再动主库。

```python
# sql_mode 升级预检：SQL 扫描 + 破坏点分类（标准库模拟）
# 基线：Python 3.9+；真实扫描对象是慢日志/代码仓库/表定义 dump

import re
from dataclasses import dataclass


@dataclass
class Finding:
    sql: str
    kind: str
    fix: str


GROUP_BY_SELECT_RE = re.compile(
    r"select\s+(?P<sel>.+?)\s+from\s+.+?\s+group\s+by\s+(?P<grp>[^;]+)", re.I | re.S
)
ZERO_DATE_RE = re.compile(r"'0000-00-00( 00:00:00)?'", re.I)
REMOVED_MODES = {"NO_AUTO_CREATE_USER", "NO_ENGINE_SUBSTITUTION_legacy"}


def scan(sql: str, group_cols: list[str]) -> Finding | None:
    m = GROUP_BY_SELECT_RE.search(sql)
    if m:
        sel = m.group("sel")
        # 简化判定：SELECT 中出现非聚合列名且不在 GROUP BY 列表 → 报错点
        plain_cols = re.findall(r"\b([a-z_]+)\b", sel)
        agg = {"count", "sum", "avg", "max", "min"}
        for c in plain_cols:
            if c not in agg and c not in group_cols and c not in ("distinct",):
                return Finding(sql, "ONLY_FULL_GROUP_BY", f"补 GROUP BY 或用 ANY_VALUE({c})")
    if ZERO_DATE_RE.search(sql):
        return Finding(sql, "ZERO_DATE", "改 NULL 或有效日期默认值")
    for mode in REMOVED_MODES:
        if mode in sql.upper():
            return Finding(sql, "REMOVED_MODE", f"移除 {mode} 配置")
    return None


def main() -> None:
    f1 = scan("select dept, owner_name, count(*) from t group by dept", ["dept"])
    assert f1 and f1.kind == "ONLY_FULL_GROUP_BY" and "ANY_VALUE(owner_name)" in f1.fix
    f2 = scan("insert into t values ('0000-00-00 00:00:00')", [])
    assert f2 and f2.kind == "ZERO_DATE"
    f3 = scan("SET GLOBAL sql_mode='...NO_AUTO_CREATE_USER...'", [])
    assert f3 and f3.kind == "REMOVED_MODE"
    f4 = scan("select dept, count(*) from t group by dept", ["dept"])
    assert f4 is None, "合规查询不报"
    print("OK: 预检命中 GROUP BY 非聚合列 / zero date / 已移除 mode 三类破坏点")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"全局关掉 ONLY_FULL_GROUP_BY"比"逐条修 SQL"更危险？
→ 一句话提示：非聚合非分组列的取值是引擎任选的（不同版本/计划可能不同），关掉防线后这类查询不报错但结果不确定，属于静默数据错误，比崩溃更难发现。

**追问 2**：sql_mode 的变更想持久化又不重启，8.0 推荐怎么做？
→ 一句话提示：`SET PERSIST sql_mode='...'`（写入 mysqld-auto.cnf，重启后生效且免改 my.cnf）；注意它有全局影响面，变更要走参数灰度与回滚预案（见 Q6558）。

## 背诵要点
- 8.0 升级破坏点三类：GROUP BY 非聚合列（ONLY_FULL_GROUP_BY）、zero date 非法（STRICT + NO_ZERO_DATE）、配置里写死被移除的 mode（如 NO_AUTO_CREATE_USER）导致启动失败。
- 分治而非全局关闭：新代码守严格模式，遗留 SQL 用 ANY_VALUE() 显式声明；应用连接串不覆盖全局 mode。
- 灰度手段：先在 5.7 从库开新 mode 收集报错清单，主库用 SET PERSIST 变更并配回滚。

## 复盘追问
- 8.0 还有哪些"sql_mode 之外"的默认值变化容易踩？提示：explicit_defaults_for_timestamp 默认开启（TIMESTAMP 不再自动 DEFAULT CURRENT_TIMESTAMP）、默认字符集 utf8mb4/0900_ai_ci（另见 Q6549）、密码认证插件 caching_sha2_password 导致老驱动连不上（见 Q6578）。
- 为什么建议 ORM 层不管理 sql_mode？提示：全局一份事实源便于审计与灰度；ORM 按连接各自 SET 会让"同一个查询在不同会话结果不同"，排查成本极高。
