---
title: [AGT-630] 拿到一个 Agent 回答错了的工单，从定位到修复回归的完整工作流？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-630：拿到一个 Agent 回答错了的工单，从定位到修复回归的完整工作流

**答**：
- 五步：① trace 定位（工单 traceId→回放现场）；② 归因（检索没召回/工具选错/提示词缺失约束/模型能力边界，四选一归类）；③ 最小复现（该案例进评测集，重现失败）；④ 修复（改提示词/加工具/调检索参数）；⑤ 回归（评测集跑分对比 + 灰度验证 + 上线后该用户回访）。
- 关键纪律：不允许"看起来改好了"直接上线——必须转化为评测用例，否则同类问题会复发且无感知。
- 归因分布统计：月度看四类归因占比变化，指导改进投入方向（若检索归因占 60%，优先投资 RAG 而非改提示词）。

```javascript
async function fixWorkflow(ticket) {
  const trace = await replay(ticket.traceId);            // ① 现场
  const cause = await attribute(trace);                  // ② 归因四分类
  const caseId = evalPool.add({ from: ticket, trace });  // ③ 最小复现
  await runEval([caseId]);                               //   确认复现失败
  await ship(cause.fix, { canary: true });               // ④ 灰度修复
  const reg = await runEval(fullset());                  // ⑤ 回归
  assert(reg.score >= baseline.score);
  notify(ticket.user, '已修复并验证');                    //   回访闭环
}
```

