---
title: [DP-376] Saga 模式：长流程编排与补偿
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-376：Saga 模式

**答**：
- Saga 核心：长流程拆为多步本地事务 + 每步的补偿动作——失败时「逆向补偿已完成的步骤」（不是回滚数据库，是逐个撤销）
- 前端场景：多步向导（选品→配置→支付→开通——第 3 步失败要补偿前 2 步：释放库存/退优惠券）
- 实战结构：steps: [{ run, compensate }]——顺序执行 run，失败时逆序执行已完成步骤的 compensate——补偿也要容错（补偿失败记录人工处理队列）
- 与状态机的组合：saga 的流程推进用状态机管理（当前步骤/已完成/补偿中）——刷新页面后可恢复（持久化 saga 上下文）
- 深水点：补偿的「业务语义」——某些步骤不可补偿（短信已发）→ 设计上把不可补偿步骤放最后（减少补偿暴露面）

```javascript
async function runSaga(steps, ctx) {
  const done = [];
  for (const step of steps) {
    try {
      ctx = await step.run(ctx);
      done.push(step);
    } catch (e) {
      for (const d of done.reverse())              // 逆序补偿
        await d.compensate?.(ctx).catch((err) => manualQueue.push({ step: d, err }));
      throw e;
    }
  }
  return ctx;
}
// steps: [{ run: reserveStock, compensate: releaseStock },
//         { run: chargeCoupon, compensate: returnCoupon },
//         { run: sendSms }]  ← 不可补偿的放最后
```
