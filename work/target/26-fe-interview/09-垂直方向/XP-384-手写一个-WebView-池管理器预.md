---
title: [XP-384] 手写一个 WebView 池管理器（预热/复用/回收）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## XP-384：手写一个 WebView 池管理器（预热/复用/回收）

**答**：
- 需求：implement WebViewPool(size)。acquire() 取预热实例（无则即时创建，标记 cold）；release(wv) 归还（超 size 销毁）；stats() 输出 { poolSize, coldCreates, reuses }；预热实例加载 about:blank 占位。
- 边界：size <= 0 抛错；release 未 acquire 的实例忽略；destroy 回调清理监听器。
- 评分点：池化复用；冷创建统计；重复保护；超量销毁

```javascript
class WebViewPool {
  constructor(size) {
    if (size <= 0) throw new Error('size > 0');
    this.size = size; this.free = []; this.cold = 0; this.reuses = 0;
  }
  warmup(createFn) {
    while (this.free.length < this.size) {
      const wv = createFn();
      wv.loadUrl('about:blank');
      this.free.push(wv);
    }
  }
  acquire(createFn) {
    const wv = this.free.pop();
    if (wv) { this.reuses++; return { wv, cold: false }; }
    this.cold++;
    return { wv: createFn(), cold: true };
  }
  release(wv, destroyFn) {
    if (this.free.includes(wv)) return;                // 忽略重复
    if (this.free.length < this.size) {
      wv.loadUrl('about:blank');
      this.free.push(wv);
    } else destroyFn?.(wv);
  }
  stats() { return { poolSize: this.free.length,
    coldCreates: this.cold, reuses: this.reuses }; }
}
```
