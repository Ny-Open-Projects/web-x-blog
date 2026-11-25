---
title: [WCN-658] 笔试：实现编译器的静态提升 pass（遍历 AST 标记可提升节点并提取到模块级）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-658：笔试：实现编译器的静态提升 pass（遍历 AST 标记可提升节点并提取到模块级）

**答**：
- 需求：实现 hoistStatic(ast)：遍历节点树，若节点及其子树均无动态绑定（isStatic）则打上 hoisted 标记并收集到 hoists 列表；返回 { ast, hoists }。
- 思路：后序遍历（先子节点）；节点 isStatic = 自身无动态 props 且所有子节点 isStatic；静态节点收集且从父节点替换引用。
- 边界：根节点是否提升由策略决定（通常不提升根）；文本节点总是静态；动态节点不提升。

```javascript
function hoistStatic(root) {
  const hoists = [];
  function walk(node, isRoot = false) {
    if (node.type === 'text') return true;
    const childrenStatic = (node.children || []).map(c => walk(c)).every(Boolean);
    const selfStatic = !(node.dynamicProps?.length) && !(node.dynamicText);
    const isStatic = selfStatic && childrenStatic;
    if (isStatic && !isRoot) {
      node.hoisted = true;
      hoists.push(node);
    }
    return isStatic;
  }
  walk(root, true);
  return { ast: root, hoists };
}
const ast = {
  type: 'element', tag: 'div', children: [
    { type: 'element', tag: 'p', children: [{ type: 'text', value: 'hi' }] },
    { type: 'element', tag: 'b', dynamicText: true, children: [] },
  ],
};
const { hoists } = hoistStatic(ast);
console.log(hoists.map(n => n.tag)); // ['p']：静态 p 被提升，动态 b 不被提升
```

**评分点**：
- 后序遍历，先判定子树再判定自身（顺序正确）。
- isStatic 综合自身动态属性与子树状态（判断准确）。
- 静态节点收集到 hoists 并打标，动态节点保留在原树。
- 根节点不提升的策略处理（避免误提升整个模板）。
