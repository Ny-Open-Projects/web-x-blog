---
title: [PER-356] 长会话（SPA 挂一整天）的 Web Vitals 漂移：指标随会话时间劣化的发现与治理？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-356：长会话（SPA 挂一整天）的 Web Vitals 漂移：指标随会话时间劣化的发现与治理？

**答**：
- 漂移现象：SPA 会话越长指标越差——INP 从 150ms 涨到 500ms+，交互响应逐步变钝。根因通常是内存泄漏累积（GC 频繁 + 堆大标记慢，PER-273）、监听器堆积、缓存无上限。
- 发现手段：RUM 上报带"会话时长分桶"（<5min / 5~30min / 30min~2h / >2h），按桶看 INP/LCP 分布——若长桶显著劣化即漂移实锤；结合 heap baseline 采样（PER-271）的会话内趋势。
- 治理手段：① 修泄漏（根源，PER-263~275 全套）；② 缓解——会话内定期"轻量复位"（清理全局缓存、重置监听器计数）、关键页面软刷新提示（挂机超 2h 提示刷新）；③ 架构——高交互页面考虑多页面应用形态或 iframe 隔离（页面级内存随导航释放）。
- 验收：长会话分桶的 INP p75 与短会话差距收敛到 20% 以内；heap baseline 无台阶上涨。

```javascript
// 会话时长分桶上报
const sessionStart = Date.now();
function sessionBucket() {
  const min = (Date.now() - sessionStart) / 60000;
  return min < 5 ? 'a' : min < 30 ? 'b' : min < 120 ? 'c' : 'd';
}
report({ type: 'INP', value: worstInp, sessionBucket: sessionBucket() });
// 看板：sessionBucket × INP p75 —— d 桶显著高于 a 桶 => 会话漂移
// 轻量复位（缓解）：每 30min 清理全局缓存与监听器计数
setInterval(() => { globalCache.clear(); auditListenerCount(); }, 30 * 60000);
```
