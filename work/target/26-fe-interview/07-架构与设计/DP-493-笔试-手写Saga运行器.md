---
title: [DP-493] 笔试：手写 Saga 运行器
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 笔试题, 设计模式]
type: 笔试题
---

## DP-493：笔试：手写 Saga

**答**：实现 Saga 运行器 `runSaga`：① steps: [{ name, run, compensate }]——顺序执行，失败逆序补偿；② 补偿容错：补偿自身失败 → 进人工处理队列（不阻塞后续补偿）；③ 持久化：saga 上下文（已完成步骤/ctx）持久化——页面刷新后可恢复继续；④ 进度事件（onStep/onCompensate——UI 进度条）；⑤ 不可补偿步骤的声明（compensate 缺失 → 演练时标红——设计上放流程最后）。写出实现。

```javascript
async function runSaga(steps, initialCtx, { persist, onStep, restore } = {}) {
  let ctx = restore?.() ?? initialCtx;                 // 恢复续跑
  const done = restore?.doneSteps ?? [];
  const startIdx = done.length;
  try {
    for (let i = startIdx; i < steps.length; i++) {
      const step = steps[i];
      ctx = await step.run(ctx);
      done.push(step.name);
      persist?.({ doneSteps: done, ctx });
      onStep?.(step.name, i + 1, steps.length);
    }
    return { ok: true, ctx };
  } catch (e) {
    // 逆序补偿已完成步骤
    for (const name of [...done].reverse()) {
      const step = steps.find((s) => s.name === name);
      try { await step.compensate?.(ctx); }
      catch (err) { manualQueue.push({ saga: name, err }); }   // 补偿失败: 人工队列
    }
    return { ok: false, error: e };
  }
}
// steps: [{ name: 'reserve', run: reserveStock, compensate: releaseStock },
//         { name: 'sms', run: sendSms }]               ← compensate 缺失 = 不可逆, 放最后
```

**评分点**：
- 逆序补偿 + 补偿失败的容错（人工队列——补偿也要容错）
- 持久化恢复（刷新后从已完成步骤继续）
- 不可补偿步骤的声明与「放最后」的设计原则
- 进度事件驱动 UI

## 变体与延伸（补充）

**变体与延伸**：

1. 补偿动作本身被重复执行怎么防？→ 每个 compensate 带业务唯一键并由服务端去重，重放不产生二次退款，去重键由业务单号加步骤名组成。
2. 刷新恢复时服务端状态已经变了怎么办？→ 先按已完成步骤回查真实状态，以服务端为准修正上下文再续跑，回查失败的步骤按未完成处理并重新执行。
3. 跨服务长事务超时怎么处理？→ 每步设超时并映射为可补偿失败，超时即触发逆序补偿并写入人工队列。
