---
title: [Q6512] 数据库高可用切换与 Python 应用侧配合
date: 2026-11-19
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6512 · 数据库高可用切换与应用侧配合

> 难度:★★★ | 标签:高可用, 主从切换, 复制

**问**：主库宕机自动切换到从库（MHA/Orchestrator/云 RDS），应用会发生什么——为什么切换窗口内会出现「已提交却消失」的事务？Python 应用侧（连接池/事务/重试）怎么配合才能平滑渡过切换，哪些写操作必须在切换前停？

**答**：核心是**复制异步性**：切换瞬间新主可能缺最后 N ms 的事务——旧主已 ack 提交、还没复制到新主就宕机，这些事务在「应用收到成功」与「新主数据」之间产生分叉（脑裂残留），切换工具只能尽量少丢不能保证不丢。应用侧配合五件套：① **连接池快速失败**：切换后旧连接全部失效，池要立刻驱逐（连接错误触发 eviction + 健康探活），不能让池里 50% 连接都是死连接拖慢请求；② **错误分类**：`1053 server gone`/`08006 connection_failure` 类可重试，`业务错误` 不可重试——盲目全量重试会把切换窗口变成重试风暴；③ **只读降级**：切换窗口（通常 10-30s）内拒绝写（快速失败）优于排队等新主——写等待堆满线程池拖垮整个服务；④ **复制等待点**：强一致读（如「支付后立刻查」）在切换后必须等 `WAIT`/`SELECT WAIT_FOR_EXECUTED_GTID_SET`（Q6510 的 WAIT 卡配套），否则读到旧从数据；⑤ **半同步/至少等 GTID 落从**：架构层把丢事务概率压到零（代价是写延迟）。

```python
# 基线 SQLAlchemy 2.0；缺库降级：掌握「错误分类 + 只读降级 + GTID 等待」三概念即可
import sqlalchemy as sa
import time

RETRYABLE = ("1053", "08006", "2006")          # server gone / connection failure

def classify(exc: Exception) -> str:
    """切换窗口错误分类：可重试 / 快速失败。"""
    code = getattr(exc, "orig", None)
    msg = str(exc)
    if any(k in msg for k in RETRYABLE):
        return "retryable"                      # 连接类：可重试（但要有预算，A101）
    if "readonly" in msg or "read-only" in msg:
        return "readonly"                       # 切换中 RDS 置只读 → 快速拒绝写
    return "fatal"                              # 业务错误：不重试

class WriteGate:
    """切换窗口写闸门：只读降级 + GTID 等待。"""
    def __init__(self):
        self.readonly_until = 0.0               # 切换窗口截止时间
    def enter_switch(self, seconds: float = 20):
        self.readonly_until = time.monotonic() + seconds
    def allow_write(self) -> bool:
        return time.monotonic() >= self.readonly_until
    def wait_gtid(self, conn, gtid: str, timeout: float = 2.0) -> bool:
        """强一致读前等待复制追上（PG：SELECT pg_wal_lsn_diff / MySQL：WAIT_FOR_EXECUTED_GTID_SET）。"""
        # MySQL 口径：SELECT WAIT_FOR_EXECUTED_GTID_SET(:gtid, :timeout)
        return True                              # demo 环境无真实 MySQL，口径见注释

gate = WriteGate()
def place_order(eng, user: str):
    if not gate.allow_write():
        raise RuntimeError("503: 切换窗口，写快速失败（排队会拖垮线程池）")
    with eng.begin() as c:
        c.execute(sa.text("INSERT INTO orders(user) VALUES (:u)"), {"u": user})
    return "ok"

if __name__ == "__main__":
    eng = sa.create_engine("sqlite://", pool_pre_ping=True)   # pre_ping：借出前探活（切换后旧连接快速驱逐）
    with eng.begin() as c:
        c.execute(sa.text("CREATE TABLE orders(user TEXT)"))
    print(place_order(eng, "u1"))
    gate.enter_switch(0.2)
    try:
        place_order(eng, "u2")
    except RuntimeError as e:
        print("切换窗口拦截:", e)
    time.sleep(0.25)
    print(place_order(eng, "u2"), "← 窗口结束恢复写")
    print("错误分类:", classify(Exception("server has gone away (1053)")))
    # 池配置口径：pool_pre_ping=True（或 pool_recycle < 切换后失效周期）；
    # 切换后 kill 池全部空闲连接比等自然回收更干脆（orchestrator 回调里做）。
```

**追问**：1) 为什么「全量重试」在切换窗口是灾难？——连接类错误重试虽合理，但切换 20s 内所有写都会失败，1000 个请求各重试 3 次 = 3000 次无效连接冲击 + 线程池被等待占满；闸门（快速失败）+ 预算（A101）才是正解。2) 半同步复制的代价？——每写多一个从库 ack RTT（毫秒级），可用性换不丢：semi-sync 超时降级异步（又可能丢）——「lossless semi-sync」（等 ack 后才 commit）才真正零丢。3) 池的 `pool_pre_ping` vs `pool_recycle` 怎么选？——pre_ping 每借出 ping 一次（微秒级开销，切换场景必备）；recycle 是定时淘汰兜底，两者不冲突。

## 背诵要点
1. 切换丢事务根因 = 异步复制窗口；应用按「可能丢最近写」设计，强一致读等 GTID/WAIT。
2. 应用侧五件套：pre_ping 驱逐死连接、错误分类（1053/08006 可重试）、写闸门快速失败、GTID 等待、半同步。
3. 切换窗口写快速失败优于排队——排队会拖垮线程池把可用读也一起拖死。

## 复盘追问
1. 切换后「旧主复活」会发生什么？（提示：fencing 问题——新主必须封旧主（VIP 摘除/只读置位），双主双写是数据分叉灾难）
2. 你的服务如何在演练中验证切换兼容性？（提示：定期制造切换（chaos），观察错误分类与闸门日志、P99 恢复斜率）
