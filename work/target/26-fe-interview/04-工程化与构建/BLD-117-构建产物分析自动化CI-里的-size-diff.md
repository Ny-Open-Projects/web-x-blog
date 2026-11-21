---
title: [BLD-117] 构建产物分析自动化：CI 里的 size diff bot 完整实现。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-117：构建产物分析自动化：CI 里的 size diff bot 完整实现。
**答**：
- 流程：PR 触发 CI → 构建（与基线同配置）→ 解析 `stats.json` 计算每个 chunk/asset 的 gzip 体积 → 与目标基线（main 分支最近一次构建产物）逐项 diff → 生成 Markdown 评论到 PR；超预算则 `exit 1` 卡口。
- 基线存储三选：GitHub artifact（按分支存最近产物）、远程缓存（turborepo 直接复用 main 的构建）、或独立产物仓库（OSS + manifest）；面试实现选 artifact 方案演示即可。
- 统计口径要对齐：**gzip 后体积**（贴近传输）、按 chunk 聚合、排除 contenthash 干扰（按 chunk 名聚合而非文件名）。
- 关键代码点：`stats.toJson({ assets: true, chunks: true })` 解析、`gzipSync` 计量、阈值配置（绝对增量 + 相对百分比双阈值）。

```javascript
// scripts/size-diff.mjs：PR 产物体积对比 bot（配合 GitHub Actions 使用）
import { readFileSync, existsSync } from 'node:fs';
import { gzipSync } from 'node:zlib';

const load = (p) => {
  const stats = JSON.parse(readFileSync(p, 'utf8'));
  const map = {};
  // 按 chunk 名聚合（消掉 contenthash），记 gzip 体积
  for (const asset of stats.assets) {
    if (!/\.(js|css)$/.test(asset.name)) continue;
    const key = asset.chunkNames?.[0] ?? asset.name.replace(/-[0-9a-f]{8,}\./, '.');
    const buf = readFileSync(`${process.env.DIST}/${asset.name}`);
    map[key] = (map[key] ?? 0) + gzipSync(buf).length;
  }
  return map;
};

const base = load('.size-baseline/stats.json');   // main 分支基线（CI 下载 artifact）
const head = load('dist/stats.json');
const LIMIT_ABS = 10 * 1024;                       // 绝对阈值 10KB
const LIMIT_PCT = 0.05;                            // 相对阈值 5%

const rows = [];
let failed = false;
for (const [chunk, size] of Object.entries(head)) {
  const before = base[chunk] ?? 0;
  const delta = size - before;
  const pct = before ? delta / before : 1;
  const bad = delta > LIMIT_ABS && pct > LIMIT_PCT; // 双阈值同时超才算违规，避免小文件误报
  if (bad) failed = true;
  rows.push(`| ${chunk} | ${(before / 1024).toFixed(1)} | ${(size / 1024).toFixed(1)} | ${(delta / 1024).toFixed(1)} | ${bad ? ':x:' : ':white_check_mark:'} |`);
}
const md = ['## Bundle Size Report', '', '| chunk | base(KB) | head(KB) | diff(KB) | status |', '|---|---|---|---|---|', ...rows].join('\n');
console.log(md);
// gh pr comment $PR_NUMBER --body-file <(node scripts/size-diff.mjs)
process.exit(process.env.STRICT === '1' && failed ? 1 : 0); // STRICT=1 时作为卡口
```

```yaml
# .github/workflows/size.yml（配合脚本）
name: size-diff
on: pull_request
jobs:
  size:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm build -- --json dist/stats.json
      - run: |
          id=$(gh run list -b main -w size-diff -s success -L1 --json databaseId -q '.[0].databaseId')
          gh run download $id -n size-baseline -D .size-baseline || echo '{}' > .size-baseline/none
        env: { GH_TOKEN: ${{ secrets.GITHUB_TOKEN }} }
      - run: node scripts/size-diff.mjs | tee size-report.md
      - run: gh pr comment ${{ github.event.number }} --body-file size-report.md
        env: { GH_TOKEN: ${{ secrets.GITHUB_TOKEN }} }
      - uses: actions/upload-artifact@v4
        with: { name: size-baseline, path: dist/stats.json }  # 为 main 提供下一条基线
```
