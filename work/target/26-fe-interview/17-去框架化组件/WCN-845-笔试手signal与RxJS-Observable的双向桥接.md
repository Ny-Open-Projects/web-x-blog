---
title: [WCN-845] 笔试：手写 signal 与 RxJS Observable 的双向桥接（toObservable / fromObservable）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-845：笔试：手写 signal 与 RxJS Observable 的双向桥接（toObservable / fromObservable）

**题目**：基于一个最小 signal 实现（含 `get/set/subscribe`），实现两个桥接函数：① `toObservable(s)`：返回一个 Observable，订阅时立即推送 signal 的当前值，之后每次变化推送新值；用 `Object.is` 去重；返回的 subscription 退订时要移除 signal 订阅。② `fromObservable(obs, initial)`：返回一个 signal，其值为 Observable 的最新值；订阅 obs，退订函数挂在 signal 的 `dispose` 上；支持传入 `equals` 比较器避免重复 set。边界：Observable 出错时 signal 保留最后值；toObservable 的多个订阅者互相独立。

**答**：

```javascript
// 最小 signal（get/set/subscribe），与具体库无关
function signal(initial, equals = Object.is) {
  let value = initial;
  const subs = new Set();
  return {
    get: () => value,
    set(v) { if (equals(value, v)) return; value = v; subs.forEach(f => f(v)); },
    subscribe(f) { subs.add(f); return () => subs.delete(f); },
    dispose: () => subs.clear(),
  };
}
// Observable（最小实现）
function Observable(producer) {
  return { subscribe(observer) { return producer(observer); } };
}
function toObservable(s) {
  return Observable(observer => {
    let last = s.get();
    observer.next?.(last);                                  // 立即推当前值
    const unsub = s.subscribe(v => { if (!Object.is(last, v)) { last = v; observer.next?.(v); } });
    return { unsubscribe: unsub };
  });
}
function fromObservable(obs, initial, equals) {
  const s = signal(initial, equals);
  const sub = obs.subscribe({ next: v => s.set(v), error: () => {} /* 保留最后值 */ });
  s.dispose = () => { sub.unsubscribe?.(); s._realDispose?.(); }; // 组合退订
  return s;
}

const count = signal(0);
const obs = toObservable(count);
const sub1 = obs.subscribe({ next: v => console.log('A:', v) });
count.set(1);              // A: 0（立即）, A: 1
sub1.unsubscribe();
```

**评分点**：
- toObservable 订阅时立即推送当前值并去重（BehaviorSubject 语义，正确性）。
- 退订链完整：Observable 退订移除 signal 订阅，fromObservable 的 dispose 退订上游（无泄漏）。
- fromObservable 的 error 保留最后值、equals 去重（边界与性能）。
- 多订阅者独立，互不共享状态（Observable 契约）。
