---
title: [AIC-573] 笔试：手写 AI 版权扫描器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-573：笔试：手写 AI 版权扫描

**答**：实现 `scanCopyright(code, { knownSnippets })`。knownSnippets: `{ id, snippet, license }[]`（已知许可证代码片段库）。规则：1) **许可证头检测**：GPL/Apache/MIT 头注释的存在——GPL → error（copyleft 污染）；Apache/MIT → warn（需要保留声明）；2) **代码片段匹配**：code 中包含 knownSnippets 的 snippet（子串匹配——简化版；生产应 AST 匹配）；3) **连续相似度**：code 中连续 10 行与 knownSnippet 的相似度 > 80% → 'similar-code'（近似复制——改了变量名但逻辑相同）；4) 返回 `{ findings: Array<{ type, license, severity }>, ok }`（ok = 无 error；GPL error 阻断）。边界：knownSnippets 空（只检查许可证头）；code 空（pass）；snippet 空字符串（跳过）。

```javascript
function scanCopyright(code = '', knownSnippets = []) {
  const findings = [];
  // 1) 许可证头检测
  const HEAD_PATTERNS = [
    { re: /GNU\s+General\s+Public\s+License/i, license: 'GPL', severity: 'error' },
    { re: /Apache\s+License/i, license: 'Apache-2.0', severity: 'warn' },
    { re: /MIT\s+License/i, license: 'MIT', severity: 'warn' },
  ];
  for (const p of HEAD_PATTERNS)
    if (p.re.test(code))
      findings.push({ type: 'license-header', license: p.license, severity: p.severity });
  // 2) 代码片段匹配
  for (const snip of knownSnippets) {
    if (!snip.snippet) continue;
    if (code.includes(snip.snippet))
      findings.push({ type: 'exact-match', license: snip.license, snippetId: snip.id,
        severity: snip.license === 'GPL' ? 'error' : 'warn' });
  }
  // 3) 连续相似度（简化：连续 10 行的 hash 比对）
  const codeLines = code.split('\n').map(l => l.trim()).filter(Boolean);
  for (const snip of knownSnippets) {
    const snipLines = snip.snippet?.split('\n').map(l => l.trim()).filter(Boolean) ?? [];
    if (snipLines.length < 10) continue;
    for (let i = 0; i + 10 <= codeLines.length; i++) {
      const window = codeLines.slice(i, i + 10);
      const matches = window.filter((l, j) => l === snipLines[j]).length;
      if (matches / 10 >= 0.8)
        findings.push({ type: 'similar-code', license: snip.license,
          snippetId: snip.id, line: i + 1,
          severity: snip.license === 'GPL' ? 'error' : 'warn' });
    }
  }
  return { findings, ok: !findings.some(f => f.severity === 'error') };
}

// 自测
const snippets = [
  { id: 'gpl-1', snippet: 'function gplSort(a, b) {\n  return a - b;\n}\n\nfunction helper() {\n  return 42;\n}\n\nfunction utils() {\n  return {}; }\n\nfunction more() {\n  return true;\n}\n\nfunction last() {\n  return null;\n}', license: 'GPL-3.0' },
  { id: 'mit-1', snippet: 'function mitSort(arr) { return arr.slice().sort(); }', license: 'MIT' },
];
// GPL 头
let r = scanCopyright('/* GNU General Public License v3 */\nconst x = 1;', snippets);
console.log(r.findings.some(f => f.type === 'license-header' && f.license === 'GPL' && f.severity === 'error'));
console.log(r.ok === false);                             // GPL error 阻断

// MIT 头 → warn
r = scanCopyright('/* MIT License */\nconst x = 1;', snippets);
console.log(r.findings.some(f => f.license === 'MIT' && f.severity === 'warn'));
console.log(r.ok === true);                              // warn 不阻断

// 无版权头 + 无匹配
r = scanCopyright('const x = 1;', snippets);
console.log(r.ok === true && r.findings.length === 0);

// 空代码
console.log(scanCopyright('', snippets).ok === true);
```

**评分点**：
- 双维检测：许可证头（GPL/Apache/MIT 的正则检测）+ 代码片段匹配（子串 + 连续相似度）
- GPL error 阻断 / Apache/MIT warn（copyleft vs permissive 的严重度差异）；连续相似度窗口（10 行滑动）
- 边界（空 code/空 snippets/无许可证头）；snippet 匹配的三种类型（header/exact/similar）
- 能说清「AI 代码的版权问题：训练数据泄露 = AI 复现 GPL 代码但无复制痕迹——AST/相似度匹配是唯一检测手段」属于加分
