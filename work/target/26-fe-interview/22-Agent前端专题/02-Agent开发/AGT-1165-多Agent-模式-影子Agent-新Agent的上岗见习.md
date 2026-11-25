---
title: [1165] 新 Agent「影子见习」期怎么设计
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 运营]
type: 面试题
---

## 1165：新 Agent「影子见习」期怎么设计

**答**：
- 见习三阶段：影子期（影子跑不采用，只对比旧实现 diff，2 周）、灰度期（接 5%→50% 流量，旧实现热备随时回落）、转正期（旧实现保留一个观察月后下线）。
- 影子期的验收数据：与旧实现的「决策一致率」（同任务同决策比例）、分歧样本的人工评审（分歧里新对的占多少——新实现有没有真提升）、成本与延迟对比。
- 转正标准前置声明：一致率 ≥ 目标值 + 分歧评审新实现胜率 ≥ 50% + 成本不劣化，三个数字写在见习计划里，达标自动提权，避免「感觉差不多了」。
- 追问钩子：影子期发现的分歧全是新实现更好，能不能立刻全量？——不行：一致率低说明「行为面」变化大，未在样本里的场景风险未知；先灰度收集真实分布再提权。

```ts
const apprenticeship = {
  stages: ['shadow', 'canary', 'full'],
  promote: { shadow: { agree: 0.9, humanWin: 0.5, cost: 'not-worse' } },
};
async function shadowRun(task) {
  const [oldR, newR] = await Promise.all([old.run(task), novice.run(task)]);
  const agree = sameDecision(oldR, newR);
  if (!agree) await humanQueue.push({ task, oldR, newR }); // 分歧送人工评审
  return oldR;                                    // 用户永远拿旧结果
}
```
