---
title: [OPT-195] CLS 达标专项的"尺寸预留全清单"包含哪些项？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-195：CLS 达标专项的"尺寸预留全清单"包含哪些项？

**答**：
- 全清单（按线上 CLS 来源频率排序）：①图片/视频无宽高 → 全部补 width/height 或 aspect-ratio；②动态内容插入（banner/推荐/评论懒加载）→ 容器 min-height 预留；③web 字体替换（FOUT）→ size-adjust/fallback 度量对齐；④广告 iframe → 外层固定尺寸；⑤骨架屏与真实内容不一致 → 尺寸契约（OPT-124）；⑥异步弹层（顶部通知条）→ 预留 space 或用 overlay 不占位。
- 检测定位：用 `Layout Instability` API 上报每次位移的 sources（哪个节点位移了），比只看总分有效得多。
- 验收口径：CLS P75 ≤ 0.1（CWV）；单次位移 > 0.05 即单点治理。
- 回归防护：Storybook/组件库给"无 CLS"测试（Chromium layout instability 探测进 CI）。

```javascript
// 一一对应：CLS 来源自动归因上报（sources 指出具体节点）
new PerformanceObserver(list => {
  for (const entry of list.getEntries()) {
    if (entry.hadRecentInput) continue;          // 用户输入后 500ms 内的位移不计
    const sources = (entry.sources || []).map(s => ({
      node: s.node
        ? `${s.node.tagName}.${(s.node.className || '').toString().split(' ')[0]}`
        : 'unknown',
      prevRect: { t: Math.round(s.previousRect?.top ?? 0), h: s.previousRect?.height },
      currRect: { t: Math.round(s.currentRect?.top ?? 0), h: s.currentRect?.height },
    }));
    navigator.sendBeacon('/api/perf/cls-source', JSON.stringify({
      value: +entry.value.toFixed(4), sources: sources.slice(0, 3), route: location.pathname,
    }));
  }
}).observe({ type: 'layout-shift', buffered: true });

// 修复模式对照（全清单的代码面）：
// 1. 图片：<img width height> 或 CSS aspect-ratio
// 2. 动态区块：.recommend { min-height: 320px; }  ← 先占位再填内容
// 3. 字体：@font-face { size-adjust: 98%; ascent-override: 90%; } 对齐回退字体度量
// 4. 广告位：.ad-slot { height: 250px; contain: strict; }
// 5. 通知条：position: fixed/overlay，或 body { padding-top 预留 }
```
