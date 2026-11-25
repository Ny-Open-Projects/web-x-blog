---
title: [HW-133] 手写 idleThrottle——低优先级事件（resize/observers）空闲时才处理，积压合并到一次
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-133：手写 idleThrottle——低优先级事件（resize/observers）空闲时才处理，积压合并到一次
**答**：resize/媒体查询/observer 回调这类"不必即时"的事件：不防抖（用户可能等很久）也不节流（浪费帧），而是 idle 节流——触发时记"脏"标记，空闲时处理一次，处理时读最新状态（自然合并积压）。

```javascript
function idleThrottle(fn, { timeout = 2000 } = {}) {
  let dirty = false, lastArgs = null;
  const scheduled = () => {
    (window.requestIdleCallback || ((f) => setTimeout(f, 200)))(() => {
      if (!dirty) return;
      dirty = false;
      fn.apply(null, lastArgs);              // 空闲时处理，读最新参数（积压合并）
    }, { timeout });                         // timeout：最迟 2s 必须处理（防无限饿）
  };
  return (...args) => {
    dirty = true; lastArgs = args;           // 每次触发只标记，不排队
    scheduled();
  };
}
// 用法：resize 后重算图表布局（不必逐次 resize 处理，空闲时按最终尺寸一次算完）
const relayout = idleThrottle((w, h) => chart.resize(w, h), { timeout: 1500 });
addEventListener('resize', () => relayout(innerWidth, innerHeight));
// 对比：
// debounce 300ms：固定延迟，网络/机器慢时可能"来不及"
// idleThrottle：立即标记 + 空闲处理 + timeout 兜底 —— 快机器几乎即时，慢机器不卡但最迟 1.5s 内处理
```

**评分点**：
- dirty 标记 + 空闲处理 + 参数覆盖合并（积压一次处理）的模型。
- timeout 兜底防饿死（与纯 rIC 的区别）。
- 与 debounce/rafThrottle 的适用差异说清（低优事件/高优事件/渲染同步事件）。
- 降级链（无 rIC 用 setTimeout 模拟）。
