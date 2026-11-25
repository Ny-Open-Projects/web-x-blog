---
title: [WCN-856] 编译器如何做「副作用分析」以指导 tree-shaking？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-856：编译器如何做「副作用分析」以指导 tree-shaking？

**答**：
- 结论先行：tree-shaking 的前提是「知道哪些代码删了不影响行为」——副作用分析就是判断语句/表达式是否「有可观察影响」，只有纯的、未被使用的代码才能安全删除。
- 副作用判定：纯表达式（字面量、纯函数调用、无副作用的运算）可删；有副作用（修改外部状态、I/O、DOM 操作、`console`、未知函数调用、`new`、getter）不能删；`package.json` 的 `sideEffects: false` 是给打包器的全局承诺。
- 分析层次：语句级（顶层表达式是否有副作用）、函数级（函数体是否纯）、调用级（被调用函数是否纯——需要跨模块分析/纯函数标注如 `/*#__PURE__*/`）；编译响应式里，`effect()` 调用本身有副作用，不能删。
- 与响应式编译的关系：编译产物里「注册 effect」「绑定事件」「DOM 更新」都有副作用，必须保留；而「静态模板定义」「未使用的 computed」可摇掉——分析要准确标注。
- 保守原则：不确定就当作有副作用（宁可少删不可错删）——误删会导致运行时 bug；用 `/*#__PURE__*/` 注解帮助打包器识别纯调用。
- 追问钩子：面试官会问「为什么有的导出没被用但还在产物里」——答：要么被判定有副作用（如顶层 `new`/注册代码），要么 `sideEffects` 配置不准，或存在动态使用（如 `import * as`、字符串引用）导致无法安全删除。

```javascript
// 副作用分析（简化）：判断表达式是否可安全删除
function hasSideEffect(node, pureCalls = new Set(['Math.max', 'Object.assign'])) {
  switch (node.type) {
    case 'Literal': case 'Identifier': return false;
    case 'Binary': case 'Unary':
      return hasSideEffect(node.left ?? node.arg) || hasSideEffect(node.right);
    case 'Call':
      if (pureCalls.has(node.callee)) return node.args.some(a => hasSideEffect(a));
      return true;                                  // 未知调用 → 保守认为有副作用
    case 'New': case 'Assignment': case 'Update': return true;
    case 'Effect': case 'EventBind': return true;    // 响应式注册是副作用，不能删
    default: return true;
  }
}
function shake(program) {
  return program.filter(stmt => !(stmt.unused && !hasSideEffect(stmt.expr)));
}
console.log(shake([
  { unused: true, expr: { type: 'Binary', left: { type: 'Literal' }, right: { type: 'Literal' } } }, // 删
  { unused: true, expr: { type: 'Effect' } }, // 保留
]));
```
