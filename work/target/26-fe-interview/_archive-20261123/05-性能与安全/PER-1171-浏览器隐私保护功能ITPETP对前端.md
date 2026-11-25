---
title: [PER-1171] 浏览器隐私保护功能（ITP/ETP）对前端埋点的实际影响与对策
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1171：浏览器隐私保护功能（ITP/ETP）对前端埋点的实际影响与对策

**答**：
- ITP（Safari）：智能防追踪——三方 cookie 清零、7 天后第一方 cookie 过期（有交互延长）、CDR 削减 document.cookie。
- ETP（Firefox）与 Chrome 跟踪保护：拦截已知追踪域请求。
- 对策：埋点改用第一方域收集（自有域名 CNAME 或同域上报）、缩短归因窗口预期、不依赖跨站 ID。
- 度量：按浏览器分桶看采集完整率，Safari 明显偏低属预期，校准大盘口径。

```javascript
// 浏览器采集完整率监控
function captureRate(rum) {
  const byUA = {};
  for (const r of rum) {
    const b = browserFamily(r.ua);
    byUA[b] ??= { sessions: 0, events: 0 };
    byUA[b].sessions += r.sessions; byUA[b].events += r.events;
  }
  return Object.fromEntries(Object.entries(byUA)
    .map(([b, v]) => [b, +(v.events / v.sessions).toFixed(1) + ' events/session']));
}
// Safari 偏低 -> 检查上报是否走了三方域被拦截
```
