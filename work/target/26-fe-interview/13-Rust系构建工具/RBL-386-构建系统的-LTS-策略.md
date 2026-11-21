---
title: [RBL-386] 构建工具的 LTS（长期支持）版本策略
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-386：构建工具的 LTS 版本策略

**答**:
- LTS 价值：企业用户需要稳定承诺（安全补丁不发新特性）——LTS = 某个 minor 冻结 + 只发安全/关键修复
- 支撑成本：多版本并行维护（bug fix 要 cherry-pick 到 LTS 分支）——LTS 数量控制（最多 1-2 个并行），过期 LTS 明确 EOL 日期
- 选择标准：LTS 候选 = 被大量生产使用的版本（采纳数据驱动）——不是每个 minor 都值得 LTS
- 团队内应用：内部 preset 的 LTS 语义（锁定版本 + 只修不升，升级走专项）——企业内部工具的 LTS 是稳定承诺

```text
LTS = 冻结 minor + 安全补丁 cherry-pick + EOL 日期
成本：多版本并行维护；选择：采纳数据驱动
内部映射：preset 锁版本只修不升
```
