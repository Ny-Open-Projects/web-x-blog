---
title: [JS-169] BroadcastChannel 如何封装跨标签页通信？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-169：BroadcastChannel 如何封装跨标签页通信？

**答**：
- `new BroadcastChannel(name)`：同源的所有标签页（含 iframe）加入同一频道，postMessage 广播，其余页面 onmessage 接收。
- 自己发的消息自己收不到——天然的「通知其他页」语义，适合多标签登录态同步、主题切换、购物车同步。
- 与 storage 事件方案对比：BroadcastChannel 更快（内存直达）、可发结构化对象；storage 事件跨同源但只能存字符串且延迟一拍。
- 封装要点：消息带 id/timeStamp、订阅返回取消函数、用完 close 释放频道。

```javascript
class TabBus {
  constructor(channel) {
    this.id = crypto.randomUUID();          // 标识本标签页
    this.bc = new BroadcastChannel(channel);
    this.handlers = new Set();
    this.bc.onmessage = (e) => this.handlers.forEach((h) => h(e.data));
    this.bc.onmessageerror = (e) => console.warn('消息解析失败', e);
  }
  post(type, payload = {}) {
    this.bc.postMessage({                   // 统一信封：类型 + 载荷 + 来源
      type, payload,
      from: this.id,
      ts: Date.now(),
    });
  }
  sub(fn) {
    this.handlers.add(fn);
    return () => this.handlers.delete(fn);  // 返回取消订阅
  }
  destroy() { this.bc.close(); this.handlers.clear(); }
}

// 场景：多标签页登录态与主题同步
const bus = new TabBus('app-sync');
const off = bus.sub((msg) => {
  if (msg.type === 'logout') {
    console.log('其他标签页已退出，本页同步登出');
    location.href = '/login';
  }
  if (msg.type === 'theme') {
    document.documentElement.dataset.theme = msg.payload.theme;
  }
});
bus.post('theme', { theme: 'dark' });   // 其它同源标签页立即换肤，本页不收到
// 页面卸载时 bus.destroy() 释放频道
```
