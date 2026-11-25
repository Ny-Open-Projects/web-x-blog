---
title: [XP-386] 手写一个桥调用批处理器（带超时 flush）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## XP-386：手写一个桥调用批处理器（带超时 flush）

**答**：
- 需求：implement BridgeBatcher(bridge, windowMs=100)。call(method, args) 入队；窗口到期或队列 >= 20 条立即 flush（bridge.call __batch__）；flush 返回 Promise（等结果分发回各调用）；输出每次 call 的结果 Promise。
- 边界：method 白名单校验（未注册抛错）；队列超 50 强制 flush；结果按序分发。
- 评分点：白名单；双触发；按序分发；超限保护

```javascript
class BridgeBatcher {
  constructor(bridge, whitelist, windowMs = 100) {
    this.bridge = bridge; this.wl = new Set(whitelist);
    this.win = windowMs; this.buf = [];
  }
  call(method, args) {
    if (!this.wl.has(method)) return Promise.reject(new Error('未注册方法'));
    return new Promise(resolve => {
      this.buf.push({ method, args, resolve });
      if (this.buf.length >= 20) return this.flush();
      if (!this.timer)
        this.timer = setTimeout(() => this.flush(), this.windowMs ?? 100);
    });
  }
  async flush() {
    clearTimeout(this.timer); this.timer = null;
    if (!this.buf.length) return;
    const ops = this.buf; this.buf = [];
    if (ops.length >= 50) this.flush();                // 超限保护（剩余）
    try {
      const results = await this.bridge.call('__batch__',
        ops.map(o => ({ method: o.method, args: o.args })));
      ops.forEach((o, i) => o.resolve(results[i]));
    } catch (e) { ops.forEach(o => o.resolve(Promise.reject(e))); }
  }
}
```
