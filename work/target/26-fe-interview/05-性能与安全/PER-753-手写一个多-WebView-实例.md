---
title: [PER-753] 手写一个多 WebView 实例管理器：上限控制、LRU 销毁与容器桥协同的内存上报
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-753：手写一个多 WebView 实例管理器：上限控制、LRU 销毁与容器桥协同的内存上报

**答**：
- 实现：`acquire(route)` 获取实例——有空闲（池）复用，无空闲且未达上限新建，达上限销毁最旧（销毁前通知其 H5 执行释放清单）；`release(route)` 归还池。
- 要点：销毁通知要等 H5 确认（release 钩子完成再销毁，最多等 500ms）；销毁顺序 LRU（lastUsed 时间戳）；实例内存用量定期向容器查询（bridge 内存 JSAPI）聚合上报。
- 边界：正在前台交互的实例不销毁；跨页状态（登录 cookie）在新实例保持（cookie 共享由容器配置）；销毁失败的兜底（强制销毁并记录）。
- 评分点：销毁前确认协议与前台保护。

```javascript

class WebviewManager {
  constructor(bridge, { cap } = {}) {
    this.bridge = bridge;
    this.cap = cap ?? (isIOS() ? 3 : 2);
    this.pool = [];                                             // {route, wv, lastUsed}
  }
  async acquire(route) {
    let slot = this.pool.find(s => s.route === route);          // 同路由复用
    if (!slot) slot = this.pool.find(s => !s.front);            // 空闲复用
    if (!slot) {
      if (this.pool.length >= this.cap) await this.destroyOldest();
      const wv = await this.bridge.createWebView();
      slot = { route, wv, lastUsed: Date.now(), front: true };
      this.pool.push(slot);
    } else slot.front = true;
    slot.lastUsed = Date.now();
    return slot;
  }
  async destroyOldest() {
    const victim = this.pool.filter(s => !s.front)              // 前台保护
      .sort((a, b) => a.lastUsed - b.lastUsed)[0];
    if (!victim) return;
    const released = await Promise.race([
      this.bridge.notifyRelease(victim.wv),                     // H5 释放清单
      sleep(500),                                               // 最多等 500ms
    ]);
    await this.bridge.destroy(victim.wv, { force: !released }); // 确认后才销毁
    this.pool = this.pool.filter(s => s !== victim);
  }
  async memoryReport() {                                        // 聚合容器内存 JSAPI
    const usages = await Promise.all(this.pool.map(s =>
      this.bridge.getMemory(s.wv).catch(() => -1)));
    return this.pool.map((s, i) => ({ route: s.route, mb: usages[i] }));
  }
}
```
