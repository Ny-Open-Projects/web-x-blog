---
title: [WCN-751] 模板编译中的死代码消除（DCE）与分支剪枝怎么做？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-751：模板编译中的死代码消除（DCE）与分支剪枝怎么做？

**答**：
- 结论：编译期对常量条件（如 `if(false)`、`process.env.NODE_ENV`）求值为布尔，把不可能到达的分支节点从 AST 中删除，减小产物体积与运行时判断。
- 对展开的静态条件做传播：常量折叠后用 reachability 分析标记不可达节点并移除；配合 tree-shaking 移除只被死代码引用的导入。
- 追问钩子：运行时才知道的条件（如用户权限）能编译期消除吗？考察「编译期 vs 运行期边界」——不能，只能运行期分支。

```javascript
function foldAndPrune(node, env = { NODE_ENV: 'production' }) {
  if (!node) return node;
  if (node.type === 'Cond' && node.test.type === 'Lit') {
    return node.test.value ? foldAndPrune(node.consequent, env) : foldAndPrune(node.alt, env);
  }
  if (node.type === 'Ident' && node.name.startsWith('process.env.')) {
    return { type: 'Lit', value: env[node.name.slice('process.env.'.length)] };
  }
  if (node.children) node.children = node.children.map((c) => foldAndPrune(c, env)).filter(Boolean);
  return node;
}
const ast = { type: 'Cond', test: { type: 'Lit', value: false },
  consequent: { type: 'El', name: 'dev-only' }, alt: { type: 'El', name: 'prod' } };
console.log(foldAndPrune(ast));   // 仅保留 prod
```
