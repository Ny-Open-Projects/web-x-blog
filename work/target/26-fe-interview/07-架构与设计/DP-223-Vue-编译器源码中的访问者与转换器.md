---
title: [DP-223] 源码识别：Vue/Svelte 编译器源码中的访问者与转换器？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-223：源码识别：Vue/Svelte 编译器源码中的访问者与转换器？
**答**：
- 访问者模式：Vue compiler-core 的 transform 阶段——nodeTransforms 数组遍历 AST，每个 transform 是 visitor（enter/exit 双钩子）；Babel 的 visitor 同构。
- 管道+职责链：模板 → parse AST → transform（一串 visitor 顺序应用：transformOnce/For/Model/VBind…）→ generate 代码，各 transform 只关心自己的节点类型。
- 组合模式：AST 本身是组合模式（node.children 递归），任何编译器都绕不开。
- 识别要点：能写出 mini visitor（enter/exit），并解释 exit 时机（子节点处理完后自底向上，transformText 合并静态文本靠它）。

```javascript
// Vue 编译器 transform（源码级简化）
function transform(ast, nodeTransforms) {
  const context = { helpers: new Set(), replaceNode(n) { /* … */ } };
  function traverse(node, parent) {
    if (node.type === NodeTypes.ELEMENT) {
      for (const t of nodeTransforms) t.enter?.(node, context);   // 自顶向下
      node.children?.forEach(c => traverse(c, node));
      for (const t of nodeTransforms) t.exit?.(node, context);    // 自底向上（exit）
    }
  }
  traverse(ast, null);
  return context;
}
// visitor 示例：识别 v-if
const transformIf = {
  enter(node, ctx) {
    const dir = node.props.find(p => p.name === 'if');
    if (dir) ctx.replaceNode(createIfNode(node, dir.exp));        // IF → 结构化节点
  },
};
// generate：遍历最终 AST 输出 render 函数代码（`_createElementVNode("div", null, ...)`）
```
