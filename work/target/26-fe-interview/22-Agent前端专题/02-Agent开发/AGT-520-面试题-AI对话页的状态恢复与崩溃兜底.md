---
title: [AGT-520] 页面崩溃/浏览器崩溃后重新打开，AI 对话页如何恢复到崩溃前状态？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-520：页面崩溃/浏览器崩溃后重新打开，AI 对话页如何恢复到崩溃前状态

**答**：
- 关键状态分层持久化：已确认消息在服务端；进行中的流式回合把「请求参数 + 已收 delta」定期快照到 IndexedDB（每 500ms 或每 N 个 delta）。
- 恢复时先渲染快照（半成品标记"生成中断于 xx"），再向服务端查询该回合最终状态：成功则替换，失败则提供"继续生成"（带已生成前缀续写）。
- 避免恢复风暴：多标签页恢复时用 BroadcastChannel 协调，只由一个标签发起续传。

```javascript
function snapshotTurn(turn) {
  idb.put('turnSnap', { id: turn.id, req: turn.req,
    deltas: turn.deltas, at: Date.now() });   // 周期快照
}
async function recover(turnId) {
  const snap = await idb.get('turnSnap', turnId);
  renderPartial(snap);                          // 先显示半成品
  const final = await api.turnStatus(turnId);
  if (final.done) replaceWithFinal(final);
  else offerContinue(snap);                     // 带 prefix 续写
}
```

