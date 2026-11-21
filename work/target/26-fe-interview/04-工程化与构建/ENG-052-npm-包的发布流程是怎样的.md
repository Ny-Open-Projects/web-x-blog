---
title: [ENG-052] npm 包的发布流程是怎样的？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-052：npm 包的发布流程是怎样的？
**答**：
- 前置检查：registry 指向官方源、npm login 状态、prepublishOnly 钩子跑通测试与构建。
- 用 npm version 递增版本并自动打 git tag；先发 prerelease 验证再发正式版。
- --dry-run 预演发布内容，确认 files 字段与 .npmignore 没把源码/测试打进包里。
- scope 包需要 --access public；发错版本不能覆盖，只能 deprecate 或撤回（72 小时内 unpublish）。

```bash
# 登录与预演
npm whoami
npm publish --dry-run

# 预发布版本：beta 标签，不影响 latest
npm version prerelease --preid=beta
npm publish --tag beta

# 正式发布
npm version patch   # 1.0.0 -> 1.0.1，同时打 git tag
npm publish

# scope 包首次发布需要公开
npm publish --access public
```
