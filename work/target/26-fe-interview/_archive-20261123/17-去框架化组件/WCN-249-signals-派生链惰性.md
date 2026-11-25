---
title: [WCN-249] 深层派生链（a→b→c→d）的惰性求值如何避免「未订阅也重算」？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-249：深层派生链（a→b→c→d）的惰性求值如何避免「未订阅也重算」？
**答**：
- 无订阅者的中间 computed 不重算（纯惰性：dirty 标记传播，读取时才验证）。
- 「效果级」求值：只有挂到 effect 的分支才真正计算（Preact Signals 的惰性 computed）。
- 成本权衡：惰性省计算但增加验证开销——热点路径可「持续订阅」换取直接重算。
- 检测：性能剖析 computed 实际执行次数 vs 订阅数。

```javascript
// 惰性 computed：没有订阅者就不算
class Computed {
  #subscribers = 0;
  get value() {
    if (this.#subscribers === 0) return this.computeFresh();  // 拉取式
    if (this.dirty) this.recompute();
    return this.cached;
  }
}
r
```
