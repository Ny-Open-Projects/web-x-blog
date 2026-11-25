---
title: "[Q6777] 备份一跑命中率崩了：缓冲池 young/old 子链与扫描页污染"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6777 · 备份一跑命中率崩了：缓冲池 young/old 子链与扫描页污染

难度：P6 ｜ 标签：InnoDB、buffer pool、LRU、young/old 子链、全表扫描

基线：Python 3.12；实现 InnoDB 式 young/old 双子链 LRU（含 old_blocks_time 晋升门槛）与朴素 LRU 对照，对比全表扫描后热页留存率，全标准库实跑。

**问**：夜间备份或大报表一跑，白天业务高峰的缓存命中率骤降、IO 打满——明明 buffer pool 里刚还有业务热数据。朴素 LRU 为什么扛不住全表扫描？InnoDB 的 young/old 子链和 `innodb_old_blocks_time` 是怎么防污染的？读接口不同（大 IO 读 vs 点查）在这条链上待遇为什么不一样？

**答**：
- **结论**：朴素 LRU 是"最近使用优先"，但全表扫描会**把每个页都访问一遍**：一次扫描 200 页、缓存 50 页，扫完热页全部被逐出——扫描页在缓存里只存活了"被扫描的那一刻"，却是新访问，天然挤掉真正的高频页。InnoDB 的解法是**双子链**：新读入的页一律先放 **old 子链头部**（占约 5/8 链长的尾部区域），只有当页**再次被访问且距首次进入超过 `innodb_old_blocks_time`（默认 1000ms）**才晋升到 young 子链。全表扫描页的特点恰好被这个门槛杀死：扫描对同页的后续访问（读页内多行）间隔是毫秒级甚至同瞬间的，永远过不了 1 秒门槛，留在 old 区，逐出也从 old 尾部先走——**young 区的热集纹丝不动**。防污染的本质是"用存活时间过滤访问模式"：点查有跨秒的重复访问，扫描没有。
- **取舍**：① `innodb_old_blocks_time` 调大：过滤更狠（更抗扫描），但正常点查的页也可能错过晋升窗口（业务访问间隔恰好 > 阈值），命中率反降；调小则过滤失效；② old 区占比（`innodb_old_blocks_pct`，默认 37%）：扫描负载重的数仓侧调大（old 区多容纳扫描页），纯 OLTP 调小；③ 备份走物理快照（文件级）比逻辑备份（逐页读）对缓存友好得多——根本绕开污染源（Q6760 物理备份原理的衔接）；④ 大 IO 读（预读/全扫）绕过 young 晋升是故意设计：`innodb_random_read_ahead` 关闭时预读页也只进 old。
- **实战**：① 命中率突降的排查顺序：先看是否有全扫/备份任务（information_schema.processlist 长查询），再谈扩内存——污染是模式问题不是容量问题；② 定时报表统一走只读从库，主库 buffer pool 不接扫描；③ 参数调优用业务流量回放对比命中率，别拍脑袋；④ 监控 young/old 区各自的命中率（`SHOW ENGINE INNODB STATUS` 的 Buffer pool hit rate 与 pages made young），young 命中率才是业务热度的真话。

