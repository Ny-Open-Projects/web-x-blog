---
title: [WCN-678] 设计令牌的三层架构（primitive / semantic / component）如何落地消费约束？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-678：设计令牌的三层架构（primitive / semantic / component）如何落地消费约束？

**答**：
- 结论：primitive（色值）→ semantic（用途如 color-action）→ component（btn-bg）；强制业务只消费 semantic 及以上，避免锁死主题。
- 约束手段：lint 规则禁止直接使用 primitive token；构建期扫描 CSS；语义 token 变更走 RFC；提供「别名映射」支持渐进迁移。
- 追问钩子：为什么组件层可选？因为组件层 token 利定制但易膨胀——考察对「灵活性与治理成本」的权衡。

```javascript
const TOKENS = {
  primitive: { blue500: '#165DFF', gray100: '#F2F3F5' },
  semantic: { action: 'var(--ds-primitive-blue500)',
              surface: 'var(--ds-primitive-gray100)' },
  component: { btnBg: 'var(--ds-semantic-action)' },
};
// 消费约束：业务只能用 semantic/component
const ALLOWED_PREFIX = ['--ds-semantic-', '--ds-component-'];
function lintTokenUsage(css) {
  const used = [...css.matchAll(/var\((--[\w-]+)\)/g)].map(m => m[1]);
  return used.filter(t => !ALLOWED_PREFIX.some(p => t.startsWith(p)))
             .map(t => `禁止直接使用基础层 token: ${t}`);
}
console.log(lintTokenUsage('color:var(--ds-primitive-blue500)'));
// ['禁止直接使用基础层 token: --ds-primitive-blue500']
```
