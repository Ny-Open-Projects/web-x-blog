---
title: [HW-116] 手写 rAF 融合节流——scroll/pointermove 事件每帧最多一次 + 帧内多次事件合并参数
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-116：手写 rAF 融合节流——scroll/pointermove 事件每帧最多一次 + 帧内多次事件合并参数
**答**：高频事件（scroll/pointermove）的最优节流不是定时器而是 rAF：每帧最多执行一次，且帧内多次触发**合并参数**（如取最后的 scroll 位置 + 标记方向变化），回调拿到的是"这一帧的净状态"。

```javascript
function rafThrottle(fn) {
  let scheduled = false, lastArgs = null, lastThis = null;
  function wrapper(...args) {
    lastArgs = args; lastThis = this;                    // 帧内多次触发：参数被覆盖合并
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(() => {
      scheduled = false;
      fn.apply(lastThis, lastArgs);                      // 每帧最多一次
      lastArgs = null;
    });
  }
  wrapper.cancel = () => { scheduled = false; lastArgs = null; };
  return wrapper;
}
// 用法：滚动进度条 —— 帧内可能触发 3 次 scroll，回调只拿最终位置
const updateProgress = rafThrottle((scrollTop) => {
  bar.style.width = (scrollTop / max) * 100 + '%';
});
container.addEventListener('scroll', () => updateProgress(container.scrollTop), { passive: true });
// 对比定时器节流：rAF 版与渲染同步（不产生"回调在两帧之间"的错位），且无 4ms 钳制
```

**评分点**：
- rAF 而非定时器（与渲染同步、无钳制）是本题核心认知。
- 帧内参数合并（lastArgs 覆盖）语义：回调拿净状态。
- passive: true 配合；cancel 清理。
- 能对比定时器节流的错位问题。
