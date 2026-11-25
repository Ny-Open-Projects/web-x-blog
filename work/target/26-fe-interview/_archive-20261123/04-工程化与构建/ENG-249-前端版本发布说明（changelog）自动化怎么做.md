---
title: [ENG-249] Changelog 与发布说明自动化怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-249：Changelog 自动化怎么做？
**答**：
- 单源输入：conventional commits（feat/fix/breaking）由 CI 校验提交格式，changelog 从提交历史生成——手写 changelog 必然遗漏与漂移。
- 分层输出：包级 changelog（消费方视角：API 变化/迁移指引）+ 应用级 release note（用户视角：功能列表/截图）——两种受众两种文档。
- breaking 强制块：BREAKING CHANGE 提交必须附迁移说明，缺块 CI 拒绝（发布质量门禁）。
- 自动化链：merge 到 main → changesets 聚合 → 版本 PR（changelog 预览）→ merge 后自动发布（ENG-204 联动）。
- 追问钩子：为什么「应用级 release note」不能从 commits 生成——commits 是工程师视角（"refactor store"），用户关心「这次更新我能感知什么」；用户视角需要产品语言改写，模板 + 人工润色混合最实际。

```bash
# commitlint 强制 conventional
echo "module.exports = { extends: ['@commitlint/config-conventional'] }" > commitlint.config.js
# BREAKING 强制迁移说明
if grep -q "BREAKING CHANGE" "$1" && ! grep -q "MIGRATION" "$1"; then exit 1; fi
```
