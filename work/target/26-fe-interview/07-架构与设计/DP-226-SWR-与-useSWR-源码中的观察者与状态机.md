---
title: [DP-226] 源码识别：SWR 源码中的观察者与去重策略？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-226：源码识别：SWR 源码中的观察者与去重策略？
**答**:
- 缓存 + 观察者：SWRGlobalState 存 cache Map（key → { data, error, ts }）+ listeners；useSWR 订阅 key，mutate 时广播——与 TanStack Query 同款架构（DP-209），差异在策略。
- 策略集：stale-while-revalidate（先给缓存再静默刷新）、dedupingInterval（窗口内重复请求合并）、revalidateOnFocus（visibility 事件触发）——每条都是可配置策略。
- 状态机：单请求状态机简单（loading→success/error），复杂性在"多请求窗口去重 + 广播"。
- 识别要点：面试能说清"SWR 的 key 即缓存指纹，同 key 并发请求被 dedupe 合并成一次"——两个组件同 key 只发一个请求的原理。

```javascript
// SWR 核心（源码级简化）
const cache = new Map(); const listeners = new Map();
function useSWR(key, fetcher, opts) {
  const { dedupingInterval = 2000, revalidateOnFocus = true } = opts;
  useEffect(() => subscribe(key, setStateFromCache), [key]);
  useEffect(() => {                                    // revalidate（可能被去重）
    if (isRecentFetch(key, dedupingInterval)) return;  // 窗口内已有在途请求 → 复用
    startFetch(key, fetcher).finally(() => notify(key));
  }, [key]);
  useEffect(() => {
    if (!revalidateOnFocus) return;
    const onVis = () => document.visibilityState === 'visible' && startFetch(key, fetcher);
    document.addEventListener('visibilitychange', onVis);   // 策略：聚焦重验证
    return () => document.removeEventListener('visibilitychange', onVis);
  }, [key]);
  return cache.get(key);
}
// 同 key 并发：A 组件挂载发起 fetch → 2s 内 B 组件挂载命中 dedupe → 共享同一 promise
```
