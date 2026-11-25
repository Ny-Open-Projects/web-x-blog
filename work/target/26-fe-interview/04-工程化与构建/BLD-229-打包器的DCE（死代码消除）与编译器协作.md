---
title: [BLD-229] 死代码消除（DCE）与编译器怎么协作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-229：DCE 协作怎么运作？
**答**：
- 分工：打包器做「模块级摇除」（未引用模块整体不打包——SCN-BLD-203），压缩器做「语句级 DCE」（不可达代码/常量条件分支删除）。
- 常量传播协作：Define（__DEV__）→ 压缩器识别 `if (false)` 分支删除——Define 的值必须是字面量（压缩器才能判定）。
- DCE 失效模式：副作用不确定的调用（getter/Proxy）、动态特征（eval/with）、跨模块的可变导出（编译器保守不删）。
- 编译指令协作：/*#__PURE__*/ / /*#__NO_SIDE_EFFECTS__*/ 注释辅助压缩器判定——库作者的义务。
- 追问钩子：为什么「Define 的值必须是字面量」——`if (__DEV__)` 中 __DEV__ 若是复杂表达式，压缩器无法在编译期判定真假，分支保留（体积损失）；Define true/false 字面量 → 压缩器把 if(false) 分支直接删掉——构建 Define 与压缩 DCE 是一对协作机制，字面量是握手的契约。

```javascript
// Define + DCE 协作
new DefinePlugin({ __DEV__: JSON.stringify(false) })  // 字面量！
// 产物: if (false) { /* 整段被压缩器删除 */ }
// 库作者的 PURE 声明
export const result = /*#__PURE__*/ computeHeavy();   // 未使用可删
```
