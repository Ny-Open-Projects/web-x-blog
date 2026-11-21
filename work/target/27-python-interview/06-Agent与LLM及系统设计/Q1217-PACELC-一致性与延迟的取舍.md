---
title: [Q1217] PACELC:一致性与延迟的取舍
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1217 · PACELC:一致性与延迟的取舍

> 难度:★★★★ | 标签:PACELC, 理论

**问**:PACELC 比 CAP 多说了什么?怎么指导选型?

**答**:PACELC 补上了"没有分区时"的取舍:If Partition, choose A or C;Else, choose Latency or Consistency。即正常运行时,强一致(PAXOS/同步复制)要等多数确认,延迟高;异步复制延迟低但可能读到旧值。注意 E 之后的字母表示 Else 分支**选择的一侧**:EC = 选一致性(牺牲延迟),EL = 选低延迟(牺牲一致性),不要按字面把 EL 理解成「牺牲延迟」。选型翻译:支付/库存这类读自己写要强一致,选 EC;社交 feed、商品浏览容忍旧值,选 EL 换低延迟。工程上还常做成"会话内强一致"折中:写后短期内把该用户读路由到主副本,兼顾两者。

```python
# file: code/06_Agent与LLM及系统设计/q1217_pacelc.py
"""PACELC 演示:同步复制低差异高延迟 vs 异步复制低延迟有旧读 + 会话粘住方案。"""
import time


class ReplicatedStore:
    def __init__(self, mode):
        self.mode = mode                # "sync" or "async"
        self.primary, self.replica = {}, {}
        self.replica_lag = 0.01         # 模拟复制延迟
        self.pending = []

    def write(self, k, v):
        t0 = time.monotonic()
        self.primary[k] = v
        if self.mode == "sync":
            self.replica[k] = v         # 写路径等待副本
        else:
            self.pending.append((k, v))  # 异步:先记账后复制
        return (time.monotonic() - t0, 0.01 if self.mode == "sync" else 0.0)

    def replicate_tick(self):
        while self.pending:
            k, v = self.pending.pop(0)
            self.replica[k] = v

    def read(self, k, from_replica=True):
        src = self.replica if from_replica else self.primary
        return src.get(k)


if __name__ == "__main__":
    sync = ReplicatedStore("sync")
    lat, _ = sync.write("price", 99)
    print(f"sync 写延迟 +{lat:.3f}s(等待副本),副本立即可读:", sync.read("price"))
    assert sync.read("price") == 99, "强一致读必为新值"

    async_s = ReplicatedStore("async")
    lat2, _ = async_s.write("price", 99)
    stale = async_s.read("price")
    print(f"async 写延迟 +{lat2:.3f}s(不等副本),副本读 = {stale}(旧值)")
    assert stale is None, "复制未完成,读到旧值"
    async_s.replicate_tick()
    assert async_s.read("price") == 99
    print("复制完成后收敛;写后读用户应粘住主副本规避旧读")
    # 会话粘住:同一会话读主
    assert async_s.read("price", from_replica=False) == 99
    print("会话粘主策略生效:自己的写自己立即可见")
```

**追问**:
- 会话粘住有什么坑?答:主副本故障切换时粘性表失效,要处理"粘住的节点没了"的降级;且粘住主副本会把读流量集中到主,需设置粘性 TTL 按复制进度解除。
- 为什么不能全系统强一致?答:强一致的写延迟随副本地理距离与节点数线性上升,全量强一致等于放弃可用性和延迟,只有资金类数据值得。
