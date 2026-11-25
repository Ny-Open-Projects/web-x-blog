---
title: [1232] 笔试手写：实现知识库文档的探针可达断言
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG]
type: 笔试题
---

## 1232：笔试手写：实现知识库文档的探针可达断言

**需求**：实现 probeAssert(doc, retrieve, gen)：gen(text) 返回 { q, mustContain }[]；对每探针 retrieve(q) 后断言「任一结果 docId === doc.id 且该结果文本包含全部 mustContain」。输出 { results: [{ q, pass }], rate }（2 位）。

```js
function probeAssert(doc, retrieve, gen) {
  const probes = gen(doc.text);
  const results = probes.map(p => {
    const hits = retrieve(p.q);
    const hit = hits.find(h => h.docId === doc.id);
    const pass = !!hit && p.mustContain.every(k => hit.text.includes(k));
    return { q: p.q, pass };
  });
  const ok = results.filter(r => r.pass).length;
  return { results, rate: +(ok / (results.length || 1)).toFixed(2) };
}
const doc = { id: 'd1', text: '灰度发布支持按 UID 尾号切流，回滚走别名' };
const gen = t => [
  { q: '灰度怎么切流', mustContain: ['UID'] },
  { q: '回滚怎么做', mustContain: ['别名'] },
];
const retrieve = q => [{ docId: 'd1', text: '灰度发布支持按 UID 尾号切流，回滚走别名' }];
console.log(probeAssert(doc, retrieve, gen));  // rate '1.00'
```

**评分点**：
- 双重断言（docId 命中 + 关键词全覆盖——真可达）
- 除零保护与 rate 精度
- gen/retrieve 注入（可 mock 可真实）
- 能讨论：探针 false negative（问题太偏）的人工抽检、入库即验收的左移机制

