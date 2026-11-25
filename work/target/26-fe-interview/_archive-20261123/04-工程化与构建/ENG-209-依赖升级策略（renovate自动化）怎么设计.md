---
title: [ENG-209] 依赖升级的自动化策略（Renovate 分级）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-209：依赖升级自动化怎么设计？
**答**：
- 分级策略：patch/minor 自动合并（CI 绿即合）、major 建 PR 人工评审、安全补丁即时合并（override 一切限制）——自动化程度与风险成反比。
- 升级节奏：批量升级（每周一次聚合 PR）减少 CI 压力与 review 噪声；安全更新例外即时。
- 风险评估：升级 PR 自动跑受影响包测试 + bundle size diff + 关键路径 E2E——数据进 PR 描述供 review 判断。
- 锁定与豁免：战略依赖（React/Vite 大版本）白名单锁定节奏；不再维护的包标 deprecated 推进替换。
- 追问钩子：为什么 patch 也要跑测试而不是直接合——patch 也可能引入行为变化（依赖作者的「修复」破坏你的隐式依赖）；自动化程度高不等于验证省略，CI 绿是所有级别的前提。

```jsonc
// renovate.json —— 分级策略
{
  "packageRules": [
    { "matchUpdateTypes": ["patch", "minor"], "automerge": true, "automergeType": "pr" },
    { "matchUpdateTypes": ["major"], "dependencyDashboardApproval": true },
    { "matchPackageNames": ["react", "vite"], "rangeStrategy": "pin", "separateMajorMinor": true },
    { "matchDepTypes": ["devDependencies"], "automerge": true, "groupSlaveSchedule": ["weekly"] },
    { "matchDatasources": ["npm"], "vulnerabilityAlerts": { "enabled": true } }
  ]
}
```
