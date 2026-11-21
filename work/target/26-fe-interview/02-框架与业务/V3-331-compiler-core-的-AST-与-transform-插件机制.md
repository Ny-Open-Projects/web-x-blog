---
title: [V3-331] @vue/compiler-core 的 AST 与 transform 插件机制是怎样的？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-331：@vue/compiler-core 的 AST 与 transform 插件机制是怎样的？
**答**：
- 编译管线：parse（模板→AST）→ transform（AST→带代码生成信息的 JSAST）→ generate（JSAST→render 代码）。
- AST 节点类型：Root/Element/Text/Comment/Interpolation/CompoundExpression/IF/FOR 等，节点带 `codegenNode` 保存生成阶段的辅助信息。
- transform 插件：`nodeTransforms`（改结构：v-if 转 IF 节点、v-for 转 FOR、静态提升）与 `directiveTransforms`（改指令：v-model/v-on/v-bind 展开）两类数组，按序深度遍历执行。
- 每个插件拿到 `context` 可往 context.helpers 注册运行时 helper、读写作用域变量（v-for 的 item/index 走 pushScope/popScope）。
- 应用：自定义编译期指令 = 写一个 directiveTransform 改写 props 与 helper，这也是 Vue 编译优化（patchFlag 标注）的实现方式。
```javascript
baseCompile(source, {
  nodeTransforms: [transformIf, transformFor, myTransform],
  directiveTransforms: { myDir: (dir, node, context) => { /* 改写 props */ } }
})
```
