---
title: [AIC-902] 同一 prompt 在 CI 里重复跑，产出发生漂移，如何定位是模型版本变更还是上下文顺序问题？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-902：同一 prompt 在 CI 里重复跑，产出发生漂移，如何定位是模型版本变更还是上下文顺序问题？
**答**：
- 用「控制变量法」二分：固定模型版本只变上下文 → 固定上下文只变模型版本，两次实验各自独立，哪次复现漂移元凶就是谁。
- 模型版本要可观测：每次调用记录 model-id + 版本号 + 时间戳到元数据（呼应审计链），漂移时先对照这段时间有没有版本切换。
- 上下文顺序问题常见来源是 Map/Set 遍历、并行检索结果顺序不稳定、文件 glob 顺序——要求所有输入源「先排序再拼装」。
- 追问钩子：能提出「把 prompt、上下文、模型版本三者当作可版本化的输入快照，漂移时能逐字段 diff」的候选人具备可复现实验思维。

```typescript
// 控制变量定位漂移源
const snapshot = { model:'gpt-x@2026-11-01', prompt:hash(prompt), ctxOrder:['a','b','c'] };
function bisectDrift(run, base) {
  // 实验 A：锁定上下文，仅放开模型版本
  const a = run({ ...base, ctxOrder: base.ctxOrder.slice().sort() });
  // 实验 B：锁定模型版本，仅打乱上下文
  const b = run({ ...base, model: base.model });
  return {
    contextCulprit: fingerprint(a) !== fingerprint(base), // A 漂移→上下文顺序
    modelCulprit: fingerprint(b) !== fingerprint(base),    // B 漂移→模型版本
  };
}
function hash(s){ let h=0; for(const c of s) h=(h*31+c.charCodeAt(0))|0; return h>>>0; }
function fingerprint(o){ return hash(JSON.stringify(o)); }
// 关键：所有上下文来源先排序，消除 Map/glob 的隐式顺序
```
