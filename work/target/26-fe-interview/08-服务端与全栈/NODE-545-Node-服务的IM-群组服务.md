---
title: [NODE-545] Node 服务的 IM 群组服务（成员/权限/大群）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-545：IM 群组服务
**答**:
- 群组模型：群信息 + 成员关系（角色：群主/管理员/成员——权限矩阵：踢人/禁言/公告）+ 成员状态变更流（入群/退群事件——通知与索引更新）。
- 大群挑战：万人群——成员列表不全员维护（成员名单懒加载/搜索制——ARC-580 通讯录）、消息扇出（群消息写扩散 vs 读扩散：小群写扩散（每人收件箱）大群读扩散（公共 timeline + 成员校验）——按群规模分档）。
- 入群/退群：入群审批（申请制/直接/邀请——群设置驱动）、退群权限清理（退群即失去消息检索与回执）、被踢/拉黑（黑名单——禁止再入）。
- 群消息权限：禁言（成员禁言——发送拦截）、仅管理员发言模式、@提及（提及通知——只对被@者高优先级推送 NODE-453）。
- 一致性：成员变更的消息可见性（新成员看不到入群前消息——入群时间水位过滤；或全历史可见——群配置）、群解散（消息保留期与成员通知）。
```javascript
// 大群读扩散 + 权限
async function groupTimeline(groupId, uid, cursor) {
  await assertMember(groupId, uid);                              // 读扩散：公共 timeline + 成员校验
  const sinceJoin = await joinSeq(groupId, uid);                 // 入群水位
  return msgRepo.bySeq(groupId, cursor, { minSeq: group.historyVisible ? 0 : sinceJoin });
}
```
