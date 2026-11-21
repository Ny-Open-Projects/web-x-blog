---
title: [Q1414] 内存碎片治理: 从碎片率读数到 activedefrag 动作
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1414 · 内存碎片治理: 从碎片率读数到 activedefrag 动作

> 难度:★★★☆ | 标签:Redis, 内存管理

**问**:mem_fragmentation_ratio 高到多少需要处理?activedefrag 是怎么工作的?

**答**:碎片率 = 操作系统分配给 Redis 的物理内存 / Redis 自报的 used_memory。读法:接近 1 是健康;略大于 1.5 开始关注;大于 1.5 且 used_memory 远小于 RSS 说明空洞严重;小于 1 反而是 swap 或内存被压缩的危险信号。碎片来自反复的分配释放:大量 set 后 delete、过期不均匀都会留下allocator 洞。治理三招:重启实例(最暴力,主从切换式重启);升级 jemalloc 版本;开启 activedefrag yes——Redis 在后台把分散的数据搬回紧凑区域,配合 active-defrag-threshold-lower 等参数控制激进度,注意搬移本身消耗 CPU,高峰期要限制。防患于未然的做法是控制大 key、用与业务尺寸匹配的编码,少做反复 set 大 value 的模式。

```python
# file: code/04_数据库与缓存/q1414_fragmentation.py
"""内存碎片: 分配释放产生空洞, 压缩整理降低碎片率"""
class Pool:
    def __init__(self, size=32):
        self.slots = [None] * size
    def alloc(self, n, tag):
        start = None
        for i, s in enumerate(self.slots):
            if s is None:
                start = i if start is None else start
                if i - start + 1 == n:
                    for j in range(start, start + n):
                        self.slots[j] = tag
                    return start
            else:
                start = None
        raise MemoryError("no contiguous space")
    def free(self, tag):
        for i, s in enumerate(self.slots):
            if s == tag:
                self.slots[i] = None
    def compact(self):
        live = [s for s in self.slots if s is not None]
        self.slots = live + [None] * (len(self.slots) - len(live))

pool = Pool()
pool.alloc(8, "A"); pool.alloc(8, "B"); pool.alloc(8, "C"); pool.alloc(8, "D")
pool.free("B"); pool.free("D")
print("释放后占用 16, 空洞:", len(pool.slots) - 16)
try:
    pool.alloc(12, "E")
except MemoryError:
    print("再分配 12 格失败: 总空闲 16 但被切成两个 8, <- 这就是碎片")
pool.compact()
print("compact 后可容纳大块: 布局", "".join(s or "." for s in pool.slots))
print("Redis activedefrag 做的就是把数据搬回紧凑区, 不停服但耗 CPU")
```

**追问**:
- 为什么碎片率低于 1 更危险?——说明物理内存不够、部分数据被换到 swap,访问延迟毫秒级,比碎片本身严重得多,先查宿主机内存。
- activedefrag 为什么默认关闭?——它通过搬运键值回收碎片,CPU 消耗与业务争抢;默认关闭把开启时机与激进度留给运维按内存水位决策。
- 碎片是怎么攒出来的?——jemalloc 按 size class 分配,反复写删不同尺寸 value 留下同类空洞;used_memory 只算逻辑占用,RSS 含空洞,比率因此升高。
- 生产陷阱?——大 value 频繁 set/delete 的写入模式持续造洞,defrag 追不上产洞速度;根在大 key 与写入模式,defrag 只是止血。

---
