---
title: [WEB-387] V8 的 Ignition 和 TurboFan 分别是干什么的？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-387：V8 的 Ignition 和 TurboFan 分别是干什么的？
**答**：
- Ignition 解释器：字节码快速启动；TurboFan 优化编译器：热点函数基于类型反馈编译成机器码。
- 去优化（deopt）：假设被打破（类型突变）→ 回退解释器并丢弃优化代码；常见触发：参数类型变化、try-catch 内热点、debugger。
- 性能启示：函数参数与返回值保持类型稳定、避免多态形状（同一函数吃不同对象形状）、不要在关键路径频繁切换。

```javascript
function sum(a, b) { return a + b; }
for (let i = 0; i < 1e5; i++) sum(i, i);   // 热点 → TurboFan 优化（都按数字）
sum('x', 'y');                              // 类型假设打破 → deopt 回 Ignition
console.log('%GetOptimizationStatus 需 --allow-natives-syntax 观察');
// 实践: 一个函数别又吃数字又吃字符串
```
