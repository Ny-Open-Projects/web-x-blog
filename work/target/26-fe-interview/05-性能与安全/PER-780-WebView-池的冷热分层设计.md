---
title: [PER-780] WebView 池的冷热分层设计：热池常驻复用与冷池按需创建的容量与预热时机
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-780：WebView 池的冷热分层设计：热池常驻复用与冷池按需创建的容量与预热时机

**答**：
- 结论：池分两层——热池（已加载空页 about:blank/常驻 2~4 个，点击即用，秒级收益）与冷池（只登记不实例化，扩容时才创建，控内存）。
- 预热时机：热池在首页 idle 或上次取用后立即补位；冷池扩容跟随页面访问频率（高频路由升级为热池成员）。
- 容量信号：热池个数受设备分档约束（低端机 1~2 个）；冷池上限防内存失控。
- 追问钩子：池化 WebView 与预渲染（prerender）二选一还是叠加？——预渲染带真实 URL 成本更高，池适合"不知道去哪"的导航。

```javascript
class WebViewPool {
  constructor({ hot = 2, coldMax = 8, lowEnd = false } = {}) {
    this.hot = []; this.cold = 0;
    this.limit = { hot: lowEnd ? 1 : hot, coldMax };
  }
  warm() {                                    // idle 时补热池
    requestIdleCallback(() => {
      while (this.hot.length < this.limit.hot) this.hot.push(this.create());
    });
  }
  acquire() {                                 // 取用：热池直取，否则走冷池创建
    const w = this.hot.pop();
    if (w) { this.warm(); return { w, reused: true }; }
    if (this.cold < this.limit.coldMax) { this.cold++; return { w: this.create(), reused: false }; }
    return null;                              // 超上限：排队或销毁最旧
  }
  release(w, clean) { clean(w); this.hot.length < this.limit.hot ? this.hot.push(w) : this.destroy(w); }
  create() { /* native bridge: create webview */ } destroy(w) { this.cold--; }
}
```
