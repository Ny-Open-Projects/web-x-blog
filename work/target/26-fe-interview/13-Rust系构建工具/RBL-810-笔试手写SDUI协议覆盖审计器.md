---
title: [RBL-810] 笔试：手写 SDUI 协议覆盖审计器（双向 diff + 降级安全性）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-810：笔试：手写 SDUI 协议覆盖审计器（双向 diff + 降级安全）

**答**：实现 `auditSDUI(schema, registry, { allowFallback })`。schema: `{ version, components: Array<{ type, props: string[] }> }`；registry: `Record<type, { props: string[], lazy: boolean }>`. 规则：1) 服务端组件类型客户端未注册 → blocker 'unknown-component'（除非 allowFallback=true 时降级为 warn 'fallback-covered'）；2) 客户端注册但服务端未用 → info 'unused'（覆盖度）；3) props 审计：schema 声明的 props 中客户端未支持的 → blocker 'missing-prop'；4) 降级安全性：注册表懒加载组件的类型若被 fallback 覆盖 → blocker 'fallback-lazy'（降级不能依赖懒加载）。返回 `{ blockers, warnings, coverage }`（coverage = 已用/已注册百分比）。边界：空 schema；registry 空。

```javascript
function auditSDUI(schema, registry = {}, { allowFallback = false } = {}) {
  const blockers = [], warnings = [];
  const usedTypes = schema.components?.map(c => c.type) ?? [];
  const regTypes = Object.keys(registry);
  const missing = usedTypes.filter(t => !(t in registry));
  for (const t of missing) {
    if (allowFallback) warnings.push({ type: 'fallback-covered', component: t });
    else blockers.push({ type: 'unknown-component', component: t });
  }
  for (const c of schema.components ?? []) {
    const reg = registry[c.type];
    if (!reg) continue;
    const missingProps = c.props.filter(p => !reg.props.includes(p));
    if (missingProps.length)
      blockers.push({ type: 'missing-prop', component: c.type, props: missingProps });
  }
  const unused = regTypes.filter(t => !usedTypes.includes(t));
  const coverage = regTypes.length
    ? +((regTypes.length - unused.length) / regTypes.length * 100).toFixed(1) : 0;
  // 降级路径不能依赖懒加载
  for (const t of missing)
    if (allowFallback && registry[t]?.lazy) blockers.push({ type: 'fallback-lazy', component: t });
  return { blockers, warnings, coverage, unused };
}

// 自测
const schema = { version: '2.0', components: [
  { type: 'banner', props: ['text', 'bgColor'] },
  { type: 'button', props: ['label'] },
  { type: 'chart', props: ['data'] },                     // 未注册
] };
const registry = {
  banner: { props: ['text', 'bgColor'], lazy: true },
  button: { props: ['label'], lazy: false },
  modal: { props: [], lazy: false },                      // 未使用
};
let r = auditSDUI(schema, registry);
console.log(r.blockers.some(b => b.type === 'unknown-component' && b.component === 'chart'));
console.log(r.coverage === 100);                         // banner/button 都用到
console.log(r.unused.join(',') === 'modal');

// allowFallback
r = auditSDUI(schema, registry, { allowFallback: true });
console.log(r.blockers.some(b => b.type === 'fallback-lazy' && b.component === 'chart'));   // banner 懒但 chart 不在 registry
console.log(r.warnings.some(w => w.type === 'fallback-covered'));

// missing-prop
r = auditSDUI({ version: '2.0', components: [{ type: 'banner', props: ['text', 'onClick'] }] }, registry);
console.log(r.blockers.some(b => b.type === 'missing-prop' && b.props.join(',') === 'onClick'));

console.log(auditSDUI({ version: '1', components: [] }, registry).blockers.length === 0);
```

**评分点**：
- 双向 diff（unknown-component blocker / unused info）与 fallback 政策开关
- props 级审计（missing-prop 聚合到组件）；fallback-lazy 检查（降级路径零依赖原则）
- coverage 百分比计算；空 schema 安全
- 能说清「降级渲染器不能懒加载——降级触发时恰是产物旧/网络差的场景」属于加分
