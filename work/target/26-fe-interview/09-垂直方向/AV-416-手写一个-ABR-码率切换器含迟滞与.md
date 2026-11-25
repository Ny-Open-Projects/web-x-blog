---
title: [AV-416] 手写一个 ABR 码率切换器（含迟滞与崩溃保护）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## AV-416：手写一个 ABR 码率切换器（含迟滞与崩溃保护）

**答**：
- 需求：实现 AbrController。feed({ throughputKbps, bufferSec }) 返回目标档位；规则：吞吐 80% 以下可切、升档需连续 3 次达标且 buffer > 10s、降档即时；档位间相邻切换；输出 { level, reason }。
- 边界：buffer < 3s 强制最低档；levels 空抛错；throughput 估计用 EWMA（α=0.2）。
- 评分点：EWMA；升档条件；降档即时；最低档保护

```javascript
class AbrController {
  constructor(levels) {
    if (!levels.length) throw new Error('levels 空');
    this.levels = levels; this.level = 0;
    this.ewma = levels[0].kbps; this.good = 0;
  }
  feed({ throughputKbps, bufferSec }) {
    this.ewma = this.ewma * 0.8 + throughputKbps * 0.2;   // EWMA
    if (bufferSec < 3)
      return this.set(0, '缓冲告急最低档');
    const safe = this.ewma * 0.8;
    const maxIdx = this.levels.findIndex(l => l.kbps > safe) - 1;
    const cap = maxIdx < 0 ? this.levels.length - 1 : maxIdx;
    if (cap > this.level) {
      if (this.ewma >= this.levels[this.level + 1].kbps && bufferSec > 10) {
        if (++this.good >= 3) return this.set(this.level + 1, '连续达标升档');
      } else this.good = 0;
    } else if (cap < this.level)
      return this.set(cap, '吞吐下降降档');
    return { level: this.level, reason: '维持' };
  }
  set(i, reason) {
    this.level = Math.min(this.levels.length - 1, Math.max(0, i));
    this.good = 0;
    return { level: this.level, reason };
  }
}
```
