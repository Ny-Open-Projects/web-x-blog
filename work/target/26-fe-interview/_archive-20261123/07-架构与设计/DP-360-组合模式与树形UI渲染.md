---
title: [DP-360] 组合模式实战：树形 UI 与递归渲染
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-360：组合模式：树形 UI

**答**：
- 组合模式核心：叶子与容器统一接口（叶子是「没有 children 的容器」）——树形 UI（菜单/文件树/组织架构）递归渲染的基础
- 实战结构：Node 统一模型 { id, type, children?, render }——渲染函数对叶子/容器无差别递归
- 与 vdom 的关系：vdom 就是组合模式的极致应用（元素树统一接口——React 元素是描述不是实例）
- 实战增强：树的「操作统一化」（expand/collapse 对叶子是 no-op——统一接口让操作无需分型）、路径查找（id 路径递归）
- 深水点：树的「扁平化存储」——大数据树的性能优化（扁平 map + parent 指针替代嵌套 children——渲染层用嵌套，数据层用扁平）

```javascript
// 统一节点渲染 (组合模式)
function renderNode(node, ctx) {
  const children = (node.children ?? []).map((c) => renderNode(c, ctx));
  return node.type === 'leaf'
    ? renderLeaf(node, ctx)
    : renderBranch(node, children, ctx);   // 容器持有 children 渲染结果
}
// 扁平存储:
// const nodes = { id1: { id:'id1', parent:null, label:'src' }, id2: { id:'id2', parent:'id1', label:'a.ts' } }
// childrenOf(id) → Object.values(nodes).filter(n => n.parent === id)
```
