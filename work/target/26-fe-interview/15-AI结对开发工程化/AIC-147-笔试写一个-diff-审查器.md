---
title: [AIC-147] 笔试：实现一个 diff 审查器，解析 unified diff、统计变更、按规则分级产出审查意见？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-147：笔试：实现一个 diff 审查器，解析 unified diff、统计变更、按规则分级产出审查意见？
**需求**：实现 `reviewDiff(diffText, rules)`：
1. 解析 unified diff：文件名、变更 hunk、每个 hunk 的行号范围（新文件侧）；
2. 对新增行（`+` 开头）逐行跑规则，产出 `{file, line, level, msg}`；
3. 汇总每文件变更量，产出 `danger` 标记（单文件新增 > 300 行或删除 > 50% 内容）；
4. 输出结构化意见列表，供 AI review 前置过滤。

```javascript
function parseDiff(text) {
  const files = [];
  let cur = null;
  for (const line of text.split('\n')) {
    const fm = line.match(/^diff --git a\/(.+?) b\/(.+)$/);
    if (fm) { cur = { file: fm[2], hunks: [], added: 0, deleted: 0 }; files.push(cur); continue; }
    const hm = line.match(/^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@/);
    if (hm && cur) cur.hunks.push({ newStart: +hm[1], lines: [] });
    if (cur && cur.hunks.length) {
      const h = cur.hunks.at(-1);
      if (line.startsWith('+') && !line.startsWith('+++')) { h.lines.push(line.slice(1)); cur.added++; }
      else if (line.startsWith('-') && !line.startsWith('---')) cur.deleted++;
      else if (h.lines) h.newStart += 1; // 上下文行推进行号
    }
  }
  return files;
}

const defaultRules = [
  { level: 'blocker', re: /(api[_-]?key|secret)\s*[:=]\s*['"][^'"]{8,}/i, msg: '疑似硬编码凭据' },
  { level: 'blocker', re: /\b(eval|new Function)\s*\(/, msg: '动态执行' },
  { level: 'suggestion', re: /console\.log\(/, msg: '遗留调试输出' },
  { level: 'suggestion', re: /\bas\s+any\b/, msg: '断言为 any' },
];

function reviewDiff(diffText, rules = defaultRules) {
  const findings = [];
  for (const f of parseDiff(diffText)) {
    if (f.added > 300 || (f.added > 50 && f.deleted > f.added * 2)) {
      findings.push({ file: f.file, line: 0, level: 'blocker', msg: `变更量异常：+${f.added}/-${f.deleted}，建议拆分 PR` });
    }
    for (const h of f.hunks) {
      h.lines.forEach((content, i) => {
        for (const r of rules) {
          if (r.re.test(content)) findings.push({ file: f.file, line: h.newStart + i, level: r.level, msg: r.msg });
        }
      });
    }
  }
  return findings;
}

// 测试
const d = `diff --git a/src/a.ts b/src/a.ts
@@ -1,2 +1,4 @@
 const x = 1;
+const key = 'sk-abcdefgh12345678';
+console.log('debug');
+console.log('debug2');`;
console.log(reviewDiff(d));
// blocker: 硬编码凭据；suggestion: 两处 console.log
```

**评分点**：
1. 行号计算：hunk 头的 `+start` 是新文件行号，上下文行与新增行都要推进计数，多数人漏掉上下文行推进；
2. 必须区分 `+`/`+++`（diff 头）与 `-`/`---`，误判会污染统计；
3. 规则命中在「新增行」而非全文件——只在新增行报错才符合增量审查语义；
4. 变更量危险标记（拆 PR）体现门禁意识；
5. 输出结构化（file/line/level/msg）可对接 AI review 意见流。
