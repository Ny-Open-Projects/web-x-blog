---
title: [PER-567] 手写一个前端 span 采集与导出器：页面加载/请求/交互三类 span，兼容 OpenTelemetry 格式导出
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-567：手写一个前端 span 采集与导出器：页面加载/请求/交互三类 span，兼容 OpenTelemetry 格式导出

**答**：
- OTel span 的关键字段：`traceId/parentSpanId/spanId/name/kind/startTimeUnixNano/attributes/status`；前端导出成 OTLP JSON 批量 POST 到 collector。
- 要点：父 span 关系要维护（页面加载是根，请求/交互是其子）；批量导出（攒 20 条或 5 秒）用 sendBeacon/keepalive；span 结束才算完整（请求 span 在 fetch finally 里 close）。
- 边界：页面 unload 时 flush 残留 span；span 上报自身不能产生新 span（防止自递归），要对 collector URL 过滤。
- 评分点：父子关系维护与自递归过滤。

```javascript

class SpanExporter {
  constructor(collector) {
    this.collector = collector; this.buf = []; this.rootSpanId = null;
    setInterval(() => this.flush(), 5000);
    addEventListener('pagehide', () => this.flush());
  }
  start(name, attrs = {}) {
    const span = {
      traceId: window.__traceId, spanId: crypto.randomUUID().replace(/-/g, '').slice(0, 16),
      parentSpanId: this.rootSpanId, name, kind: 'INTERNAL',
      startTimeUnixNano: String(BigInt(Math.round(performance.timeOrigin + performance.now()) * 1e6)),
      attributes: attrs, status: 'UNSET',
    };
    if (!this.rootSpanId) this.rootSpanId = span.spanId;  // 首个 span 为根
    return { ...span, end: (status = 'OK') => {
      span.status = status;
      span.endTimeUnixNano = String(BigInt(Math.round(performance.timeOrigin + performance.now()) * 1e6));
      this.push(span);
    }};
  }
  push(span) {
    if (span.name.includes('/collect')) return;           // 自递归过滤
    this.buf.push(span);
    if (this.buf.length >= 20) this.flush();
  }
  flush() {
    if (!this.buf.length) return;
    const body = JSON.stringify({ resourceSpans: [{ scopeSpans: [{ spans: this.buf.splice(0) }] }] });
    fetch(this.collector, { method: 'POST', body, keepalive: true }).catch(() => {});
  }
}
```
