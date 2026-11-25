---
title: [WCN-683] 笔试：实现组件 API 一致性检查器（扫描多个组件的 props 定义，找出命名/类型/默认值不一致）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-683：笔试：实现组件 API 一致性检查器（扫描多个组件的 props 定义，找出命名/类型/默认值不一致）

**答**：
- 需求：实现 checkConsistency(components)：输入 {name: {props:{...}}}，找出① 同义不同名（用别名表）② 同名不同类型 ③ 同名不同默认值（按约定应一致）。返回问题列表。
- 思路：遍历收集每个 prop 的出现情况；别名表归一化；按归一化名聚合类型/默认值集合；集合大小>1 即不一致。
- 边界：别名表可扩展；可选 props 缺失不报错；输出带组件名便于定位。

```javascript
const ALIASES = { type: 'variant', kind: 'variant', appearance: 'variant' };
export function checkConsistency(components) {
  const seen = new Map();
  for (const [comp, def] of Object.entries(components)) {
    for (const [prop, meta] of Object.entries(def.props || {})) {
      const key = ALIASES[prop] || prop;
      if (!seen.has(key)) seen.set(key, []);
      seen.get(key).push({ comp, prop, type: meta.type, default: meta.default });
    }
  }
  const issues = [];
  for (const [key, entries] of seen) {
    const types = new Set(entries.map(e => e.type));
    if (types.size > 1)
      issues.push({ key, kind: '类型不一致', detail: [...types] });
    const defs = new Set(entries.map(e => String(e.default)));
    if (defs.size > 1)
      issues.push({ key, kind: '默认值不一致',
        detail: entries.map(e => `${e.comp}:${e.default}`) });
  }
  return issues;
}
console.log(checkConsistency({
  Button: { props: { variant: { type: 'enum', default: 'primary' } } },
  Input:  { props: { type: { type: 'enum', default: 'default' } } }, // 别名→variant
}));
```

**评分点**：
- 别名表归一化同义属性（type→variant）。
- 按归一化名聚合，识别类型/默认值不一致。
- 输出带组件名，便于定位责任方。
- 可选属性缺失不误报（只检查出现过的）。
