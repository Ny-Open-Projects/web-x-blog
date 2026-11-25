---
title: [AV-258] 直播间 WebSocket 信令断线重连与消息补偿
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 笔试题, 26]
type: 笔试题
---

## AV-258：直播间 WebSocket 信令断线重连与消息补偿

**答**：
- 题目：直播间 WS 断线重连 + 断连期间消息补偿（重连后拉取增量消息，按 seq 去重排序）。
- 思路：心跳断线检测（HW-250 复用）；重连成功 → 携带 lastSeq 请求增量（服务端缓存最近 N 条）；合并去重排序渲染。
- 评分点：断线检测；增量补偿协议；去重排序。

```javascript
class DanmakuRecovery {
  constructor(ws, container) { this.lastSeq = 0; this.ws = ws; }
  onMessage({ seq, ...msg }) { this.lastSeq = seq; this.render(msg); }
  async reconnect() {                                        // 重连 + 补偿
    await this.connect();
    const { messages } = await this.ws.request('replay', { since: this.lastSeq });   // 增量
    const known = new Set(this.renderedSeqs);                 // 已渲染 seq
    messages.filter(m => !known.has(m.seq))
      .sort((a, b) => a.seq - b.seq)                          // 排序补渲染
      .forEach(m => { this.lastSeq = Math.max(this.lastSeq, m.seq); this.render(m); });
    if (messages.length > 100) showCollapseNotice(messages.length);   // 过多折叠
  }
}
```
