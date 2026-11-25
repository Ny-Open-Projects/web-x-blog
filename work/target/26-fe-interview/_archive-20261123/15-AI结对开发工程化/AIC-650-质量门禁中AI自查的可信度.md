---
title: [AIC-650] 门禁里让 AI「自查」代码可信吗？自评和他评差在哪？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-650：门禁里让 AI「自查」代码可信吗？自评和他评差在哪？

**答**：
- 结论先行：**AI 自查（让生成代码的同一个模型判断自己代码有没有问题）可信度很低——它对自己错误的盲区和生成时一样**。门禁里 AI 自查只能当「快速筛查」，不能当「放行依据」。
- 自评为什么不可信：1) **同源盲区**：生成时没考虑到的边界，自查时同样想不到（同一套权重、同一段上下文）；2) **确认偏误**：AI 倾向于论证「我的代码是对的」，会为可疑逻辑找合理解释（AIC-615 解释性债务）；3) **示例**：让 AI 给自己的代码打分，几乎总是高分。
- 他评（换模型/换 prompt 角色）为什么更好：1) **异质盲区**：不同模型/不同训练数据的盲点不重叠，能发现同源看不出的问题（AIC-048 交叉审查）；2) **对抗性视角**：用「审查者」system prompt + 明确「找出至少 3 个问题」的指令，把 AI 从「辩护」切到「挑刺」模式。
- 门禁设计：自查 → 他评 → 确定性工具（ESLint/类型/测试）三级；确定性工具是最终底线，AI 他评是主力，AI 自查只做初筛降噪。
- 追问钩子：为什么「确定性工具」比「他评 AI」更该做最终底线？——因为工具是 100% 确定的（类型错误就是错误），而 AI 他评仍是概率的（可能误报/漏报）；把确定性的检查放在最后一道，保证「至少这些绝对不会漏」，概率检查只能锦上添花。

```typescript
type ReviewLevel = { name: string; trustworthy: number; role: string };

function buildGate(useSelfReview: boolean): ReviewLevel[] {
  const gate: ReviewLevel[] = [
    { name: 'self-review', trustworthy: 0.3, role: '初筛降噪（不可作放行依据）' },
    { name: 'cross-review', trustworthy: 0.7, role: '异质模型挑刺（主力）' },
    { name: 'deterministic', trustworthy: 1.0, role: 'ESLint/类型/测试（最终底线）' },
  ];
  return useSelfReview ? gate : gate.filter(g => g.name !== 'self-review');
}

const gate = buildGate(true);
console.log(gate[0].trustworthy < gate[2].trustworthy); // 自查 < 确定性工具
console.log(gate.find(g => g.name === 'deterministic').role.includes('底线'));
```
