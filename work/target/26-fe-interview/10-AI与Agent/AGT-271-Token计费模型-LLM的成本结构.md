---
title: [AGT-271] Token 计费模型——LLM 应用的成本结构怎么算清？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-271：LLM 应用的成本结构是什么——为什么输入比输出贵好几倍的问题要算清？

**答**:
- 计费构成：输入 token（含缓存命中价，约 1/5~1/10）、输出 token（最贵）、工具/检索调用费（embedding/搜索/代码执行）、基础设施（网关/日志/评测）——Agent 场景输入占大头（每轮都重发全部历史），输入优化优先级最高。
- Agent 的成本乘数：多轮工具调用意味着同样的历史被计费 N 次（每轮一次完整 forward）——一个 20 步的 Agent 任务，其上下文被计费 20 遍，"上下文越长×轮数越多"成本指数放大，这是 Agent 成本失控的核心机制。
- 必做的成本建模：单任务成本 = Σ(每轮输入 token × 输入价 + 输出 token × 输出价 + 工具费)——按任务类型建立成本基线（P50/P95），预算控制才有依据。
- 降本三板斧对应的账：上下文裁剪/摘要（减输入轮数与长度）、前缀缓存（缓存价替代全价，AGT-224）、模型分级（简单步骤用便宜模型）——每项都要折算成钱对比实施成本。

```javascript
function taskCost(trace, price) {
  return trace.reduce((sum, step) => {
    const cached = step.cachedTokens || 0;
    return sum
      + (step.input - cached) * price.input
      + cached * price.cached
      + step.output * price.output
      + (step.toolCost || 0);          // embedding/搜索费
  }, 0);
}
// 例：20 步 × 每步 20k 输入 = 400k 输入计费
// → 历史压缩 + 前缀缓存是第一杠杆。
```
