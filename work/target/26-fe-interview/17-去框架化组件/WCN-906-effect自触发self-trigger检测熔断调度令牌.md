---
title: [WCN-906] effect 内读又写同一个 signal 的自触发（self-trigger）怎么检测与熔断
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-906：effect 内读又写同一个 signal 的自触发（self-trigger）怎么检测与熔断

**答**：
- 结论先行：effect 里读 signal 又写它，会形成「写→标脏→再次调度 effect」的自循环；框架通常靠「写值与旧值相等则不触发」兜底，但值每次都变时就会无限跑。
- 检测手段：给每次调度打调度令牌/深度计数，若同一 effect 在一次 flush 内被重新调度超过阈值（如 100 次），判定为自触发并抛错/警告。
- 设计规避：effect 应只读依赖、只写「输出型 signal」；读写分离（输入 signal 与派生 output 分开），避免同一 signal 既当因又当果（IM 未读数累计场景常见）。
- 微任务批处理的边界：如果写在 queueMicrotask 里，自触发会跨多个微任务才暴露，熔断计数要按「effect 实例 + 时间窗口」而非单次 flush。
- 追问钩子：面试官问「累加器场景怎么合法地+=1」——答：用 `untracked(() => s.value += 1)` 写入（读不建立依赖），或改用专门的状态机/reducer，让 effect 只响应不驱动。

```javascript
// 自触发熔断：同一 effect 单轮 flush 重新调度超阈值即报错
function createSafeEffect(fn, limit = 100) {
  let running = false, runs = 0, token = 0;
  function schedule() {
    const myToken = ++token;
    if (running) {
      if (++runs > limit) throw new Error('effect 自触发，已熔断');
      return;
    }
    queueMicrotask(() => {
      running = true; runs = 0;
      try { fn(); } finally { running = false; }
    });
  }
  schedule();
  return schedule;
}
let n = 0;
const s = { get v() { return n; }, set v(x) { n = x; sched(); } };
const sched = createSafeEffect(() => { console.log(s.v); s.v = s.v + 1; }); // 触发熔断
```
