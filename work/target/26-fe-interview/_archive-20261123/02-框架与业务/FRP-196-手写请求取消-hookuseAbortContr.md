---
title: [FRP-196] 手写请求取消 hook：useAbortController 如何做到自动清理与竞态防护？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-196：手写请求取消 hook：useAbortController 如何做到自动清理与竞态防护？

**答**：
- 两个目标：**组件卸载时 abort 进行中请求**（防止 setState 到已卸载组件）、**新请求发起时 abort 旧请求**（竞态防护：慢的旧响应不能覆盖新结果）。
- 实现：用 ref 保存当前 AbortController，每次 effect 重新执行前 abort 上一个；cleanup 里 abort 当前——AbortController 被 abort 后 fetch 以 AbortError reject，需 catch 忽略。
- signal 一路透传给 fetch；配合 `signal.aborted` 检查可以在响应处理前再守一道。
- 变体：手动模式（返回 abort 函数给用户触发）与自动模式（effect 依赖变化即取消）。

```javascript
// 简化实现，帮助理解 useAbortController
import { useEffect, useRef, useState } from 'react';

function useFetchWithAbort(url) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const controllerRef = useRef(null);

  useEffect(() => {
    // 1. 竞态防护：新请求前取消旧请求
    controllerRef.current?.abort();
    const controller = new AbortController();
    controllerRef.current = controller;
    setData(null); setError(null);

    fetch(url, { signal: controller.signal })   // 2. signal 透传给 fetch
      .then(r => r.json())
      .then(json => {
        if (controller.signal.aborted) return;  // 3. 双保险：abort 后不再写 state
        setData(json);
      })
      .catch(e => {
        if (e.name === 'AbortError') return;    // 4. 取消不是错误：静默
        setError(e);
      });

    // 5. 卸载/依赖变化：自动 abort
    return () => controller.abort();
  }, [url]);

  return { data, error, abort: () => controllerRef.current?.abort() };
}

// —— 底层变体：只提供 controller 管理 ——
function useAbortController() {
  const ref = useRef(null);
  const run = (fetchFn) => {
    ref.current?.abort();
    const c = new AbortController();
    ref.current = c;
    return fetchFn(c.signal);                    // 用户自行传入 signal
  };
  useEffect(() => () => ref.current?.abort(), []);  // 卸载清理
  return { run, abort: () => ref.current?.abort() };
}

// 时序演示（竞态场景）：
// t0 输入 'a' -> 请求 A（3s 响应）
// t1 输入 'ab' -> abort A！请求 B
// t2 A 的响应到达 -> AbortError -> 被 catch 静默 —— 不会用 'a' 的结果覆盖
// t3 B 返回 -> 上屏
// 没有 abort 的版本：A 比 B 后到 -> 列表显示 'a' 的结果 —— 经典竞态 bug
```
