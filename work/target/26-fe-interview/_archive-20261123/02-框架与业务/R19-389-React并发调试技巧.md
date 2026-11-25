---
title: [R19-389] React 并发调试技巧：从现象到根因的工具链
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## R19-389：React 并发调试技巧：从现象到根因的工具链

**答**：
- 现象→根因映射：输入卡顿（渲染在输入路径）→ Profiler 看输入事件里的渲染树；更新闪烁（重复提交）→ Effect 双执行/依赖不稳；状态撕裂 → 非 useSyncExternalStore 的外部订阅
- StrictMode 作为探针：开发期双执行暴露非幂等 effect——「生产不闪 dev 闪」的问题在 strict 下必然复现
- 时间线工具：React DevTools 的 profiler recording + 浏览器 Performance 联动——「Transition 被打断」可以看到两轮渲染与丢弃
- console 诊断：React 19 的 hydration diff、use 指令的 promise 重复警告——读懂框架警告比猜快
- 自建探针：Profiler API + 性能 mark——把「组件渲染」放进自己的监控体系（生产可采样）

```text
调试决策树:
  输入延迟?  → 检查 transition 包裹输入 / 大过滤在渲染路径
  请求重复?  → StrictMode 双执行 / deps 不稳(每次新引用)
  白屏闪?    → hydration mismatch / Suspense fallback 闪烁
  偶发不一致? → 外部 store 未用 useSyncExternalStore (tearing)
```
