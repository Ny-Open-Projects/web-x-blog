---
title: [1123] 笔试手写：实现 store 契约测试器
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, 测试]
type: 笔试题
---

## 1123：笔试手写：实现 store 契约测试器

**答**：实现 contractTest(store, contract)：contract 为 { fields: [{ name, type, readonly }], actions: [name] }。校验：声明字段存在且类型匹配；readonly 字段被 store 的 action 修改则报违规（笔试以 setter 拦截模拟）；contract.actions 中不存在的 action 报缺失；store 上未声明的导出报多余。返回 { pass, violations }。

```js
function contractTest(store, contract) {
  const typeOf = v => Array.isArray(v) ? 'array'
    : v instanceof Date ? 'date' : typeof v;
  const violations = [];
  for (const f of contract.fields) {
    const v = store[f.name];
    if (v === undefined) { violations.push(`${f.name}: 缺失`); continue; }
    if (typeOf(v) !== f.type) violations.push(`${f.name}: 期望 ${f.type} 实际 ${typeOf(v)}`);
  }
  const declaredActions = new Set(contract.actions);
  const actualActions = Object.keys(store).filter(k => typeof store[k] === 'function');
  for (const a of contract.actions)
    if (typeof store[a] !== 'function') violations.push(`action ${a}: 不存在`);
  for (const a of actualActions)
    if (!declaredActions.has(a) && !contract.fields.some(f => f.name === a))
      violations.push(`${a}: 未在契约声明（多余导出）`);
  return { pass: violations.length === 0, violations };
}
```

**评分点**：
- 字段类型表驱动校验（含 array/date 的 typeOf 细分）
- 双向校验：缺失与多余都报（契约完整性）
- actions 与 fields 分开判定
- 能讨论：契约测试在 CI 的位置——store 导出即公共 API，破坏性变更必须过门禁
