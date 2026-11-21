---
title: [ARC-151] Prompt 资产管理架构（版本/评测/复用）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-151：Prompt 资产管理架构（版本/评测/复用）如何设计？
**答**：
- Prompt 即代码：prompt 模板入库（带模板变量、描述、适用场景、owner），走 PR review；版本不可变（tag），应用锁定版本引用，升级是显式变更。
- 评测回归：每个 prompt 关联评测集（输入 + 期望要点），prompt 或模型变更时自动跑评测，指标劣化阻断合并——没有评测的 prompt 迭代是玄学调参。
- 复用机制：中央 prompt 注册表按场景检索（任务类型/输入输出 schema/示例），相似场景复用模板而不是各写一份；公共片段（角色设定/输出格式约束）抽成可组合模块。
- 线上实验：prompt 版本支持 A/B（按流量灰度对比采纳率与人工反馈），数据反哺评测集。

```yaml
# Prompt 注册表条目（prompt 即代码）
prompts:
  - id: order-summary
    version: 1.3.0
    owner: trade-ai-group
    task_type: summarization
    template_file: prompts/order-summary@1.3.0.md     # 模板正文入库，支持 {{变量}}
    variables:
      - name: order_json
        type: json
        description: 订单结构化数据
      - name: audience
        type: enum [customer, cs]
    evaluation_set: evals/order-summary.jsonl          # 30 条标注样本
    eval_metrics: [coverage, tone, hallucination_rate]
    gate: "任一指标劣化 > 5% 阻断 prompt 合并"
    rollout:                                           # 线上 A/B
      control: 1.2.0    # 50%
      treatment: 1.3.0  # 50%
      success_criteria: "客服采纳率 + 3%，人工负反馈不升"
    usage: { locked_by: [cs-workbench, im-bot] }       # 应用锁定的版本清单
# 组合复用：公共片段 registry/shared/system-role.md，模板 include 引用，改一处全局生效（走评测）
```
