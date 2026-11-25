---
title: [MFW-705] 笔试：手写 SSG 页面指纹计算器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-705：笔试：手写 SSG 页面指纹

**答**：实现 `pageFingerprint({ content, template, data })`。规则：1) 拼接 content + template + stableStringify(data)——SHA256 取前 16 hex；2) stableStringify：键排序的 JSON 序列化（对象键序稳定 RBL-582）；3) 指纹稳定性：同输入同指纹；数组保序（数组内容顺序影响渲染）；data 为 null → 空 JSON；4) **碰撞防御**：16 hex（64 bit）的碰撞概率——百万页面级可接受（2^64 空间）。实现 `diffFingerprints(current, previous)`：返回 `{ changed, added, removed }`。边界：data 含循环引用（抛错——序列化不支持）；data 含 Date（toISOString 转换）；content 含 unicode（UTF-8 hash）。

```javascript
const crypto = require('crypto');
function stableStringify(v) {
  if (v === null || v === undefined) return 'null';
  if (v instanceof Date) return JSON.stringify(v.toISOString());
  if (Array.isArray(v)) return '[' + v.map(stableStringify).join(',') + ']';
  if (typeof v === 'object') {
    return '{' + Object.keys(v).sort().map(k =>
      `${JSON.stringify(k)}:${stableStringify(v[k])}`).join(',') + '}';
  }
  return JSON.stringify(v);
}
function pageFingerprint({ content, template, data }) {
  const h = crypto.createHash('sha256');
  h.update(content ?? '');
  h.update(template ?? '');
  h.update(stableStringify(data ?? null));
  return h.digest('hex').slice(0, 16);
}
function diffFingerprints(current = {}, previous = {}) {
  const changed = [], added = [];
  for (const [path, fp] of Object.entries(current)) {
    if (!(path in previous)) { added.push(path); continue; }
    if (previous[path] !== fp) changed.push(path);
  }
  const removed = Object.keys(previous).filter(p => !(p in current));
  return { changed, added, removed };
}

// 自测
// 稳定性
const page1 = { content: 'hello', template: 'Layout', data: { b: 2, a: 1 } };
const page2 = { content: 'hello', template: 'Layout', data: { a: 1, b: 2 } };   // 键序不同
console.log(pageFingerprint(page1) === pageFingerprint(page2));   // stableStringify 键排序

// 内容变更 → 指纹变
console.log(pageFingerprint({ ...page1, content: 'world' }) !== pageFingerprint(page1));
// 模板变更 → 指纹变
console.log(pageFingerprint({ ...page1, template: 'LayoutV2' }) !== pageFingerprint(page1));
// Date 转换
r = pageFingerprint({ content: 'x', template: 't', data: { d: new Date('2026-01-01') } });
console.log(typeof r === 'string' && r.length === 16);

// 循环引用抛错
const circular = {}; circular.self = circular;
e = null; try { pageFingerprint({ content: 'x', template: 't', data: circular }); }
catch (x) { e = x; }
console.log(e !== null);                                 // 循环引用不支持

// diff
const prev = { '/a': 'fp1', '/b': 'fp2', '/old': 'fp9' };
const cur = { '/a': 'fp1', '/b': 'fp2-changed', '/new': 'fp3' };
const d = diffFingerprints(cur, prev);
console.log(d.changed.join(',') === '/b');
console.log(d.added.join(',') === '/new');
console.log(d.removed.join(',') === '/old');
```

**评分点**：
- stableStringify（键排序 + Date 转换——RBL-582 键序稳定）；三要素指纹（内容+模板+数据）
- 循环引用的诚实抛错（序列化不支持——不静默）；diff 三类（changed/added/removed）
- 边界（Date/null data/unicode）；16 hex 碰撞概率说明
- 能说清「SSG 指纹的最小完备性：内容+模板+数据——漏模板 hash = 模板变更的静默漏检」属于加分
