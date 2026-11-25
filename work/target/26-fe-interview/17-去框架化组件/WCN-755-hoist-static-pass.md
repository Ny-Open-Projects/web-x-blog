---
title: [WCN-755] 笔试：手写模板编译的静态节点提升（hoistStatic）pass
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-755：笔试：手写模板编译的静态节点提升（hoistStatic）pass

**答**：
- 需求：实现 `hoistStatic(ast)`，ast 为树节点 `{ type:'El'|'Text', tag?, attrs?, children?, dynamic? }`，标记 `dynamic:true` 的节点为动态节点。遍历整棵树：把「整棵子树都不含 dynamic 节点」的节点收集到提升数组并返回占位符 `{ type:'Hoisted', id }`；动态节点原样保留并递归处理其 children。返回 `{ ast, hoisted }`。
- 要点：用后序遍历（先处理 children）判断是否整棵静态；静态 Text 也提升；边界：根节点静态、空 children。

```javascript
function hoistStatic(root) {
  const hoisted = [];
  function walk(node) {
    if (!node) return node;
    if (node.dynamic) {                            // 动态节点：递归处理子树
      if (node.children) node.children = node.children.map(walk);
      return node;
    }
    // 判断子树是否全静态
    let allStatic = !node.dynamic;
    if (node.children) {
      const kids = node.children.map(walk);
      node.children = kids;
      allStatic = kids.every((k) => k.type === 'Hoisted' || k.type === 'Text');
    }
    if (allStatic) {
      hoisted.push(node);
      return { type: 'Hoisted', id: hoisted.length - 1 };
    }
    return node;
  }
  return { ast: walk(root), hoisted };
}
const ast = { type: 'El', tag: 'div', children: [
  { type: 'El', tag: 'span', children: [{ type: 'Text', value: 'hi' }] },
  { type: 'El', tag: 'p', dynamic: true, children: [{ type: 'Text', value: 'x' }] },
] };
const r = hoistStatic(ast);
console.log(r.hoisted.length, r.ast.children[0].type);
```

**评分点**：
- 后序遍历正确判断子树是否全静态。
- 静态子树提升到数组并返回 Hoisted 占位，动态节点保留。
- 动态节点内部仍递归处理，混合子树处理正确。
- 空 children/根节点静态等边界有处理。
