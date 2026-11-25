---
title: [TST-880] 笔试：综合题——设计并实现「AI 辅助测试流水线」的核心编排器
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-880：笔试：综合题——设计并实现「AI 辅助测试流水线」的核心编排器
**答**：
- 需求：实现 aiTestPipeline(change, deps) —— 编排「AI 生成用例 → 确定性校验 → 执行 → 失败归因 → 置信度路由」的完整流水线。
- 规则：每步产出传给下一步；生成用例必须先过 validate 校验，未过则转人工不执行；失败归因置信度低则转人工。
- 边界：任一步抛错不中断整体，记录 step 错误并返回 partial 结果；返回每步状态与最终结果。

```javascript
async function aiTestPipeline(change, deps) {
  const trace = { steps: [], status: 'running' };
  const step = async (name, fn, input) => {
    try { const out = await fn(input); trace.steps.push({ name, ok: true }); return out; }
    catch (e) { trace.steps.push({ name, ok: false, error: e.message }); return null; }
  };
  const generated = await step('generate', deps.generate, change);
  const validated = generated ? await step('validate', deps.validate, generated) : null;
  if (!validated?.allValid) { trace.status = 'needs-human'; return trace; } // 校验不过不执行
  const executed = await step('execute', deps.execute, validated);
  const triaged = executed ? await step('triage', deps.triage, executed) : null;
  trace.result = triaged && triaged.confidence >= 0.7 ? 'auto-merge' : 'needs-human';
  trace.status = 'done';
  return trace;
}
// deps: { generate, validate, execute, triage } 由外部注入，便于测试与替换

// 手动模拟一次流水线（真实由平台注入 deps）
const deps = {
  generate: async () => ({ allValid: true }),
  validate: async (x) => x,
  execute: async () => ({ failed: false }),
  triage: async () => ({ confidence: 0.9 }),
};
aiTestPipeline('PR-1024', deps).then(console.log); // status:'done', result:'auto-merge'
```
**评分点**：
- 流水线编排逻辑正确：生成→校验→执行→归因→路由，校验不过不执行。
- 每步 try/catch 隔离，抛错不中断整体，记录 step 状态（可观测）。
- 失败归因置信度路由（呼应 calibrate），低置信转人工。
- 依赖注入 deps 便于测试与替换，体现工程化可维护性。
