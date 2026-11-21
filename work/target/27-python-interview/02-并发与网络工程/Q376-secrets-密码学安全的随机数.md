---
title: [Q376] secrets:密码学安全的随机数
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q376 · secrets:密码学安全的随机数

> 难度:★★☆ | 标签:secrets, 安全, 随机数

**问**:生成 token、密钥、验证码为什么禁止用 `random` 模块?

**答**:`random` 是 Mersenne Twister 伪随机,观察足够多输出可预测后续值,不能用于安全场景。`secrets` 底层用操作系统的熵源(`/dev/urandom`),专用于 token、密钥、盐、重置链接。口诀:安全用 `secrets`,模拟抽样用 `random`,统计/游戏用 `random` 无妨。

```python
# file: code/02_并发与网络工程/q376_secrets.py
"""secrets 的三种典型用法。"""
import secrets
import string

if __name__ == "__main__":
    # 1. 随机字节与 hex token(会话 ID、API key)
    print("token  :", secrets.token_hex(32))     # 64 个 hex 字符
    print("urlsafe:", secrets.token_urlsafe(32))  # 可进 URL 的 token

    # 2. 生成强随机密码
    alphabet = string.ascii_letters + string.digits + "!@#$%"
    password = "".join(secrets.choice(alphabet) for _ in range(16))
    print("password:", password)

    # 3. 安全比较:防止时序攻击(内部即 hmac.compare_digest)
    print("compare:", secrets.compare_digest("abc", "abc"))
```

**追问**:
- 需要"随机但可复现"的实验用什么?`random.Random(seed)` 显式实例化,实验可复现且不污染全局;安全与复现是两个互斥目标。
- secrets 的常用 API?——`token_hex/token_urlsafe(n)` 生成 token、`secrets.choice` 安全抽样、`compare_digest` 做常量时间比较防时序攻击。
- 为什么比较 token 也要防时序?——`==` 短路比较耗时与匹配前缀长度相关,可逐字节爆破;`hmac.compare_digest` 恒定耗时。
- UUID4 能当安全凭证吗?——可以,UUID4 同样基于 os 熵源(secrets 的来源);UUID1 含 MAC 与时间戳,反而泄露信息,别用于安全场景。
