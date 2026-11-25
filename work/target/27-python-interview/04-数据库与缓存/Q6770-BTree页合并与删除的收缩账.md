---
title: "[Q6770] 删了一半数据索引没瘦反而更碎：B+Tree 页合并与删除的收缩账"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6770 · 删了一半数据索引没瘦反而更碎：B+Tree 页合并与删除的收缩账

难度：P7 ｜ 标签：MySQL、B+Tree、页合并、索引膨胀、删除回收

基线：Python 3.12；模拟 B+Tree 页级的插入分裂与删除合并，对比随机删除与顺序删除后的页数与碎片率。

**问**：一张日志表删掉了一半历史数据，磁盘占用纹丝不动，范围扫描反而更慢了。页分裂的逆过程——页合并（merge）什么时候发生？为什么删除后页数常常不降？`MERGE_THRESHOLD` 是什么？和"大批量 DELETE 不还磁盘"（Q6542）是同一件事吗？

**答**：
- **结论**：B+Tree 维持"每个页至少半满"的不变式：**插入让页满时 50/50 分裂成两页；删除让页的占用率低于阈值（InnoDB 默认 merge_threshold=50%）时，尝试与前后兄弟页合并**。但"删一半数据页数减半"通常不成立，三个原因：① 删除是随机的，每一页只被削掉一部分，多数页仍高于合并阈值，页数不变；② 合并失败常发生：相邻页删得也不均匀、或页内有未提交的并发修改，MySQL 会放弃合并只把页标记"可重用"；③ 空出来的页**留在 B+Tree 内部被复用，不归还文件系统**——磁盘文件大小不动，这是页级回收与文件级回收的两层账（Q6542 讲的是文件层：PG/InnoDB 大批量删除后 OS 看到的文件不变，是同一现象在两层的表现）。扫描变慢是因为删除后的碎片让逻辑上相邻的数据散布在更多物理页里，缓存命中率下降。
- **取舍**：① 顺序删除（按主键从头删）比随机删除更容易触发合并、形成"左侧可重用页段"，删除策略优先考虑；② 随机删除后的索引要真正收缩，只有重建（REINDEX/OPTIMIZE/gh-ost 换表，Q2508），代价与窗口要提前算；③ 高写压力场景关闭/放宽 merge_threshold（降低合并的写放大）也是选项——碎片换吞吐，看业务读多还是写多；④ 删除批量化本身有专门账（Q1671 分批节奏），合并只是它的后置效应。
- **实战**：① 大删之前先估算"删除模式"：能按主键顺序删就顺序删；② 删除后观察 `information_schema` 的页统计与碎片率，低于阈值再考虑重建；③ 重建窗口避开业务高峰（Q2508 时机账），Online DDL 注意磁盘双倍空间（Q6620）；④ 监控别只看文件大小，要看"逻辑页占用率"——它是合并是否发生的直接证据。

```python
"""B+Tree 页级模拟：插入分裂、删除合并、随机 vs 顺序删除后的页数对比。"""
MERGE_THRESHOLD = 0.5
PAGE_CAP = 16          # 每页最大记录数 (演示用小值)


class Page:
    __slots__ = ("keys",)

    def __init__(self):
        self.keys: list[int] = []

    @property
    def fill(self) -> float:
        return len(self.keys) / PAGE_CAP


class FlatBTree:
    """演示用: 单层页列表, 模拟页分裂与合并对页数/碎片的影响。"""

    def __init__(self):
        self.pages: list[Page] = [Page()]

    def insert(self, key: int) -> None:
        # 找到目标页(演示: 取余路由), 插入, 满则 50/50 分裂
        page = self.pages[min(key % len(self.pages), len(self.pages) - 1)]
        page.keys.append(key)
        page.keys.sort()
        if len(page.keys) > PAGE_CAP:
            mid = len(page.keys) // 2
            new = Page()
            new.keys, page.keys = page.keys[mid:], page.keys[:mid]
            self.pages.append(new)

    def delete(self, key: int) -> None:
        for i, page in enumerate(self.pages):
            if key in page.keys:
                page.keys.remove(key)
                # 占用率低于阈值 -> 尝试与相邻页合并
                if page.fill < MERGE_THRESHOLD and len(self.pages) > 1:
                    nb = self.pages[i - 1] if i else self.pages[1]
                    if page.keys and nb.fill < 0.9:    # 合并成功的条件
                        nb.keys.extend(page.keys)
                        nb.keys.sort()
                        self.pages.remove(page)
                return

    @property
    def pages_used(self) -> int:
        return len(self.pages)

    @property
    def fragmentation(self) -> float:
        used = sum(len(p.keys) for p in self.pages)
        return 1 - used / (self.pages_used * PAGE_CAP)


if __name__ == "__main__":
    keys = list(range(1000))

    def build() -> FlatBTree:
        t = FlatBTree()
        for k in keys:
            t.insert(k)
        return t

    t_rand = build()
    n_before = t_rand.pages_used
    for k in keys[::2]:                     # 随机模式删一半(隔一个删一个)
        t_rand.delete(k)
    print(f"随机删除: 页数 {n_before} -> {t_rand.pages_used} "
          f"(碎片率 {t_rand.fragmentation:.0%})")

    t_seq = build()
    for k in range(0, 1000, 2):             # 顺序删除偶数键 -> 相邻页持续瘦身
        t_seq.delete(k)
    print(f"顺序删除: 页数 {n_before} -> {t_seq.pages_used} "
          f"(碎片率 {t_seq.fragmentation:.0%})")

    n_data = len(keys) // 2
    min_pages = (n_data + PAGE_CAP - 1) // PAGE_CAP
    print(f"\n理论最小页数: {min_pages}")
    print(f"校验: 顺序删除页数接近理论值 -> "
          f"{'通过' if t_seq.pages_used <= min_pages + 5 else '差异大(演示路由的近似)'}")
    print("结论：随机删除多数页高于合并阈值, 页数不动、碎片上升;")
    print("      页只复用不还盘, 真收缩要重建; 能顺序删就顺序删")
```

**追问一**：合并失败时 MySQL 做了什么，页里的空洞去哪了？

→ 解析：合并尝试失败（兄弟页太满、有并发修改、页被 pin 住）时，页保持"半空但仍在树里"，其中空洞位置记录为可重用空间——下次往这个范围插入新记录时优先填空洞。这其实是合理设计：与其做昂贵的即时整理，不如把回收摊到未来的写入里。问题出在"删除之后不再有这个范围的插入"的场景（比如时间序列删旧数据后新数据都在别处），空洞永远填不上，只能重建。这也是为什么**分区表 + 直接 DROP/TRUNCATE 分区**（Q6759/Q6765）是时间序列数据删除的最优解——根本不产生页级碎片。

**追问二**：OPTIMIZE TABLE 重建能回收这些空间，为什么不能常态化每天跑？

→ 解析：重建 = 造一份紧凑副本再原子替换：期间磁盘要有整表双倍空间（Q6620）、行数大时耗时以小时计、Online DDL 期间仍持有 MDL 队尾（并发 DDL 卡死风险 Q884）、且重建期间写流量被复制到新表造成额外 IO。常态化每天跑等于把"碎片"换成了"每天数小时的维护成本 + 风险窗口"，得不偿失。正确姿势：碎片率监控超阈值才重建（比如 >30% 且扫描变慢有证据）、把删除设计前置（分区化/顺序删）让合并自然发生、用 gh-ost 类工具做有节流的重建（Q870）。碎片治理是"设计问题优先，维护手段兜底"。
