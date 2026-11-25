---
title: [TST-743] 用 LLM 解释「性能火焰图」——可行性与可信度怎么保证
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-743：用 LLM 解释「性能火焰图」——可行性与可信度怎么保证

**答**：
- 结论：LLM 擅长把火焰图的调用栈翻译成自然语言，但不擅长精确定量，定位应交给确定性分析，LLM 只做「摘要 + 假设生成」。
- 输入要给结构化摘要（热点函数、自身耗时、调用链），而非原始截图，降低幻觉。
- 可信度靠「引用约束」：每条结论必须指向具体帧，无法引用则标注「不确定」。
- 追问钩子：LLM 给出的热点与 Profiler 数据矛盾，以谁为准？

```javascript
// 把火焰图栈摘要成结构化输入给 LLM
function summarizeFlame(stacks) {
  const self = new Map();
  for (const s of stacks) {
    const top = s.frames[s.frames.length - 1];
    self.set(top, (self.get(top) || 0) + s.samples);
  }
  return [...self.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([fn, samples]) => ({ fn, samples, pct: +(samples / stacks.length * 100).toFixed(1) }));
}
console.log(summarizeFlame([
  { frames: ['root', 'render', 'sort'], samples: 80 },
  { frames: ['root', 'render'], samples: 20 },
]));
```
