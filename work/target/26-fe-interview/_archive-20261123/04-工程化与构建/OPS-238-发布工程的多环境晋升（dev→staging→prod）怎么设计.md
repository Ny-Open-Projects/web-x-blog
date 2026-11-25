---
title: [OPS-238] 多环境晋升（dev→staging→prod 晋升链）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## OPS-238：多环境晋升怎么设计？
**答**：
- 晋升链设计：同一产物晋升（dev 构建一次，产物沿链晋升）而非每环境重新构建——重新构建会破坏「测过什么就上什么」（SCN-ENG-222 可复现）。
- 晋升门禁：每级晋升有独立门禁（staging 冒烟 + 性能基线 → prod 门禁），晋升是显式动作（自动触发但可卡点）。
- 环境差异最小化：staging 与 prod 的差异仅限数据与规模（配置一致）——环境差异越大，「staging 绿 prod 挂」越频繁（SCN-ENG-237 漂移治理）。
- 晋升节奏：dev 可随时（自动化），staging 定时（每日一次聚合），prod 走发布窗口——节奏递减、成本递增。
- 追问钩子：为什么「构建一次、产物晋升」优于「每环境重新构建」——重新构建意味着 staging 测的产物与 prod 部署的产物可能不同（依赖漂移/环境差异入构建）；同一 hash 产物晋升才能宣称「测过即所上」，这是发布可信度的根基。

```yaml
promotion:
  artifact: build-once-promote   # dev 构建 → hash 晋升
  gates:
    staging: [smoke, perf-baseline, config-drift-check]
    prod: [release-window, risk-leveling, gates-229]
  cadence: { dev: on-merge, staging: daily, prod: window-based }
```
