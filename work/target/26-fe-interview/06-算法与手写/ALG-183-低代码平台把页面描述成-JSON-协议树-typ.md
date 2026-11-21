---
title: [ALG-183] 低代码平台把页面描述成 JSON 协议树（type + props + children，props 里带 `{{state.x}}` 数据绑定）。渲染引擎如何把这棵树变成真实 DOM？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-183：低代码平台把页面描述成 JSON 协议树（type + props + children，props 里带 `{{state.x}}` 数据绑定）。渲染引擎如何把这棵树变成真实 DOM？
**答**：递归三步：① 查物料注册表把 type 映射为组件工厂，未知物料报错（协议校验前置）；② 解析 props 中的 `{{expr}}` 绑定——从状态求值后替换（求值函数由沙箱提供）；③ 递归渲染 children 并 append，形成与协议树同构的组件树。整体 O(节点数 × props 数)。难点延伸：状态更新时按"绑定路径 -> 受影响节点"的索引做最小更新，避免整树重渲。

```javascript
function renderProtocol(node, ctx) {
  const { type, props = {}, children = [] } = node;
  const Component = ctx.registry[type];     // 1. 物料注册表：type => 组件工厂
  if (!Component) throw new Error(`unknown material: ${type}`);
  // 2. 解析数据绑定：'{{state.ok}}' => 从沙箱状态求值
  const resolved = Object.fromEntries(Object.entries(props).map(([k, v]) =>
    [k, typeof v === 'string' && v.startsWith('{{')
      ? ctx.evalExpr(v.slice(2, -2))        // 沙箱内求值，不暴露全局
      : v]));
  const el = Component(resolved);
  // 3. 递归渲染子树
  for (const child of children) el.appendChild(renderProtocol(child, ctx));
  return el;
}
// 协议示例：
// { type: 'Button', props: { text: '{{state.label}}', disabled: '{{!state.ok}}' },
//   children: [{ type: 'Text', props: { value: 'hi' } }] }
```
