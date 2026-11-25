---
title: [1182] 长任务的总预算怎么分给各步骤
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 预算]
type: 面试题
---

## 1182：长任务的总预算怎么分给各步骤

**答**：
- 分配三策略：静态均分（简单但不合理——审查步骤和生成步骤消耗差 5 倍）、按历史分布分配（各步骤的历史成本 P50 占比分配总预算，主流方案）、动态再分配（执行中某步骤提前完成，剩余预算回流池供后续步骤借用）。
- 超预算的处理分级：单步骤超预算先「收尾当前步骤」（输出已完成部分）→ 全局超预算「总结收尾」→ 关键步骤可「借预算」（从非关键步骤挪）。
- 预算与质量联动：预算不是越少越好——预算分配要保证「关键路径步骤不受限」，非关键步骤（探索类）可压缩。
- 追问钩子：动态再分配的坑？——「先到先得」会让早期步骤挥霍预算；约束是「每步预分配上限 + 回流池」，早期步骤超上限同样要收尾。

```ts
class TaskBudget {
  constructor(total, weights) {                     // 按历史占比分配
    this.alloc = mapValues(weights, w => total * w);
    this.pool = total;
  }
  spend(step, tokens) {
    if (tokens <= this.alloc[step]) { this.alloc[step] -= tokens; return 'ok'; }
    if (this.pool < tokens) return summarizeAndStop(step);   // 全局收尾
    this.alloc[step] -= tokens; this.pool -= tokens;
    return 'borrowed';                              // 借池内预算
  }
  release(step, unused) { this.pool += unused; }    // 提前完成回流
}
```
