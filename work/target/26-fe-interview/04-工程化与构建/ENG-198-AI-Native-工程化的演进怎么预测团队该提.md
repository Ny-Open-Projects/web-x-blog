---
title: [ENG-198] AI Native 工程化的演进怎么预测？团队该提前做什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-198：AI Native 工程化的演进怎么预测？团队该提前做什么？
**答**：
- 阶段判断：当前是 AI 辅助（补全 按需调用）→ 下一阶段 AI 编排（agent 主导执行 人做验收）→ 远期 AI Native（流程以 AI 为一等公民设计）。
- 可预判变化：spec-driven 开发抬头（人写规格 AI 实现）、review 负载成为新瓶颈、度量单位从代码量转向验收通过的规格数。
- 提前做的基建：机器可读的仓库上下文、可作为验收规格的自动化 E2E、AI 操作审计留痕。
- 组织弹性：工具预测常会错，但人转向规格与验收角色的趋势相对确定，技能转型先于工具押注。

```yaml
# roadmap/ai-native.yaml —— AI Native 演进路线
phases:
  - stage: 辅助 copilot
    now: true
    capabilities: [代码补全, 单测生成, 代码解释]
    human_role: 编写与验收
  - stage: 编排 agent
    capabilities: [任务级生成, 自动修 CI, 重构代理]
    human_role: 拆解规格 验收与 review
    preconditions:
      - 仓库级上下文索引成熟        # 见 ENG-176
      - E2E 可作为机器可读验收规格
  - stage: ai-native
    capabilities: [spec-to-pr 全自动, 自愈流水线]
    human_role: 制定规格 评审重大决策
engineering_shift:
  - review 容量成为吞吐瓶颈 需要分级评审策略
  - 度量转向验收通过率与规格交付周期
  - 所有 AI 操作强制审计留痕
```
