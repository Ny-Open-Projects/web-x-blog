---
title: [JS-418] 笔试：手写 Atomics 计数器与生产者消费者（Worker 间）
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## JS-418：笔试：手写 Atomics 计数器与生产者消费者

**答**：用 SharedArrayBuffer + Atomics 实现主线程与 Worker 的「生产者-消费者」环形队列（容量 8 槽）：① SAB 布局：`[0]=head(写位) [1]=tail(读位) [2..9]=槽位指针(数据偏移)`；② 生产者（主线程）Atomics.compareExchange 抢 head 写槽；③ 消费者（Worker）Atomics.wait 阻塞等待新数据，读 tail 取槽；④ 无数据时消费者休眠（wait 不烧 CPU）；⑤ 主线程不能 wait（会冻结 UI），用 notify 唤醒即可。写出布局与两端代码骨架。

```javascript
// 主线程(生产者)
const sab = new SharedArrayBuffer(16 * 4);           // 0,1 控制位 + 8 槽
const i32 = new Int32Array(sab);
const CAP = 8;

function produce(dataOffset) {
  while (true) {
    const head = Atomics.load(i32, 0);
    const tail = Atomics.load(i32, 1);
    if ((head - tail) >= CAP) continue;               // 满: 自旋(可让步)
    if (Atomics.compareExchange(i32, 0, head, head + 1) === head) {
      i32[2 + (head % CAP)] = dataOffset;             // 写槽
      Atomics.notify(i32, 1);                          // 唤醒消费者
      return head;
    }                                                  // CAS 失败: 重试
  }
}

// worker.js (消费者)
const i32 = new Int32Array(sab);
function consume() {
  while (true) {
    const tail = Atomics.load(i32, 1);
    const head = Atomics.load(i32, 0);
    if (head > tail) {
      const off = i32[2 + (tail % CAP)];
      Atomics.store(i32, 1, tail + 1);                // 消费完推进 tail
      return off;
    }
    Atomics.wait(i32, 1, tail);                       // 无数据: 阻塞等待 tail 变化
  }
}
```

**评分点**：
- SAB 布局设计（控制位与槽位分离）
- compareExchange 抢槽防两生产者竞争（CAS 语义）
- Atomics.wait 只能在 Worker（主线程 wait 会冻结 UI）
- notify 唤醒点正确（生产后）与 head/tail 环绕取模
