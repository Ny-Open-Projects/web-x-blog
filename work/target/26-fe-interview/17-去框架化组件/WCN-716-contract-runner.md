---
title: [WCN-716] 笔试：手写轻量契约测试运行器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-716：笔试：手写轻量契约测试运行器

**答**：
- 需求：输入契约对象契约 `{ tag, attributes: {名:类型}, events: string[], parts: string[] }` 与组件描述 `{ attributes, events, parts, slots }`，返回不满足项的错误数组。
- 要点：逐维度比对，类型用 `typeof` 校验（boolean 对应 'boolean'）；事件/part 用集合比较；边界：契约或实现缺字段时按空集处理。

```javascript
function verifyContract(contract, impl) {
  const errs = [];
  const c = contract || {}, m = impl || {};
  const attrs = c.attributes || {}, iAttrs = m.attributes || {};
  for (const [name, type] of Object.entries(attrs)) {
    if (!(name in iAttrs)) { errs.push(`缺少属性 ${name}`); continue; }
    if (typeof iAttrs[name] !== type) errs.push(`属性 ${name} 类型应为 ${type}`);
  }
  for (const ev of c.events || []) {
    if (!(m.events || []).includes(ev)) errs.push(`缺少事件 ${ev}`);
  }
  for (const p of c.parts || []) {
    if (!(m.parts || []).includes(p)) errs.push(`缺少 part ${p}`);
  }
  if (c.tag && m.tag && c.tag !== m.tag) errs.push(`tag 不符: ${m.tag}`);
  return errs;
}
console.log(verifyContract(
  { tag: 'ds-input', attributes: { size: 'string' }, events: ['ds-change'], parts: ['input'] },
  { tag: 'ds-input', attributes: { size: 1 }, events: [], parts: ['input'] }
));
```

**评分点**：
- 逐维度（属性/事件/part/tag）校验，错误可定位到具体字段。
- 属性既检查存在性也检查类型，覆盖类型破坏场景。
- 对缺失字段按空集处理，具备边界防御。
- 返回结构化错误数组，便于 CI 输出报告。
