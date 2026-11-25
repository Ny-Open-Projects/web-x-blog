---
title: [TST-587] IM 场景的弱网与消息乱序混沌测试
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-587：IM 场景的弱网与消息乱序混沌测试

**答**：
- 结论：IM 场景要验证「弱网下的消息可靠性」——断线重连、消息不丢不重、顺序正确、离线消息补发、发送状态（发送中/失败重试）准确。
- 做法：注入网络抖动/丢包/断网，模拟消息乱序与重复到达；断言本地消息队列去重（按 msgId）、按 seq 排序、重连后补拉离线消息、UI 状态与真实投递一致。
- 追问钩子：消息重复到达怎么测？——注入相同 msgId 的重复消息，断言 UI 只显示一条；这是 IM 幂等处理的经典用例，需专门覆盖。

```javascript
// IM 消息去重与排序：按 msgId 去重，按 seq 排序
function normalizeMessages(msgs) {
  const seen = new Map();
  for (const m of msgs) if (!seen.has(m.msgId) || m.updatedAt > seen.get(m.msgId).updatedAt)
    seen.set(m.msgId, m);
  return [...seen.values()].sort((a, b) => a.seq - b.seq);
}
console.log(normalizeMessages([
  { msgId: 'm1', seq: 2, text: 'b', updatedAt: 1 },
  { msgId: 'm1', seq: 2, text: 'b', updatedAt: 1 }, // 重复
  { msgId: 'm2', seq: 1, text: 'a', updatedAt: 2 },
]).map(m => m.text)); // ['a','b']
```
