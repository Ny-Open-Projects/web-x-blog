---
title: [SCN-174] 几十个前端仓库依赖升级全靠人肉，如何用机器人（Renovate）建立自动化升级流水线？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-174：几十个前端仓库依赖升级全靠人肉，如何用机器人（Renovate）建立自动化升级流水线？
**答**：
- 分级策略是关键：patch/minor 自动合并（有测试保护的前提下），major 建单独 MR + 指定 owner 评审；安全补丁最高优先级立即升。
- 合并门槛写进配置：CI 必须全绿（lint/单测/build/e2e 冒烟），锁文件由机器人维护，人不手改。
- 噪声治理：`schedule` 错峰（每周固定窗口批量处理），`automerge` 白名单限定低风险依赖（types、eslint 插件类），框架级依赖（react/vue）永远人工。
- 升级信息要带上下文：MR 描述带 changelog 与 breaking changes 链接，评审人只做判断不做考古。

```yaml
# renovate.json（JSON 即合法 YAML）：分级自动升级策略
{
  "extends": ["config:recommended", ":semanticCommits"],
  "timezone": "Asia/Shanghai",
  "schedule": ["after 10am and before 4pm every weekday"],  # 错峰：工作时段批量处理
  "packageRules": [
    {
      "description": "安全补丁最高优先级立即升级",
      "matchUpdateTypes": ["patch"],
      "matchDepTypes": ["dependencies"],
      "vulnerabilityAlerts": { "labels": ["security"] },
      "automerge": true,
      "automergeType": "pr"
    },
    {
      "description": "低风险 devDependencies 自动合并",
      "matchDepTypes": ["devDependencies"],
      "matchUpdateTypes": ["patch", "minor"],
      "automerge": true,
      "matchPackagePatterns": ["@types/", "eslint-", "prettier"]
    },
    {
      "description": "框架级 major 永远人工：单独 MR 加评审人与升级清单",
      "matchPackagePatterns": ["^react$", "^vue$", "^vite$", "^typescript$"],
      "automerge": false,
      "reviewers": ["team:frontend-core"],
      "labels": ["major-upgrade"],
      "prBodyNotes": ["请对照迁移指南升级，并跑全量 e2e"]
    },
    {
      "description": "限制并发 MR 数量，防升级风暴",
      "prConcurrentLimit": 5,
      "branchConcurrentLimit": 10
    }
  ],
  "lockFileMaintenance": { "enabled": true, "schedule": ["before 6am on monday"] }
}
```
