---
title: [WEB-575] 笔试：手写 QUIC 连接迁移事件采集器（App/WebView 桥）
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 网络]
type: 笔试题
---

## WEB-575：笔试：手写 QUIC 连接迁移事件采集器（App/WebView 桥）

**答**：在 Hybrid 场景实现 `MigrationCollector`：① 通过 JSBridge 订阅原生层网络变化与 QUIC 连接迁移事件（桥方法约定 `net.change` / `conn.migrated`）；② 采集字段：迁移前后 IP 类型（v4/v6）、网络类型、迁移耗时、迁移结果；③ 事件去重：同一连接 2s 内多次迁移合并为一条（保留最后一次）；④ 本地缓冲队列，满 20 条或 10s 定时批量上报；⑤ 失败上报重试一次后丢弃。写出核心实现。

```javascript
class MigrationCollector {
  constructor(bridge) {
    this.queue = []; this.dedup = new Map(); this.timer = null;
    bridge.on('net.change', (e) => this._onEvent({ ...e, type: 'net.change' }));
    bridge.on('conn.migrated', (e) => this._onEvent({ ...e, type: 'conn.migrated' }));
    setInterval(() => this._flush(), 10_000);
  }
  _onEvent(e) {
    const key = e.cid || `${e.from}→${e.to}`;
    const prev = this.dedup.get(key);
    if (prev && Date.now() - prev.ts < 2000) {
      this.dedup.set(key, e);           // 合并保留最后一次
      this.queue[this.queue.indexOf(prev)] = e;
      return;
    }
    this.dedup.set(key, e);
    this.queue.push(e);
    if (this.queue.length >= 20) this._flush();
  }
  _flush() {
    const batch = this.queue.splice(0);
    if (!batch.length) return;
    navigator.sendBeacon('/api/mon/migration', JSON.stringify(batch));
    // sendBeacon 失败无法感知: 桥场景改用 fetch, 失败重试1次后丢弃
  }
}
```

**评分点**：
- 桥事件协议字段设计完整（cid/前后 IP/网络类型/耗时/结果）
- 2s 合并去重逻辑正确且队列同步更新
- 批量触发条件双通道（数量 + 定时）
- 上报用批量信标并考虑失败兜底
