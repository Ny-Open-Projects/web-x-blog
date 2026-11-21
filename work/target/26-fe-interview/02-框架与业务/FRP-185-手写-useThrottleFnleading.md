---
title: [FRP-185] 手写 useThrottleFn：leading / trailing 双端节流的实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-185：手写 useThrottleFn：leading / trailing 双端节流的实现？

**答**：
- 节流：**时间闸门**——wait 周期内最多执行一次；关键在两个选项：`leading`（周期开始立即执行）与 `trailing`（周期结束后补执行最后一次调用）。
- 纯 leading 实现：`now - last > wait` 就执行——简单但会"丢"最后一次调用（停止触发后尾部的输入被忽略）。
- trailing 的实现：周期内记录最后参数 + 定时器在周期末补发——两者组合才是完整节流（滚动监听必需，否则停在半路的状态丢失）。
- 生命周期同 useDebounceFn：scope 卸载自动清理定时器。

```javascript
// 简化实现，帮助理解 useThrottleFn
function useThrottleFn(fn, wait = 200, trailing = true, leading = true) {
  let timer = null;
  let lastExecTime = 0;       // 上次执行时间
  let pendingArgs = null;

  function exec(args) {
    pendingArgs = null;
    lastExecTime = Date.now();
    fn(...args);
  }

  function throttled(...args) {
    const now = Date.now();
    const elapsed = now - lastExecTime;

    // 周期空闲：leading 放行
    if (elapsed >= wait && leading) {
      exec(args);
      return;
    }
    // 周期内：只记录参数，等 trailing 补发
    pendingArgs = args;
    if (!timer && trailing) {
      const remain = wait - elapsed;
      timer = setTimeout(() => {
        timer = null;
        if (pendingArgs) exec(pendingArgs);   // 周期结束：补执行最后一次
      }, remain);
    }
  }

  throttled.cancel = () => { clearTimeout(timer); timer = null; pendingArgs = null; };
  throttled.flush  = () => { if (timer) { clearTimeout(timer); timer = null; if (pendingArgs) exec(pendingArgs); } };
  if (getCurrentScope()) onScopeDispose(throttled.cancel);

  return throttled;
}

// 行为对照（wait=200，用户连续调用 t=0..900 每 100ms 一次）：
// leading+trailing：执行于 0, 200(补), 400(补), 600(补), 800(补), 1000(补) —— 不丢尾部
// 仅 leading：执行于 0, 200, 400, 600, 800 —— t=900 的最后一次调用被丢弃
// 仅 trailing：执行于 200, 400, ... —— 首次调用要等 200ms（滚动场景开头延迟明显）

// 用法：
// const onScroll = useThrottleFn(() => {
//   updateProgressBar();          // 滚动进度：必须 trailing，否则停在中途进度不准
// }, 100);
// window.addEventListener('scroll', onScroll);
```
