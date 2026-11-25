---
title: [ENG-145] ADR 实践怎么落地？架构决策记录的模板与流程怎么设计？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-145：ADR 实践怎么落地？架构决策记录的模板与流程怎么设计？
**答**：
- ADR 流程比模板更重要：提案（PR 评审）→ 决策（负责人确认）→ 归档（编号合并进 main）→ 状态演进 proposed/accepted/superseded/deprecated。
- 轻量模板四段：背景与问题、候选方案对比、决策与理由、后果与影响面，控制在一页，重在记录。
- 工具链用 adr-tools：new 自动编号并维护 supersede 关联，避免手工编号错乱。
- 判断标准：凡是三个月后有人会问为什么这么定的选择（选型 协议 目录 发布策略）都值得一条 ADR。

```bash
# adr-tools 落地：模板进仓库 决策随代码评审
# 1. 初始化 ADR 目录与编号
mkdir -p docs/adr && adr init 0001-采用-git-flow-分支模型

# 2. 新决策自动递增编号 s 参数声明替代旧决策
adr new 0009-构建工具从-webpack-迁移到-vite
adr new -s 0008 0010-样式方案改为-css-modules

# 3. CI 卡口：状态合法 proposed 超 30 天未决策提醒
node scripts/adr-lint.mjs docs/adr --max-proposed-age 30d
```
