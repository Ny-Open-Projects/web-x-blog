---
title: [JS-409] 笔试：手写 WaitGroup（计数屏障）
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## JS-409：笔试：手写 WaitGroup

**答**：实现 `WaitGroup`：① add(n)：计数 +n（任务动态加入）；② done()：计数 -1，归零时唤醒 wait()；③ wait(timeout)：返回 Promise，全部完成或超时（超时 reject 并报告未完成数）；④ 计数降到 0 后再 add 要允许（新一轮等待）；⑤ 负数 done 抛错。写出实现与「并行抓取 + 统一收尾」示例。

```javascript
class WaitGroup {
  #n = 0; #d = null;
  add(n = 1) {
    if (n < 0) throw new Error('use done() to decrement');
    this.#n += n;
  }
  done() {
    if (this.#n <= 0) throw new Error('done() without add()');
    if (--this.#n === 0 && this.#d) { const d = this.#d; this.#d = null; d.resolve(); }
  }
  wait(timeout) {
    if (this.#n === 0) return Promise.resolve();
    if (!this.#d) this.#d = Promise.withResolvers?.() ?? ((res, rej) => {}); // fallback
    this.#d ||= (() => { let resolve, reject; const p = new Promise((r, j) => { resolve = r; reject = j; }); p.resolve = resolve; p.reject = reject; return p; })();
    const d = this.#d;
    let t;
    if (timeout) t = setTimeout(() => {
      d.reject(new Error(`wait timeout, ${this.#n} pending`));
      this.#d = null;
    }, timeout);
    return d.p.finally(() => clearTimeout(t));
  }
}
// 用法: 并行抓取 + 统一收尾
const wg = new WaitGroup();
const results = [];
for (const url of urls) {
  wg.add();
  fetch(url).then(r => results.push(r)).finally(() => wg.done());
}
// 期间动态加入新任务: wg.add(); fetch(more)... wg.done();
await wg.wait(10_000);
console.log(results);
```

**评分点**：
- add/done 计数语义（动态任务加入）与负数防御
- 归零唤醒且「新一轮 add」复用（#d 置空后重建）
- wait 超时 reject 并报告 pending 数
- 计数器与 deferred 的组合实现
