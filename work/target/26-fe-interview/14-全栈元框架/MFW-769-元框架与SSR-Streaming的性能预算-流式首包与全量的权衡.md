---
title: [MFW-769] 流式首包与全量的权衡
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-769：流式首包与全量的权衡

**答**:
- 流式传输的权衡维度：1) **首包时间 vs 完成时间**（首包快（shell 即发 TTFB 200ms）但全量完成可能 3s（慢查询的 Suspense）——TTFB 与 TTI 的分离 RBL-520）；2) **流式 chunk 的粒度**（小 chunk = 低延迟但网络开销大（每 chunk 的 TCP/HTTP 开销——HTTP/2 减少开销）；大 chunk = 高效率但延迟（等够一批再发——压缩窗口 RBL-702）；3) **压缩与流的权衡**（压缩窗口大小——小窗口低延迟低压缩率；大窗口高压缩率高延迟 RBL-703）。
- 大促场景的最优权衡：首包优先（shell + LCP 洞先发——TTFB 关键）；非关键内容批量（footer/评论——攒够一批再发——压缩效率）；「分层的 chunk 策略」（RBL-703 策略表的实际应用）。
- 追问钩子：为什么「流式传输不是越早越好」的权衡需要「内容分级」？——过早发送 = 小 chunk 高网络开销（每个 200 字节的 token 都一个 chunk——TCP 头开销 > 数据）；过晚 = 用户等待（延迟感知）；「内容分级」：LCP/首屏内容小 chunk 即发（首包优先）+ 非关键内容攒批（压缩效率）——权衡的解不是「全早或全晚」而是「按内容分级」（RBL-703 压缩策略表的设计哲学）。

```javascript
// 分层的 chunk 策略
const STREAM_TIERS = {
  lcp: { chunkKB: 4, flushOnData: true },               // LCP：即发（低延迟）
  critical: { chunkKB: 8, flushOnData: true },          // 关键：即发
  content: { chunkKB: 16, flushMs: 50 },                // 内容：50ms 合帧
  lazy: { chunkKB: 32, flushMs: 200 },                  // 非关键：攒批
};
// 分层 flush 策略
class TieredFlusher {
  constructor(tiers) { this.tiers = tiers; this.buffers = new Map(); }
  add(content, tier) {
    const cfg = STREAM_TIERS[tier] ?? STREAM_TIERS.content;
    const buf = this.buffers.get(tier) || this.buffers.set(tier, { data: [], bytes: 0 }).get(tier);
    buf.data.push(content); buf.bytes += content.length;
    // flush 条件：flushOnData 或 达到 chunkKB 或 flushMs 超时
    const shouldFlush = cfg.flushOnData ||
      buf.bytes >= cfg.chunkKB * 1024 ||
      Date.now() - (buf.lastFlush ?? Date.now()) >= cfg.flushMs;
    if (shouldFlush) return this.flush(tier);
  }
  flush(tier) {
    const buf = this.buffers.get(tier);
    if (!buf?.data.length) return null;
    const data = buf.data.join(''); buf.data = []; buf.bytes = 0;
    buf.lastFlush = Date.now();
    return { tier, data };
  }
}
// LCP 内容：add(lcpHtml, 'lcp') → 立即 flush（低延迟）
// 非关键：add(footerHtml, 'lazy') → 攒到 32KB 或 200ms → flush（压缩效率）
```
