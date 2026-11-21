---
title: [Q1646] 密码重置 token 的单次消费
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1646 · 密码重置 token 的单次消费

> 难度:★★★☆ | 标签:重置流程, 安全

**问**:密码重置链接里的 token 要满足哪些安全性质?怎么做到严格单次有效?

**答**:四个性质:不可预测(secrets.token_urlsafe(32) 的 256 位熵,别用时间戳加用户 ID 拼)、限时效(15 分钟左右的短 TTL)、单次有效、存储安全——库里只存 sha256 哈希,原文只在邮件里出现一次,拖库也撞不出可用 token。单次有效靠原子消费:一条 UPDATE 置位语句,条件带上 token 哈希、used 为 0、未过期,看 rowcount 是否为 1 判定成败——两个并发请求带同一 token 来,数据库行级原子性保证只有一个 rowcount 等于 1,不需要应用层加锁。校验失败要区分日志但不区分对外表现:统一提示链接无效或已过期。

```python
# file: code/03_Web后端开发/q1646_reset_token.py
"""密码重置 token: 存哈希、限时效、单次原子消费(标准库 secrets + sqlite3)。"""
import hashlib
import secrets
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE reset_tokens "
             "(token_hash TEXT PRIMARY KEY, user_id TEXT, expires REAL, used INT DEFAULT 0)")


def issue(user_id, now):
    raw = secrets.token_urlsafe(32)              # 只下发原文, 库里只存哈希
    conn.execute("INSERT INTO reset_tokens VALUES (?, ?, ?, 0)",
                 (hashlib.sha256(raw.encode()).hexdigest(), user_id, now + 900))
    conn.commit()
    return raw


def consume(raw, now):
    th = hashlib.sha256(raw.encode()).hexdigest()
    cur = conn.execute(
        "UPDATE reset_tokens SET used = 1 "
        "WHERE token_hash = ? AND used = 0 AND expires > ?",
        (th, now))
    conn.commit()
    if cur.rowcount == 1:
        return conn.execute("SELECT user_id FROM reset_tokens "
                            "WHERE token_hash = ?", (th,)).fetchone()[0]
    return None


t = time.time()
tok = issue("u9", t)
print("下发 token 前缀:", tok[:8], "...")
print("首次消费:", consume(tok, t + 10))
print("重复消费:", consume(tok, t + 20))
print("过期消费:", consume(issue("u1", t), t + 1800))
print("伪造 token:", consume("attacker-guess", t))
print("要点: 库里只有哈希防拖库撞 token; 消费用单条 UPDATE 原子置位, 并发重放只有一个成功")
```

**追问**:
- 用户要求重发链接怎么办?——生成新 token 并作废旧 token,旧链接自然失效。
- 为什么存哈希而不是明文?——token 即凭证,明文落库等于把一次性密码存进数据库,拖库即接管账号。
