---
title: [AIC-523] 笔试：手写 AI 规范一致性审计
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-523：笔试：手写 AI 规范一致性审计

**答**：实现 `auditStyleConsistency(code, rules)`。rules: `{ noAny?: boolean, requireZod?: boolean, preferFunction?: boolean, noClassComp?: boolean }`。规则：1) noAny：检测 `: any` / `as any` / `<any>` → violation；2) requireZod：有 POST/PUT handler 但无 `.parse(` → violation；3) preferFunction：检测 `class X extends React.Component` → violation（应使用函数组件）；4) noClassComp：同上（别名）；5) provenance 检查：AI 生成的代码如果有 violation → severity 'error'（AI 应遵守规范）；人写的 violation → 'warn'（人可能有自己的理由）。返回 `{ violations: Array<{ rule, line, severity }>, ok }`（ok = 无 error）。边界：空 code；rules 全 false（无检查）；全 human 代码的 violation（warn 不阻断）。

```javascript
function auditStyleConsistency(code = '', rules = {}) {
  const findings = []; let provenance = 'human';
  if (/provenance:\s*ai/.test(code)) provenance = 'ai';
  const severity = provenance === 'ai' ? 'error' : 'warn';
  code.split('\n').forEach((line, i) => {
    const n = i + 1;
    if (rules.noAny && /:\s*any\b|\bas\s+any\b/.test(line))
      findings.push({ rule: 'noAny', line: n, severity });
    if (rules.requireZv || rules.requireZod) {
      if (/(?:POST|PUT|PATCH)\s*(?:req|request)/i.test(line) || /export\s+async\s+function\s+(?:POST|PUT|PATCH)/.test(line)) {
        // 检查同文件是否有 zod parse
        if (rules.requireZod && !code.includes('.parse(') && !code.includes('.safeParse('))
          findings.push({ rule: 'requireZod', line: n, severity });   // 同文件级别只报一次
      }
    }
    if ((rules.preferFunction || rules.noClassComp) && /class\s+\w+\s+extends\s+(?:React\.)?Component/.test(line))
      findings.push({ rule: 'noClassComp', line: n, severity });
  });
  // requireZod 去重
  const deduped = findings.filter((f, i, arr) =>
    arr.findIndex(x => x.rule === f.rule) === i || f.rule !== 'requireZod');
  return { violations: deduped, ok: !deduped.some(f => f.severity === 'error') };
}

// 自测
// AI 代码有 any → error
const aiCode = `// provenance: ai-assisted
const data: any = fetch();`;
let r = auditStyleConsistency(aiCode, { noAny: true });
console.log(r.violations[0].severity === 'error');
console.log(r.ok === false);

// 人写代码有 any → warn
const humanCode = `const data: any = legacy();`;
r = auditStyleConsistency(humanCode, { noAny: true });
console.log(r.violations[0].severity === 'warn');
console.log(r.ok === true);                              // warn 不阻断

// class component → violation
r = auditStyleConsistency('class Foo extends React.Component {}', { noClassComp: true });
console.log(r.violations.some(v => v.rule === 'noClassComp'));

// 空
console.log(auditStyleConsistency('', { noAny: true }).violations.length === 0);
console.log(auditStyleConsistency('const x = 1;', {}).violations.length === 0);
```

**评分点**：
- provenance 驱动 severity（AI violation = error 阻断 / 人 violation = warn 不阻断——AI 更应遵守规范）
- 四条规则检查（noAny/requireZod/preferFunction/noClassComp）；requireZod 去重
- 边界（空 code/空 rules/全 human）；provenance 检测
- 能说清「AI 生成的代码违反规范 = AI 的错（error 阻断）vs 人写的违规 = 人的选择（warn）——AI 应更严格遵守规范」属于加分
