---
title: [ENG-170] CI 中的安全扫描全家桶怎么搭？依赖 密钥 SAST 怎么组合？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-170：CI 中的安全扫描全家桶怎么搭？依赖 密钥 SAST 怎么组合？
**答**：
- 三层扫描一次 PR 全跑：依赖漏洞（npm audit/osv-scanner）、密钥泄露（gitleaks）、代码缺陷（Semgrep SAST）。
- 结果分流：critical 阻断合并、high 限期修复、low 报表；设置 baseline 防止历史问题淹没新问题。
- 误报治理：扫描器都要有豁免机制（ignore 文件 + 豁免带过期时间），豁免本身要 review。
- 性能折中：PR 增量扫描 + 每晚定时全量扫描，是耗时与覆盖的标准平衡。

```yaml
# .github/workflows/security.yml —— 依赖 密钥 SAST 全家桶
name: security
on:
  pull_request:
  schedule: [{ cron: '0 18 * * *' }]   # 每晚全量兜底
jobs:
  deps-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pnpm install --frozen-lockfile
      - run: pnpm audit --prod --audit-level high
  secrets-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }        # 全历史扫描
      - uses: gitleaks/gitleaks-action@v2
        env: { GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} }
  sast:
    runs-on: ubuntu-latest
    container: semgrep/semgrep
    steps:
      - uses: actions/checkout@v4
      - run: semgrep ci --config p/owasp-top-ten
```
