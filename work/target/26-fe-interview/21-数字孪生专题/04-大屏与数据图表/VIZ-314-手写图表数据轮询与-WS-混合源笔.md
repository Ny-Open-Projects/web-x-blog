---
title: [VIZ-314] 手写图表数据轮询与 WS 混合源（笔试）
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-314：手写图表数据轮询与 WS 混合源（笔试）

**答**：
- 题目：图表数据源双通道——WS 实时推送 + 轮询兜底（WS 断连自动切轮询，恢复切回）；数据版本号防旧覆盖新。
- 思路：WS 状态监听（断连 → 启动轮询定时器；恢复 → 停轮询）；版本号（数据单调递增）校验；双通道数据合并（WS 增量 + 轮询全量）。
- 评分点：通道切换；版本防旧；增量合并。

```javascript
class HybridDataSource {
  constructor(metric, { pollMs = 30000 } = {}) { this.metric = metric;
    this.pollMs = pollMs; this.version = 0; this.wsReady = false; }
  start() {
    this.ws = new WebSocket(`/stream/${this.metric}`);
    this.ws.onopen = () => { this.wsReady = true; this.stopPolling(); };
    this.ws.onclose = () => { this.wsReady = false; this.startPolling(); };   // 断连切轮询
    this.ws.onmessage = (e) => this.apply(JSON.parse(e.data), 'ws');
    this.startPolling();                                   // 先轮询兜底
  }
  startPolling() { this.poll ??= setInterval(async () => {
    const data = await fetchLatest(this.metric);
    this.apply(data, 'poll');
  }, this.pollMs); }
  stopPolling() { clearInterval(this.poll); this.poll = null; }
  apply(data, source) {
    if (data.version <= this.version) return;              // 防旧覆盖新
    this.version = data.version;
    this.onData(data.points, source);
  }
}
```
