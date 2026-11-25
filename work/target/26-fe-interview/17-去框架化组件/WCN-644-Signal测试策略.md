---
title: [WCN-644] 如何为 Signal 逻辑写确定性测试？时间/异步如何控制？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-644：如何为 Signal 逻辑写确定性测试？时间/异步如何控制？

**答**：
- 结论：Signal 逻辑应是纯函数式可注入的——测试时创建独立 signal 实例与手动调度器，用「推进时钟」代替真实等待。
- 做法：把 effect 调度器抽象为可注入接口；测试用 mockScheduler.flush() 精确控制何时执行；断言每次 flush 后的值。
- 追问钩子：为什么不直接 setTimeout 等？真实时间让测试慢且不稳定——考察对「确定性测试」的理解。

```javascript
function createTestScheduler() {
  const queue = [];
  return {
    schedule(fn) { queue.push(fn); },
    flush() { while (queue.length) queue.shift()(); },
  };
}
function makeSystem(scheduler) {
  const count = signal(0);
  const double = computed(() => count.get() * 2);
  effect(() => scheduler.schedule(() => console.log(double.get())));
  return { count, double };
}
const sch = createTestScheduler();
const sys = makeSystem(sch);
sys.count.set(2);        // 仅入队，不立即执行
sch.flush();             // 手动推进 → 输出 4
// 断言：expect(sys.double.get()).toBe(4) —— 完全确定性
```
