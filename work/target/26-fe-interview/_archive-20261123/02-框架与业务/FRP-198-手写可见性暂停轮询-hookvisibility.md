---
title: [FRP-198] 手写可见性暂停轮询 hook：visibilitychange 与 Interval 的协调？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-198：手写可见性暂停轮询 hook：visibilitychange 与 Interval 的协调？

**答**：
- 需求：页面切到后台时暂停轮询（省电、省请求），回到前台立即恢复并**立刻补一次**最新数据。
- 核心 API：`document.visibilityState`（visible/hidden）+ `visibilitychange` 事件；配合 `document.hasFocus()` 可进一步细化。
- 实现：hidden 时 clearInterval（或暂停标志位），visible 时恢复定时器并立即执行一次；恢复用**防抖**处理频繁切换（移动端切应用边界抖动）。
- 进阶：与 AbortController 组合——隐藏时不仅停轮询，还 abort 在途请求；用 `requestIdleCallback` 让轮询避开关键渲染期。

```javascript
// 简化实现，帮助理解可见性暂停轮询
import { useEffect, useRef } from 'react';

function usePolling(fn, interval, { immediate = true, pauseOnHidden = true } = {}) {
  const timerRef = useRef(null);
  const fnRef = useRef(fn);
  fnRef.current = fn;                          // 保持最新闭包，避免重启轮询

  useEffect(() => {
    let stopped = false;

    function start() {
      if (stopped || timerRef.current) return;
      if (immediate) fnRef.current();          // 恢复时立刻补一次
      timerRef.current = setInterval(() => fnRef.current(), interval);
    }
    function stop() {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }

    start();

    if (pauseOnHidden) {
      // 防抖：频繁切换 tab 不反复启停
      let debounceTimer = null;
      const onVisibility = () => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
          if (document.visibilityState === 'hidden') {
            stop();                             // 隐藏：停轮询
          } else {
            start();                            // 可见：恢复 + 立即刷新
          }
        }, 200);
      };
      document.addEventListener('visibilitychange', onVisibility);
      return () => {
        stopped = true;
        stop();
        clearTimeout(debounceTimer);
        document.removeEventListener('visibilitychange', onVisibility);
      };
    }

    return () => { stopped = true; stop(); };
  }, [interval, immediate, pauseOnHidden]);
}

// 使用：
// usePolling(async () => {
//   const res = await fetch('/api/quotes', { signal: pollAbort.signal });
//   setQuotes(await res.json());
// }, 5000);
// 行为：前台每 5s 拉一次；切后台停；切回前台立即拉一次再进入 5s 节奏

// 与 Vue 的 scope 集成版：
// function usePollingVue(fn, interval) {
//   let timer = null;
//   const run = () => { fn(); };
//   const start = () => { if (!timer) { run(); timer = setInterval(run, interval); } };
//   const stop = () => { clearInterval(timer); timer = null; };
//   start();
//   document.addEventListener('visibilitychange', () =>
//     document.hidden ? stop() : start());
//   onScopeDispose(() => { stop(); /* scope 卸载自动清理（FRP-125） */ });
// }
```
