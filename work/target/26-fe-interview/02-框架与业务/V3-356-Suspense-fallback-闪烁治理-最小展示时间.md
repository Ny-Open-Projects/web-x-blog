---
title: [V3-356] Suspense fallback 闪烁怎么治理？最小展示时间怎么实现？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-356：Suspense fallback 闪烁怎么治理？最小展示时间怎么实现？
**答**：
- 闪烁场景：异步依赖 30ms 就 resolve，fallback 一闪而过反而比无 fallback 更跳；或超时 fallback 出现后 1s 内 resolve 又切回。
- 方案一：数据层 minDelay——异步依赖统一包 `withMinDelay(promise, 200)`，保证最快也 200ms 后 resolve，fallback 稳定展示。
- 方案二：延迟 fallback 出现——数据层加 `race([p, timeout(100)])`，超时才进入 Suspense pending，避免短加载也展示骨架。
- 方案三：fallback 用「可中断的骨架屏」组件，配合淡入淡出（与 Transition 组合）掩盖切换。
- 原则：闪烁是「时序体验」问题，优先在数据层控制节奏，而不是给 Suspense 打补丁。
```javascript
const withMinDelay = (p, ms = 200) => Promise.all([p, new Promise(r => setTimeout(r, ms))])
const withLateFallback = (p, ms = 100) => Promise.race([p, new Promise((_, rej) => setTimeout(() => rej(new FallbackSignal()), ms))])
```
