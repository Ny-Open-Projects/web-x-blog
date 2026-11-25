---
title: [RBL-594] Tree Shaking 的副作用判定：从 /*@__PURE__*/ 到模块级 sideEffects
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-594：Tree Shaking 的副作用判定：从 /*@__PURE__*/ 到模块级 sideEffects

**答**：
- Tree shaking 的判定链三层：1) **模块级**：package.json `sideEffects: false / ["*.css"]`——整个包/指定文件声明无副作用，未引用模块整体剔除（最粗粒度，收益最大）；2) **语句级**：分析模块顶层语句是否纯（赋值/调用/window 操作视为副作用），DCE 时剔除未使用的纯声明；3) **表达式级**：`/*@__PURE__*/` 注释标记调用表达式可删（用户显式承诺）。
- 「纯」的判定陷阱：getter/setter、Proxy、toString/valueOf 重写、数组的原生方法副作用（`arr.map(fn)` 里 fn 可能乱写）——保守策略是「凡调用皆可疑」，所以 sideEffects 声明权交回包作者（作者最清楚）；构建器的乐观假设 + 包作者的显式声明组合才是安全模型。
- re-export 链的 shaking：`export { a } from './b'` 的中间转发模块未被实际引用时，整条转发链要随真实引用一起收敛——依赖「导出绑定解析」（export 解析到最终源模块与名字），而不是停留在表层模块。
- 保守性来源：JS 的动态性（with/eval/动态访问）让静态分析注定不完备——工程答案不是追求完备，而是「显式注解 + 保守默认 + 诊断提示」（可疑未删的模块给 warn，让用户加 sideEffects）。
- 追问钩子：为什么 `import './polyfill'` 不能被 shake？——无绑定的 import 显式表达「仅为副作用」，声明即意图；而 `import { x } from ...` 未用 x 时的剔除要靠「副作用证明」，两者语义不同——polyfill 包在 sideEffects 里要显式列白名单文件。

```javascript
// 三层 shaking 的判定示意
// 1) 模块级：package.json
// { "sideEffects": ["*.css", "./polyfill.js"] }   // 白名单外的模块未引用即删

// 2) 语句级：顶层语句纯性分类
function classifyTop(stmt) {
  if (stmt.type === 'FunctionDecl' || stmt.type === 'ClassDecl') return 'pure-def';   // 纯声明
  if (stmt.type === 'VarDecl') return allInitPure(stmt) ? 'pure-def' : 'side-effect';
  if (stmt.type === 'ExpressionStmt') return isPureExpr(stmt.expr) ? 'pure-expr' : 'side-effect';
  return 'side-effect';
}
const isPureExpr = (e) =>
  e.type === 'Literal' || e.type === 'Ident' ||
  (e.type === 'Call' && e.pure /* @__PURE__ */ && argsAllPure(e));

// 3) DCE：未引用的纯声明剔除
const used = collectUsedBindings(graph);            // 从入口导出反推
for (const [mod, stmts] of topStatements) {
  kept[mod] = stmts.filter(s =>
    classifyTop(s) !== 'pure-def' && classifyTop(s) !== 'pure-expr'
    || s.bindings.some(b => used.has(mod + ':' + b)));
}
```
