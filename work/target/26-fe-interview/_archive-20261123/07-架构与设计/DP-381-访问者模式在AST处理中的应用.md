---
title: [DP-381] 访问者模式：AST 与编译期处理
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-381：访问者模式：AST 处理

**答**：
- 访问者核心：数据结构稳定（AST 节点类型固定）+ 操作多变（分析/转换/检查）——把操作从数据结构解耦
- 前端实战：Babel 插件（visitor 按 node type 注册——CallExpression 拦截）、ESLint 规则、i18n 扫描（提取模板中的中文）
- 实战结构：visitor: { 'CallExpression(path) {...}' }——traverse 驱动（遍历 AST，命中节点类型调 visitor）
- 访问者的「enter/exit」两阶段：enter 处理进入（改写子节点前）、exit 处理退出（子树完整后聚合）——编译器转换的两阶段设计
- 深水点：访问者的「替换与删除」——path.replaceWith / path.remove——转换类插件的原子操作

```javascript
// Babel 插件: 提取所有 i18n 调用
module.exports = function () {
  return {
    visitor: {
      CallExpression(path) {
        if (path.get('callee').isIdentifier({ name: 't' })) {
          const key = path.node.arguments[0]?.value;
          if (key) collected.add(key);               // enter: 收集
        }
      },
      Program: { exit() { /* exit: 子树完整后聚合输出 */ } },
    },
  };
};
```
