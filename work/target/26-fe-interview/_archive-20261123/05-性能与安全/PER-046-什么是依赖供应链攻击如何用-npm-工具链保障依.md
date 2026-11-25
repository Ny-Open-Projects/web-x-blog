---
title: [PER-046] 什么是依赖供应链攻击？如何用 npm 工具链保障依赖安全？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-046：什么是依赖供应链攻击？如何用 npm 工具链保障依赖安全？

**答**：
- 供应链攻击：恶意代码藏在依赖包或其新版本中（如 typosquatting 假包、维护者账号被盗推投毒版本、postinstall 脚本执行恶意代码）。
- 防线一：`package-lock.json` 提交入库并锁定精确版本，安装用 `npm ci` 保证环境一致。
- 防线二：CI 里跑 `npm audit --audit-level=high` 卡点；无法自动修复的传递依赖用 `overrides` 强制钉版本。
- 防线三：新依赖先查下载量/维护状态；用 Renovate/Dependabot 定期更新；锁 postinstall 或用 `--ignore-scripts` 审查后再装。

```bash
# 审计依赖漏洞，存在达到阈值的漏洞时退出码非 0，CI 直接失败
npm audit --audit-level=high

# 查看漏洞详情与修复建议
npm audit

# 自动升级到无破坏性的修复版本（同步更新 package-lock.json）
npm audit fix

# 无法自动修复时，用 overrides 强制替换存在漏洞的传递依赖
npm pkg set 'overrides.lodash=^4.17.21'

# CI 安装必须用 npm ci：严格按 lockfile 安装，防止依赖漂移
npm ci
```
