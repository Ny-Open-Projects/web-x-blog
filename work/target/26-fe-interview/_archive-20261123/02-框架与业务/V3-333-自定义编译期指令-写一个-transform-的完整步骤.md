---
title: [V3-333] 如何自定义一个编译期指令？完整步骤是什么？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-333：如何自定义一个编译期指令？完整步骤是什么？
**答**：
- 场景：`v-perm="'admin'"` 想在编译期直接生成权限判断代码，而不是运行时指令钩子。
- 步骤一：写 directiveTransform，把 `v-perm` 改写为组件 props（如 `perm`）或编译期表达式，从 node.props 移除原始指令。
- 步骤二：注册进编译配置（vite plugin 的 compilerOptions.directiveTransforms）。
- 步骤三：codegen 阶段该指令变成普通 props 传递，运行时组件内读 `props.perm` 决定渲染。
- 校验与提示：编译期检查表达式合法性，非法时用 context.onError 报编译错误（比运行时静默失败好得多）。
```javascript
const permTransform = (dir, node, context) => {
  const exp = dir.exp // 'admin'
  node.props.push({ type: 6, name: 'perm', value: exp })
  context.helper('withDirectives') // 如需保留部分运行时行为
}
```
