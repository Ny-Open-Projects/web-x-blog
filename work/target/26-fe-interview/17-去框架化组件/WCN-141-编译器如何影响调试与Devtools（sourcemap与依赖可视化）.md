---
title: [WCN-141] 编译器如何影响调试体验？sourcemap 策略与依赖可视化工具怎么设计？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-141：编译器如何影响调试体验？sourcemap 与依赖可视化怎么设计？

**答**：
- 核心问题：编译产物与源码的对应关系被打断（一个表达式变成独立 effect），断点/堆栈定位变难；sourcemap 必须做到"表达式级映射"而不仅是行级。
- 工具形态：solid-devtools（依赖图可视化、信号 inspector）、Vue DevTools（vapor 模式适配）、Svelte DevTools（组件树+state inspector）——把"隐式依赖"重新显式化。
- 设计要点一：给每个编译生成的 effect 标注源码位置（`__source: {file, line}`），性能面板与调试器显示真实文件行号。
- 设计要点二：信号面板显示"谁在订阅/最近触发原因"（复用 WCN-098 的调试器思路），解决"为什么渲染了"问题。
- Devtools 与编译器要同版本演进（产物结构变化破坏 inspector），这是编译器框架的长期维护成本。

```javascript
// 编译产物标注源码位置（示意）
renderEffect(() => setText(el, count.value), {
  __source: { file: 'Counter.vue', line: 12, expr: 'count' },
  __name: 'text#12',
});
// DevTools 面板：按 __source 分组展示 effect 与其依赖信号
```
