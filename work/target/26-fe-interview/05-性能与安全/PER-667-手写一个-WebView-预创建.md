---
title: [PER-667] 手写一个 WebView 预创建与复用池：提前预热 webview 实例并按路由复用，统计命中收益
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-667：手写一个 WebView 预创建与复用池：提前预热 webview 实例并按路由复用，统计命中收益

**答**：
- 思路（H5 模拟层 + 容器协议）：维护池子，预创建 N 个空白 webview"（容器 JSAPI `createWebView`），用户点击时从池中取实例并 loadUrl，池空则现场创建（退化路径）；用完回收（重置状态归还）。
- 要点：预创建要有触发时机（进入首页后空闲预建 1~2 个，`requestIdleCallback`），避免抢占首屏资源；复用时状态重置要彻底（清 storage 可配置、终止残留请求）；统计命中/未命中上报收益（命中省的 webview 启动 ms）。
- 边界：预建的 webview 占内存，低端机减少池容量；页面间有共享登录态（cookie 隔离需配置）。
- 评分点：空闲预建时机与状态重置。

```javascript

class WebViewPool {
  constructor(bridge, { size = 2 } = {}) {
    this.bridge = bridge; this.pool = []; this.stats = { hit: 0, miss: 0 };
    // 空闲时预建，不抢首屏资源
    (window.requestIdleCallback ?? setTimeout)(() => this.warm(size));
  }
  async warm(n) {
    while (this.pool.length < n) {
      const w = await this.bridge.createWebView({ blank: true });  // 容器 JSAPI
      this.pool.push({ w, busy: false });
    }
  }
  async open(url, { isolate = false } = {}) {
    const slot = this.pool.find(s => !s.busy);
    if (slot) {
      this.stats.hit++;
      slot.busy = true;
      if (isolate) await this.bridge.clearStorage(slot.w);       // 状态重置
      await this.bridge.stopLoading(slot.w);                     // 终止残留请求
      await this.bridge.loadUrl(slot.w, url);
      return slot.w;
    }
    this.stats.miss++;                                           // 池空：现场创建（退化）
    return this.bridge.createWebView({ url });
  }
  recycle(w) {
    const slot = this.pool.find(s => s.w === w);
    if (slot) { slot.busy = false; this.bridge.reset(slot.w); }  // 归还复用
    else this.bridge.destroy(w);
  }
  report() { // 收益 = 命中数 × 单次 webview 启动省时（容器实测约 300ms）
    return { ...this.stats, savedMs: this.stats.hit * 300 };
  }
}
```
