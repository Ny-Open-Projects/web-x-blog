---
title: [SCN-214] IM 消息有序性——多端发送与推送乱序怎么处理？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-214：IM 消息的顺序保证——手机和电脑同时发消息会乱吗？

**答**:
- 排序基准：服务端 seq 是唯一排序依据（会话内单调递增），客户端时间戳只做展示——本地时钟漂移/多设备时钟不一致都会导致按时间排序错乱。
- 乱序到达处理：WS 推送可能乱序（网络多路径）——按 seq 插入正确位置（不是 append），等待缺口机制（seq 缺口时先缓存，触发按 lastSeq 拉取补齐，超时补齐失败降级全量拉取）。
- 多端发送：手机/电脑同时发消息各自进服务端队列获取 seq——客户端发送队列只保证单设备内有序，跨设备顺序由服务端 seq 裁决，本地乐观消息在 ack 后按 serverId 归位（乐观消息先显示在末尾，ack 后重排）。
- 撤回与编辑的顺序性：撤回/编辑也是消息（控制消息走同一 seq 流水），保证与普通消息的相对顺序（撤回不能早于被撤回消息被处理）。

```javascript
function onIncoming(msg) {
  if (msg.seq <= lastSeq) return dedupe(msg);   // 旧消息/重复
  if (msg.seq === lastSeq + 1) {
    insertSorted(msg); lastSeq = msg.seq;
    flushBuffered();                            // 补齐缓冲中的连续段
  } else {
    buffered.set(msg.seq, msg);                 // 缺口：先缓冲
    pullSince(lastSeq);                         // 拉取补齐
    setTimeout(() => {                          // 兜底：1s 仍缺→全量拉
      if (hasGap()) fullSync(lastSeq);
    }, 1000);
  }
}
// 本地乐观消息：sending 态显示在末尾，
// ack 后按 serverId/seq 归位重排（闪烁可接受）。
```
