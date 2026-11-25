---
title: [ENG-148] 依赖升级策略怎么定？renovate 的分组与自动合并怎么配置？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-148：依赖升级策略怎么定？renovate 的分组与自动合并怎么配置？
**答**：
- 原则：升级常态化而非憋大招，每周小批量优于每年大爆炸；renovate 比 dependabot 更可定制（分组 调度 自动合并）。
- 分组策略：patch 与 dev 依赖测试通过自动合并；react 全家桶绑定成组整体升；安全修复走独立高优先级通道。
- 降噪：schedule 限定时段、rebaseWhen conflicted、并发 PR 限流，避免 CI 排队雪崩。
- Monorepo 联动：renovate 能感知 workspace 内部引用，内部包升级自动同步下游版本号。

```json
// renovate.json —— 升级分组与自动化策略
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended", ":semanticCommits"],
  "schedule": ["after 9pm every weekday"],
  "prConcurrentLimit": 5,
  "rebaseWhen": "conflicted",
  "packageRules": [
    {
      "description": "patch 与 dev 依赖 测试通过自动合并",
      "matchUpdateTypes": ["patch"],
      "matchDepTypes": ["devDependencies"],
      "automerge": true,
      "automergeType": "pr"
    },
    {
      "description": "react 全家桶绑定成组整体升级",
      "matchPackagePatterns": ["^react", "^@types/react"],
      "groupName": "react-family"
    },
    {
      "description": "安全修复独立通道 高优先级",
      "matchCurrentVersion": "!/^0/",
      "vulnerabilityAlerts": { "enabled": true },
      "labels": ["security"],
      "prPriority": 10
    }
  ]
}
```
