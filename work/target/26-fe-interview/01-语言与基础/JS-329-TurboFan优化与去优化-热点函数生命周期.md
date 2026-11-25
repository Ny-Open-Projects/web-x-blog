---
title: [JS-329] TurboFan 优化与去优化：热点函数生命周期
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, V8]
type: 面试题
---

## JS-329：TurboFan 优化与去优化：热点函数生命周期

**答**：
- 分层执行：Ignition 解释器（字节码）→ Sparkplug 基线编译（快速）→ Maglev（中档优化）→ TurboFan（激进优化）——函数被反复调用（热点）逐级提升
- TurboFan 基于类型反馈（IC 数据）假设：如「这个参数总是 SMI」编译出无类型检查的机器码；假设被打破 → deopt（去优化），回退解释器并丢弃反馈重新热身
- 常见 deopt 触发：参数类型漂移、delete 属性、修改原型、eval/debugger、try-catch 边界（老版本）、未预料的 arguments 泄漏
- 观测手段：`--trace-opt --trace-deopt`（Node/Chromium 内部 flag）、Node `--allow-natives-syntax` 下 %GetOptimizationStatus；线上只能靠耗时异常推断
- 前端应用：热点循环（游戏物理/数据处理）保持类型稳定、避免在循环中改共享结构——「写稳定的 JS」比「聪明的 JS」快

```javascript
function sum(arr) {
  let s = 0;
  for (const x of arr) s += x;   // arr 全是数字 → TurboFan 假设 double
  return s;
}
sum([1, 2, 3]); // 预热
sum([1, 2, 3]); // 再次调用 → 优化
sum([1, 'a']);  // 类型漂移 → deopt, 函数重新解释执行
```
