"""本地消息表完整实现: 业务与消息同事务落库, 中继扫描投递与退避重试"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE orders(id INTEGER PRIMARY KEY, no TEXT, amount REAL);
CREATE TABLE outbox(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  topic TEXT, biz_key TEXT, payload TEXT,
  status TEXT DEFAULT 'pending',          -- pending / sent / dead
  retry INTEGER DEFAULT 0,
  next_retry_at REAL DEFAULT 0
);
CREATE UNIQUE INDEX uq_biz ON outbox(topic, biz_key);   -- 业务键防重复落消息
CREATE INDEX idx_scan ON outbox(status, next_retry_at);
""")

def pay_order(no, amount):
    """业务行与消息行写在同一个事务: 这是本地消息表的全部秘密"""
    conn.execute("INSERT INTO orders(no, amount) VALUES(?,?)", (no, amount))
    conn.execute(
        "INSERT INTO outbox(topic, biz_key, payload) VALUES('order.paid', ?, ?)",
        (no, '{"no":"%s","amount":%s}' % (no, amount)))
    conn.commit()

def relay(broker, batch=10, now=0.0):
    """中继: 扫 pending 且到期的, 投递成功标 sent, 失败指数退避"""
    rows = conn.execute(
        "SELECT id, biz_key, payload, retry FROM outbox "
        "WHERE status='pending' AND next_retry_at <= ? ORDER BY id LIMIT ?",
        (now, batch)).fetchall()
    for mid, biz_key, payload, retry in rows:
        try:
            broker.publish("order.paid", biz_key, payload)
            conn.execute("UPDATE outbox SET status='sent' WHERE id=?", (mid,))
        except Exception:
            nr = retry + 1
            if nr >= 5:
                conn.execute("UPDATE outbox SET status='dead' WHERE id=?", (mid,))
            else:
                conn.execute(
                    "UPDATE outbox SET retry=?, next_retry_at=? WHERE id=?",
                    (nr, now + 2 ** nr, mid))
        conn.commit()

class FlakyBroker:
    def __init__(self):
        self.seen, self.fails = {}, 0

    def publish(self, topic, biz_key, payload):
        if self.fails < 1:                # 第一次投递网络抖动
            self.fails += 1
            raise IOError("broker 超时")
        self.seen[biz_key] = payload      # 按 biz_key 幂等

pay_order("SO-1", 99.0)
pay_order("SO-2", 49.5)
broker = FlakyBroker()
relay(broker, now=100)                    # 一条成功一条失败
print("第一轮后:", conn.execute("SELECT id, status, retry, next_retry_at FROM outbox").fetchall())
relay(broker, now=100)                    # 退避期内不应被捞起
n = conn.execute("SELECT COUNT(*) FROM outbox WHERE status='pending' "
                 "AND next_retry_at<=100").fetchone()[0]
print("退避期内待扫条数:", n)
relay(broker, now=110)                    # 到期后重试成功
print("重试后:", conn.execute("SELECT id, status, retry FROM outbox").fetchall())
print("broker 收到:", broker.seen)
print("要点: 同事务保证不丢单; 投递是至少一次, 幂等靠消费端 biz_key 去重; dead 状态人工介入")
