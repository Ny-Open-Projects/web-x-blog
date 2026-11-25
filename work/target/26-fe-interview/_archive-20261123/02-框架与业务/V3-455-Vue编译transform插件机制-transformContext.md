---
title: [V3-455] transform 插件机制：transformContext 与 helper 注入
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-455：transform 插件机制：transformContext 与 helper 注入

**答**：
- transform 是插件数组：`transform(ast, { nodeTransforms })`——每个插件 `enter/exit` 两阶段（enter 处理子节点前、exit 处理子节点后），退出阶段才能拿到完整子树信息（如 children 全静态才提升）
- transformContext 提供能力：`helper()` 注册运行时辅助函数（_createElementVNode/_resolveComponent 等，generate 时自动 import）、`replaceNode/removeNode`（v-if 转 IF 节点靠它）、`onExit`（延迟处理）
- helper 注册机制：transform 标记需要哪些 runtime helper → generate 收集去重生成 import 语句——这就是「编译产物顶部的一串 import」的来源
- 插件顺序敏感：v-if/v-for 结构转换必须先于静态提升（先确定结构再谈优化）——数组顺序即执行顺序
- 自定义 transform 的应用：给元素自动埋点属性、i18n 表达式替换、平台专属指令转换（小程序/Taro 定制）

```javascript
// 自定义 transform 骨架
const myTransform = {
  name: 'auto-track',
  enter(node, ctx) {
    if (node.type === NodeTypes.ELEMENT && node.tagType === ElementTypes.COMPONENT)
      ctx.helper('withDirectives');        // 注册 helper
    node.props.push({ /* 注入 track 属性 */ });
  },
  exit(node, ctx) { /* 子树处理完再做的事 */ },
};
// 编译配置: nodeTransforms: [myTransform, ...baseTransforms]
```
