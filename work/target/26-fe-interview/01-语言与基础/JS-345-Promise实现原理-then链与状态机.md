---
title: [JS-345] Promise 实现原理：状态机与 then 链
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-345：Promise 实现原理：状态机与 then 链

**答**：
- 状态机三态：pending → fulfilled/rejected 不可逆；then 注册回调（pending 时入队，已决时立即入微任务）——手写核心是「回调队列 + 状态分发」
- then 链穿透：then 返回新 Promise，value 是 Promise 时递归解包（resolution procedure）；链上无回调时值/错误向下穿透
- 微任务时机：回调必须异步执行（规范要求，防同步调用时状态混乱）——queueMicrotask 或模拟；这是手写题常见的扣分点
- all/race/allSettled/any 语义：all 快速失败、any 首个成功、allSettled 全部完成、race 首个结算——实现细节是「计数器 + 结果数组按索引填充」
- 常见陷阱：then 里 throw 与 return Promise.reject 等价、resolve(Promise) 会采用其状态、未捕获 rejection 的 unhandledrejection 事件

```javascript
class MyPromise {
  #state = 'pending'; #value; #cbs = [];
  constructor(fn) {
    const resolve = (v) => { if (this.#state !== 'pending') return;
      const adopt = (x) => x instanceof MyPromise ? x.then(resolve, reject) : (this.#state='fulfilled', this.#value=x, this.#flush()); adopt(v); };
    const reject = (e) => { if (this.#state !== 'pending') return; this.#state='rejected'; this.#value=e; this.#flush(); };
    try { fn(resolve, reject); } catch (e) { reject(e); }
  }
  then(onOk, onErr) {
    return new MyPromise((resolve, reject) => {
      const run = () => queueMicrotask(() => {          // 必须异步
        try {
          const r = this.#state === 'fulfilled' ? (onOk || (v => v))(this.#value)
                                                : (onErr || (e => { throw e }))(this.#value);
          resolve(r);
        } catch (e) { reject(e); }
      });
      this.#state === 'pending' ? this.#cbs.push(run) : run();
    });
  }
  #flush() { this.#cbs.forEach(f => f()); this.#cbs = []; }
}
```

## 追问（补充）

**追问**：

1. then 回调为什么必须进微任务而不能同步执行？ → 规范要求回调总在当前执行栈清空后异步运行，同步调用会导致注册顺序与执行顺序错乱，且 pending 态分发时机不可控。
2. 手写实现里 resolve 一个 thenable 为什么要递归解包？ → 要遵循 resolution procedure：若值本身是 Promise 则采用其最终状态，否则 then 链上层拿到的会是 Promise 对象而非值。
3. Node 与浏览器对未捕获 rejection 的默认行为差异？ → 新版 Node 默认 `--unhandled-rejections=throw` 会让进程退出，浏览器只在控制台打印不中断页面，同一段代码结论不同。
