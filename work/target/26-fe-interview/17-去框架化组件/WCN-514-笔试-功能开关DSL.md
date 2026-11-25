---
title: [WCN-514] 笔试：实现元素级功能开关（feature flag）运行时 DSL 解析器。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-514：笔试：实现元素级功能开关（feature flag）运行时 DSL 解析器。

**答**：
- 结论：把开关表达式解析成 AST，按「租户 / 版本 / 用户分桶」上下文求值，元素渲染前判定。
- DSL 支持 and/or/not 与比较运算，禁止任意代码执行（白名单求值，杜绝 eval）。
- 求值结果缓存：同一上下文 + 表达式只算一次，避免渲染热路径重复解析。
- 追问：开关变更如何实时生效？（答：订阅开关配置信号，变更时重算并触发元素更新）

```javascript
function parse(expr) { return expr.split(/\s+(and|or)\s+/).map(t => parseAtom(t)); }
function parseAtom(t) {
  const m = t.match(/^([\w.]+)\s*(>=|<=|==|!=|>|<)\s*(.+)$/);
  if (m) return { field: m[1], op: m[2], value: m[3].replace(/['"]/g, '') };
  return { field: t, op: 'truthy' };
}
function evaluate(expr, ctx) {
  const parts = expr.split(/\s+and\s+/);                  // 简化：只处理 and
  return parts.every(p => {
    const { field, op, value } = parseAtom(p.trim());
    const actual = field.split('.').reduce((o, k) => o?.[k], ctx);
    switch (op) {
      case '>': return actual > +value; case '==': return String(actual) === value;
      case 'truthy': return !!actual; default: return false;
    }
  });
}
evaluate("tenant.id == 'A' and user.bucket < 10", ctx);
```

**评分点**：
- 白名单 AST 求值，杜绝 eval
- and/or/not 与比较运算
- 表达式求值缓存
- 配置变更订阅刷新
