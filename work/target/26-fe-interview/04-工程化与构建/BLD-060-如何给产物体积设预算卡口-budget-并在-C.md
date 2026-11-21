---
title: [BLD-060] 如何给产物体积设预算卡口（budget）并在 CI 中落地？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-060：如何给产物体积设预算卡口（budget）并在 CI 中落地？
**答**：
- 三层卡口：webpack performance 提示（构建时）、size-limit（基于真实 gzip/brotli 体积，可对具体文件设阈值）、CI diff（与基线分支 stats.json 比对，输出增量报告）。
- 预算制定：按"入口 js gzip 不超 X KB、单 chunk 不超 Y KB、vendor 增幅不超 Z%"分级，超出阻断或告警。
- size-limit 原理：按 entry 打一个最小化产物再压缩测体积，支持 CI 失败退出码。
- 报告形态：PR 评论贴 markdown 表（文件、体积、diff、是否超限），让业务同学在 review 时感知成本。

```json
// package.json：size-limit 预算
{
  "scripts": {
    "size": "size-limit"
  },
  "size-limit": [
    { "path": "dist/js/main.*.js", "limit": "180 KB", "gzip": true },
    { "path": "dist/js/vendors.*.js", "limit": "250 KB", "gzip": true },
    { "path": "dist/css/*.css", "limit": "50 KB", "gzip": true }
  ]
}
```

```yaml
# .github/workflows/size.yml：CI 卡口与 PR 报告
name: size-limit
on: [pull_request]
jobs:
  size:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm build
      - name: 体积预算检查
        run: pnpm size
      - name: 与基线 diff 报告
        run: node scripts/chunk-diff-report.js ./base-stats.json ./dist/stats.json
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 第九章 Module Federation（BLD-061 ~ BLD-068）
