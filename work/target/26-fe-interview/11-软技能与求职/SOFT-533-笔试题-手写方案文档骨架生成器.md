---
title: [SOFT-533] 手写方案文档骨架生成器：输入任务描述与约束，输出六段骨架与每段填写提示？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-533：手写方案文档骨架生成器：输入任务描述与约束，输出六段骨架与每段填写提示

**需求与边界**：
- 实现 genOutline(task)：输入 { title, kind: 'feature'|'migration'|'debt' }，输出含填写提示的六段骨架。
- 边界要求：① 按 kind 定制各段提示（migration 强制回退段/对账段，debt 强制成本证据段）；② 目标段强制要求可量化指标占位；③ 备选段强制至少 2 个备选占位；④ 输出 markdown 字符串；⑤ kind 未知抛错。

**答**：
```javascript
function genOutline({ title, kind }) {
  const kinds = ['feature', 'migration', 'debt'];
  if (!kinds.includes(kind)) throw new Error('BAD_KIND');
  const prompts = {
    feature: ['现状痛点（量化）', 'POC/同体量案例'],
    migration: ['双跑与对账设计', '回退步骤逐条验证'],
    debt: ['债务成本证据（故障归因/耗时统计）', '利息预测'],
  }[kind];
  return `# ${title} 技术方案
## 1 背景与问题
> 填写：${prompts[0]}，3段内，数据标出处
## 2 目标与指标
> 填写：成功指标（基线__ → 目标__，采集方式）；非目标
## 3 方案设计
### 3.1 架构图（一张图）
### 3.2 关键决策点（2~4个，各含理由）
### 3.3 备选方案
> 必填：方案B（激进）与方案C（保守），被否理由须可验证
> 附加提示：${prompts[1]}
## 4 风险与对策
> top3：具体场景+预警指标+预防+兜底+检查点
## 5 里程碑
> 每阶段：交付物+验证方式；依赖前置倒排
## 6 资源与排期
> 人力/依赖/排期表${kind === 'migration' ? '\n## 7 回退与对账\n> 迁移专属：双跑判定标准+回退数据处理的完整步骤' : ''}`;
}
```

**评分点**:
- 按 kind 定制提示（migration 强制回退对账/debt 强制证据）——模板差异化。
- 目标/备选段的强制占位（防"一条路方案"）。
- 未知 kind 抛错。

