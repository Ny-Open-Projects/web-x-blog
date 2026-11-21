---
title: [TST-124] 笔试：手写覆盖率门禁脚本（解析 lcov + 阈值 + 差异化配置）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-124：笔试：手写覆盖率门禁脚本（解析 lcov + 阈值 + 差异化配置）
**答**：
- 需求：实现 `coverageGate(lcovPath, thresholds)`——解析 lcov.info，按文件聚合四项指标，支持全局阈值 + glob 覆写（`src/utils/**` 更严）、`perFile`（任一文件不达标即失败）、输出未达标清单并以退出码 0/1 决定 CI 是否通过。
- lcov 格式关键记录：`SF:文件路径`、`LF:总行数`、`LH:命中行数`、`BRF:分支总数`、`BRH:命中分支数`、`FN/FNF/FNH` 函数。比率 = 命中/总数。
- 边界：文件无分支记录时 branch 率按 100%（分母为 0）；glob 匹配用 `picomatch`；阈值 > 100 或为负要校验报错。

```javascript
import { readFileSync } from 'node:fs';
import picomatch from 'picomatch';

function parseLcov(text) {
  const files = {};
  for (const rec of text.split('end_of_record')) {
    const get = (p) => +rec.match(new RegExp(`^${p}:(\\d+)`, 'm'))?.[1] ?? 0;
    const sf = rec.match(/^SF:(.+)$/m)?.[1];
    if (!sf) continue;
    files[sf] = {
      lines: [get('LF'), get('LH')],
      branches: [get('BRF'), get('BRH')],
      fns: [get('FNF'), get('FNH')],
    };
  }
  return files;
}

const rate = ([total, hit]) => (total === 0 ? 1 : hit / total);

function coverageGate(lcovPath, { global, overrides = {}, perFile = false } = {}) {
  const files = parseLcov(readFileSync(lcovPath, 'utf8'));
  const failed = [];
  const entries = Object.entries(files).map(([file, m]) => ({
    file,
    rates: { lines: rate(m.lines), branches: rate(m.branches), fns: rate(m.fns) },
  }));

  for (const { file, rates } of entries) {
    // glob 覆写优先于全局阈值
    const rule = Object.entries(overrides).find(([g]) => picomatch(g)(file))?.[1] ?? global;
    for (const [metric, min] of Object.entries(rule)) {
      const bad = perFile ? rates[metric] < min : false;
      if (bad) failed.push({ file, metric, actual: rates[metric], min });
    }
  }
  // 非 perFile：按全局聚合判断
  if (!perFile) {
    const agg = (k) => entries.reduce((s, e) => s + e.rates[k], 0) / entries.length;
    for (const [metric, min] of Object.entries(global)) {
      if (agg(metric) < min) failed.push({ file: '<aggregate>', metric, min });
    }
  }

  if (failed.length) {
    console.table(failed);
    process.exit(1); // CI 门禁失败
  }
  console.log('coverage gate passed');
}
// coverageGate('coverage/lcov.info', {
//   global: { lines: 0.75, branches: 0.7, fns: 0.7 },
//   overrides: { 'src/utils/**': { lines: 0.9, branches: 0.85 } },
//   perFile: true,
// });
```

**评分点**：
1. lcov 记录解析是否按 `end_of_record` 分块、正则用 multiline。
2. 分母为 0（无分支）是否按 100% 处理而非 NaN。
3. glob 覆写优先级与 perFile 语义实现正确。
4. 是否用 process.exitCode 让 CI 可接入 + 输出可读的失败明细。
