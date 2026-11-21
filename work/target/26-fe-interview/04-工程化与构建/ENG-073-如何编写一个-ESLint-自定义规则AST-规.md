---
title: [ENG-073] 如何编写一个 ESLint 自定义规则？AST 规则实战？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-073：如何编写一个 ESLint 自定义规则？AST 规则实战？
**答**：
- 规则三件套：meta（类型、schema、消息模板）、create（返回 AST 访问器对象）、配套 RuleTester 单测。
- 選点很关键：ImportDeclaration 管 import 来源、CallExpression 管函数调用、MemberExpression 管属性访问。
- 插件形态：本地 monorepo 内共享（eslint-plugin-myorg）或发布到私有 registry，flat config 中直接 import。
- 报错要给修复路径：message 里写清"禁止 X，请用 Y"，必要时实现 fix 函数支持 --fix。

```javascript
// eslint-plugin-myorg 自定义规则：禁止 import 禁用包
module.exports = {
  meta: {
    type: 'problem',
    docs: { description: '禁止 import 内部禁用的包' },
    schema: [{ type: 'array', items: { type: 'string' } }], // 接收禁用包列表
    messages: { banned: '禁止使用 {{name}}，请使用内部封装层' },
  },
  create(context) {
    const banned = context.options[0] ?? [];
    return {
      ImportDeclaration(node) {
        const source = String(node.source.value);
        if (banned.includes(source)) {
          context.report({ node, messageId: 'banned', data: { name: source } });
        }
      },
    };
  },
};

// 使用：rules: { 'myorg/no-banned-import': ['error', ['moment', 'lodash']] }
```
