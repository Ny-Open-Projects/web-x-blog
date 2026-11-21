---
title: [AGT-182] AI 正在重构前端，哪些模块会先被 AI 化？路径如何评估？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-182：AI 正在重构前端，哪些模块会先被 AI 化？路径如何评估？
**答**：
- 评估维度两条轴：交互不确定性（AI 输出可靠度）× 错误代价（错了多严重）——双低先 AI 化，双高最后。
- 先行模块：内容生成类（文案/邮件/商品描述）、辅助输入类（智能搜索/表单自动填充/代码补全）、总结摘要类（会话纪要/变更日志）——错误可被用户一眼纠正。
- 中期模块：数据分析（Text2BI）、客服（有 RAG 兜底 + 人工升级）、测试生成（有验证闭环）。
- 滞后模块：支付/权限/鉴权等安全关键路径、强实时强一致的协同核心——AI 只能做旁路辅助（生成测试用例、审查 diff），不能接管执行。
- 落地路径评估法：对每个模块打分（可靠度、可验证性、回滚成本、用户预期），输出「AI 化优先级矩阵」，而不是拍脑袋追热点。

```typescript
// AI 化优先级评估矩阵
interface ModuleProfile {
  name: string;
  aiReliability: number;      // AI 输出可靠度 0-1（评测集数据）
  verifiability: number;      // 可验证性 0-1（能否程序化校验输出）
  errorCost: number;          // 错误代价 0-1（1 = 不可逆/涉资金）
  userExpectation: number;    // 用户对 AI 化的预期 0-1
}

export function prioritizeAi(modules: ModuleProfile[]) {
  return modules
    .map((m) => {
      // 优先级 = 价值（可靠度×预期）÷ 风险（错误代价×不可验证性）
      const value = m.aiReliability * 0.6 + m.userExpectation * 0.4;
      const risk = m.errorCost * (1 - m.verifiability) + m.errorCost * 0.3;
      const score = value - risk * 0.8;
      const phase = score > 0.55 ? 'phase-1 立即 AI 化'
        : score > 0.35 ? 'phase-2 试点（HITL 兜底）'
        : 'phase-3 暂缓（仅旁路辅助）';
      return { name: m.name, score: Number(score.toFixed(2)), phase };
    })
    .sort((a, b) => b.score - a.score);
}

// 示例：典型前端模块的评估结果
const modules: ModuleProfile[] = [
  { name: '营销文案生成',   aiReliability: 0.9, verifiability: 0.5, errorCost: 0.1, userExpectation: 0.9 },
  { name: '表单智能填充',   aiReliability: 0.8, verifiability: 0.7, errorCost: 0.2, userExpectation: 0.8 },
  { name: '客服问答',       aiReliability: 0.75, verifiability: 0.6, errorCost: 0.3, userExpectation: 0.85 },
  { name: '支付流程自动化', aiReliability: 0.85, verifiability: 0.9, errorCost: 1.0, userExpectation: 0.3 },
];
// 输出排序后即得 AI 化路线图：文案 → 填充 → 客服 → 支付仅旁路
```
