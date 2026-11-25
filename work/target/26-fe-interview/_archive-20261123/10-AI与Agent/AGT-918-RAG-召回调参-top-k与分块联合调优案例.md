---
title: [918] top-k 和 chunk 大小的联合调优怎么做一个真实案例
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 调参]
type: 面试题
---

## 918：top-k 和 chunk 大小的联合调优怎么做一个真实案例

**答**：
- 两者强耦合不能单独调：chunk 变大一倍，同样 top-5 带入的 token 翻倍但覆盖的独立信息源变少；正确姿势是网格实验（chunk 400/600/800 × top-k 3/5/8）跑同一评估集。
- 案例结论：工单问答场景 600 token + top-5 综合最优（准确率 0.78、平均成本 0.9 分/次）；top-8 准确率仅 +0.01 但成本 +60%，果断放弃。
- 实验纪律：一次只动一组变量、每次跑全量评估集并记录表格、把最优配置写进配置中心而非代码。
- 追问钩子：为什么 top-k 增大准确率不升？——上下文变长触发「中间迷失」，无关内容反而干扰生成，这正是压缩与重排存在的意义。

```ts
const grid = [400, 600, 800].flatMap(chunk =>
  [3, 5, 8].map(topK => ({ chunk, topK })));
for (const cfg of grid) {
  rebuildIndex(cfg.chunk);
  const { acc, cost } = await runEval(evalSet, { ...cfg, rerank: true });
  results.push({ ...cfg, acc, cost });  // 记录成表，避免凭感觉拍参数
}
console.table(results.sort((a, b) => b.acc - a.acc));
```

