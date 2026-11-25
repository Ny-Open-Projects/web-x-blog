---
title: [MFW-856] 流式渲染怎么度量「壳先到但内容后到」的用户体验（Shell-to-Content）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-856：流式渲染怎么度量「壳先到但内容后到」的用户体验（Shell-to-Content）

**答**：
- 结论：LCP 只看最大内容绘制，无法反映「壳秒开、关键信息晚到」的落差；需 Shell-to-Content（STC）= 关键内容出现时间 − 壳绘制时间。
- 落地：在壳与关键内容节点分别 performance.mark，算差值上报；区分「壳可交互但空」与「内容就绪」两个时刻。
- 追问钩子：STC 大但 LCP 小说明什么？——壳快数据慢，用户盯骨架屏等待，该优化数据层而非渲染层。

```javascript
// 服务端流出壳时打点（客户端渲染侧 mark）
performance.mark('shell');
// 关键内容就绪后打点
performance.mark('hero-content');
performance.measure('stc', 'shell', 'hero-content');
const stc = performance.getEntriesByName('stc')[0].duration;
// 上报
navigator.sendBeacon('/api/vitals', JSON.stringify({ metric: 'stc', value: stc }));

// 解读：LCP=800ms 但 STC=1500ms → 壳快、数据慢
function gradeSTC(stc) {
  if (stc < 200) return 'good';
  if (stc < 800) return 'needs-improvement';
  return 'poor';
}
// 服务端渲染阶段也可用 serverTiming 下发给采集器
res.setHeader('Server-Timing', `stc;dur=${stc};desc="Shell to Content"`);
console.log(gradeSTC(stc));                 // 按档位决定是否优化数据层
```
