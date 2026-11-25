---
title: [WCN-784] 视觉回归 diff 如何接入人工审批门禁与工单系统？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-784：视觉回归 diff 如何接入人工审批门禁与工单系统？

**答**：
- 结论：视觉回归工具（如 Chromatic/Percy）产出 diff 后生成审批任务，只有 reviewer 在平台点「通过」才更新基线；未审批的 diff 阻断合并（CI status check）。
- 集成工单系统（Jira）自动建 issue、附上 diff 截图与影响组件；分类「预期变更/意外回归」，预期变更需说明原因。
- 追问钩子：大量噪声 diff（如动画帧、时间戳）淹没真正回归怎么办？考察「隐藏动态区域 + 稳定性等待 + diff 阈值」降噪。

```javascript
// 审批门禁状态机
const states = { PENDING: '待审批', APPROVED: '已通过', REJECTED: '已拒绝' };
function review(diffId, decision, reviewer) {
  const task = { diffId, decision, reviewer, at: Date.now() };
  if (decision === 'APPROVED') {
    updateBaseline(diffId);                       // 通过才更新基线
    closeTicket(diffId, states.APPROVED);
  } else {
    blockMerge(diffId);                            // 阻断合并
    reopenTicket(diffId, states.REJECTED, reviewer);
  }
  return task;
}
function updateBaseline() {}, function closeTicket() {},
function blockMerge() {}, function reopenTicket() {}
console.log(review('diff-1', 'APPROVED', 'alice').decision);
```
