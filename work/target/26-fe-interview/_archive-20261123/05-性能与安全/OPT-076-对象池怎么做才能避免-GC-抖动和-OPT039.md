---
title: [OPT-076] 对象池怎么做才能避免 GC 抖动？和 OPT-039 的简单池差别在哪？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-076：对象池怎么做才能避免 GC 抖动？和 OPT-039 的简单池差别在哪？

**答**：
- GC 抖动来自"每帧大量小对象分配 → 频繁 minor GC"；对象池让稳态分配数为 0，常见于粒子系统、弹幕、物理模拟。
- 简单池（find+Set 标记）的问题：acquire 是 O(n) 线性查找，且 Set 自身也产生分配；**正确的池用双栈/环形数组**，acquire/release 都是 O(1)。
- 关键细节：release 时要**重置对象内部状态**（把引用类型字段清 null），否则池化对象带着旧引用反而变泄漏；池要设上限防膨胀。
- 判断是否需要：Performance 面板 GC 轨道每秒多次、堆内存锯齿剧烈，才值得上池；普通业务不要过度设计。

```javascript
// 一一对应：O(1) 双栈对象池（对比 OPT-039 的 find 版本：免线性查找、零稳态分配）
class ObjectPool {
  constructor(factory, reset, initial = 0, max = 1000) {
    this.factory = factory;
    this.reset = reset;         // 必须由业务提供：清干净所有引用字段
    this.free = [];             // 空闲栈
    this.max = max;             // 上限防膨胀
    for (let i = 0; i < initial; i++) this.free.push(factory());
    this.allocated = this.free.length; // 已创建总数（含在用）
  }
  acquire() {
    let obj = this.free.pop();
    if (!obj) {
      if (this.allocated >= this.max) throw new Error('pool exhausted'); // 泄漏预警
      obj = this.factory();
      this.allocated++;
    }
    return obj;
  }
  release(obj) {
    this.reset(obj);            // 关键：清引用，防池内对象持有旧数据
    if (this.free.length < this.max) this.free.push(obj);
  }
}

// 弹幕场景：每帧数十条，稳态零分配
const pool = new ObjectPool(
  () => ({ text: '', x: 0, y: 0, vx: 0, ref: null }), // factory
  (d) => { d.text = ''; d.ref = null; },               // reset：引用字段必须清
  100, 500
);
function spawnDanmaku(text) {
  const d = pool.acquire();
  d.text = text; d.x = canvasWidth;
  danmakuList.push(d);
}
function despawn(d) {
  const i = danmakuList.indexOf(d);
  danmakuList.splice(i, 1);
  pool.release(d);
}
```
