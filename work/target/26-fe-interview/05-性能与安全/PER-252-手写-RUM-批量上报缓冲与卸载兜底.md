---
title: [PER-252] 笔试题：手写 RUM 采集的批量缓冲队列（满量/定时/卸载三路 flush + 幂等键）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-252：手写 RUM 采集的批量缓冲队列（满量/定时/卸载三路 flush + 幂等键）

**题目**：实现 `RUMQueue({ url, maxBatch = 20, interval = 5000 })`：① push 缓冲；② 满 maxBatch、interval 定时、页面 hidden/pagehide 三路触发 flush；③ flush 用 sendBeacon 优先，不支持或返回 false 时降级 fetch keepalive；④ 每条数据带 sid+seq 幂等键；⑤ 定时器在页面隐藏时暂停（省电），恢复可见时重启；⑥ flush 后清空缓冲，失败不阻塞后续。

**答**：三路 flush 保证"不积压、不丢卸载数"；定时器随可见性启停是移动端省电的基本礼节；幂等键让服务端可安全去重。

```javascript
class RUMQueue {
  constructor({ url, maxBatch = 20, interval = 5000 }) {
    Object.assign(this, { url, maxBatch, interval, buf: [], seq: 0,
      sid: crypto.randomUUID?.() ?? String(Date.now()) });
    this.timer = setInterval(() => this.flush(), interval);
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden') { this.flush(); clearInterval(this.timer); }
      else this.timer = setInterval(() => this.flush(), interval);
    });
    addEventListener('pagehide', () => this.flush());
  }
  push(data) {
    this.buf.push({ ...data, sid: this.sid, seq: ++this.seq, ts: Date.now() });
    if (this.buf.length >= this.maxBatch) this.flush();
  }
  flush() {
    const batch = this.buf.splice(0, this.buf.length);
    if (!batch.length) return;
    const body = JSON.stringify(batch);
    try {
      if (navigator.sendBeacon && navigator.sendBeacon(this.url, body)) return;  // 主路径
      fetch(this.url, { method: 'POST', body, keepalive: true }).catch(() => {}); // 降级
    } catch { /* 上报失败静默：性能数据允许丢 */ }
  }
}
// 使用：const q = new RUMQueue({ url: '/rum/batch' });
// q.push({ metric: 'LCP', value: 2100, page: '/goods/:id' });
```

**评分点**：
- 三路触发完整：满量、定时、hidden/pagehide；pagehide 用 visibilitychange(hidden) 联动而非 unload。
- sendBeacon 返回值检查 + fetch keepalive 降级，全程 try-catch 静默。
- 幂等键（sid + 递增 seq）齐备，服务端可去重。
- 定时器随可见性启停，隐藏期间不空转。
