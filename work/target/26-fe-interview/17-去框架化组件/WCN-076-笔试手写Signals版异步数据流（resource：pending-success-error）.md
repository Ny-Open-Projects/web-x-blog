---
title: [WCN-076] 笔试：手写 Signals 版异步 Resource（pending / success / error 状态机）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-076：笔试：手写 Signals 版异步 Resource

**题目**：实现 `createResource(fetcher)`：① fetcher 是 `(sourceSignal) => Promise`；② 状态为 `{ loading, data, error }` 三个独立 signal；③ source 变化自动重新请求（旧请求作废：AbortController + seq 对比）；④ 手动 `refetch()`；⑤ 返回 `{ loading(), data(), error(), refetch(), dispose() }`。

**答**：

```javascript
import { createSignal, effect } from './mini.js';

export function createResource(fetcher, source) {
  const [loading, setLoading] = createSignal(false);
  const [data, setData] = createSignal(null);
  const [error, setError] = createSignal(null);
  let ac, seq = 0;

  async function run(signalValue) {
    const mySeq = ++seq;
    ac?.abort(); ac = new AbortController();      // 旧请求作废
    setLoading(true); setError(null);
    try {
      const res = await fetcher(signalValue, ac.signal);
      if (mySeq !== seq) return;                  // 过期响应丢弃（竞态）
      setData(res); setLoading(false);
    } catch (e) {
      if (mySeq !== seq || e.name === 'AbortError') return;
      setError(e); setLoading(false);
    }
  }

  const stop = effect(() => { if (source) run(source()); else run(undefined); });
  return {
    loading, data, error,
    refetch() { run(source?.() ?? null); },
    dispose() { stop(); ac?.abort(); },
  };
}

// 口径：
// const kw = createSignal('');
// const user = createResource((k, signal) =>
//   fetch(`/api/search?q=${k}`, { signal }).then((r) => r.json()), kw);
// effect(() => console.log(user.loading() ? '加载中' : user.data()));
```

**评分点**：
- seq + AbortController 双保险处理竞态（过期响应与中断都覆盖）。
- 三个状态独立 signal，消费方可分别订阅（细粒度）。
- 请求重入自动 abort；错误态复位时机正确（新请求开始时清 error）。
- effect 生命周期：dispose 停止追踪并中断请求。
