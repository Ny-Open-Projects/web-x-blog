---
title: [AGT-591] 手写跨标签页同步：delta广播、只读态、对账哈希、关闭清理？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-591：手写跨标签页同步：delta广播、只读态、对账哈希、关闭清理

**需求与边界**：
- 实现 SessionSyncChannel(sessionId)：同源标签页间同步流式会话。
- 边界要求：① 发起方广播 turn_start/delta/done，接收方进入只读态；② done 后接收方与服务端对账（内容哈希不一致重拉）；③ 接收方禁用输入（防双窗口并发发送制造混乱分叉），发起方关闭后释放；④ 多个接收方幂等（重复消息按 seq 丢弃）。

**答**：
```javascript
class SessionSyncChannel {
  constructor(sessionId, myRole) {
    this.bc = new BroadcastChannel(`ai-session-${sessionId}`);
    this.role = myRole;                        // 'owner' | 'viewer'
    this.lastSeq = 0; this.closed = false;
    this.bc.onmessage = ({ data }) => this.receive(data);
  }
  receive(m) {
    if (m.seq <= this.lastSeq) return;         // 幂等：seq 判重
    this.lastSeq = m.seq;
    if (m.type === 'turn_start') setReadOnly(true);
    if (m.type === 'delta') applyDelta(m);
    if (m.type === 'done') {                   // 对账：哈希不一致重拉
      reconcile(m.turnId, m.hash).catch(() => refetchTurn(m.turnId));
      setReadOnly(true);                       // 仍只读，等 owner 释放
    }
    if (m.type === 'release') setReadOnly(false);  // owner 关闭释放
  }
  broadcast(m) {                               // 仅 owner 调用
    if (this.role !== 'owner') throw new Error('viewer 不可广播');
    this.bc.postMessage(m);
  }
  close() {
    if (this.closed) return; this.closed = true;
    if (this.role === 'owner') this.bc.postMessage({ type: 'release' });
    this.bc.close();
  }
}
```

**评分点**:
- seq 判重保证多接收方幂等；本地广播只做加速，权威对账在服务端。
- viewer 全程只读（防双窗口并发写），owner 关闭广播 release 释放。
- close 幂等且清理通道。

