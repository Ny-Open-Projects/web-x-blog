---
title: [TST-117] 增量覆盖率（diff coverage）怎么实现？为什么比全量门禁合理？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-117：增量覆盖率（diff coverage）怎么实现？为什么比全量门禁合理？
**答**：
- 为什么增量更合理：存量代码没有测试是历史债，一刀切卡 80% 只会逼团队「要么刷假测试要么绕过门禁」；增量策略是「旧债不追究，新代码必须干净」——棘轮式（ratchet）让整体水位只升不降。
- 实现三步：① 从 Git 拿 PR 的 diff（`git diff origin/main...HEAD`）解析出每个文件新增的行号区间；② 读覆盖率报告（lcov/istanbul json），取这些行上的命中信息（`BRDA`/`DA` 记录）；③ 命中行/新增行 = 增量覆盖率，低于阈值 fail CI 并在 PR 评论明细。
- 现成工具：`solidoc/diff-cover`（Python CLI，支持 lcov/xml），前端可直接用；或自研 Node 脚本（面试笔试题高频：手写 diff coverage 计算，见 TST-155）。
- 细节坑：diff 行号要区分新旧文件的行号基准（覆盖率报告里的行号是「新文件」的）；重命名/移动文件要 diff 相似度匹配；删掉的行不计入分母。
- 追问钩子：怎么把棘轮和增量结合？——增量阈值 80% 起，每季度上调 2%；同时全量覆盖率不许比上个季度末低。

```javascript
// scripts/diff-coverage.mjs —— 核心：新增行 × 覆盖行 交集
import { execSync } from 'node:child_process';
import { readFileSync } from 'node:fs';

// 1) 新增行号：unified diff 解析（简化）
const diff = execSync('git diff origin/main...HEAD -U0 -- "*.ts" "*.tsx"', { encoding: 'utf8' });
const added = {}; // file -> [lineNo...]
let cur = null;
for (const l of diff.split('\n')) {
  const h = l.match(/^\+\+\+ b\/(.+)/); if (h) cur = h[1];
  const r = l.match(/^@@ -\d+(,\d+)? \+(\d+)(,(\d+))?/);
  if (r && cur) for (let i = +r[2]; i < +r[2] + (+r[4] || 1); i++) (added[cur] ||= []).push(i);
}

// 2) lcov 命中行
const lcov = readFileSync('coverage/lcov.info', 'utf8').split('end_of_record');
const hit = {}; // file -> Set(hitLines)
for (const rec of lcov) {
  const f = rec.match(/^SF:(.+)/m)?.[1]; if (!f) continue;
  hit[f] ||= new Set();
  for (const m of rec.matchAll(/^DA:(\d+),[1-9]/gm)) hit[f].add(+m[1]); // count>0
}

// 3) 计算
let total = 0, covered = 0;
for (const [file, lines] of Object.entries(added)) {
  const h = hit[file] ?? new Set();
  for (const ln of lines) { total++; if (h.has(ln)) covered++; }
}
const rate = total ? (covered / total * 100).toFixed(1) : '100.0';
console.log(`diff coverage: ${rate}% (${covered}/${total})`);
process.exit(+rate < 80 ? 1 : 0); // 门禁：低于 80% fail
```
