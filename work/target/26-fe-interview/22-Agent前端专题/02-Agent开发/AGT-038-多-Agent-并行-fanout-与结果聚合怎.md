---
title: [AGT-038] 多 Agent 并行 fan-out 与结果聚合怎么实现？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-038：多 Agent 并行 fan-out 与结果聚合怎么实现？
**答**：
- fan-out：把同一问题同时交给多个专家 Agent 并行处理，用 `Promise.allSettled` 保证单个失败不拖垮整体。
- 聚合：把各专家结果交给汇总模型去重、取舍、综合，输出统一结论并注明采纳来源。
- 适用场景：多视角评审（架构/成本/运维）、多方案生成后择优、投票式判断。
- 控制并发数（信号量）避免同时打爆 LLM 限流；每个分支独立超时。

```typescript
// 并行 fan-out：多专家同时分析，汇总模型聚合裁决
interface ExpertResult {
  expert: string;
  ok: boolean;
  answer: string;
}

async function fanOut(
  question: string,
  experts: Array<{ name: string; run: (q: string) => Promise<string> }>,
): Promise<string> {
  const settled = await Promise.allSettled(experts.map((e) => e.run(question)));

  const results: ExpertResult[] = experts.map((e, i) => {
    const s = settled[i];
    return s.status === 'fulfilled'
      ? { expert: e.name, ok: true, answer: s.value }
      : { expert: e.name, ok: false, answer: String(s.reason) };
  });

  return llmComplete(
    '多位专家对同一问题给出了意见，请去重、取舍后给出综合结论，并注明采纳了谁的观点。\n' +
    results.map((r) => `【${r.expert}】${r.ok ? r.answer : `执行失败：${r.answer}`}`).join('\n\n'),
  );
}

// 用法：三个视角并行评审
const verdict = await fanOut('这个系统该不该拆微服务', [
  { name: '架构专家', run: (q) => agentLoop(q) },
  { name: '成本专家', run: (q) => llmComplete(`从成本角度分析：${q}`) },
  { name: '运维专家', run: (q) => llmComplete(`从运维复杂度角度分析：${q}`) },
]);
```

---

## 十、评测与质量
