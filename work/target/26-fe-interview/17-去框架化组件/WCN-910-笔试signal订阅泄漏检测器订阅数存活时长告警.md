---
title: [WCN-910] 手写 signal 订阅泄漏检测器：统计订阅数与 effect 存活时长阈值告警
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-910：手写 signal 订阅泄漏检测器：统计订阅数与 effect 存活时长阈值告警

**题目**：实现 `createLeakDetector({ maxSubscribers, maxLifetimeMs })`，返回 `{ track(signal), trackEffect(effectDispose, label), report() }`。要求：① track 为每个 signal 维护 subscriber 计数，订阅时 ++、取消时 --（通过返回的 unsubscribe）；② trackEffect 记录 effect 创建时间，调用 dispose 时记录存活时长；③ report() 输出两类告警：订阅数超 maxSubscribers 的 signal、存活超过 maxLifetimeMs 且从未被 dispose 的 effect（疑似泄漏）；④ 提供 `checkpoint()` 模拟时间推进（用注入的 now 函数，便于测试，不依赖真实时间）；⑤ 输出结构 `{ leakySignals: [...], longLivedEffects: [...] }`。请自足实现并给出可运行示例。

**答**：

```javascript
function createLeakDetector({ maxSubscribers = 5, maxLifetimeMs = 1000, now = () => 0 } = {}) {
  const signals = new Map(); // name -> count
  const effects = new Map(); // label -> { start, disposed }
  return {
    track(name) {
      signals.set(name, (signals.get(name) || 0) + 1);
      let active = true;
      return () => { if (active) { signals.set(name, signals.get(name) - 1); active = false; } };
    },
    trackEffect(label) {
      effects.set(label, { start: now(), disposed: false, disposeAt: null });
      let active = true;
      return () => { const e = effects.get(label); if (e && active) { e.disposed = true; e.disposeAt = now(); active = false; } };
    },
    checkpoint() { /* now 由外部闭包推进 */ },
    report() {
      return {
        leakySignals: [...signals].filter(([, n]) => n > maxSubscribers).map(([name, n]) => ({ name, subscribers: n })),
        longLivedEffects: [...effects].filter(([, e]) => !e.disposed && now() - e.start > maxLifetimeMs)
          .map(([label, e]) => ({ label, aliveMs: now() - e.start })),
      };
    },
  };
}
let t = 0;
const d = createLeakDetector({ maxSubscribers: 2, maxLifetimeMs: 500, now: () => t });
const unsub = [d.track('price'), d.track('price'), d.track('price')];
d.trackEffect('cartEffect');
t = 600; // 模拟时间推进
console.log(d.report());
// leakySignals:[{name:'price',subscribers:3}], longLivedEffects:[{label:'cartEffect',aliveMs:600}]
d.trackEffect('done'); // 另一个 effect
```

**评分点**：
- 订阅计数：track 返回 unsubscribe，调用后正确递减，不重复递减（active 标志）。
- effect 生命周期记录：trackEffect 记录开始时间，dispose 标记已释放并记录时刻。
- report 两类告警逻辑正确：超订阅阈值、超存活时长且未 dispose。
- 注入 now 函数便于测试，不依赖真实时间（checkpoint 可模拟推进）。
- 输出结构符合约定、示例可运行且结果正确。
