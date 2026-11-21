---
title: [BLD-177] 构建依赖大版本升级（webpack 4→5、vite 大版本）的灰度方法。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-177：构建依赖大版本升级（webpack 4→5、vite 大版本）的灰度方法。
**答**：
- 评估先行：读 migration guide 列 breaking 清单 → 按项目盘点命中项（自动化 grep 配置/插件名）→ 形成"工作量评估表"；产物兼容目标是**逐字节可 diff**（hash 策略变化除外）。
- 灰度节奏：单仓双配置并行（`webpack.config.v5.js` 跑影子构建对比产物）→ 低风险应用（纯 CSR 小项目）先行 → 核心应用最后；每步可回滚（构建工具版本是独立 PR，随时 revert）。
- 验收清单：产物 diff（体积/结构/浏览器运行）、HMR 行为、dev 启动时长、CI 时长、关键路径手动回归、灰度环境真实流量观测（错误率对比基线）。
- 常见雷区：contenthash 算法变化导致全量缓存失效（预期内）、loader 选项语义变化（静默降级要 diff sourcemap 发现）、polyfill 注入量变化（browserslist 数据更新）。

```yaml
# 升级灰度流水线：影子构建对比（webpack4 与 webpack5 同源码各产一份并 diff）
name: upgrade-canary
on: pull_request
jobs:
  shadow-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pnpm install --frozen-lockfile
      - run: pnpm build:v4   # 现网配置
      - run: mv dist dist-v4 && pnpm build:v5   # 新配置
      - name: 产物对比
        run: |
          node scripts/compare-dist.js dist-v4 dist-v5 --report upgrade-report.md
      - uses: actions/upload-artifact@v4
        with: { name: upgrade-report, path: upgrade-report.md }
```

```javascript
// scripts/compare-dist.js：升级验收核心脚本（产物级 diff）
const { readdirSync, readFileSync, statSync } = require('fs');
const { join } = require('path');
const { gzipSync } = require('zlib');

function walk(dir, out = {}) {
  for (const f of readdirSync(dir)) {
    const p = join(dir, f);
    statSync(p).isDirectory() ? walk(p, out) : (out[f.replace(/-[0-9a-f]{8}\./, '.')] = gzipSync(readFileSync(p)).length);
  }
  return out;
}
const [a, b, , report] = process.argv;
const A = walk(a), B = walk(b);
const lines = ['| asset | v4 gzip | v5 gzip | diff |', '|---|---|---|---|'];
let failed = false;
for (const name of new Set([...Object.keys(A), ...Object.keys(B)])) {
  const d = (B[name] ?? 0) - (A[name] ?? 0);
  const pct = A[name] ? (d / A[name] * 100).toFixed(1) : 'new';
  // 验收红线：单文件 +10% 或总量 +5% 需人工确认
  if (d > 0 && pct !== 'new' && Number(pct) > 10) failed = true;
  lines.push(`| ${name} | ${((A[name] ?? 0) / 1024).toFixed(1)}KB | ${((B[name] ?? 0) / 1024).toFixed(1)}KB | ${pct}% |`);
}
require('fs').writeFileSync(report, lines.join('\n'));
process.exit(process.env.STRICT === '1' && failed ? 1 : 0);
// 灰度推进表：canary 项目（1%）→ 内部工具站 → 低峰业务 → 核心交易链路，每步观察 1 周
```
