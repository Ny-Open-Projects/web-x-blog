---
title: [TST-767] AI 辅助「故障演练编排」：从场景库到执行计划的生成
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-767：AI 辅助「故障演练编排」：从场景库到执行计划的生成

**答**：
- 结论：AI 把自然语言演练目标转成结构化执行计划（场景 + 顺序 + 稳态假设 + 回滚），但必须做「安全校验 + 资源冲突检测」才能下发。
- 场景库要有元数据（影响面、前置条件、互斥组），AI 按目标检索组合，避免生成危险组合。
- 执行计划生成后先 dry-run 展示「将做什么」，人工确认才真正注入。
- 追问钩子：AI 生成的计划把两个互斥场景排在一起，如何拦截？

```javascript
// 执行计划生成后的互斥检测
function detectConflict(plan, scenarioMeta) {
  const groups = new Set();
  for (const step of plan) {
    const g = scenarioMeta[step.scenario]?.mutexGroup;
    if (g && groups.has(g)) return { ok: false, conflict: g };
    if (g) groups.add(g);
  }
  return { ok: true };
}
console.log(detectConflict(
  [{ scenario: 'networkDelay' }, { scenario: 'networkDrop' }],
  { networkDelay: { mutexGroup: 'net' }, networkDrop: { mutexGroup: 'net' } }
)); // 冲突
```
