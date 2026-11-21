---
title: [PER-256] sendBeacon 有 64KB 体积限制，批量上报超限怎么办？大报文的拆包与压缩策略？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-256：sendBeacon 有 64KB 体积限制，批量上报超限怎么办？大报文的拆包与压缩策略？

**答**：
- 限制本质：sendBeacon 把数据放进浏览器排队队列，超过限额（Chrome 约 64KB，跨域各站共享）会静默失败返回 false——所以必须检查返回值，false 就降级 fetch keepalive。
- 拆包策略：批量按"条数 × 预估体积"双控——既限条数（20 条）也限字节（45KB 保险线）；超长单条（如 LoAF 明细、错误堆栈）单独截断（堆栈 5KB 上限）或拆成独立条目。
- 压缩：文本 JSON 优先压缩字段名（映射表 k->短键）、去掉冗余 URL 前缀；有余力用 CompressionStream 做 gzip（浏览器原生、异步），服务端解压。体积能降 70%+。
- 优先级取舍：CWV 指标 > 归因明细 > 埋点流水；超限时按优先级丢弃低优先级数据而不是整体失败。

```javascript
async function compressBatch(batch) {
  const map = { metric: 'm', value: 'v', page: 'p', sid: 's', seq: 'q', ts: 't' }; // 键名压缩
  let json = JSON.stringify(batch.map(o =>
    Object.fromEntries(Object.entries(o).map(([k, v]) => [map[k] || k, v]))));
  if (json.length > 45000) {                    // 字节保险线，超限降级
    if ('CompressionStream' in window) {
      const cs = new CompressionStream('gzip');
      const stream = new Blob([json]).stream().pipeThrough(cs);
      const buf = await new Response(stream).arrayBuffer();
      return { body: buf, gzip: true };          // 服务端按 Content-Encoding 解包
    }
    return { body: JSON.stringify(batch.slice(0, Math.ceil(batch.length / 2))), gzip: false }; // 拆半
  }
  return { body: json, gzip: false };
}
// sendBeacon 返回 false（超 64KB 排队限制）必须降级 fetch keepalive
```
