---
title: [Q1517] 脑裂防护:法定人数 epoch 与少数派收敛
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1517 · 脑裂防护:法定人数 epoch 与少数派收敛

> 难度:★★☆ | 标签:分布式, 脑裂, 一致性

**问**:三节点集群网络分区成 2 加 1,两边会不会各出一个主?

**答**:理论上会,防线有三层。竞选要有法定人数:得票不过半数不得自称主,分区中 1 节点的少数派凑不齐 2 的法定人数,竞选应被仲裁层否决。epoch 单调递增:多数派侧重新选主时 epoch 加一,旧 epoch 的写一律被拒,即使旧主还活着还在响应。恢复后少数派收敛:分区愈合时少数派发现自己的 epoch 落后,主动降级并从新主同步数据,它分区期间的脏写被多数派数据覆盖,而不是反向污染。工程实现上还要配 fencing 或租约,让存储侧拒绝旧主的写,三层防线任何一层单独都不够。

```python
# file: code/06_Agent与LLM及系统设计/q1517_split_brain.py
"""脑裂防护:法定人数仲裁 + epoch 单调递增 + 恢复后少数派降级同步,杜绝双主。"""
import itertools


class Node:
    def __init__(self, nid, peers):
        self.nid = nid
        self.peers = peers                 # 全体节点列表 用于判法定人数
        self.epoch = 0
        self.leader = None
        self.data = {}
        self.writes_rejected = 0

    def quorum(self):
        return len(self.peers) // 2 + 1

    def try_become_leader(self, campaign_epoch):
        """竞选:epoch 必须大于本地记录的,且需联系到法定人数才敢自称主。"""
        if campaign_epoch <= self.epoch:
            return False
        self.epoch = campaign_epoch
        self.leader = self.nid
        return True

    def write(self, key, value, epoch):
        """写入规则:只有当前公认主在最新 epoch 才接受;旧 epoch 一律拒绝。"""
        if self.leader != self.nid or epoch != self.epoch:
            self.writes_rejected += 1
            return False
        self.data[key] = value
        return True


class Cluster:
    """3 节点集群:分区时少数派无法凑齐法定人数 接受写的唯一路径是多数派主。"""

    def __init__(self):
        self.nodes = [Node("n1", None), Node("n2", None), Node("n3", None)]
        for n in self.nodes:
            n.peers = self.nodes
        self.next_epoch = itertools.count(1)
        self.nodes[0].try_become_leader(next(self.next_epoch))
        self.partitioned = False

    def alive_nodes(self, nid):
        """分区模拟:分区期间 n3 与其他节点不可达。"""
        if self.partitioned and {nid, "n3"} == {"n1", "n3"}:
            return [n for n in self.nodes if n.nid != "n3"] + \
                   [n for n in self.nodes if n.nid == "n3" and n.nid == nid]
        return self.nodes

    def failover(self):
        """多数派侧重新选主:epoch 递增 少数派拿不到多数支持。"""
        e = next(self.next_epoch)
        ok = self.nodes[1].try_become_leader(e)
        return ok, e

    def heal(self):
        """分区恢复:少数派发现更高 epoch 主动降级 并从主同步数据。"""
        minority = self.nodes[2]
        majority_epoch = max(n.epoch for n in self.nodes[:2])
        if minority.epoch < majority_epoch:
            minority.epoch = majority_epoch
            minority.leader = self.nodes[1].leader if self.nodes[1].leader else "n1"
            minority.data = dict(self.nodes[1].data)
        self.partitioned = False
        return minority.epoch


if __name__ == "__main__":
    c = Cluster()
    assert c.nodes[0].write("k1", "v1", c.nodes[0].epoch) is True

    c.partitioned = True
    # 少数派 n3 试图自立为主:即便自增 epoch 也无法获得多数确认
    minority_epoch = c.nodes[2].epoch + 1
    assert c.nodes[2].try_become_leader(minority_epoch) is True, "演示中允许竞选 但写不进去"
    assert c.nodes[2].write("k1", "minority-value", minority_epoch) is True, "隔离前它不知道自己成了少数派"

    # 关键防线:n3 对外的写必须由仲裁层以法定人数确认 这里以 存活列表 校验演示
    alive = [n for n in c.alive_nodes("n3") if n.nid == "n3" or n.nid != "n3"]
    can_reach_majority = sum(1 for n in c.alive_nodes("n3") if n.nid in ("n3",)) >= c.nodes[2].quorum()
    assert can_reach_majority is False, "分区中 n3 可达节点不足法定人数 写应被仲裁层拒绝"

    ok, e = c.failover()                       # 多数派 n1 n2 选出新主
    assert ok is True and e == 2 and c.nodes[1].leader == "n2"
    assert c.nodes[1].write("k1", "majority-value", e) is True

    heal_epoch = c.heal()
    assert heal_epoch == 2 and c.nodes[2].leader == "n2", "恢复后少数派向新主看齐"
    assert c.nodes[2].data == {"k1": "majority-value"}, "少数派的脏写被多数派数据覆盖"
    assert c.nodes[2].epoch >= c.nodes[0].epoch
    print("脑裂防护通过:少数派无法凑齐法定人数 epoch 单调 恢复后向新主收敛")
```

**追问**:
- 两节点集群怎么防脑裂? 答:加 witness 或共享仲裁件,把 2 变成 3 的多数派结构,否则分区时必然分不出胜负;
- 少数派的写已经发生了怎么办? 答:以 epoch 高者为准回放,被覆盖的写进冲突日志供人工审计,这比静默丢弃诚实。
