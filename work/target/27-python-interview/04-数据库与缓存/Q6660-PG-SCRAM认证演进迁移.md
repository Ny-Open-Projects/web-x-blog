---
title: [Q6660] PG 认证演进：md5 到 SCRAM-SHA-256 迁移
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6660 · PostgreSQL 认证演进：md5 到 SCRAM-SHA-256 迁移

难度：P6-P7 | 标签：PostgreSQL、安全、版本演进

**问**：PG 14 起 `password_encryption` 默认从 md5 换成 scram-sha-256，老应用升级后报 `authentication method 10 not supported`。为什么？全链路迁移清单是什么？

**答**：结论：SCRAM-SHA-256 替代 md5 的是"防重放+不存明文等价密钥"的挑战响应认证；失败的两类原因：① 驱动太老不认识 SASL 握手（psycopg2 < 2.8、旧 pgBouncer），② 密码仍按 md5 存储而服务端 `pg_hba.conf` 已要求 scram。迁移是**服务端配置 → 密码重置 → 驱动/中间件升级 → 验证**四步链，任何一步遗漏都会在深夜连接池重建时集中爆（Q6553 断连自愈踩坑同款）。

实战要点：
1. 顺序铁律：先升驱动与连接池中间件（支持 SASL），再改 `pg_hba.conf` 的 METHOD，最后重置密码（`SET password_encryption='scram-sha-256'; ALTER USER ... PASSWORD ...`）——密码不会自动重加密，md5 存储的旧密码永远无法原地转 scram。
2. 双写过渡：`pg_hba.conf` 里对同一用户可按来源 IP 先保留 md5、灰度网段改 scram，验证后再收敛。
3. 密码滚动配合：滚动密码时确认所有密码更新入口（云 IAM、vault、应用配置）写入的是明文密码（由服务端选择存储算法），而不是预先算好的 md5 串。

```python
"""迁移 readiness 检查清单（标准库演示，可运行）"""
from dataclasses import dataclass


@dataclass
class MigrationCheck:
    driver_min_scram: tuple[int, int] = (2, 8)   # psycopg2 >= 2.8
    pooler_scram_ok: bool = False                # pgbouncer >= 1.12 + so
    hba_method: str = "md5"
    password_storage: str = "md5"                # 查 pg_authid.roletype/md5 前缀

    def report(self) -> list[str]:
        out = []
        if not self.pooler_scram_ok:
            out.append("[阻塞] 连接池中间件不支持 SASL，先升级 pgbouncer")
        if self.hba_method == "scram-sha-256" and self.password_storage == "md5":
            out.append("[阻塞] hba 已要求 scram 但密码仍 md5 存储：必须重置密码")
        if self.hba_method == "md5":
            out.append("[待办] pg_hba 仍 md5：灰度网段切 scram 后收敛")
        if not out:
            out.append("[OK] 可以切 scram")
        return out


# 事故现场：hba 已切 scram，密码没重置
c = MigrationCheck(pooler_scram_ok=True,
                   hba_method="scram-sha-256", password_storage="md5")
for line in c.report():
    print(line)
```

**追问 1**：为什么 md5 存储的密码无法"原地"转成 scram？
**提示**：scram 需要**明文**（或服务端 secret 派生）计算 salted verifier，md5 只存了 `md5(password+user)`，密码原文不在库里，只能重置。

**追问 2**：连接池把连接长期持有，为什么升级后"重启前没事，一重启全挂"？
**提示**：旧连接是升级前用 md5 握手建立的，存活期不受影响；一旦进程重启重建连接，新连接走 SASL 就暴露驱动/池不支持。

## 背诵要点
- 迁移铁律顺序：升驱动与池（SASL 支持）→ 改 pg_hba → 重置密码，md5 密码无法原地转 scram。
- psycopg2 ≥ 2.8、pgbouncer ≥ 1.12 是 scram 基线；旧连接存活会掩盖问题，重启即爆。
- 灰度可按来源网段分段切换 hba 的 METHOD，验证后收敛。

## 复盘追问
- 如何在升级演练里主动触发"重建连接"，避免上线后半夜集中爆？
- 密码滚动系统若写入了预计算的 md5 串， scram 下会发生什么，如何在接入时校验？
