---
title: [BAS-190] conventional commits 怎么配合生成 changelog？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-190：conventional commits 怎么配合生成 changelog？
**答**：
- 提交格式 `type(scope): description`，type 决定版本号：feat 升 MINOR、fix 升 PATCH、`!` 或 body 里的 BREAKING CHANGE 升 MAJOR。
- 常用 type：feat/fix/docs/style/refactor/perf/test/chore，只有 feat/fix 参与用户可见的 changelog。
- 工具链：semantic-release 或 standard-version 读取提交历史，自动定版本、生成 CHANGELOG、打 tag。

```bash
git commit -m "feat(auth): 支持手机号登录"     # feat → MINOR
git commit -m "fix: 修复列表分页越界"          # fix → PATCH
git commit -m "feat!: 移除 v1 旧接口"          # ! → MAJOR 破坏性变更
# body 中写 BREAKING CHANGE: 说明迁移方式，效果等同 !
# semantic-release 按上述规则自动算版本并生成 CHANGELOG
```
