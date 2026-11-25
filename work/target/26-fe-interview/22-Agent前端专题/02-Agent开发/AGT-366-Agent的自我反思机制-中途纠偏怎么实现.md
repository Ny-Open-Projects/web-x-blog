---
title: [AGT-366] 自我反思与纠偏——Agent 中途发现走偏怎么自纠？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-366：Agent 执行中途的反思（reflection）与纠偏机制怎么实现？

**答**:
- 反思触发点：阶段完成时（对照目标检查产出）、异常信号时（工具连续失败/结果与预期矛盾/步数超预算）、外部反馈时（用户纠偏/校验器报警）——反思是预算内行为（定期+事件触发），不是每步都反思（成本爆炸）。
- 反思内容：目标对齐检查（当前进展是否服务原始目标——防目标漂移 AGT-336）、方法有效性（当前路径是否有进展还是原地打转——AGT-253 循环检测）、资源核算（剩余预算还够不够）。
- 纠偏动作：微调（同方向调整参数）、转向（换方法/换检索词）、回滚（撤销最近无效步骤回到检查点）、上报（自身无法解决→转人，AGT-339 接管机制）——纠偏动作要记录进 trace（反思质量可评测）。
- 评测反思能力：构造"需要中途转向"的评测任务（初始路径必然失败的场景），测 Agent 的纠偏成功率与转向延迟——反思能力是可以训练和评测的。

```javascript
async function stepWithReflection(agent, ctx) {
  if (shouldReflect(ctx)) {           // 阶段末/异常/预算
    const review = await agent.reflect({
      goal: ctx.goal, progress: ctx.log,
      checks: ['目标对齐', '方法有效', '资源剩余'] });
    if (review.drift) ctx.plan = revise(ctx.plan, review);
    if (review.deadEnd) ctx.rollback(checkpoint);
    if (review.stuck) return handoffToHuman(ctx);
  }
  return agent.step(ctx);
}
```
