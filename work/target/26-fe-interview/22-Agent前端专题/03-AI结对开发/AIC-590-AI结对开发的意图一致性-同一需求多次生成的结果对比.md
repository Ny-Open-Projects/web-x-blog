---
title: [AIC-590] 同一需求多次生成的结果对比
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-590：同一需求多次生成

**答**:
- 同一需求多次生成的结果差异：1) **LLM 的非确定性**（temperature > 0 时同一 prompt 生成不同代码——"LLM 的随机性"（不是 bug——是 LLM 的设计特性）；2) **差异的维度**：实现方式不同（A 用 reduce、B 用 for 循环——语义等价但代码不同）/ 命名不同（`fetchData` vs `loadData`）/ 边界处理不同（A 处理 null、B 不处理——行为差异 RBL-507）；3) **多次生成的价值**：对比多次生成的代码 → 发现"共识部分"（所有生成一致的 = LLM 有把握的）vs "分歧部分"（不一致 = LLM 不确定的——人需要重点审）。
- 一致性的度量：1) **AST 一致性**（RBL-667 双包一致性验证的 AI 版——多次生成的 AST 对比；2) **行为一致性**（多次生成的代码跑同一测试集——行为一致 = 高置信度；3) **分歧检测**：不一致的区域 = AI 不确定的地方 = 人需要审查的靶点。
- 追问钩子：为什么「多次生成的分歧区域」是审查的最高效靶点？——所有生成一致的代码 = LLM 有共识（大概率正确——LLM 的共识相当于"多个独立实现的交叉验证"）；不一致的代码 = LLM 不确定（可能有 bug——最需要人审的区域）；「分歧 = 审查的优先级」：人不需要审"LLM 有把握的"代码（一致的部分——可信）——人只需要审"LLM 不确定的"（分歧区域——高效审查）。

```typescript
// 多次生成的分歧检测
async function detectDivergence(prompt: string, generate: () => Promise<string>,
  { runs = 3, comparator } = {}) {
  const outputs = await Promise.all(Array.from({ length: runs }, () => generate(prompt)));
  const norm = comparator ?? ((c: string) => c.replace(/\s+/g, ' ').trim());
  const normalized = outputs.map(norm);
  // 分歧检测：两两比较
  const divergentPairs: [number, number][] = [];
  for (let i = 0; i < normalized.length; i++)
    for (let j = i + 1; j < normalized.length; j++)
      if (normalized[i] !== normalized[j])
        divergentPairs.push([i, j]);
  const consistent = divergentPairs.length === 0;
  return { outputs, consistent, divergentPairs,
    confidence: consistent ? 'high' : divergentPairs.length >= runs - 1 ? 'low' : 'medium' };
}
```

## 追问（补充）

**追问**：

1. 三次生成完全一致，就能直接合并吗 → 不能，一致只说明模型有共识，共识也可能是同一个错误认知；仍需测试与类型兜底，一致性只用来排审查优先级。
2. 把 temperature 设 0 是不是就确定唯一了 → 不是，浮点累加顺序、批处理、模型版本更新都会引入差异，可复现要靠固定 seed 并记录模型版本。
3. 文本 diff 做分歧检测太粗糙，怎么改进 → 归一化后比 AST 结构（忽略命名与格式），再让各版本跑同一测试集，行为一致才算真共识。
