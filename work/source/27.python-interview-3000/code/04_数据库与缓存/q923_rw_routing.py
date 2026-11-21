"""RoutingSession: 写走主库 读走从库, 写后短窗口粘主"""
import time

try:
    from sqlalchemy import create_engine, event, text
    from sqlalchemy.orm import Session
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class RoutingSession(Session):
    def __init__(self, master, replica, sticky_sec=1.0, **kw):
        super().__init__(bind=master, **kw)
        self.master = master
        self.replica = replica
        self.sticky_until = 0.0
        self.sticky_sec = sticky_sec

    def get_bind(self, mapper=None, clause=None, **kw):
        if self._flushing or time.monotonic() < self.sticky_until:
            return self.master
        return self.replica

    def _on_write(self):
        self.sticky_until = time.monotonic() + self.sticky_sec

if __name__ == "__main__":
    import os
    for p in ("q923_master.db", "q923_replica.db"):   # 重复运行前清理
        if os.path.exists(p):
            os.remove(p)
    master = create_engine("sqlite:///q923_master.db")
    replica = create_engine("sqlite:///q923_replica.db")
    for e in (master, replica):
        with e.connect() as c:
            c.execute(text("CREATE TABLE IF NOT EXISTS kv (k TEXT PRIMARY KEY, v TEXT)"))
    chosen = []
    @event.listens_for(master, "before_cursor_execute")
    def _m(*a): chosen.append("master")
    @event.listens_for(replica, "before_cursor_execute")
    def _r(*a): chosen.append("replica")

    s = RoutingSession(master, replica)
    s._on_write()                                  # 业务侧识别为写路径
    s.execute(text("INSERT INTO kv VALUES ('a', '1')"))
    s.commit()
    print("写后立即读路由到:", end=" ")
    s.execute(text("SELECT * FROM kv")).all()
    print(chosen[-1])
    time.sleep(1.1)
    chosen.clear()
    s.execute(text("SELECT * FROM kv")).all()
    print("粘性过期后读路由到:", chosen[-1])
