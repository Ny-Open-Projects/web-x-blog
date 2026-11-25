---
title: [TST-870] 大规模下「AI 生成测试的成本控制」（token/调用次数/缓存）如何做？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-870：大规模下「AI 生成测试的成本控制」（token/调用次数/缓存）如何做？
**答**：
- 结论：AI 成本 = 调用次数 × 单次 token，控制手段是「缓存复用 + 精准上下文 + 分级调用 + 本地小模型兜底」。
- 缓存：相同 prompt/相同代码片段的生成结果缓存复用，避免重复生成（如同一函数多次请求）。
- 精准上下文：RAG 只检索最相关片段（而非塞整个仓库），压缩 prompt 降 token。
- 分级：简单样板用例用小模型/规则模板，复杂场景才调大模型；批量生成优先批处理 API。
- 追问钩子：缓存命中率高但生成质量下降（复用了过时结果），你如何设计缓存失效策略？

```javascript
// AI 调用缓存 + 成本统计
class AICostControl {
  constructor(llm) { this.llm = llm; this.cache = new Map(); this.cost = 0; }
  async generate(prompt, { codeHash }) {
    const key = `${codeHash}:${prompt}`;
    if (this.cache.has(key)) return { ...this.cache.get(key), cached: true };
    const result = await this.llm(prompt); // 假设返回 { text, tokens }
    this.cost += result.tokens;
    this.cache.set(key, result);
    return { ...result, cached: false };
  }
  invalidates(codeHash) { // 代码变更时失效旧缓存
    for (const k of this.cache.keys()) if (k.startsWith(codeHash)) this.cache.delete(k);
  }
}
const ctrl = new AICostControl(async p => ({ text: '...', tokens: 800 }));
ctrl.generate('生成测试', { codeHash: 'abc' }).then(r => console.log(r.cached));
```
