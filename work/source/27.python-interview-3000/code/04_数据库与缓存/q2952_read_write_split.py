"""读写分离完整实现: 写主读从 复制延迟窗口 会话粘主保读己之写"""
import sqlite3
import time


def new_db():
    c = sqlite3.connect(":memory:")
    c.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v TEXT)")
    return c


class Router:
    def __init__(self, lag=0.05):
        self.master, self.replica = new_db(), new_db()
        self.lag = lag
        self.binlog = []          # (commit_ts, sql, params)
        self.applied_ts = 0.0     # 副本已应用到的时点
        self.stats = {"write": 0, "master_read": 0, "replica_read": 0}

    def write(self, sql, params=()):
        self.master.execute(sql, params)
        self.master.commit()
        self.binlog.append((time.monotonic(), sql, params))
        self.stats["write"] += 1

    def replicate(self):
        """模拟从库拉 binlog: 只应用已滑出延迟窗口的事务"""
        cutoff = time.monotonic() - self.lag
        for ts, sql, params in list(self.binlog):
            if ts <= cutoff:
                self.replica.execute(sql, params)
                self.applied_ts = ts
                self.binlog.remove((ts, sql, params))
        self.replica.commit()

    def read(self, sql, params=(), last_write_ts=None):
        """会话粘主: 本会话刚写过且副本还没追上 -> 读主"""
        if last_write_ts is not None and self.applied_ts < last_write_ts:
            self.stats["master_read"] += 1
            return self.master.execute(sql, params).fetchall()
        self.stats["replica_read"] += 1
        return self.replica.execute(sql, params).fetchall()


r = Router(lag=0.05)
w_ts = time.monotonic()
r.write("INSERT INTO t(v) VALUES('a')")
r.write("INSERT INTO t(v) VALUES('b')")
print("写后立刻读:", r.read("SELECT v FROM t", last_write_ts=w_ts),
      "<- 粘主, 读到最新")
time.sleep(0.06)   # 超过复制延迟窗口
r.replicate()
print("副本追上后读:", r.read("SELECT v FROM t"), "<- 走副本分摊读压力")
print("路由统计:", r.stats)
assert r.stats["master_read"] == 1 and r.stats["replica_read"] == 1
