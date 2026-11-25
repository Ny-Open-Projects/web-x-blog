---
title: [R19-370] 并发渲染边界：Effect 双执行与 StrictMode 语义
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## R19-370：并发渲染边界：Effect 双执行与 StrictMode 语义

**答**：
- StrictMode 双执行：mount → unmount → mount 模拟——暴露「cleanup 缺失」的副作用（订阅未清、请求未 abort）；并发特性要求 effect 幂等
- 并发渲染的 effect 语义：渲染可丢弃（被高优打断的渲染不执行 effect）——「在 render 里发起副作用」（fetch in render）在并发下必然出 bug
- effect 与外部系统对齐原则：effect 是「同步 React 状态到外部系统」的通道——事件处理器能做的不进 effect（点击上报放 handler）
- 双执行适配清单：订阅清理、AbortController、乐观操作可逆、动画可取消——「写不出幂等 effect」说明状态设计有问题
- React 19 的 ref callback cleanup 与 strict mode 配合：ref 挂卸也双执行——ref 里建监听必须配 cleanup

```jsx
useEffect(() => {
  const ctrl = new AbortController();
  fetch(url, { signal: ctrl.signal }).then(setData).catch(ignoredIfAborted);
  return () => ctrl.abort();        // 双执行下必须 cleanup
}, [url]);
// StrictMode: mount → cleanup → mount — 无 cleanup 则第一次请求泄漏
```
