---
title: [941] 多 Agent 分工按「能力」还是按「阶段」切，生产怎么选
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 分工设计]
type: 面试题
---

## 941：多 Agent 分工按「能力」还是按「阶段」切，生产怎么选

**答**：
- 按阶段切（规划→执行→验证）：管线清晰、每阶段上下文可预测，是默认选择；缺点是阶段串行，总延迟高。
- 按能力切（前端/后端/测试专家）：可并行，但需要一个「总线调度」决定谁接活，调度错误率成为新风险。
- 生产常见混合式：阶段为骨架、阶段内按能力并行（执行阶段同时派前端、后端两个专家 Agent）。
- 判断依据：子任务间依赖强 → 按阶段；独立同构任务多 → 按能力并行；先跑通阶段式再优化并行度。
- 追问钩子：并行度怎么定？——看共享资源瓶颈（工具限流、合并冲突率），不是越大越好，实测并行 4 之后合并成本反超收益。

```ts
// 阶段骨架 + 阶段内能力并行
const pipeline = ['plan', 'execute', 'verify'];
for (const phase of pipeline) {
  const jobs = planOf(phase);                 // 该阶段的子任务
  if (phase === 'execute') {
    await Promise.all(jobs.map(j => expertFor(j.domain).run(j))); // 按能力并行
  } else {
    for (const j of jobs) await workers[phase].run(j);             // 串行阶段
  }
}
```

