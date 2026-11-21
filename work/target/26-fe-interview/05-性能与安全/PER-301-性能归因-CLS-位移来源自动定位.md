---
title: [PER-301] CLS 的位移来源如何自动定位？sources 数组之外还有哪些手段？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-301：CLS 的位移来源如何自动定位？sources 数组之外还有哪些手段？

**答**：
- sources 数组：layout-shift entry 的 sources[i] 含 node、previousRect/currentRect（位移前后矩形）——能直接算位移方向与距离，是第一手证据。注意 node 在上报时要序列化成语义标识（tag+class+data-test-id），不能直接传 DOM。
- DevTools 定位：Performance 面板开启 Layout Shift Regions（渲染时高亮位移区域）+ Experience 轨道的紫色 CLS 块，点击块看发生时刻的 DOM 与帧截图；Rendering 面板的 Paint flashing 辅助。
- 常见根因速查表：无尺寸媒体（img/iframe/视频）、动态插入内容（公告条/广告/推荐位）、字体交换（FOUT）、异步数据把已有内容顶下去、骨架屏与真内容尺寸不一致、动画用 top/left。
- 自动归因落地：RUM 把 sources + previousRect/currentRect + 发生时间（相对 FCP）一起上报，服务端按"元素语义标识 + 位移模式（高度变化/插入/字体）"聚类出 Top 抖动元素排行，直接生成修复工单。

```javascript
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    if (e.hadRecentInput || e.value < 0.02) continue;
    report({
      type: 'cls-source',
      value: +e.value.toFixed(3),
      at: Math.round(e.startTime),                     // 相对导航开始的位移时刻
      sources: (e.sources || []).map((s) => ({
        el: s.node ? `${s.node.tagName}.${String(s.node.className).split(' ')[0]}` : 'unknown',
        before: s.previousRect && { w: s.previousRect.width, h: s.previousRect.height, y: s.previousRect.y },
        after:  s.currentRect  && { w: s.currentRect.width,  h: s.currentRect.height,  y: s.currentRect.y },
      })),
    });
  }
}).observe({ type: 'layout-shift', buffered: true });
// 判读：高度变化 => 无尺寸媒体；y 突增 => 上方插入了内容；整批文本位移 => 字体交换
```
