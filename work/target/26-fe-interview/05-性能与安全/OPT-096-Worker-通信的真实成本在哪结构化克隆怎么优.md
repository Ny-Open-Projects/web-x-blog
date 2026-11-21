---
title: [OPT-096] Worker 通信的真实成本在哪？结构化克隆怎么优化？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-096：Worker 通信的真实成本在哪？结构化克隆怎么优化？

**答**：
- postMessage 走**结构化克隆**：深拷贝整个对象图，MB 级数据的克隆耗时与主线程 JSON 序列化同量级，"以为异步了不卡"是错觉——克隆发生在主线程。
- 成本排序：小对象（<100KB）克隆无感；大 JSON 对象克隆阻塞主线程；**TypedArray/ArrayBuffer 走 Transferable 零拷贝**（见 OPT-097）；Blob/ImageBitmap 天然可转移。
- 优化三板斧：传引用不传副本（Transferable）、**克隆发生在谁那边要想清**（在 Worker 里 fetch+裁剪，只回传小结果）、高频小消息**攒批发送**（每帧一条而非每条一条）。
- 检测：postMessage 前后打 `performance.now()`，主线程侧的差值就是克隆成本。

```javascript
// 一一对应：结构化克隆成本实测与三种优化写法
function measureClone(data, label) {
  const t0 = performance.now();
  worker.postMessage(data);          // 主线程侧完成结构化克隆
  const cost = performance.now() - t0;
  if (cost > 5) console.warn(`克隆成本 ${label}: ${cost.toFixed(1)}ms（阻塞主线程）`);
}

// 优化一：高频小消息攒批——100 条/帧变 1 条/帧
const buffer = [];
let scheduled = false;
function send(item) {
  buffer.push(item);
  if (!scheduled) {
    scheduled = true;
    setTimeout(() => {              // 帧末统一发
      worker.postMessage(buffer);   // 一次克隆一批
      buffer.length = 0;
      scheduled = false;
    }, 16);
  }
}

// 优化二：让数据不进主线程——Worker 内 fetch + 裁剪（对比反例）
// 反例：主线程 fetch 30MB -> res.json() 阻塞 -> 再克隆传给 Worker，双重灾难
// 正解：URL 传给 Worker，一切在 Worker 内完成（见 OPT-060 方案一）

// 优化三：能转移的不克隆（大数组、二进制走 Transferable）
const bigTyped = new Float64Array(1_000_000);
worker.postMessage(bigTyped, [bigTyped.buffer]); // 零拷贝转移，无克隆成本

// 克隆的隐性行为要背：
// 函数、DOM 节点、Symbol 无法克隆直接报错；
// Map/Set/Date/RegExp/ArrayBuffer 可克隆；
// getter 与原型链丢失，克隆后只剩自有可枚举属性
```
