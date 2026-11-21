---
title: [DP-264] 源码识别：日志采集 SDK 源码中的采样与聚合策略？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-264：源码识别：日志采集 SDK 源码中的采样与聚合策略？
**答**:
- 策略链：采样策略（全量/比例/按错误类型分级）、去重策略（错误指纹窗口内合并）、脱敏策略（PII mask）——DP-216 管线的策略化细节。
- 聚合（备忘录+批量）：内存聚合计数（同指纹 count++），flush 时发聚合数据而非逐条——大错误风暴的流量保护。
- 观察者：错误源（window.onerror/unhandledrejection/reported fetch）统一进 emitter，SDK 内部多消费者（上报/本地存储/调试面板）。
- 识别要点：能说清"错误指纹 = 堆栈前 N 帧 + 消息模板（参数归一化）"，聚合 key 设计决定去重质量。

```javascript
// 采集 SDK 策略管线（源码级简化）
const agg = new Map();                        // 指纹 → { count, first, last, sample }
function fingerprint(err) {
  const stack = err.stack?.split('\n').slice(0, 4).join('|') ?? 'no-stack';
  return `${stack}::${err.message.replace(/\d+/g, 'N')}`;   // 参数归一化
}
function consume(err) {
  const fp = fingerprint(err);
  const item = agg.get(fp) ?? agg.set(fp, { count: 0, sample: err }).get(fp);
  item.count++;                               // 聚合：窗口内只计数
}
setInterval(flush, 5000);                     // 批量上报聚合结果
function flush() {
  const batch = [...agg.entries()].map(([fp, { count, sample }]) => ({
    fp, count, sample: sampled(sample),       // 采样策略：count>100 时只报 10% 明细
  }));
  agg.clear();
  transport.send(batch);
}
```
