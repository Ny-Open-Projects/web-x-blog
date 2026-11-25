---
title: [PER-402] 移动端浏览器的 INP 特调：iOS Safari 与 Android Chrome 的差异点与针对性优化？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-402：iOS Safari 与 Android Chrome 的 INP 差异点与针对性优化？

**答**：
- 差异点清单：① Safari 无 scheduler.yield/postTask——切片降级链必须覆盖（PER-215）；② Safari 的 touch 事件合成与 Chrome 行为细节不同（passive 语义）；③ Safari 的 rAF 在滚动中可能节流，滚动联动逻辑不能依赖 rAF 精确帧；④ iOS 对非活跃标签页的进程冻结更激进（恢复后的指标要重置，PER-226）；⑤ Safari 的 input focus 视口滚动行为影响表单交互体感。
- 针对性优化：切片 util 做全降级（MessageChannel 兜底）；触摸反馈全用 CSS :active（合成器路径，两端一致）；滚动联动用 IntersectionObserver 替代 scroll+rAF（IO 两端语义一致且不占主线程）；表单页用 `interactive-widget=resizes-content` viewport meta 控制键盘行为。
- 度量分端：RUM 按 UA 分端出 INP 分布——Safari 的 p75 通常比 Chrome 差 10~25%（无 yield + 冻结策略），SLO 允许分端阈值或统一但记录偏差。

```css
/* iOS 键盘行为控制（Safari 16.4+） */
<meta name="viewport" content="width=device-width, interactive-widget=resizes-content">
```
```javascript
// 全降级切片 util（Safari 无 scheduler）
const yieldToMain = () => scheduler?.yield?.()
  ?? scheduler?.postTask?.(() => {}, { priority: 'user-visible' })
  ?? new Promise((r) => { const ch = new MessageChannel(); ch.port1.onmessage = r; ch.port2.postMessage(0); });
// 滚动联动：IntersectionObserver 替代 scroll handler（两端一致、不占主线程）
new IntersectionObserver(([e]) => header.classList.toggle('compact', !e.isIntersecting),
  { rootMargin: '-60px' }).observe(sentinel);
```
