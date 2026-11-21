---
title: [Q988] 全局 ID: 号段模式与双 buffer
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q988 · 全局 ID: 号段模式与双 buffer

> 难度:★★★★ | 标签:全局 ID, 架构

**问**:号段模式怎么发号?单点号段服务的抖动怎么缓解?

**答**:号段模式:DB 存 (biz_tag, max_id, step),发号服务每次取一段 `UPDATE ... SET max_id = max_id + step` 后在内存发号,数据库只承受 step 级压力。抖动问题:号段用尽瞬间要去 DB 拿下一段,造成尖刺延迟——双 buffer 优化:当前号段消耗到 10%~20% 时异步预加载下一号段,切换零感知。要点:step 平衡 DB 压力与浪费(宕机丢号,号段内未发的号作废——业务必须容忍不连续);多机房按奇偶/不同 biz_tag 隔离;对比雪花(本地生成无依赖但时钟敏感)与 UUID(无序伤索引),号段是"有序 + 中心化"折衷,美团 Leaf 是标准实现。

```python
# file: code/04_数据库与缓存/q988_segment_id.py
"""号段发号 + 双 buffer 预加载"""
import threading

class SegmentAllocator:
    def __init__(self, db_max=0, step=100):
        self.step = step
        self.next_db_max = db_max + step        # 模拟第一次取号段
        self.cur = {"lo": db_max + 1, "hi": db_max + step}
        self.buffer = None                       # 预加载的下一号段
        self.lock = threading.Lock()

    def _fetch_new_segment(self):
        lo = self.next_db_max + 1                # 模拟 UPDATE max_id+step
        self.next_db_max += self.step
        return {"lo": lo, "hi": self.next_db_max}

    def next_id(self):
        with self.lock:
            if self.cur["lo"] > self.cur["hi"]:  # 当前号段耗尽
                self.cur = self.buffer or self._fetch_new_segment()
                self.buffer = None
            elif self.buffer is None and \
                    self.cur["lo"] > (self.cur["hi"] + self.cur["lo"]) // 2:
                self.buffer = self._fetch_new_segment()   # 消耗过半预加载
            v = self.cur["lo"]
            self.cur["lo"] += 1
            return v

if __name__ == "__main__":
    alloc = SegmentAllocator(step=5)
    ids = [alloc.next_id() for _ in range(12)]
    print("发号:", ids)
    print("有序:", ids == sorted(ids), "趋势递增, 允许宕机跳号")
    print("双 buffer: 消耗过半即预取下一段, 切换无尖刺")
```

**追问**:
- 号段不连续业务能接受吗?——订单号等展示键一般可接受(只要求唯一有序);金额流水号若要求连续,要改为逐号确认机制,复杂度高很多。
- 与雪花混合怎么选?——DB 依赖轻、要求强趋势递增(索引友好)选号段;不想引入中心服务、容忍时钟管理成本选雪花。

---
