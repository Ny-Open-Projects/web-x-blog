---
title: [AGT-362] Few-shot 示例工程——示例怎么选才有效？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-362：few-shot 示例怎么选——示例质量与多样性的工程？

**答**:
- 示例的强影响：模型高度模仿示例的风格/格式/行为（包括坏习惯）——示例质量是输出质量的上限；示例带入的偏差（示例中的偏见/错误）会被放大复制。
- 选择原则：覆盖典型意图分布（每类意图 ≥1 例）、含边界案例（拒答示例/歧义示例——教模型"什么时候不答"）、格式标准（示例的格式就是输出的格式模板）、数量适中（3~5 个高质量 > 10 个平庸，过多稀释注意力）。
- 动态示例（dynamic few-shot）：按当前 query 检索最相似的历史成功案例作为示例（向量检索示例库）——比静态示例更相关；示例库来自真实成功案例+人工审核。
- 评测示例有效性：换示例集跑对比评测（示例是 prompt 的一部分，变更走评测门禁 AGT-321）——示例不是装饰是核心配置。

```javascript
async function dynamicFewshot(query, k = 3) {
  const examples = await vectorSearch(EXAMPLE_LIB,
    { query, k, filter: { reviewed: true, success: true } });
  return prompt`
    示例：
    ${examples.map(fmtExample)}
    现在处理：${query}`;
}
// 示例库 = 真实成功案例 + 人工审核 + 边界示例。
```
