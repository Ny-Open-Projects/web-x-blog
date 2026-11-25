---
title: [RBL-818] 笔试：手写文档示例 API 漂移检测器（props 引用比对 + 废弃标注）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-818：笔试：手写文档示例 API 漂移检测器（props 比对 + 废弃）

**答**：实现 `auditDocs(docs, api)`。docs: `Array<{ page, snippets: string[] }>`（文档页的示例代码）；api: `Record<component, { props: Set<string>, deprecated?: Record<prop, { since, replacement }> }>`. 规则：1) 示例中 `Component prop="x"` 或 `prop:` 形式提取 props：组件不存在 → finding 'unknown-component'；prop 不在 api → finding 'unknown-prop'；2) prop 已废弃 → warn 'deprecated-prop'（附 replacement）；3) 全部废弃 props 使用且组件无其他问题 → info 'fully-deprecated'（页面需要重写）；4) 返回 `{ findings: Array<{ page, component, prop?, type }>, ok }`。边界：无示例；api 空（全部 unknown-component）。

```javascript
function auditDocs(docs, api = {}) {
  const findings = [];
  for (const d of docs) {
    for (const snip of d.snippets ?? []) {
      // 提取 <Comp prop="x" prop2={y}> 与 prop: 形式
      for (const m of snip.matchAll(/<(\w+)\b([^>]*)>/g)) {
        const [, comp, attrs] = m;
        if (!(comp in api)) { findings.push({ page: d.page, component: comp, type: 'unknown-component' }); continue; }
        const meta = api[comp];
        const used = new Set();
        for (const a of attrs.matchAll(/([\w-]+)=/g)) used.add(a[1]);
        for (const p of used) {
          if (!meta.props.has(p)) { findings.push({ page: d.page, component: comp, prop: p, type: 'unknown-prop' }); continue; }
          const dep = meta.deprecated?.[p];
          if (dep)
            findings.push({ page: d.page, component: comp, prop: p, type: 'deprecated-prop',
              replacement: dep.replacement });
        }
        if (used.size && [...used].every(p => meta.deprecated?.[p]))
          findings.push({ page: d.page, component: comp, type: 'fully-deprecated' });
      }
    }
  }
  return { findings, ok: !findings.some(f => f.type === 'unknown-component' || f.type === 'unknown-prop') };
}

// 自测
const api = {
  Button: { props: new Set(['label', 'size', 'variant']),
    deprecated: { variant: { since: '2.0', replacement: 'tone' } } },
  Modal: { props: new Set(['open', 'onClose']) },
};
const docs = [
  { page: 'button', snippets: ['<Button label="OK" size="lg" />'] },       // ok
  { page: 'legacy', snippets: ['<Button label="X" variant="primary" />'] },  // deprecated
  { page: 'wrong', snippets: ['<Button lable="X" />'] },                    // 拼错 prop
  { page: 'ghost', snippets: ['<Tabs items={[]} />'] },                     // 未知组件
];
let r = auditDocs(docs, api);
console.log(r.ok === false);
console.log(r.findings.some(f => f.type === 'deprecated-prop' && f.replacement === 'tone'));
console.log(r.findings.some(f => f.type === 'unknown-prop' && f.prop === 'lable'));
console.log(r.findings.some(f => f.type === 'unknown-component' && f.component === 'Tabs'));

r = auditDocs([{ page: 'p', snippets: ['<Button variant="x" />'] }], api);
console.log(r.findings.some(f => f.type === 'fully-deprecated'));
console.log(auditDocs([], api).ok === true);
```

**评分点**：
- 示例 props 提取（JSX 属性形态）；四类 finding 分级（unknown-component/unknown-prop 阻断，deprecated/fully-deprecated 警示）
- 废弃替换建议（replacement）与全废弃页面提示
- 边界：无示例、空 api
- 能说清「文档示例与 API 漂移是文档腐化的主形式，doctest + props 比对机械化」属于加分
