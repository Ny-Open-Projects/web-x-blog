---
title: [939] 多 Agent 协商怎么设计终止条件，避免永远谈不完
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 终止条件]
type: 面试题
---

## 939：多 Agent 协商怎么设计终止条件，避免永远谈不完

**答**：
- 终止三条件取或：达成显式共识（评审 Agent 给出 pass）、资源耗尽（轮次/token 预算）、超时；三者都必须存在，缺一就是线上事故。
- 防抖：连续两轮产物差异低于阈值视为收敛（否则两个 Agent 互相小改永远不停止）；用编辑距离/语义相似度做「变化量」度量。
- 非收敛收尾：预算耗尽时强制「裁判 Agent 总结当前最优方案 + 未决分歧清单」输出，把僵局变成可人工裁决的材料。
- 追问钩子：为什么不能只靠轮次上限？——轮次打满输出可能是半成品，必须有「总结收尾」动作把上下文沉淀为可用产物。

```ts
async function negotiate(a, b, budget) {
  let prev = null;
  while (budget.rounds-- > 0) {
    const cur = await a.run(await b.lastOutput());
    if (prev && similarity(prev, cur) > 0.98) break;      // 变化量低于阈值 = 收敛
    if ((await judge.review(cur)).pass) break;            // 显式共识
    prev = cur;
    await b.respond(cur);
  }
  if (budget.rounds <= 0) return judge.summarize(prev);   // 强制总结收尾
  return prev;
}
```

