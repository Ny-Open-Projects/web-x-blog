---
title: [JS-182] 防抖节流之外还有哪些调度手段？requestIdleCallback、时间切片、Worker 怎么选？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-182：防抖节流之外还有哪些调度手段？requestIdleCallback、时间切片、Worker 怎么选？

**答**：
- 防抖/节流解决"降低触发频率"；调度三件套解决"长任务如何不阻塞渲染"：切片让出主线程、空闲调度填充空隙、离线程搬出去算。
- requestIdleCallback：浏览器空闲期执行低优任务，deadline.timeRemaining() 控制单次工作量；必须传 timeout 保底，Safari 不支持需降级 setTimeout。
- 时间切片（React Scheduler 思想）：把计算切成约 5ms 小块，用 MessageChannel 宏任务调度（比 setTimeout(0) 更快且不受 4ms 嵌套钳制），切片间可响应高优输入。
- Web Worker：CPU 密集（大 JSON 序列化、图像处理、加密）直接搬离主线程；注意结构化克隆成本，小数据搬线程得不偿失，大数据用 Transferable 零拷贝。
- 决策矩阵：IO/事件驱动 → 防抖节流；可中断计算 → 时间切片；低优后台任务 → idle callback；CPU 密集一次性 → Worker。

```javascript
// 1. requestIdleCallback 封装：空闲分批 + timeout 保底 + 降级
const scheduleIdle = window.requestIdleCallback
  ? window.requestIdleCallback.bind(window)
  : (cb) => setTimeout(() => cb({ timeRemaining: () => 0, didTimeout: true }), 1);

function runWhenIdle(items, handler) {
  let i = 0;
  function step(deadline) {
    while (i < items.length && (deadline.timeRemaining() > 0 || deadline.didTimeout)) {
      handler(items[i++]);
    }
    if (i < items.length) scheduleIdle(step, { timeout: 2000 }); // 最迟 2 秒内跑完
  }
  scheduleIdle(step, { timeout: 2000 });
}
// runWhenIdle(bigList, (item) => buildIndex(item)); 索引/预取等低优任务

// 2. 时间切片：MessageChannel 宏任务驱动，每片约 5ms
function createScheduler(sliceMs = 5) {
  const { port1, port2 } = new MessageChannel();
  let task = null;
  port1.onmessage = () => {
    const start = performance.now();
    while (task && task.list.length) {
      task.work(task.list.shift());
      if (performance.now() - start > sliceMs) { port2.postMessage(null); return; } // 超片让出
    }
    task = null;
  };
  return (list, work) => { task = { list: [...list], work }; port2.postMessage(null); };
}
// const schedule = createScheduler();
// schedule(rows, (row) => renderRow(row)); // 长列表分帧渲染，滚动不卡

// 3. Worker 分流：CPU 密集任务离线程
// worker.js: onmessage = (e) => postMessage(heavyCompute(e.data));
const worker = new Worker('worker.js');
function computeOffThread(data, transfer = []) {
  return new Promise((resolve) => {
    worker.onmessage = (e) => resolve(e.data);
    worker.postMessage(data, transfer); // 大 ArrayBuffer 走 transfer 零拷贝
  });
}

// 4. 决策速查
// 搜索联想输入 → 防抖；滚动加载 → 节流；
// 千行列表渲染 → 时间切片；大文件解析 → Worker 或流式；
// 埋点索引/缓存清理 → requestIdleCallback
```
