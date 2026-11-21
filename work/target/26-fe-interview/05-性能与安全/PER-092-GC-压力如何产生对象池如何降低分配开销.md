---
title: [PER-092] GC 压力如何产生？对象池如何降低分配开销？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-092：GC 压力如何产生？对象池如何降低分配开销？

**答**：
- GC 压力来源：高频创建短命对象（每帧 new 数组/对象/闭包），触发频繁的 Minor GC，每次几十毫秒的分代回收在动画中表现为周期性卡顿。
- 对象池思想：**复用而不是丢弃**——对象用完归还池子，下次从池里取，把 N 次分配压缩成池初始化的 1 次。
- 适用场景：粒子系统、飞行动画、物理模拟、高频消息对象；不适合长生命周期、数量不可控的对象。
- 注意归还时**重置状态**（清数组、清字段），否则池化对象带脏数据造成逻辑 bug。

```javascript
// 通用对象池：复用短命对象，降低 Minor GC 频率
class ObjectPool {
  constructor(factory, reset, initial = 32) {
    this.factory = factory;
    this.reset = reset;
    this.free = Array.from({ length: initial }, factory); // 一次分配，之后零新增
    this.allocated = 0;
  }
  acquire() {
    const obj = this.free.pop() ?? this.factory(); // 池空才新建，稳态不再分配
    this.allocated++;
    return obj;
  }
  release(obj) {
    this.reset(obj);           // 归还前重置状态，防脏数据
    this.free.push(obj);
    this.allocated--;
  }
}

// 粒子系统实战：每帧上千个粒子对象全靠池子供应
const particlePool = new ObjectPool(
  () => ({ x: 0, y: 0, vx: 0, vy: 0, life: 0 }),
  (p) => { p.x = 0; p.y = 0; p.vx = 0; p.vy = 0; p.life = 0; },
  1024,
);

function spawnParticles(count) {
  const batch = [];
  for (let i = 0; i < count; i++) batch.push(particlePool.acquire());
  return batch; // 动画结束后逐个 particlePool.release(p)，下一帧复用
}
```
