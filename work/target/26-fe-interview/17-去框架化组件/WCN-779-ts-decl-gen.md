---
title: [WCN-779] 笔试：手写从组件 schema 生成 TS 类型声明的生成器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-779：笔试：手写从组件 schema 生成 TS 类型声明的生成器

**答**：
- 需求：实现 `genInterface(name, schema)`，schema 形如 `{ propName: 'string'|'number'|'boolean'|'string[]' }`，返回 `interface NAME { propName?: TYPE; ... }` 字符串。类型映射：string→string、number→number、boolean→boolean、string[]→string[]；未知类型回退 any；边界：空 schema 返回空 interface，属性名合法性过滤。
- 要点：typeMap 映射；逐条生成 `  key?: type;`；过滤非法属性名（非标识符）；拼接 interface 字符串。

```javascript
function genInterface(name, schema) {
  const typeMap = { string: 'string', number: 'number', boolean: 'boolean', 'string[]': 'string[]' };
  const lines = [];
  for (const [k, t] of Object.entries(schema || {})) {
    if (!/^[A-Za-z_$][\w$]*$/.test(k)) continue;       // 过滤非法属性名
    lines.push(`  ${k}?: ${typeMap[t] || 'any'};`);      // 未知类型回退 any
  }
  return `interface ${name} {\n${lines.join('\n')}\n}`;
}
console.log(genInterface('DsButtonProps', {
  size: 'string', disabled: 'boolean', tags: 'string[]', weird: 'date', 'bad-name': 'string',
}));
```

**评分点**：
- 类型映射正确（含 string[] 数组类型）。
- 未知类型回退 any，具备健壮性。
- 非法属性名过滤，生成合法 TS。
- 空 schema 仍返回合法空 interface。
