---
title: [RBL-835] 笔试：手写 mock 残留与类型同构审计器
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-835：笔试：手写 mock 残留与类型同构审计器

**答**：实现两部分。1) `auditMockResidue(files)`：检测生产产物中的 mock 残留：`__mocks__`/`msw`/`fixture`/`lorem` 模式 → finding `{ file, matched }`（匹配到的模式名）。2) `verifyContract(realApi, mockApi)`：realApi/mockApi 为 `Record<method, { args: string[], ret: string }>`。规则：mock 缺少 real 的方法 → 'missing-method'；mock 多出方法 → 'extra-method'（warn）；ret 类型不一致 → 'ret-mismatch'；args 数量不一致 → 'arg-mismatch'。返回 `{ residue, contract: { problems }, ok }`（ok = residue 空且 contract 无 blocker）。边界：realApi 空；两方全空。

```javascript
const MOCK_PATTERNS = { mocks: /__mocks__/, msw: /\bmsw\b/, fixture: /fixture/i, lorem: /lorem ipsum/i };

function auditMockResidue(files) {
  const residue = [];
  for (const f of files)
    for (const [name, re] of Object.entries(MOCK_PATTERNS))
      if (re.test(f.code ?? ''))
        residue.push({ file: f.name, matched: name });
  return residue;
}

function verifyContract(real = {}, mock = {}) {
  const problems = [];
  for (const [m, r] of Object.entries(real)) {
    if (!(m in mock)) { problems.push({ type: 'missing-method', method: m }); continue; }
    const mo = mock[m];
    if (r.args.length !== mo.args.length)
      problems.push({ type: 'arg-mismatch', method: m });
    if (r.ret !== mo.ret)
      problems.push({ type: 'ret-mismatch', method: m, expected: r.ret, got: mo.ret });
  }
  for (const m of Object.keys(mock))
    if (!(m in real))
      problems.push({ type: 'extra-method', method: m });
  return { problems };
}

// 自测
const files = [
  { name: 'app.js', code: 'fetch("/api/user");' },                            // 干净
  { name: 'chunk.js', code: 'if (msw) worker.start(); __mocks__/user.js;' },  // 残留
  { name: 'lazy.js', code: 'const f = getFixture("x"); // lorem ipsum', },
];
let r = auditMockResidue(files);
console.log(r.find(x => x.file === 'chunk.js').matched); // 'msw'（先命中）
console.log(r.filter(x => x.file === 'chunk.js').length >= 1);
console.log(r.find(x => x.file === 'lazy.js').matched === 'fixture');
console.log(r.find(x => x.file === 'app.js') === undefined);

const real = { getUser: { args: ['id'], ret: 'User' }, listUsers: { args: [], ret: 'User[]' } };
const mock = { getUser: { args: ['id'], ret: 'User' }, deleteUser: { args: ['id'], ret: 'void' },
  listUsers: { args: [], ret: 'any' } };
const c = verifyContract(real, mock);
console.log(c.problems.some(p => p.type === 'extra-method' && p.method === 'deleteUser'));
console.log(c.problems.some(p => p.type === 'ret-mismatch' && p.method === 'listUsers'));

const c2 = verifyContract(real, { getUser: { args: ['id'], ret: 'User' }, listUsers: { args: [], ret: 'User[]' } });
console.log(c2.problems.length === 0);
console.log(verifyContract({}, {}).problems.length === 0);
```

**评分点**：
- mock 模式多向量检测（mocks/msw/fixture/lorem）；生产产物残留是合规+体积双重问题
- 契约校验四向（missing/extra/ret/args）；extra 是 warn 级语义但按问题返回
- 边界：空 api/双方全空
- 能说清「resolve 条件切换让 mock 物理不在产物（解析期分支），env if 靠 DCE 是脆弱的」属于加分
