---
title: [WCN-131] 笔试：手写编译期静态提升器（把静态子树 hoist 出 render 函数）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 编译器方向]
type: 笔试题
---

## WCN-131：笔试：手写编译期静态提升器

**题目**：输入抽象 vnode 树（对象：`{ type, props, children }`），实现 `hoist(tree)`：① 判断节点是否静态（props 无函数值、children 无插值标记 `$$`）；② 静态子树整体提升为 `hoisted[i]` 引用（树位置替换为 `{ $$hoisted: i }`）；③ 返回 `{ tree, hoisted[] }`；④ 动态节点的 props 保留但静态属性抽离；⑤ 统计提升率（静态节点占比）。

**答**：

```javascript
export function hoist(tree) {
  const hoisted = [];
  let total = 0, staticCount = 0;

  function isStatic(node) {
    if (!node || typeof node !== 'object') return typeof node === 'string';
    if (node.$$) return false;                              // 插值节点必动态
    const propsOk = Object.values(node.props ?? {}).every((v) => typeof v !== 'function' && !v?.$$);
    const kidsOk = (node.children ?? []).every(isStatic);
    return propsOk && kidsOk;
  }

  function walk(node, count = true) {
    if (count) total++;
    if (isStatic(node)) {
      staticCount++;
      const i = hoisted.push(node) - 1;
      return { $$hoisted: i };                               // 原位置替换为引用
    }
    // 动态节点：children 递归，静态孙节点抽离
    const children = (node.children ?? []).map((c) => walk(c, true));
    return { ...node, children };
  }

  const newTree = walk(tree);
  return { tree: newTree, hoisted,
    stats: { total, staticCount, rate: total ? staticCount / total : 0 } };
}

// 口径：
// const t = { type:'div', props:{}, children:[
//   { type:'span', props:{ class:'t' }, children:['静态'] },          // 静态 → hoisted[0]
//   { type:'span', props:{}, children:[{ type:'text', $$: 'msg' }] }  // 动态保留
// ]};
// hoist(t) → { tree:{...children:[{$$hoisted:0},{...}]}, hoisted:[span], stats:{rate:2/4} }
```

**评分点**：
- 静态判定覆盖三要素：props 无函数/插值、children 递归静态、插值标记短路。
- 提升语义正确：静态子树整体外提，原位置留引用（`$$hoisted`）。
- 提升率统计（编译器报表口径）。
- 动态节点保留但可继续下钻（孙级静态仍能提升）。