```python
"""Q6777 InnoDB young/old 子链: 新页进 old 头, 存活过 old_blocks_time 才晋升 young。"""
from collections import OrderedDict

OLD_BLOCKS_TIME = 3            # 模拟 innodb_old_blocks_time: 重访问间隔达到阈值才晋升


class InnoDBLRU:
    def __init__(self, cap: int):
        self.cap = cap
        self.young: OrderedDict[int, int] = OrderedDict()
        self.old: OrderedDict[int, int] = OrderedDict()   # key -> 首次放入 tick
        self.tick = 0

    def _touch_old(self, page: int) -> None:
        first = self.old[page]
        if self.tick - first >= OLD_BLOCKS_TIME:          # 存活够久 -> 晋升 young
            del self.old[page]
            self.young[page] = self.tick
            self.young.move_to_end(page)
        # 否则留在原地(扫描页的连续重访不晋升)

    def point_access(self, page: int) -> None:
        """点查/正常业务访问."""
        self.tick += 1
        if page in self.young:
            self.young.move_to_end(page)
        elif page in self.old:
            self._touch_old(page)
        else:
            self.old[page] = self.tick                    # 新页只进 old 头
        self._evict()

    def scan_access(self, page: int) -> None:
        """全表扫描页: 同页两次"重访"间隔极小, 不会过晋升阈值."""
        self.point_access(page)
        self.point_access(page)

    def _evict(self) -> None:
        while len(self.young) + len(self.old) > self.cap:
            if self.old:
                self.old.popitem(last=False)              # 先逐出 old 尾
            else:
                self.young.popitem(last=False)

    def has(self, page: int) -> bool:
        return page in self.young or page in self.old


class NaiveLRU:
    """对照: 单链朴素 LRU, 扫描页与业务页同等对待."""
    def __init__(self, cap: int):
        self.cap = cap
        self.items: OrderedDict[int, int] = OrderedDict()

    def point_access(self, page: int) -> None:
        self.items[page] = 0
        self.items.move_to_end(page)
        while len(self.items) > self.cap:
            self.items.popitem(last=False)

    def scan_access(self, page: int) -> None:
        self.point_access(page)

    def has(self, page: int) -> bool:
        return page in self.items


def run(buf) -> float:
    hot = set(range(40))                                   # 缓存容量 50, 热集 40 页
    for p in sorted(hot):
        buf.point_access(p)                                # 反复点查 -> 热页晋升
        buf.point_access(p)
        buf.point_access(p)
        buf.point_access(p)
    for sweep in range(3):                                 # 3 轮全表扫描, 200 页冷数据
        for p in range(40, 240):
            buf.scan_access(p)
    return sum(buf.has(p) for p in hot) / len(hot)


if __name__ == "__main__":
    kept = run(InnoDBLRU(cap=50))
    naive = run(NaiveLRU(cap=50))
    print(f"young/old 子链: 3 轮全表扫描后热页留存 {kept:.0%}")
    print(f"朴素 LRU 对照  : 热页留存 {naive:.0%} (扫描页把热页全部冲出)")
    ok = kept >= 0.9 and naive <= 0.1
    print(f"校验: old 区吸收扫描页保护热集 -> {'通过' if ok else '异常'}")
    print("结论：扫描页进 old 尾、间隔过 old_blocks_time 才晋升, 热集免遭冲刷;")
    print("      备份/大报表跑挂 OLTP 命中率, 先查这条链而不是先扩内存")
```

**追问一**：`innodb_old_blocks_time` 从 0 调到 1000ms，调大它有什么副作用？什么业务会踩到？

→ 解析：副作用是"晋升门槛变高"：一些**合法热页的访问间隔恰好超过阈值**（低频关键数据：每小时查一次的配置表、隔几秒轮询的大对象）会被反复打回 old 区，逐出后反复回源——命中率下降 + IO 放大，且症状与"容量不足"难区分。踩到的业务特征：访问间隔分布双峰（毫秒级热点 + 秒级~分级次热点）。诊断方法：对比 pages made young 速率与该类数据的回源率；对策是数据分级而不是调参：次热点数据主动 pin 到独立缓存层（应用侧 LRU 或预热常驻，Q2491 快照恢复热身），让 buffer pool 专注毫秒级真热点。参数只解决一类污染，数据分层解决访问间隔异构。

**追问二**：既然扫描页只进 old，为什么大扫描还是会让整机变慢？

→ 解析：防污染防的是"缓存命中率损失"，防不了三笔真成本：① **IO 带宽**：扫描按顺序大块读，与 OLTP 随机读抢磁盘带宽（云盘 IOPS 限流下尤其明显），点查延迟直接被拖高；② **CPU 与锁**：扫描查询占用执行线程、挤占 innodb 并发额度，页上的 latch 竞争也会增加；③ **redo/binlog 链路**：大扫描若伴随大事务（如扫全表改一批），复制与刷盘全链路承压（Q6691 主从延迟雪崩）。所以"扫描隔离"的正确姿势是三层：逻辑隔离（只读从库跑扫描）> 参数缓解（old_blocks_time 只护缓存）> 事后扩容（最贵且不解决带宽争抢）。容量规划时把"扫描带宽"单独入账（Q6640 查询单位成本的同类拆法），它和点查 QPS 是两种完全不同的资源曲线。
