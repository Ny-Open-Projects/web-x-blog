---
title: [XP-419] 手写一个 IM 消息 seq 补齐器
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## XP-419：手写一个 IM 消息 seq 补齐器

**答**：
- 需求：implement SeqGapFiller(fetchGap)。add(msg) 按 seq 插入有序队列；检测缺口（seq 不连续）时调 fetchGap(from, to) 补拉（去重并发）；flush() 输出连续段；输出 { ordered, gaps }。
- 边界：重复 seq 丢弃；gap 补拉失败保留缺口标记；队列上限 5000 溢出丢弃最旧。
- 评分点：缺口检测；并发去重；补拉回填；有序输出

```javascript
class SeqGapFiller {
  constructor(fetchGap) {
    this.fetchGap = fetchGap; this.queue = new Map();
    this.gapFetching = new Set(); this.gaps = [];
  }
  add(msg) {
    this.queue.set(msg.seq, msg);
    const gap = this.findGap();
    if (gap && !this.gapFetching.has(gap.from)) {
      this.gapFetching.add(gap.from);
      this.fetchGap(gap.from, gap.to).then(msgs => {
        msgs.forEach(m => this.queue.set(m.seq, m));
        this.gapFetching.delete(gap.from);
      }).catch(() => this.gapFetching.delete(gap.from));
    }
  }
  findGap() {
    const seqs = [...this.queue.keys()].sort((a, b) => a - b);
    for (let i = 1; i < seqs.length; i++)
      if (seqs[i] - seqs[i-1] > 1)
        return { from: seqs[i-1] + 1, to: seqs[i] - 1 };
    return null;
  }
  flush() {
    const seqs = [...this.queue.keys()].sort((a, b) => a - b);
    const ordered = seqs.map(s => this.queue.get(s));
    this.queue.clear();
    return { ordered, gaps: this.gaps };
  }
}
```
