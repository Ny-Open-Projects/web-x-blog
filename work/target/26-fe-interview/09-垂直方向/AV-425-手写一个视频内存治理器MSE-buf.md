---
title: [AV-425] 手写一个视频内存治理器（MSE buffer 清理）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## AV-425：手写一个视频内存治理器（MSE buffer 清理）

**答**：
- 需求：implement BufferManager(sourceBuffer)。ensure(currentTime) 清理 currentTime 前 keep 秒外的数据（sb.remove）；总缓冲 > maxSec 时清理尾部未播放段；输出 { removed, rangesAfter }。
- 边界：remove 在 updateend 后执行（排队）；keep 默认 30s；remove 调用期间跳过（防竞态）。
- 评分点：水位清理；尾部裁剪；竞态防护；区间报告

```javascript
class BufferManager {
  constructor(sb, { keep = 30, maxSec = 120 } = {}) {
    this.sb = sb; this.keep = keep; this.maxSec = maxSec;
    this.removing = false;
  }
  ensure(currentTime) {
    if (this.removing) return { removed: false };
    const ranges = this.sb.buffered;
    if (!ranges.length) return { removed: false };
    const start = ranges.start(0);
    if (currentTime - start > this.keep) {
      this.removing = true;
      const total = ranges.end(ranges.length - 1) - start;
      const cut = total > this.maxSec
        ? ranges.end(ranges.length - 1) - this.maxSec / 2   // 尾部也裁
        : currentTime - this.keep;
      this.sb.addEventListener('updateend', () => this.removing = false,
        { once: true });
      this.sb.remove(start, cut);
      return { removed: true, from: start, to: cut };
    }
    return { removed: false };
  }
}
```
