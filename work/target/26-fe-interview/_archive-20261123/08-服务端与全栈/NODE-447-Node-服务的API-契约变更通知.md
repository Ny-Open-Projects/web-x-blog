---
title: [NODE-447] Node 服务的契约变更通知与影响广播如何自动化？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-447：契约变更通知自动化
**答**:
- 问题：接口改了没人通知 → 调用方线上炸了才知道。自动化链路：契约 diff（OpenAPI/IDL 版本比对）→ 影响计算（NODE-428 调用方清单）→ 多渠道通知（IM 群机器人/邮件/MR 评论）→ 确认闭环（各调用方 ack 迁移计划）。
- diff 分级：兼容变更（加字段/加可选参数——自动通知即可）、不兼容变更（删字段/改语义/改错误码——必须 ack + 迁移排期，BLOCK 旧版本下线）、行为变更（同 schema 不同语义——最危险，评审重点）。
- 通知内容：变更 diff 摘要 + 受影响调用方 + 各调用方最近调用量（迁移优先级）+ 新版本沙箱入口。
- 与版本管理联动：不兼容变更自动触发大版本流程（NODE-440 sunset 计时启动）。
- 记录：契约变更历史（谁改的/谁 ack 的），事故溯源用。
```javascript
// CI 契约 diff 机器人
async function onContractDiff(diff) {
  const breaking = diff.changes.filter(c => !c.compatible);
  const callers = await impactOf(diff.routes);                   // NODE-428
  await im.post({ text: renderDiffCard(diff, callers),
    actions: callers.map(c => ({ label: `${c.svc} 确认`, cmd: `ack-contract ${diff.id} ${c.svc}` })) });
  if (breaking.length) { blockSunsetRemoval(diff); startSunset(diff, '90d'); } // 旧版保留计时
}
```
