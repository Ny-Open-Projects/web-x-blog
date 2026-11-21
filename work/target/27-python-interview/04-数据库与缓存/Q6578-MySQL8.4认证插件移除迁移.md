---
title: [Q6578] MySQL 8.4 移除 mysql_native_password 的认证迁移
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6578 · MySQL 8.4 移除 mysql_native_password 的认证迁移

难度：P6 ｜ 标签：MySQL / 版本演进 / 认证

**问**：5.7 老库升级到 MySQL 8.4 后，部分 Python 服务连接直接报 `Authentication plugin 'mysql_native_password' cannot be loaded`。为什么？完整迁移方案是什么？

**答**：
- **结论**：MySQL 8.0 起默认认证插件改为 `caching_sha2_password`，8.4 中 `mysql_native_password` 默认禁用（9.0 彻底删除），但仍带着旧插件配置（用户创建于 5.7 时代或 `IDENTIFIED WITH mysql_native_password`）的账号会连不上。这是"默认值演进"型破坏：服务端行为变了，客户端驱动只要版本够新（mysqlclient 2.2+ / PyMySQL 1.1+ / aiomysql 对应 fork）都支持 caching_sha2_password，问题通常出在老镜像里的旧驱动或明文传输要求未满足。
- **取舍**：两条路：① 升级客户端驱动 + 切换账号插件到 caching_sha2_password（正确路线，密码需重设，且该插件要求 TLS 或 RSA 密钥交换——禁 TLS 环境要配 `ssl_ca` 或 `get_server_public_key`）；② 服务端临时重新启用 `mysql_native_password=ON` 兜底（8.4 可用，仅是缓冲期）。选 ② 只作为灰度窗口的止血，不做终态。
- **实战**：迁移步骤：盘点 `SELECT user,host,plugin FROM mysql.user WHERE plugin='mysql_native_password'` → 逐账号 `ALTER USER ... IDENTIFIED WITH caching_sha2_password BY '...'` → Python 侧固定驱动最低版本（mysqlclient>=2.2, PyMySQL>=1.1）→ 连接串加 `ssl_verify_cert`（云上）→ 灰度按服务切，先切只读服务。注意连接池：认证是在建连时协商的，池里旧连接要滚动重建（改账号后池不重建会看似"改完没生效"）。

```python
# 认证插件兼容性巡检脚本（纯标准库，模拟 mysql.user 盘点）
# 基线：Python 3.9+

USER_ROWS = [
    ("svc_web", "10.%", "caching_sha2_password"),
    ("svc_report", "10.%", "mysql_native_password"),
    ("legacy", "192.168.%", "mysql_native_password"),
]

MIN_DRIVER = {"mysqlclient": (2, 2), "PyMySQL": (1, 1)}


def audit(users: list[tuple[str, str, str]]) -> list[str]:
    return [f"{u}@{h}: native_password 需迁移" for u, h, p in users
            if p == "mysql_native_password"]


def driver_ok(name: str, version: tuple[int, ...]) -> bool:
    return version >= MIN_DRIVER.get(name, (0, 0))


def main() -> None:
    for line in audit(USER_ROWS):
        print("[migrate]", line)
    assert len(audit(USER_ROWS)) == 2
    print("mysqlclient 2.1 ok?", driver_ok("mysqlclient", (2, 1)))  # False
    assert not driver_ok("mysqlclient", (2, 1))
    assert driver_ok("PyMySQL", (1, 1, 1))
    # ALTER 语句模板
    print("ALTER USER 'svc_report'@'10.%' IDENTIFIED WITH caching_sha2_password BY '***';")


if __name__ == "__main__":
    main()
```

**追问 1**：caching_sha2_password 为什么要求 TLS 或 RSA？
→ 一句话提示：它设计上禁止密码明文过网——首次认证完整流程需要加密通道，无 TLS 时用服务器 RSA 公钥加密密码传输（这就是 `get_server_public_key` 参数的用途）。

**追问 2**：为什么改了账号插件后连接池里"还有旧连接在跑"？
→ 一句话提示：认证只在握手阶段发生，既有连接不受影响；迁移要配合连接池的滚动重建（设 pool_recycle 或重启 worker），否则出现新旧行为并存的诡异现象。

## 背诵要点
- 8.4 禁用 mysql_native_password（9.0 删除），默认 caching_sha2_password；老账号是最大翻车源。
- 新插件要求 TLS 或 RSA 公钥交换；Python 驱动基线 mysqlclient≥2.2 / PyMySQL≥1.1。
- 迁移三步：盘点 mysql.user → ALTER USER 逐号迁移 → 连接池滚动重建，服务端重新启用插件只做缓冲。

## 复盘追问
- 为什么这类"默认值演进"比"API 删除"更容易漏测？提示：测试环境账号早已是新插件，只有生产遗留账号才触发，要在升级演练里导出生产 mysql.user 对比。
- 如何让 CI 提前抓住驱动版本问题？提示：锁文件固定驱动最低版本 + 起真实 8.4 容器做冒烟连接。
