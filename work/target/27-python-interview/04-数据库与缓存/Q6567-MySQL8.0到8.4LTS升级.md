---
title: "[Q6567] MySQL 8.0 到 8.4 LTS 升级破坏点清单"
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6567 · MySQL 8.0 到 8.4 LTS 升级破坏点清单

难度：P6 ｜ 标签：MySQL / 版本演进 / 升级 / 兼容性

**问**：团队计划把 MySQL 8.0.x 升到 8.4 LTS。Python 应用侧会有哪些真实的破坏点？怎么设计升级路线保证可回滚？

**答**：

**结论**：8.4 最大的破坏面是"默认值与废弃项的集中清算"：`mysql_native_password` 默认禁用（老账号认证直接失败）、一批 8.0 已废弃的选项（如 `default_authentication_plugin`）改为不可用、`utf8mb3` 进一步边缘化。应用侧典型翻车点是连接驱动：老的 PyMySQL/mysqlclient 版本不认 `caching_sha2_password` 的完整流程，或连接串里写死了废弃参数。8.0→8.4 属于同主版本内的 LTS 升级，数据字典兼容，可走 in-place，但回滚窗口（降级）非常有限——8.4 建立的数据结构不一定能被 8.0 读，所以"可回滚"必须靠克隆插件新实例并行 + 双读对拍，而不是就地降级。

**取舍**：两条路线——① 原地升级：快、省资源，但回滚靠备份恢复（小时级 RTO 不可接受），适合有从库冗余且可接受从库先行的场景；② 克隆/逻辑复制搭新集群，双跑对拍后切流：成本高（双份资源 + 对拍工程），但回滚是秒级切回。核心服务选 ②，边缘服务选 ①。先从库升级（作为 8.4 只读实例跑一周真流量只读验证），是两条路线通用的低风险第一步。

**实战**：升级前用 `Shell`/`mysqlcheck` 跑兼容检查；重点清点三张清单：账号认证方式（`SELECT user,plugin FROM mysql.user`）、连接串参数（驱动 DSN 里已废弃项）、SQL 兼容（`utf8mb3` 显式引用、废弃函数）。Python 侧：驱动版本矩阵（PyMySQL ≥1.1 / mysqlclient ≥2.2 / SQLAlchemy 2.0.x）先在预发全量回归连接与事务行为，特别是 `caching_sha2_password` 的 RSA/SSL 路径。

```python
# 升级前兼容清单审计脚本（用连接配置模拟，标准库可运行）
# 仅标准库，Python 3.9+
from __future__ import annotations

DEPRECATED_PARAMS = {
    "default_authentication_plugin", "old_mode", "innodb_locks_unsafe_for_binlog",
}
GOOD_DRIVERS = {"pymysql>=1.1.0", "mysqlclient>=2.2.0", "sqlalchemy>=2.0.0"}
OK_PLUGINS = {"caching_sha2_password", "sha256_password"}


def audit(accounts: list[dict], dsn_params: dict,
          drivers: list[str]) -> dict[str, list[str]]:
    issues: dict[str, list[str]] = {"account": [], "dsn": [], "driver": []}
    for a in accounts:
        if a["plugin"] == "mysql_native_password":
            issues["account"].append(
                f"{a['user']}: mysql_native_password 在 8.4 默认禁用，需迁移")
        elif a["plugin"] not in OK_PLUGINS:
            issues["account"].append(f"{a['user']}: 插件 {a['plugin']} 未验证")
    for p in dsn_params:
        if p in DEPRECATED_PARAMS:
            issues["dsn"].append(f"连接参数 {p} 已废弃")
    for d in drivers:
        name = d.split(">=")[0].split("<")[0]
        if not any(d.startswith(g.split(">=")[0]) for g in GOOD_DRIVERS):
            issues["driver"].append(f"{d}: 未知驱动")
        else:
            ver = d.split(">=")[1] if ">=" in d else "0"
            floor = next(g.split(">=")[1] for g in GOOD_DRIVERS
                         if g.startswith(name))
            if tuple(map(int, ver.split("."))) < tuple(map(int, floor.split("."))):
                issues["driver"].append(f"{d}: 低于 {name} {floor} 基线")
    return issues


def main() -> None:
    accounts = [
        {"user": "app_rw", "plugin": "caching_sha2_password"},
        {"user": "legacy_ro", "plugin": "mysql_native_password"},
    ]
    dsn = {"host": "db1", "default_authentication_plugin": "x"}
    drivers = ["pymysql>=1.1.0", "mysqlclient>=1.4.6"]
    issues = audit(accounts, dsn, drivers)
    for k, v in issues.items():
        print(k, "->", v or "OK")
    assert any("legacy_ro" in s for s in issues["account"])
    assert any("default_authentication_plugin" in s for s in issues["dsn"])
    assert any("mysqlclient" in s for s in issues["driver"])
    print("结论：2 个账号/参数/驱动破坏点，升级前必须清零")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么 8.4 建立的数据不一定能被 8.0 读回？——8.4 可能更新数据字典与 redo 格式版本；降级要求目标版本支持当前数据字典版本，官方对跨"降级"支持非常窄，所以回滚设计必须靠并行新实例而非 in-place 降级。
- 追问 1.1：caching_sha2_password 在非 SSL 连接下为什么会失败？——该插件首次认证需要 RSA 公钥交换（或 TLS）保护密码；驱动未配 `ssl_mode` 或拿不到 RSA public key 时报 `Authentication plugin not supported`，这也是老驱动升级后最常见的报错。
- 追问 2：从库先升级的方案里，怎么防止"从库 8.4 复制 8.0 主库"期间的复制断裂？——先在预发验证主从跨版本复制兼容（8.0 主 → 8.4 从是官方支持方向），并盯 `SHOW SLAVE STATUS` 的错误码；同时应用的双读对拍要在从库升级前完成基线，否则对拍结果混入版本差异。

**背诵要点**：

1. 8.0→8.4 集中清算废弃项：mysql_native_password 默认禁用、default_authentication_plugin 移除、utf8mb3 边缘化；升级前审计账号插件/DSN 参数/驱动版本三张清单。
2. 回滚靠并行新实例（克隆插件搭 8.4 集群双跑对拍）而非 in-place 降级；从库先行是通用低风险第一步。
3. caching_sha2_password 非 SSL 需 RSA 公钥交换，老驱动最常见报错点；驱动基线 PyMySQL≥1.1 / mysqlclient≥2.2。

**复盘追问**：

1. 如果升级后某批任务因账号插件失败，如何在不阻塞整体切流的情况下单独兜住这批账号？
2. 双跑对拍发现 0.3% 行不一致，你的归因顺序是什么（时序差异 vs 版本行为差异）？
