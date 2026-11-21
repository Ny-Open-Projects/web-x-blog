---
title: [WCN-178] 笔试：手写 WC 组件的 ESLint 自定义规则集（生命周期错位、事件未 composed 检测）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-178：笔试：手写 WC 组件的 ESLint 自定义规则集

**题目**：实现三条规则：① `wc-lifecycle-order`：constructor 内禁止调用 `this.getAttribute` / `attachShadow` 之外的 attribute 读取；connectedCallback 内禁止 `attachShadow`；② `wc-event-composed`：`new CustomEvent(...)` 出现在 class 内且未传 `{ composed: true }` 时告警（豁免：影子树内私有事件名以 `_` 开头）；③ `wc-no-raw-color`：模板字符串 CSS 中出现裸色值（#hex/rgb）告警（要求 token var）。

**答**：

```javascript
module.exports = {
  rules: {
    'wc-lifecycle-order': {
      meta: { schema: [], messages: { attach: '不要在 connectedCallback 里 attachShadow（应在 constructor）',
        attrRead: 'constructor 内读 attribute 时序不可靠' } },
      create(ctx) {
        let className = null;
        let inCtor = false, inConnected = false;
        return {
          'MethodDefinition'(n) { className = n; },
          'MethodDefinition[key.name="constructor"]'(n) { inCtor = true; },
          'MethodDefinition[key.name="constructor"]:exit'() { inCtor = false; },
          'MethodDefinition[key.name="connectedCallback"]'(n) { inConnected = true; },
          'MethodDefinition[key.name="connectedCallback"]:exit'() { inConnected = false; },
          CallExpression(n) {
            const name = n.callee.property?.name ?? '';
            if (inCtor && name === 'getAttribute')
              ctx.report({ node: n, messageId: 'attrRead' });
            if (inConnected && name === 'attachShadow')
              ctx.report({ node: n, messageId: 'attach' });
          },
        };
      },
    },
    'wc-event-composed': {
      meta: { schema: [], messages: { need: '对外事件应设置 composed: true' } },
      create(ctx) {
        return {
          NewExpression(n) {
            if (n.callee.name !== 'CustomEvent') return;
            const arg2 = n.arguments[1];
            const firstArg = n.arguments[0];
            const isPrivate = firstArg?.type === 'Literal' && String(firstArg.value).startsWith('_');
            if (isPrivate) return;
            const hasComposed = arg2?.type === 'ObjectExpression' &&
              arg2.properties.some((p) => p.key.name === 'composed');
            if (arg2 && !hasComposed) ctx.report({ node: n, messageId: 'need' });
          },
        };
      },
    },
    'wc-no-raw-color': {
      meta: { schema: [], messages: { raw: 'CSS 中出现裸色值，请使用 --acme-* token' } },
      create(ctx) {
        return {
          'TaggedTemplateExpression[tag.name="css"], TemplateLiteral'(n) {
            const raw = ctx.getSourceCode().getText(n);
            if (/#[0-9a-fA-F]{3,8}\b|rgba?\(/.test(raw))
              ctx.report({ node: n, messageId: 'raw' });
          },
        };
      },
    },
  },
};
```

**评分点**：
- 生命周期规则的状态跟踪（进入/退出 constructor 与 connectedCallback）。
- composed 规则的豁免逻辑（私有事件前缀）与 ObjectExpression 检查。
- CSS 裸色值正则覆盖 #hex 与 rgb()/rgba()。
- 三条规则的 message 清晰指向修复方式。
