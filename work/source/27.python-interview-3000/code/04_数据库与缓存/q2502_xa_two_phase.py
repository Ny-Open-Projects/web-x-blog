"""XA 两阶段提交: 协调者一停, 所有人挂在半路"""
import json

class RM:
    """资源管理器: prepare 后进入 in-doubt 状态, 只等协调者裁决"""

    def __init__(self, name):
        self.name = name
        self.wal = []                     # 预写日志: 状态可恢复

    def prepare(self, xid):
        self.wal.append({"xid": xid, "state": "prepared"})
        return "yes"

    def commit(self, xid):
        self.wal.append({"xid": xid, "state": "committed"})

    def rollback(self, xid):
        self.wal.append({"xid": xid, "state": "aborted"})


def run_2pc(rms, crash_after_prepare=False):
    xid = "tx-1001"
    # 阶段一: 投票
    votes = [rm.prepare(xid) for rm in rms]
    print("  阶段一 prepare: 票=%s" % votes)
    if crash_after_prepare:
        print("  协调者在记录全局决策前崩溃!")
        return xid, "in-doubt"
    # 阶段二: 裁决
    if all(v == "yes" for v in votes):
        for rm in rms:
            rm.commit(xid)
        return xid, "committed"
    for rm in rms:
        rm.rollback(xid)
    return xid, "aborted"

rms = [RM("db-order"), RM("db-points")]
print("正常路径:")
xid, state = run_2pc(rms)
print("  结果: %s = %s" % (xid, state))

rms = [RM("db-order"), RM("db-points")]
print("故障路径: prepare 全部通过后协调者宕机")
xid, state = run_2pc(rms, crash_after_prepare=True)
for rm in rms:
    print("  %s 卡在状态: %s (锁不释放, 业务阻塞)" % (rm.name, rm.wal[-1]["state"]))

print("恢复: 协调者重启后读自己的日志, 没写全局决策就统一回滚, 写了就统一提交")
print("结论: 2PC 的阻塞窗口是结构性的——参与者越 多/慢/易挂, 系统越脆;")
print("      微服务几乎不用 XA, 用本地消息表与 SAGA 把'强一致'换成'最终一致'")
