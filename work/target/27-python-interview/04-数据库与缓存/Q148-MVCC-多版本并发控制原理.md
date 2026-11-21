---
title: [Q148] MVCC 多版本并发控制原理
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q148 · MVCC 多版本并发控制原理

> 难度:★★★★ | 标签:MySQL, MVCC

**问**:说说 InnoDB MVCC 的工作原理,它如何做到"读不加锁、读写不冲突"?

**答**:每行记录隐藏 trx_id(最后修改事务)与 roll_pointer(指向 undo log 版本链)。事务做快照读时生成 ReadView,包含活跃未提交事务列表与高低水位;沿版本链从新到旧找第一个"对自己可见"的版本:是自己创建的可见;小于活跃事务最小 id 的必已提交、可见;大于等于高水位(快照之后才开始的事务)不可见;其余区间看是否在活跃列表,不在即已提交可见。写操作仍然加锁,读走版本链不加锁,从而实现读写并行。

```python
# file: code/04_数据库与缓存/q148_mvcc_demo.py
"""用版本链 + ReadView 模拟 InnoDB 可见性判断"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class RowVersion:
    value: str
    trx_id: int                      # 创建该版本的事务 id
    prev: Optional["RowVersion"] = None  # 更旧的版本


@dataclass
class ReadView:
    creator: int                     # 当前事务 id
    active: frozenset                # 生成快照时仍在运行的未提交事务 id 集合
    next_trx_id: int                 # 生成快照时的下一个事务 id(高水位下界)

    def visible(self, version: RowVersion) -> bool:
        trx = version.trx_id
        if trx == self.creator:
            return True              # 自己改的当然可见
        if trx >= self.next_trx_id:  # 快照之后才开始的事务, 一律不可见
            return False
        if self.active and trx < min(self.active):
            return True              # 比最早活跃事务更早, 必已在快照前提交
        return trx not in self.active  # 中间区间: 不在活跃列表即已提交


def snapshot_read(head: Optional[RowVersion], view: ReadView) -> str:
    """沿版本链从新到旧找第一个可见版本"""
    cur = head
    while cur is not None:
        if view.visible(cur):
            return cur.value
        cur = cur.prev
    return "<deleted>"


if __name__ == "__main__":
    # trx 5 写入 v1, trx 8 覆盖为 v2, trx 8 尚未提交, 系统下一个事务 id 是 9
    v1 = RowVersion(value="v1", trx_id=5)
    v2 = RowVersion(value="v2", trx_id=8, prev=v1)

    rr_view = ReadView(creator=7, active=frozenset({8}), next_trx_id=9)  # trx7 开启快照时 8 未提交
    print("RR 快照读到:", snapshot_read(v2, rr_view))       # v1, 看不见未提交的 v2

    # RC 每次读都新建视图: 此时 trx8 已提交(不再活跃), 高水位推进到 9
    rc_view = ReadView(creator=7, active=frozenset(), next_trx_id=9)
    print("trx8 提交后 RC 读到:", snapshot_read(v2, rc_view))  # v2
```

**追问**:
- 快照读和当前读的区别?——普通 SELECT 是快照读走 MVCC;UPDATE/DELETE/SELECT FOR UPDATE 是当前读,读最新版本并加锁。
- RR 下的"幻读"为什么只是基本杜绝?——快照读靠 MVCC,当前读靠间隙锁,两者混用时仍可能出现幻读,需显式加锁保持一致。

---
