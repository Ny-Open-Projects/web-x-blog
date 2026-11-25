---
title: [MP-393] 笔试：手写 CI 体积门禁脚本
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## MP-393：笔试：手写体积门禁

**答**：实现小程序体积门禁脚本 `sizeGate.js`：① 遍历构建产物 dist——按「主包/分包」统计体积（app.json 的 subpackages 解析边界）；② 预算校验：主包 <1.5MB、各分包 <1MB、总包 <12MB（超限 exit 1 阻断）；③ 增量报告：与基线对比（上次通过的产物快照——每包增减标注 TOP 文件）；④ 大文件清单（图片 >100KB 未压缩警告——进包资源治理）；⑤ 输出 markdown 报告（PR 评论格式）。写出实现。

```javascript
#!/usr/bin/env node
const fs = require('fs'), path = require('path');

function walk(dir, base = '') {
  const out = [];
  for (const f of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, f.name);
    if (f.isDirectory()) out.push(...walk(p, path.join(base, f.name)));
    else out.push({ file: path.join(base, f.name), size: fs.statSync(p).size });
  }
  return out;
}

function sizeGate({ dist, baseline, budgets }) {
  const appJson = JSON.parse(fs.readFileSync(path.join(dist, 'app.json')));
  const subRoots = (appJson.subpackages ?? []).map((s) => s.root);
  const files = walk(dist);
  const byPackage = { main: [] };
  for (const f of files) {
    const sub = subRoots.find((r) => f.file.startsWith(r));
    (byPackage[sub ?? 'main'] ??= []).push(f);
  }
  const report = [];
  let failed = false;
  for (const [pkg, fs2] of Object.entries(byPackage)) {
    const total = fs2.reduce((s, f) => s + f.size, 0);
    const budget = budgets[pkg === 'main' ? 'main' : pkg] ?? budgets.default;
    const over = total > budget;
    if (over) failed = true;
    // 增量对比
    const prevTotal = baseline?.[pkg] ?? 0;
    const top = fs2.sort((a, b) => b.size - a.size).slice(0, 5)
      .map((f) => `${f.file} (${(f.size / 1024).toFixed(0)}KB)`);
    const bigImgs = fs2.filter((f) => /\.(png|jpe?g)$/.test(f.file) && f.size > 100 * 1024);
    report.push(`### ${pkg}\n- 体积: ${(total / 1024).toFixed(0)}KB / 预算 ${(budget / 1024)}KB ${over ? '**超限**' : '✓'}\n- 增量: ${((total - prevTotal) / 1024).toFixed(0)}KB\n- TOP: ${top.join(', ')}\n- 大图警告: ${bigImgs.length}`);
  }
  console.log(report.join('\n'));
  process.exit(failed ? 1 : 0);
}
// CI: node sizeGate.js --dist dist --baseline baseline.json --budgets '{"main":1572864,"default":1048576}'
```

**评分点**：
- 分包边界解析（app.json subpackages → 归包统计）
- 预算校验 exit 1 阻断（CI 语义）
- 基线增量对比 + TOP 文件（劣化归因）
- 大图警告（进包资源治理）与 markdown 报告（PR 集成）
