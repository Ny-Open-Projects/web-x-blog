---
title: [V3-454] Vue 模板 AST 节点体系：NodeTypes 与 loc 定位
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-454：Vue 模板 AST 节点体系：NodeTypes 与 loc 定位

**答**：
- 基础节点类型（NodeTypes 枚举）：ROOT/ELEMENT/TEXT/COMMENT/INTERPOLATION（{{ }}）/SIMPLE_EXPRESSION——文本与表达式是两类：TEXT 是纯静态，INTERPOLATION 内含 SIMPLE_EXPRESSION 子节点
- transform 扩展节点：v-if/v-for 编译后变为 IF/IF_BRANCH/FOR 结构化节点（不再是普通 ELEMENT），SSR 侧另有 ssr 分支标记
- loc 信息：每个节点带 source 定位（start/end offset + line/column）——报错「第几行第几列」、sourcemap 反解、编辑器插件（Volar）都靠它
- 属性表示：DirectiveNode（指令，arg/exp/modifiers）与 AttributeNode（静态属性）分两类——transform 时指令被「消费」转成 props 代码
- 手写解析题要点：嵌套结构用栈（遇到闭合 tag 弹栈回父节点）；自闭合/void 元素（img/br）特殊处理

```text
AST 片段:
{ type: ELEMENT, tag: 'div', loc: {start:{line:1,col:1}},
  props: [ { type: DIRECTIVE, name: 'if', exp: { type: SIMPLE_EXPRESSION, content: 'show' } } ],
  children: [ { type: INTERPOLATION, content: { content: 'msg' } } ] }
```
