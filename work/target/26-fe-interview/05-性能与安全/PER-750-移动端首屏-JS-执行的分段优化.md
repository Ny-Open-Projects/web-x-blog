---
title: [PER-750] 移动端首屏 JS 执行的分段优化：解析-求值-水合三段的预算与手段
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-750：移动端首屏 JS 执行的分段优化：解析-求值-水合三段的预算与手段

**答**：
- 分段模型：**解析/编译**（JS 体积决定，v8 惰性解析缓解）、**求值**（顶层代码执行：初始化、全局副作用）、**水合**（框架 hydrate/事件绑定），移动端首屏 JS 执行预算 150ms（低端 300ms）。
- 各段手段：解析——减小体积/删死代码/避免大 JSON 内联（parse 500KB JSON ≈ 20ms+）；求值——顶层副作用最小化（延迟初始化非首屏模块、避免顶层同步 XHR）；水合——部分水合/渐进水合（首屏交互区先水合）、islands 架构。
- 度量：Performance 面板 script 分解（Evaluate Script self time）、`performance.now()` 打点分段上报（parse 不易直接测，用总执行时长+体积推算）、INP 首次交互。
- 追问钩子：为什么删代码比跑得快的代码收益大？——解析编译成本与体积线性相关，删 40% 代码直接省 40% 解析时间，而微优化只在求值段有效。

```javascript

const jsExecBudget = {
  stages: { parse: '体积线性成本：删代码 > 微优化', eval: '顶层副作用最小化、延迟非首屏 init',
    hydrate: '部分/渐进水合，islands 架构' },
  budget: { flag: 150, lowEnd: 300 },                           // ms
  measure: ['Evaluate Script self time', '分段打点上报', 'INP 首次交互'],
  insight: '删 40% 代码 = 省 40% 解析编译；微优化只作用于求值段，收益天花板低',
};
// 分段打点
performance.mark('js:start');
initCritical();                                                  // 首屏最小集
performance.mark('js:critical-done');
requestIdleCallback(() => initDeferredModules());                // 非首屏延迟
// 水合分片：首屏交互区先 hydrate，其余 idle 分批
```
