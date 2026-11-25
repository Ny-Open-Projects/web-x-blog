---
title: [V3-453] Vue 编译器三段式：parse → transform → generate 的职责边界
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-453：Vue 编译器三段式：parse → transform → generate 的职责边界

**答**：
- parse 阶段：tokenizer 切 token → 构造 AST（ElementNode/TextNode/InterpolationNode/CommentNode），只关心「结构与语法」，不关心优化——输出带 source 定位（loc）的原始 AST
- transform 阶段：深度优先遍历 AST，每个 transform 插件做「标记与改写」——patchFlags 注入、静态提升、预字符串化、事件缓存、v-for/v-if 结构化（NodeTypes 扩展），输出带优化元信息的 AST
- generate 阶段：AST → 渲染函数代码字符串（含 sourcemap 生成），只负责「按节点类型拼代码」，不做语义判断——三段解耦让 Babel/Vapor/小程序等后端可替换
- 为什么分三段：优化策略（transform）可以独立演进（Vapor 模式换 transform 而不换 parse）；错误定位靠 parse 的 loc 贯穿全链
- 面试表达：画出「template → AST(结构) → AST+标记(优化) → code(产物)」的四格图，标注每段输入输出

```text
template
  → parse:    AST { type: ElementNode, loc, props, children }
  → transform: AST + patchFlag + hoisted + cached handlers
  → generate:  function render() { ... _createVNode("div", ...) }
```
