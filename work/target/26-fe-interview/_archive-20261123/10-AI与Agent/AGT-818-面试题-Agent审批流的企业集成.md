---
title: [AGT-818] Agent 的审批动作对接企业 OA 审批流（钉钉/OA），如何设计双向集成？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-818：Agent 的审批动作对接企业 OA 审批流（钉钉/OA），如何设计双向集成

**答**：
- 双向协议：平台→OA（发起审批：携带上下文快照+风险摘要，OA 展示人类可读卡片）；OA→平台（审批结果回调：带审批人/意见/时间，验签防伪造）。审批状态机同步（pending/approved/rejected/cancelled），OA 侧撤销要同步回平台终止任务。
- 上下文保真：审批人看到的是「Agent 要做什么+关键参数+影响面」，不是黑盒"批准 Agent 继续"——审批粒度与风险对齐（高危逐条批、低危批量批）。
- 超时与代理：OA 审批超时走企业默认（自动升级到上级），平台侧对应任务 pause；审批人不在支持委托。

```javascript
async function requestApproval(tc, ctx) {
  const oa = await oaClient.create({
    title: `Agent 请求：${tc.summary}`,
    detail: humanReadable(tc),                     // 关键参数+影响面
    callback: signedCallbackUrl(tc.key),           // 验签回调
    timeout: { action: 'escalate', to: ctx.manager },
  });
  task.pause(`等待 OA 审批：${oa.id}`);
  return oa.id;
}
function onOaCallback(sig, payload) {
  verify(sig, payload);                           // 验签
  payload.action === 'approved'
    ? resumeTask(payload.key) : cancelTask(payload.key, payload.reason);
}
```

