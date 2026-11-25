---
title: [AGT-425] 笔试题——实现长任务断点续跑（幂等键+检查点+预执行记录）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-425：手写可恢复任务执行器：步骤幂等、检查点落库、恢复自检

**需求与边界**：
- 输入：计划步骤数组、持久化 store；输出：执行结果（可中断可恢复）。
- 边界要求：① 步骤幂等键（task:step），已完成跳过；② 先写意图（预执行记录）再执行（崩溃后可识别"可能已执行未记录"）；③ 每步 checkpoint 落库；④ 恢复时自检关键状态。

**答**：
```javascript
async function resumableRun({ taskId, plan, store, exec }) {
  const cp = await store.checkpoint(taskId);       // 恢复检查点
  const state = cp ?? { nextStep: 0, results: {}, ctx: {} };
  for (let s = state.nextStep; s < plan.length; s++) {
    const key = `${taskId}:${s}`;
    if (await store.isDone(key)) continue;         // 已完成跳过
    const intent = await store.markIntent(key);    // 预执行记录
    // 恢复自检：上次崩溃可能"已执行未记录"——幂等重执行
    let result;
    try {
      result = await exec(plan[s], {
        idempotencyKey: key,                       // 服务端去重
        ctx: state.ctx,
        priorIntent: intent.status === 'executing', // 上次中断标记
      });
    } catch (e) {
      await store.markFailed(key, e.message);
      if (plan[s].critical) {                      // 关键步骤失败即停
        await store.checkpoint(taskId, { ...state, nextStep: s });
        throw e;
      }
      result = { error: e.message, skipped: true }; // 非关键跳过
    }
    state.results[s] = result;
    state.ctx = plan[s].merge?.(state.ctx, result) ?? state.ctx;
    state.nextStep = s + 1;
    await store.checkpoint(taskId, state);         // 每步 checkpoint
  }
  await store.markComplete(taskId, state.results);
  return state.results;
}
// store 接口：checkpoint/isDone/markIntent/markFailed/markComplete
// 幂等约定：exec 必须把 idempotencyKey 传给下游（HTTP header / DB 唯一键）。
```

**评分点**:
- 幂等键全链路传递（步骤级→下游服务端），isDone 跳过与意图标记双保险。
- 预执行记录区分"上次中断时可能已执行"，恢复自检意识。
- checkpoint 每步落库（nextStep+results+ctx 完整快照）。
- 关键/非关键步骤失败分级（critical 停止、普通跳过继续）。
