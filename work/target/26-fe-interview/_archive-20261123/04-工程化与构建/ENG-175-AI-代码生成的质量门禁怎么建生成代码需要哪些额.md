---
title: [ENG-175] AI 代码生成的质量门禁怎么建？生成代码需要哪些额外检查？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-175：AI 代码生成的质量门禁怎么建？生成代码需要哪些额外检查？
**答**：
- AI 生成代码不能降标准而要加标准：典型问题（幻觉 API、复制粘贴重复、过度防御、无效注释）要有针对性检查项。
- 落地方式：AI 生成 PR 打 ai-generated 标签，CI 对该类 PR 加码——覆盖率阈值上调、重复度检查（jscpd）、依赖白名单校验。
- prompt 侧预防：生成时约束"禁止引入未声明依赖、优先复用 utils 已有函数"，从源头减少坏味道。
- 人审不豁免：AI PR 禁止 self-merge，至少一名人类实质 review。

```yaml
# .github/workflows/ai-pr-gate.yml —— AI 生成 PR 的加码门禁
name: ai-pr-gate
on:
  pull_request:
    types: [labeled, opened, synchronize]
jobs:
  gate:
    if: contains(github.event.pull_request.labels.*.name, 'ai-generated')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - name: 覆盖率加码 AI PR 行覆盖 85%
        run: pnpm test --coverage --coverage.thresholds.lines=85
      - name: 重复度检查
        run: npx jscpd src --min-tokens 60 --reporters consoleFull --fail-on-mismatch
      - name: 禁止越权依赖
        run: node scripts/check-deps-whitelist.mjs
```
