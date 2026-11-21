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
