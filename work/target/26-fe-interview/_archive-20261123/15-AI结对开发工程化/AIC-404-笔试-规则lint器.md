---
title: [AIC-404] 笔试：实现一个「AI 产出规范检查器」，扫描代码中的违规模式并输出报告。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-404：笔试：实现一个「AI 产出规范检查器」，扫描代码中的违规模式并输出报告。
**题目**：给定规则 `[{name, pattern, severity, fix}]`，扫描源码逐文件输出违规行（行号+内容+建议修复），同文件同类规则最多报 3 条防刷屏。

```javascript
function lintAIOutput(files, rules) {
  const report = { blocking: [], comment: [] };
  for (const f of files) {
    const lines = f.content.split('\n');
    for (const r of rules) {
      let hits = 0;
      lines.forEach((line, i) => {
        if (hits >= 3) return;                       // 防刷屏
        if (r.pattern.test(line)) {
          hits++;
          const item = { file: f.path, line: i + 1, rule: r.name,
                         text: line.trim(), fix: r.fix };
          (r.severity === 'high' ? report.blocking : report.comment).push(item);
        }
      });
    }
  }
  return report;
}
const rules = [
  { name: 'no-hex-color', pattern: /#[0-9a-fA-F]{3,8}\b/, severity: 'high', fix: '用 design token' },
  { name: 'no-direct-fetch', pattern: /\bfetch\(/, severity: 'medium', fix: '走 src/api 层' },
];
console.log(lintAIOutput([{ path: 'a.tsx', content: 'const c = "#fff";\nfetch(url);\nfetch(u2);\nfetch(u3);\nfetch(u4);' }], rules));
// blocking: 1 条 hex；comment: fetch 只报 3 条

```

**评分点**：
- 用正则实现规则匹配，注意多行内容按行扫描。
- 同文件同规则限报条数（防刷屏）——体现报告可用性设计。
- severity 分级决定输出位置（blocking/comment），fix 建议必须非空才有价值。
- 测试含中文注释行与多匹配行。
