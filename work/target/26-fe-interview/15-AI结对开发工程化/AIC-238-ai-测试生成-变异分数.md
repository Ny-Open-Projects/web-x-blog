---
title: [AIC-238] 用变异测试评估 AI 测试质量，怎么落地到流水线而不被运行时间拖垮？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-238：用变异测试评估 AI 测试质量，怎么落地到流水线而不被运行时间拖垮？
**答**：
- 范围控制：只对核心模块（支付/价格/权限）跑变异，非核心抽样跑。
- 增量变异：只对本次变更的文件生成变异体，全量周跑一次。
- 变异体预算：限制每文件变异体数量（如 20 个），超限随机采样。
- 门禁分级：核心模块变异分数 ≥ 70%，低于则 AI 测试打回补强。

```javascript
const mutationGate = {
  scope: { core: ['src/price/**', 'src/auth/**'], sample: 0.2 },
  budget: { mutantsPerFile: 20 },
  threshold: { core: 0.7, others: 0.4 },
};
r
```
