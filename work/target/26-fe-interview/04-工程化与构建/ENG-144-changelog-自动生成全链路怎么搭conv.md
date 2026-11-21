---
title: [ENG-144] changelog 自动生成全链路怎么搭？conventional-changelog 与 release 工具怎么选？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-144：changelog 自动生成全链路怎么搭？conventional-changelog 与 release 工具怎么选？
**答**：
- 全链路：Conventional Commits 提交规范 → commitlint 卡口 → release-it/semantic-release 按提交类型推导版本 → 生成 CHANGELOG → 发版打 tag。
- 规则映射：fix 到 patch、feat 到 minor、feat! 或 BREAKING CHANGE 到 major，人的责任只剩提交写规范。
- changelog 按 scope 分组展示；给业务方的升级指南单独手写，自动生成的放 CHANGELOG.md。
- Monorepo 用 changesets：以变更集文件为粒度累积，PR review 时一起审，发布时按包各自 bump。

```json
// release-it.config.json —— conventional-changelog 全链路配置
{
  "$schema": "https://unpkg.com/release-it/schema/release-it.json",
  "git": { "commitMessage": "chore: release ${version}", "tagName": "v${version}" },
  "npm": { "publish": true },
  "github": { "release": true, "releaseNotes": "npx conventional-changelog --stdin" },
  "plugins": {
    "@release-it/conventional-changelog": {
      "preset": "angular",
      "infile": "CHANGELOG.md"
    }
  },
  "hooks": {
    "before:init": ["pnpm lint", "pnpm test"],
    "after:bump": "pnpm build"
  }
}
```
