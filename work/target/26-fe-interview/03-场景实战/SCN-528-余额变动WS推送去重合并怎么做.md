---
title: [SCN-528] 余额变动的 WS 推送链路怎么设计？断线期间漏推怎么办？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-528：余额变动 WS 推送链路怎么设计？
**答**：
- 推拉结合：WS 推「变更信号」（账户 version 自增 + 事件摘要），前端收到后拉权威数据或直接信任携带的完整快照（带 version），不依赖推送内容做账。
- 断线补漏：重连时携带 lastAckVersion，服务端返回增量事件或指示全量刷新；事件带 seq，前端检测 seq 空洞触发兜底拉取。
- 去重与乱序：以 version/seq 单调性判重，乱序丢弃旧事件；同一秒多笔交易合并为一次 UI 更新。
- 降级：WS 不可用时退化为关键路径轮询（仅余额，低频），恢复后回到推送。
- 追问钩子：为什么推送只带信号不带金额也行——避免「伪造推送改余额」，金额永远来自带签名的拉取响应。

```javascript
function balanceChannel(ws, store) {
  let lastAck = store.version;
  ws.on('balance', ({ seq, version }) => {
    if (version <= store.version) return;          // 旧事件丢弃
    if (seq !== store.seq + 1) return refetchAll(); // 空洞 → 全量兜底
    store.applySeq(seq, version);
    lastAck = version;
    ws.send({ ack: lastAck });                     // ACK 供服务端记录断点
  });
  ws.on('reopen', () => ws.send({ resumeFrom: lastAck })); // 重连补漏
  ws.on('down', () => startPolling('/balance', 10_000));   // 降级轮询
}
```
