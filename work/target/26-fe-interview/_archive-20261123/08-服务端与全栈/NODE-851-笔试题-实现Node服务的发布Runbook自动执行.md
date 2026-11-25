---
title: [NODE-851] 笔试题——实现发布 Runbook 自动执行（runbook 即代码）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-851：手写 Runbook 执行

**需求与边界**：
- 需求：runbook 即代码（SCN-OPS-269）——① runbook 步骤声明（YAML 步骤 + 断言——SCN-OPS-269）；② 自动执行（发布流程消费 runbook——步骤顺序执行）；③ 步骤失败的处理（阻断/继续——步骤声明）；④ runbook 与演练脚本同源（SCN-OPS-269 一致性）。
- 边界：① 步骤间数据传递（前步输出 → 后步输入——SCN-OPS-291 计划）；② 人工确认步骤（危险步骤 requireConfirm——SCN-OPS-253 三权分离）；③ 执行记录（审计——SCN-OPS-220）。

**答**：
```yaml
# runbook.yaml（SCN-OPS-269 即代码）
steps:
  - name: verify-rollback-channel
    action: checkChannel
    assert: { ok: true }
  - name: canary-1pct
    action: setGray
    args: { pct: 1 }
  - name: observe-10min
    action: wait
    args: { ms: 600000 }
    assert: { errorRateDelta: '< 50%' }
  - name: full-rollback-confirm
    action: confirm                                    # 人工确认步骤（SCN-OPS-253）
    requires: oncall-mgr
```
```javascript
async function runRunbook(runbook, ctx) {
  const outputs = {};
  for (const step of runbook.steps) {
    if (step.action === 'confirm')                     // 人工确认步骤（SCN-OPS-253）
      await requireConfirm(step.requires, { step: step.name });
    const out = await actions[step.action](step.args, ctx, outputs);   // 执行
    outputs[step.name] = out;
    if (step.assert && !assertOk(step.assert, out))    // 断言失败（SCN-OPS-229 门禁）
      return { failedAt: step.name, out };
    audit({ step: step.name, out });                   // 审计（SCN-OPS-220）
  }
  return { done: true };
}
```

**评分点**:
- runbook 即代码（YAML 步骤 + 断言——SCN-OPS-269）。
- 人工确认步骤（危险步骤——SCN-OPS-253 三权分离）。
- 步骤断言（门禁——SCN-OPS-229）。
- 审计 + 演练脚本同源（SCN-OPS-269/220）。
