---
title: [HW-135] 手写并发池（p-limit 变体）——按权重并发（大任务占 2 槽）与公平轮询调度
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-135：手写并发池（p-limit 变体）——按权重并发（大任务占 2 槽）与公平轮询调度
**答**：HW-007 p-limit 的进阶：任务带权重（重量级任务占多个并发槽，防止 4 个大任务把池占满饿死小任务）；同权重内 FIFO 公平；权重超过总槽的任务独占执行（临时降级为串行）。

```javascript
function createWeightedPool(totalSlots) {
  let used = 0;
  const queue = [];                                  // FIFO：[{fn, weight, resolve, reject}]
  function drain() {
    for (let i = 0; i < queue.length; ) {
      const job = queue[i];
      const w = Math.min(job.weight, totalSlots);    // 超重任务：独占全池执行
      if (used + w <= totalSlots) {
        queue.splice(i, 1);
        used += w;
        Promise.resolve().then(job.fn)
          .then(job.resolve, job.reject)
          .finally(() => { used -= w; drain(); });
        // 消费后不 i++：数组已移位，同位置继续尝试
      } else i++;
    }
  }
  return function pool(fn, weight = 1) {
    return new Promise((resolve, reject) => {
      queue.push({ fn, weight, resolve, reject });
      drain();
    });
  };
}
// 用法：图片下载（小）与视频转码（重）混跑
const pool = createWeightedPool(4);
pool(() => downloadThumb(url), 1);            // 12 个小任务
pool(() => transcode(video), 3);              // 大任务占 3 槽：避免 4 个转码把池占满饿死小图
// 公平性：同权重 FIFO；小任务在转码运行时仍能用剩余 1 槽
// 语义：weight > totalSlots 的任务独占执行（临时串行），完成后立即归还
```

**评分点**：
- 权重占槽模型（used 计数 + 按权重占多槽）——本题核心。
- 超重任务独占执行（min(weight, totalSlots)）的降级语义。
- FIFO 公平 + drain 的移位遍历正确性（消费后不 i++）。
- 场景价值：防大任务饿死小任务。
