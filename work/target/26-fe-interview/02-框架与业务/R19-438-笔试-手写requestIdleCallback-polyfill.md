---
title: [R19-438] 笔试：手写 requestIdleCallback polyfill（帧对齐版）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## R19-438：笔试：手写 requestIdleCallback polyfill

**答**：实现 requestIdleCallback 的降级实现：① 无原生 API（Safari）时基于 rAF + 帧预算模拟；② 每帧计算空闲时间（16.7ms - 本帧已用时），>deadline 才执行回调；③ timeRemaining() 语义对齐；④ timeout 支持（超时强制执行——用 rAF 计数）；⑤ cancel。写出实现。

```javascript
const rIC = typeof requestIdleCallback === 'function'
  ? requestIdleCallback
  : function (cb, { timeout } = {}) {
      let start = performance.now(), id = ++ricId, cancelled = false;
      const tasks = ricTasks;
      function frame(now) {
        if (cancelled) return;
        // 空闲判定: 距帧开始 <14ms 剩余 → 执行
        const elapsed = now - frameStartRef.current;
        const remaining = 16.7 - elapsed;
        if (remaining > 1 || (timeout && now - start >= timeout)) {
          const deadlineObj = { timeRemaining: () => Math.max(0, remaining), didTimeout: !!timeout && now - start >= timeout };
          const next = cb(deadlineObj);
          if (typeof next === 'function') tasks.set(id, next);   // 支持返回续跑
          return;
        }
        requestAnimationFrame(frame);                 // 本帧不空闲, 下帧再试
      }
      requestAnimationFrame(frame);
      tasks.set(id, () => {});                        // 注册
      return id;
    };

let ricId = 0;
const ricTasks = new Map();
const frameStartRef = { current: 0 };
requestAnimationFrame(function trackFrame(now) {
  frameStartRef.current = now;
  requestAnimationFrame(trackFrame);
});

function cancelIdleCallbackShim(id) { ricTasks.delete(id); }
```

**评分点**：
- rAF 帧预算模拟（16.7ms 内的空闲窗口判定）
- timeRemaining 语义对齐 + didTimeout
- timeout 强制执行兜底
- 与原生实现的差异认知（原生有空闲窗口的精确信号）
