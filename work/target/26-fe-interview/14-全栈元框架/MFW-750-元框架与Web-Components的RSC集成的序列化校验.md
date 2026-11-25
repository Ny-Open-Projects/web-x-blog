---
title: [MFW-750] RSC 与 WC 集成的序列化校验
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 笔试题
---

## MFW-750：笔试：手写 WC 与 RSC 集成校验

**答**：实现 `validateWCInRSC(components)`。components: `{ tag, props: Record<string, { type: 'attr'|'prop'|'event', value }> }[]`. 规则：1) **attr vs prop 的判定**：string/number/boolean → attr（HTML attribute——序列化安全）；object/array/function → prop（JS property——需要 client JS RBL-WCN 目录 property vs attribute）；event（onXxx）→ prop + client 侧注册（event handler 不可序列化——需 client JS）；2) **event handler 检测**：type='event' 的 props → warn 'event-in-server'（event handler 需要 client JS——server 渲染的 WC 不能传 event handler（RBL-780 边界审计的 WC 版——handler 跨不了边界）；3) **DSD 必需检查**：有 WC 但无 DSD 模板 → warn 'missing-dsd'（无 shadow = 首屏无样式）；4) 返回 `{ findings: Array<{ tag, prop, type, severity }>, ok }`（ok = 无 error）。边界：无 event 类 props；空 props；全 attr（全安全）。

```javascript
function validateWCInRSC(components = []) {
  const findings = []; let hasDSD = false;
  for (const comp of components) {
    if (comp.hasDSD) hasDSD = true;
    for (const [prop, spec] of Object.entries(comp.props ?? {})) {
      if (spec.type === 'event')
        findings.push({ tag: comp.tag, prop, type: 'event-in-server', severity: 'error',
          detail: `event handler ${prop} 不可序列化——需要 client JS 注册` });
      else if (['object', 'array', 'function'].includes(typeof spec.value) && spec.type === 'attr')
        findings.push({ tag: comp.tag, prop, type: 'attr-type-mismatch', severity: 'warn',
          detail: `attr 类型为 ${typeof spec.value}——对象应使用 prop 而非 attr` });
      else if (spec.type === 'prop' && typeof spec.value === 'object')
        findings.push({ tag: comp.tag, prop, type: 'prop-in-server', severity: 'warn',
          detail: 'prop 传递需要 client JS——server 渲染时仅 attr 可用（DSD 静态渲染）' });
    }
  }
  if (components.length && !hasDSD)
    findings.push({ tag: components[0].tag, type: 'missing-dsd', severity: 'warn',
      detail: 'WC 无 Declarative Shadow DOM——server 渲染无样式' });
  return { findings, ok: !findings.some(f => f.severity === 'error') };
}

// 自测
// 全 attr（安全）
let r = validateWCInRSC([
  { tag: 'my-card', hasDSD: true,
    props: { name: { type: 'attr', value: 'x' }, price: { type: 'attr', value: 9.99 } } },
]);
console.log(r.ok === true && r.findings.length === 0);

// event handler：error
r = validateWCInRSC([
  { tag: 'my-btn', hasDSD: true,
    props: { onClick: { type: 'event', value: 'fn' } } },
]);
console.log(r.findings.some(f => f.type === 'event-in-server' && f.severity === 'error'));
console.log(r.ok === false);

// attr 类型不匹配
r = validateWCInRSC([
  { tag: 'my-card', hasDSD: true,
    props: { data: { type: 'attr', value: { nested: true } } } },
]);
console.log(r.findings.some(f => f.type === 'attr-type-mismatch'));

// 缺 DSD
r = validateWCInRSC([
  { tag: 'my-card', hasDSD: false,
    props: { name: { type: 'attr', value: 'x' } } },
]);
console.log(r.findings.some(f => f.type === 'missing-dsd'));
console.log(r.ok === true);                              // warn 不阻断

// 空 props
console.log(validateWCInRSC([{ tag: 'wc', hasDSD: true }]).findings.length === 0);
```

**评分点**：
- attr/prop/event 三分类的序列化判定（string→attr 安全、object→prop 需 client、event→需 client JS）
- event-in-server 的 error（handler 跨不了边界——RBL-780 的 WC 版）；DSD 缺失告警
- 边界（空 props/全 attr/无 DSD 不阻断——warn 不 error）
- 能说清「WC 在 RSC 中天然跨边界（server 渲染 DSD + client 按需注册）——event handler 是唯一不可跨界面的 props」属于加分
