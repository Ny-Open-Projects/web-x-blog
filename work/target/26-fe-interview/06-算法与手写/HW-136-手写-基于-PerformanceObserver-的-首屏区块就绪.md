---
title: [HW-136] 手写区块级就绪指标——首屏多个区块（主内容/推荐/评论）各自的渲染完成时间？
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：整页 LCP 只有一个值，但首屏多区块的业务关注"每块何时可见"。实现：每个区块挂载后用 rAF 确认"已 paint"（rAF 在 paint 后执行上一帧确认），打 mark + measure；区块就绪 = DOM 挂载 + paint 完成，并上报区块级指标（分区块 LCP 化）。

```javascript
function blockReady(name, el) {
  return new Promise((resolve) => {
    requestAnimationFrame(() => {                        // 第一帧：样式/layout 已算
      requestAnimationFrame(() => {                      // 第二帧：确认上一帧已完成 paint
        performance.mark(`block:${name}:painted`);
        resolve(Math.round(performance.now()));
      });
    });
  });
}
async function trackBlocks(defs) {
  const results = await Promise.all(
    Object.entries(defs).map(async ([name, el]) => ({ name, paintedAt: await blockReady(name, el) })),
  );
  report({ type: 'blocks-ready', blocks: results.sort((a, b) => a.paintedAt - b.paintedAt) });
  return results;
}
// 用法（React 示意）：主内容 useEffect 里 trackBlocks({ main, recs, comments })
// 输出示例：[{main: 1240}, {recs: 1890}, {comments: 2430}]
// 判读：comments 慢 1.2s → 该区块数据接口或渲染是瓶颈；可按区块单独优化与验收
// 双 rAF 的原因：单 rAF 回调在本帧 paint 前执行，双 rAF 才能确认"上一帧真的画了"
```

**评分点**：
- 双 rAF 确认 paint 完成的时序原理说清——本题核心考点。
- 区块级指标（分区块 paintedAt）填补整页 LCP 的粒度缺口。
- 排序输出便于定位最慢区块。
- 与业务首屏指标（PER-231）的关系（区块级细分）。
