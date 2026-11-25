---
title: [RBL-774] 笔试：手写 attestation 验证器（签名 + 逐文件 hash + commit 绑定）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-774：笔试：手写 attestation 验证器（签名 + 文件哈希 + commit 绑定）

**答**：实现 `verifyAttestation(att, artifacts, { verifySig, expectedCommit })`。att: `{ signed, invocation: { commit }, output: { files: [{ name, hash }] } }`；artifacts: `{ name, content }[]`。规则：1) 签名校验（注入 verifySig(sig, payload) -> boolean，payload 为去掉 signed 字段的 canonical JSON）；2) 逐文件 hash 比对（注入 hashOf(content)）：attestation 声明但产物缺失 → 'missing'；产物有但未声明 → 'extra'；hash 不符 → 'tampered'；3) commit 与 expectedCommit 不符 → 'commit-mismatch'；4) 返回 `{ ok, problems: string[] }`——签名失败/commit 不符直接短路（不再查文件）。边界：空产物；attestation 文件列表为空但产物非空。

```javascript
function verifyAttestation(att, artifacts, { verifySig, expectedCommit, hashOf }) {
  const problems = [];
  const { signed, ...payload } = att;
  if (!verifySig(signed, payload))
    return { ok: false, problems: ['signature-invalid'] };
  if (att.invocation?.commit !== expectedCommit)
    return { ok: false, problems: ['commit-mismatch'] };

  const declared = new Map(att.output.files.map(f => [f.name, f.hash]));
  const actual = new Map(artifacts.map(a => [a.name, hashOf(a.content)]));
  for (const [name, h] of declared)
    if (!actual.has(name)) problems.push(`missing: ${name}`);
    else if (actual.get(name) !== h) problems.push(`tampered: ${name}`);
  for (const name of actual.keys())
    if (!declared.has(name)) problems.push(`extra: ${name}`);
  return { ok: problems.length === 0, problems };
}

// 自测
const hashOf = (s) => 'h_' + s;
const verifySig = (sig, payload) => sig === 'sig_' + JSON.stringify(payload);

const files = [{ name: 'a.js', content: 'AAA' }, { name: 'b.js', content: 'BBB' }];
const att = (extra = []) => ({
  signed: null,
  invocation: { commit: 'c1' },
  output: { files: files.map(f => ({ name: f.name, hash: hashOf(f.content) })).concat(extra) },
});
// 注入签名计算
const sign = (att) => { const { signed, ...p } = att; return { ...att, signed: 'sig_' + JSON.stringify(p) }; };

let r = verifyAttestation(sign(att()), files, { verifySig, expectedCommit: 'c1', hashOf });
console.log(r.ok === true && r.problems.length === 0);

// 篡改
r = verifyAttestation(sign(att()), [{ ...files[0], content: 'EVIL' }, files[1]],
  { verifySig, expectedCommit: 'c1', hashOf });
console.log(r.problems[0] === 'tampered: a.js' && r.ok === false);

// commit 不符（短路）
r = verifyAttestation(sign(att()), [], { verifySig, expectedCommit: 'c2', hashOf });
console.log(r.problems[0] === 'commit-mismatch');

// 签名无效（短路）
r = verifyAttestation({ ...sign(att()), signed: 'fake' }, files,
  { verifySig, expectedCommit: 'c1', hashOf });
console.log(r.problems[0] === 'signature-invalid');

// 多余文件
r = verifyAttestation(sign(att()), [...files, { name: 'evil.sh', content: 'x' }],
  { verifySig, expectedCommit: 'c1', hashOf });
console.log(r.problems[0] === 'extra: evil.sh');
```

**评分点**：
- 短路优先级正确：签名 → commit → 文件级（信任链逐级验证）
- 文件校验三向：missing/tampered/extra（双向完整性）
- canonical payload 的签名剥离实现正确（signed 字段不参与验签）
- 能说清「可复现构建让证据链从『信任声明』升级为『验证声明』」属于加分
