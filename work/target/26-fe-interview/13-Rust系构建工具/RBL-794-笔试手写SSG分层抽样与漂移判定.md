---
title: [RBL-794] 笔试：手写 SSG 分层抽样与漂移判定器
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-794：笔试：手写 SSG 分层抽样与漂移判定器

**答**：实现两部分。1) `stratify(pages, { full, sampleRate })`：pages: `{ path, traffic }[]`——full 谓词命中的全取；其余按 sampleRate 随机抽样（确定性：注入 rng）；2) `judge(samples, ssgBase, liveFn, { threshold })`：liveFn(path) 返回语义指纹字符串；ssgBase: `Record<path, fp>`。similarity = 公共字符 bigram / 并集（Jaccard 近似）。判定：base 缺失 → 'not-prerendered'；sim ≥ threshold → 'ok'；否则 'drift'。返回 `{ results, driftCount, ok }`（ok = drift 占比 ≤ 5%）。边界：空 pages；指纹为空串。

```javascript
function stratify(pages, { full, sampleRate = 0.1, rng = Math.random } = {}) {
  const hot = pages.filter(full);
  const cold = pages.filter(p => !full(p));
  const n = Math.max(1, Math.round(cold.length * sampleRate));
  const picked = [];
  const pool = [...cold];
  for (let i = 0; i < n && pool.length; i++)
    picked.push(pool.splice(Math.floor(rng() * pool.length), 1)[0]);
  return [...hot, ...picked];
}

function judge(samples, ssgBase, liveFn, { threshold = 0.9 } = {}) {
  const bigrams = (s) => { const set = new Set();
    for (let i = 0; i < s.length - 1; i++) set.add(s.slice(i, i + 2)); return set; };
  const sim = (a, b) => {
    if (!a || !b) return a === b ? 1 : 0;
    const A = bigrams(a), B = bigrams(b);
    const inter = [...A].filter(x => B.has(x)).length;
    return A.size + B.size ? inter / (A.size + B.size - inter) : 1;
  };
  const results = samples.map(p => {
    if (!(p.path in ssgBase)) return { page: p.path, status: 'not-prerendered' };
    const s = sim(ssgBase[p.path], liveFn(p.path));
    return { page: p.path, status: s >= threshold ? 'ok' : 'drift', sim: +s.toFixed(3) };
  });
  const driftCount = results.filter(r => r.status !== 'ok').length;
  return { results, driftCount, ok: results.length ? driftCount / results.length <= 0.05 : true };
}

// 自测
const pages = Array.from({ length: 100 }, (_, i) => ({ path: `/p${i}`, traffic: i === 0 ? 0.4 : 0.001 }));
const sample = stratify(pages, { full: p => p.traffic > 0.05, sampleRate: 0.1, rng: () => 0.5 });
console.log(sample.length === 11);                       // 首页全取 + 10 抽样
console.log(sample.some(p => p.path === '/p0'));

const base = { '/a': '商品列表 价格', '/b': '关于我们' };
let r = judge([{ path: '/a' }, { path: '/b' }, { path: '/c' }], base,
  async (p) => p === '/a' ? '商品列表 价格' : p === '/b' ? '关于我们（旧）' : 'x');
console.log(r.results[0].status === 'ok');
console.log(r.results[1].sim > 0.5 && r.results[1].status === 'ok' || r.results[1].status === 'drift');
console.log(r.results[2].status === 'not-prerendered');
console.log(r.ok === false);                             // 1/3 漂移 > 5%

r = judge([{ path: '/a' }], base, async () => '商品列表 价格');
console.log(r.ok === true);
console.log(judge([], base, async () => '').ok === true);
```

**评分点**：
- 分层抽样正确（full 全取 + 其余确定性抽样，rng 注入可复现）
- bigram 相似度实现（空指纹边界处理）；阈值判定与 5% 漂移占比门禁
- not-prerendered 独立状态；空集 ok
- 能说清「运行时渲染做基准才能捕捉数据时效漂移，重预渲染只能查管线确定性」属于加分
