---
title: [AGT-039] 如何为 LLM 应用搭建自动化评测集？幻觉有哪些防御手段，引用溯源怎么做？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-039：如何为 LLM 应用搭建自动化评测集？幻觉有哪些防御手段，引用溯源怎么做？
**答**：
- 评测集 = 一组带标准要点/断言的问题（mustInclude 关键点、必须带引用等），改动 prompt、模型或参数后重跑，接 CI 做通过率门禁。
- LLM 评分（LLM-as-judge）适合开放性回答，规则断言适合事实型回答，两者常混用。
- 幻觉防御：RAG 限定"只依据资料回答"、检索分数低于阈值就拒答、低 temperature、要求标注引用。
- 引用溯源：入库时每个 chunk 带来源元数据，回答要求输出 `[n]` 标记，前端把 `[n]` 渲染成可点击的来源链接。

```typescript
// 自动化评测：规则断言 + 通过率门禁，接入 CI
interface EvalCase {
  question: string;
  mustInclude: string[]; // 答案必须覆盖的关键点
  mustCite: boolean;     // 是否必须带引用标记
}

const evalSet: EvalCase[] = [
  { question: 'Vue 3 的 watchEffect 和 watch 区别', mustInclude: ['依赖收集', '立即执行'], mustCite: true },
  { question: 'React 18 的并发特性指什么', mustInclude: ['可中断'], mustCite: true },
];

interface RagAnswer {
  text: string;
  citations: string[]; // 引用的来源文档
}

async function runEval(ragAnswer: (q: string) => Promise<RagAnswer>) {
  const report = [];
  for (const c of evalSet) {
    const { text, citations } = await ragAnswer(c.question);
    const missing = c.mustInclude.filter((k) => !text.includes(k));
    report.push({
      question: c.question,
      pass: missing.length === 0 && (!c.mustCite || citations.length > 0),
      missing,
      citations,
    });
  }
  const passRate = report.filter((r) => r.pass).length / report.length;
  console.log(`评测通过率：${(passRate * 100).toFixed(0)}%`);
  if (passRate < 0.9) process.exit(1); // CI 门禁：不达标阻断合并
  return report;
}
```

---

## 十一、工程化
