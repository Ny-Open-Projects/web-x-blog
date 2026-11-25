---
title: [WCN-539] 大型应用的 Signals 分片：按路由/功能模块拆分信号图，避免全局图膨胀的策略是什么？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-539：大型应用的 Signals 分片：按路由/功能模块拆分信号图，避免全局图膨胀的策略是什么？

**答**：
- 结论：每个功能模块一个「隔离域」，域内信号可互相依赖，跨域依赖必须显式声明并经桥接。
- 好处：一个域的脏标记不扩散到全域，flush 只处理受影响域，缩小重算范围。
- 路由切换时挂载/卸载域，域内信号随域销毁，避免全局泄漏。
- 追问：跨域只读共享状态（如用户信息）怎么办？（答：提升为 global 域，其他域单向订阅，不反向写）

```javascript
class Domain {
  constructor(name) { this.name = name; this.signals = new Set(); }
  create(v) { const s = signal(v); this.signals.add(s); return s; }
  dispose() { this.signals.forEach(s => s.dispose?.()); this.signals.clear(); }
}
const domains = { user: new Domain('user'), cart: new Domain('cart') };
// 跨域：cart 只读 user，单向桥接
bridge(domains.user.signals.id, domains.cart.create(null));

// 路由卸载时销毁域，避免跨页信号泄漏
router.onLeave(() => domains.cart.dispose());
```
