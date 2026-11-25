---
title: [1128] 给执行类 Agent 配一个评审者 Agent 值不值
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 模式]
type: 面试题
---

## 1128：给执行类 Agent 配一个评审者 Agent 值不值

**答**：
- 收益实测可观：执行后加独立评审者（不同上下文、不同视角）抓错率通常 10%~30%（抓的是执行者「自己看不出」的错——自检盲区），尤其代码/文案类。
- 成本：延迟 +1 轮、成本 +50%~100%；所以按风险分级——高危输出必评审、低危抽样评审（20% 抽检维持威慑）。
- 评审者独立性是关键：评审者不能看到执行者的推理过程（会被带偏），只看输入与输出——「盲审」才有效。
- 追问钩子：评审者和执行者意见冲突怎么办？——三级裁决：评审给出具体可验证的理由（如测试失败）→ 自动采纳重做；理由主观 → 升级人工；来回超过 2 轮 → 人工终审，防止两个 Agent 无限互相改。

```ts
async function withReview(executor, out, task) {
  if (task.risk === 'low' && Math.random() > 0.2) return out; // 抽样评审
  const review = await reviewer.check({ input: task, output: out }); // 盲审
  if (!review.pass && review.verifiable) {
    return withReview(executor, await executor.redo(task, review.issues), task); // 可验证理由自动重做
  }
  if (!review.pass) return humanUph(task, out, review);  // 主观冲突升人工
  return out;
}
```

