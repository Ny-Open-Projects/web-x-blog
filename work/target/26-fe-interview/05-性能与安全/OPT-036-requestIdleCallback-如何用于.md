---
title: [OPT-036] requestIdleCallback 如何用于低优先级任务调度？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-036：requestIdleCallback 如何用于低优先级任务调度？

**答**：
- `requestIdleCallback` 在浏览器**空闲帧**执行回调，`deadline.timeRemaining()` 告诉你还剩几毫秒，适合埋点上报、日志压缩、预计算等"不做也行"的任务。
- 关键参数 `timeout`：即使一直不空闲，超时后也强制执行，防止低优任务饿死。
- 兼容性：Safari 长期不支持，必须写 polyfill（setTimeout 兜底）。
- 约束：回调中不要做 DOM 修改（可能被下一帧打断导致样式闪烁）、不要做必须及时的任务。

```javascript
// 一一对应：空闲调度 + Safari polyfill
function scheduleIdle(fn, timeout = 2000) {
  if ('requestIdleCallback' in window) {
    return requestIdleCallback((deadline) => {
      // 剩余时间大于 10ms 才干活，否则留给下一次空闲
      if (deadline.timeRemaining() > 10 || deadline.didTimeout) fn();
      else scheduleIdle(fn, timeout);
    }, { timeout });
  }
  // polyfill：Safari 兜底，setTimeout 宏任务近似空闲时机
  return setTimeout(fn, 1);
}

// 用法：空闲时批量上报埋点，不影响首屏与交互
scheduleIdle(() => {
  const queue = takeEventQueue(); // 取走攒下的埋点
  navigator.sendBeacon('/collect', JSON.stringify(queue));
});
```

## 七、框架级与内存优化
