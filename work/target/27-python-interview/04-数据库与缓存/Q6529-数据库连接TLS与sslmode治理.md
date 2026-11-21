---
title: [Q6529] 数据库连接 TLS 与 sslmode 治理
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6529 · 数据库连接 TLS：sslmode 六档怎么选？为什么"加密但不验证"等于裸奔一半？

> 难度:★★★ | 标签:PostgreSQL, MySQL, 安全

**问**：安全审计要求"数据库连接必须加密"。DBA 把 PG 的 `sslmode=require` 加进 DSN 就算合规了吗？六档 sslmode 的真实差异是什么？

**答**：结论：不算。`sslmode=require` 只保证**链路加密**，不验证服务端身份，攻击者用自签证书做中间人时客户端照样"加密"地连到了假服务器——加密了、但对面不知道是谁。合规基线应是 `verify-full`（PG）/ `VERIFY_IDENTITY`（MySQL 8）：校验 CA 链 + 主机名匹配。六档从弱到强：`disable`、`allow`（先明文失败再试 TLS）、`prefer`（默认档，尽力而为）、`require`（加密不验证）、`verify-ca`（验证 CA 不验主机名）、`verify-full`（全验）。

机理与实战：
- verify-ca 与 verify-full 的分界：verify-ca 防伪造 CA 但不防"合法 CA 签出的其他主机名证书"（内网 DNS 污染场景仍可被劫持）；verify-full 做主机名匹配，生产必须这一档。MySQL 的六档语义对应 `ssl-mode=DISABLED/PREFERRED/REQUIRED/VERIFY_CA/VERIFY_IDENTITY`，少一档但分界相同。
- CA 轮换是运维主战场：证书到期前连接开始失败（或 verify-ca 档静默过期告警），Python 侧把 CA 路径放进连接配置（`sslrootcert`）而不是依赖系统信任库，配合双 CA 目录平滑轮换——新证书先用新 CA 签发并在服务端同时挂新旧链，客户端切换后再下线旧链。
- 性能账：TLS 握手对长连接池几乎无感（握手一次复用），连接池回收频繁时才有成本；不要因为"怕慢"退回 prefer。验证手段：`SHOW ssl` / `pg_stat_ssl` 看连接实际加密状态，审计要查事实不是查配置。

```python
# 基线:Python 3.9+ / psycopg2 2.8+ / PostgreSQL 9.5+(pg_stat_ssl) ;缺库降级:标准库 ssl
import ssl

PG_SSLMODE_RANK = {"disable": 0, "allow": 1, "prefer": 2,
                   "require": 3, "verify-ca": 4, "verify-full": 5}


def audit_dsn(dsn_params: dict) -> tuple[bool, str]:
    """合规审计:主机名校验缺失即不合规。"""
    mode = dsn_params.get("sslmode", "prefer")     # 不写默认 prefer,常见漏配
    if PG_SSLMODE_RANK[mode] < PG_SSLMODE_RANK["verify-ca"]:
        return False, f"sslmode={mode}:未验证服务端身份,中间人可接管"
    if mode != "verify-full":
        return False, f"sslmode={mode}:验了 CA 没验主机名,内网 DNS 污染仍可劫持"
    if not dsn_params.get("sslrootcert"):
        return False, "verify-full 但依赖系统信任库,CA 轮换不可控"
    return True, "verify-full + 显式 CA,合规"


def demo() -> None:
    print(audit_dsn({"sslmode": "require"}))
    print(audit_dsn({"sslmode": "verify-ca"}))
    print(audit_dsn({"sslmode": "verify-full", "sslrootcert": "/etc/ca.pem"}))
    # 标准库侧:VERIFY_X509_STRICT 是 Python ssl 的近似档位
    ctx = ssl.create_default_context(cafile="/nonexistent-ca.pem") if False else ssl.create_default_context()
    print("stdlib 默认上下文 check_hostname:", ctx.check_hostname)


try:
    import psycopg2  # noqa: F401
    HAS_PG = True
except ImportError:
    HAS_PG = False


def live_check(dsn: str) -> None:
    """生产事实核查:当前连接是否真的加密。"""
    import psycopg2
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute("SELECT ssl, version, client_addr FROM pg_stat_ssl WHERE pid = pg_backend_pid()")
    print("实际加密状态:", cur.fetchone())
    conn.close()


if __name__ == "__main__":
    demo()
    if HAS_PG:
        import os
        if os.environ.get("PG_DSN"):
            live_check(os.environ["PG_DSN"])
```

**追问一**：内网数据库也要 verify-full 吗？会不会过度设计？
答：分级。跨信任边界（VPC 外、共享网络、金融/资金库）必须 verify-full；同 VPC 强隔离环境可以 verify-ca 或 require 作为基线，但前提是有网络层兜底（安全组 + 私网无公网路由）。决策依据是"网络被攻破后数据库凭据的暴露面"，不是"内网就安全"。

**追问二**：CA 过期导致全量连接失败的应急步骤？
答：先降级止损（应急改 require 保可用、同步封网络出口防劫持），再补新 CA 重启客户端连接池；复盘时把"证书到期监控提前 30 天告警"和"双 CA 并行"写进运维流程，杜绝依赖单一证书寿命。

**背诵要点**：
- require 只加密不验证，合规基线是 verify-full（CA 链 + 主机名双验）。
- CA 路径显式配置（sslrootcert）不依赖系统信任库，双 CA 并行轮换。
- 审计查事实：pg_stat_ssl / SHOW ssl 看实际加密状态，不是看配置文件。

**复盘追问**：
- verify-ca 与 verify-full 在"合法 CA 误签"场景下差异具体是什么？
- 连接池场景 TLS 会话复用如何减少握手成本？

## 背诵要点
- 六档 sslmode 分界：require 之上才验证身份，verify-full 才防 DNS 污染劫持。
- MySQL 对应档位 VERIFY_IDENTITY；默认档 prefer 是最常见漏配。
- 应急顺序：降级止损 → 网络封堵 → 换 CA 恢复 → 复盘上监控。

## 复盘追问
- 证书轮换的双 CA 并行方案在服务端和客户端各要做什么？
- pg_stat_ssl 显示某连接 ssl=false，可能的成因链有哪些？
