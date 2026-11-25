---
title: [TST-563] 笔试：笔试：AI 生成用例的三检闸门
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-563：笔试：笔试：AI 生成用例的三检闸门

**题目**：实现 triageGate(cases, opts)。cases=[{id, name, code, tags, source:'ai'|'human'}]。opts={ minAssertions:1, forbidTags:['skip','todo'], dupThreshold:0.9 }。要求：① 仅对 source==='ai' 的用例执行三检：语法可编译（粗略：含 function/it/test 关键字且花括号配对）、断言数量 >= minAssertions、含 forbidTags 任一则拒绝；② 重复检测：与已有机 cases 的名称 Jaccard 相似度 >= dupThreshold 判重复（已有 cases 作为第二参数 existing）；③ 输出 {accepted, rejected:[{id, reasons:[]}]}；④ 边界：空 cases、existing 为空。

**答**：
- 结论：对 AI 用例依次跑「语法/断言/标签/查重」四道检查，收集所有失败原因后分流。
- 实现要点：花括号配对用计数；断言数用正则；Jaccard 基于名称字符集合；人工用例直接放行（但可选记录）。
- 追问钩子：粗粒度语法检查不够怎么办？——接入真实 parser（Babel/TS Compiler API）做 AST 级校验，并加沙箱试跑，成本更高但更可靠。

```javascript
function triageGate(cases = [], existing = [], opts = {}) {
  const { minAssertions = 1, forbidTags = ['skip', 'todo'], dupThreshold = 0.9 } = opts;
  const accepted = [], rejected = [];
  const nameSet = new Set(existing.map(c => c.name));
  const jaccard = (a, b) => {
    const A = new Set(a), B = new Set(b);
    const inter = [...A].filter(x => B.has(x)).length;
    return new Set([...A, ...B]).size ? inter / new Set([...A, ...B]).size : 0;
  };
  for (const c of cases) {
    if (c.source !== 'ai') { accepted.push(c); continue; }
    const reasons = [];
    const braces = (c.code.match(/{/g) || []).length - (c.code.match(/}/g) || []).length;
    if (braces !== 0 || !/(function|\bit\(|\btest\()/.test(c.code)) reasons.push('syntax');
    if ((c.code.match(/expect\(/g) || []).length < minAssertions) reasons.push('assertions');
    if ((c.tags || []).some(t => forbidTags.includes(t))) reasons.push('forbidden-tag');
    if ([...nameSet].some(n => jaccard(c.name, n) >= dupThreshold)) reasons.push('duplicate');
    (reasons.length ? rejected : accepted).push(reasons.length ? { id: c.id, reasons } : c);
  }
  return { accepted, rejected };
}
```

**评分点**：
- 仅对 source==='ai' 执行检查，人工用例直接放行。
- 语法/断言/标签/查重四检齐全，收集全部 reasons。
- Jaccard 相似度查重正确，阈值可配。
- 空输入与 existing 为空等边界安全，输出分流结构清晰。
