---
title: [PER-407] Object Pool 在前端的应用：高频事件路径上的对象分配治理与池化实现？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-407：Object Pool 在前端的应用：高频事件路径上的对象分配治理？

**答**:
- 适用场景：高频事件路径上每秒创建成百上千的短命对象（鼠标移动的坐标包装、行情 tick 包装、粒子对象）——分配本身廉价但 GC 压力累积（PER-273）。池化让对象复用，GC 频率显著下降。
- 池实现要点：空闲链表（数组栈）+ acquire/release 协议；release 必须重置字段（防旧值残留造成逻辑 bug——比内存问题更常见）；池上限防"池本身泄漏"；类型统一（一个池只管一种形状的对象，隐藏字段不重置就是 bug 温床）。
- 取舍：池化增加代码复杂度，只对"热点路径上确证的分配热点"使用（Allocation timeline 定位后）；普通业务代码不池化——可读性优先。注意：现代引擎对短命对象优化很好（新生代回收快），池化收益要先测再说。
- 度量：池化前后 GC 频率（Performance 面板 GC 块密度）与分配速率（Memory 面板 Allocation timeline 蓝柱密度）对比。

```javascript
class ObjectPool {
  #free = [];
  constructor(factory, reset, { max = 200 } = {}) { Object.assign(this, { factory, reset, max }); }
  acquire(...args) {
    const obj = this.#free.pop() ?? this.factory();
    this.reset(obj, ...args);            // 必须重置字段：防旧值残留 bug
    return obj;
  }
  release(obj) {
    if (this.#free.length < this.max) this.#free.push(obj);   // 上限防池泄漏
  }
}
// 高频路径示例：指针移动事件包装
const pool = new ObjectPool(
  () => ({ x: 0, y: 0, ts: 0 }),
  (o, x, y) => { o.x = x; o.y = y; o.ts = performance.now(); },   // 全字段重置
);
canvas.addEventListener('pointermove', (e) => {
  const p = pool.acquire(e.clientX, e.clientY);
  processPoint(p);
  pool.release(p);                     // 用完即还，GC 压力消失
}, { passive: true });
```
