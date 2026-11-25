---
title: [ENG-146] 文档站工程怎么选型与部署？dumi storybook vitepress 怎么取舍？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-146：文档站工程怎么选型与部署？dumi storybook vitepress 怎么取舍？
**答**：
- 按内容形态选型：组件库交互文档用 Storybook/dumi（组件沙箱 + props 自动生成）；指南与知识库用 VitePress（mdx 全文检索 构建快）。
- 工程要点：文档与代码同仓库同版本发布，组件改动必须带文档更新（CODEOWNERS 挂 docs 路径）。
- 部署走静态托管：main 合入自动构建发布，版本化路由保留旧版文档（/v2/），避免升级后老文档消失。
- 体验基线：全文检索 暗色模式 移动端可用，这三点决定文档站是被用还是被绕开。

```yaml
# .github/workflows/docs.yml —— VitePress 文档站自动构建部署
name: docs
on:
  push:
    branches: [main]
    paths: ['docs/**', 'src/components/**']
permissions:
  contents: read
  pages: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm docs:build          # vitepress build docs --base /design-system/
      - name: 死链检查
        run: node scripts/dead-link-check.mjs docs/.vitepress/dist
      - uses: actions/upload-pages-artifact@v3
        with: { path: docs/.vitepress/dist }
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: { name: github-pages, url: ${{ steps.deployment.outputs.page_url }} }
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```
