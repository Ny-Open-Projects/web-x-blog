---
title: [BLD-121] 手写 Babel 插件实战一：把可选链 `a?.b?.c` 降级的简化版实现。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 笔试题, 18]
type: 笔试题
---

## BLD-121：手写 Babel 插件实战一：把可选链 `a?.b?.c` 降级的简化版实现。
**答**：
- 思路：命中 `OptionalMemberExpression` 时生成等价的条件访问表达式；外层（最左）自下而上构造 `a == null ? void 0 : a.b` 形态，链上每一级都判空。
- 简化版实现策略：递归处理 `object`（若也是 optional 则先生成子表达式），再产出 `t.conditionalExpression(t.binaryExpression('==', obj, t.nullLiteral()), t.unaryExpression('void', t.numericLiteral(0)), t.memberExpression(obj, prop))`。
- 与官方 `@babel/plugin-proposal-optional-chaining` 差距：官方还要处理 `?.()` 可选调用、赋值目标限制、避免对象表达式重复求值（需要引入临时变量 `ref`）——面试说清"简化版未处理副作用"即合格。
- 排查技巧：`npx babel file.js --plugins ./my-plugin.js` 直接看输出，配 `ast: true` 看树。

```javascript
// babel-plugin-mini-optional-chaining.js：可选链降级简化版
module.exports = ({ types: t }) => ({
  name: 'mini-optional-chaining',
  visitor: {
    OptionalMemberExpression(path) {
      // a?.b?.c  →  递归到最左对象，再逐级包条件表达式
      const build = (node) => {
        if (!node.object.type.startsWith('Optional')) {
          return node.object;                       // 普通对象：直接作为主体
        }
        const sub = build(node.object);
        // 子链：sub?.x → (sub == null ? void 0 : sub.x)
        return t.conditionalExpression(
          t.binaryExpression('==', t.cloneNode(sub), t.nullLiteral()),
          t.unaryExpression('void', t.numericLiteral(0)),
          t.memberExpression(t.cloneNode(sub), node.object.property)
        );
      };
      const obj = build(path.node);
      // 最终本级：obj?.prop
      path.replaceWith(
        t.conditionalExpression(
          t.binaryExpression('==', t.cloneNode(obj), t.nullLiteral()),
          t.unaryExpression('void', t.numericLiteral(0)),
          t.memberExpression(t.cloneNode(obj), path.node.property)
        )
      );
    },
  },
});
// 输入： const city = user?.address?.city;
// 输出： var city = user == null ? void 0 : (user.address == null ? void 0 : user.address.city);
// 已知局限（面试必说）：a?.b 是对象字面量表达式时会重复求值，官方版用 _ref 临时变量解决
```
