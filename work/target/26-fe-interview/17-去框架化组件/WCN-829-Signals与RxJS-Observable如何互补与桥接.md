---
title: [WCN-829] Signals 与 RxJS Observable 如何互补与桥接？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-829：Signals 与 RxJS Observable 如何互补与桥接？

**答**：
- 结论先行：两者不是替代关系——Signals 擅长「当前状态是什么」（同步读、细粒度、按需计算），Observable 擅长「事件流如何随时间变化」（异步、操作符丰富、组合强）；工程上常「事件流用 RxJS，状态落地用 Signals」。
- 心智差异：Signal 是「可被拉取的容器（pull + 缓存）」，Observable 是「可被订阅的流（push）」；Signal 天然有当前值，Observable 没有（除非用 BehaviorSubject）。
- 典型分工：用户输入、WebSocket 消息、定时器用 Observable 做节流/防抖/取消/重试；处理后把结果写进 Signal，UI 通过 Signal 细粒度更新。
- 桥接方式：`toObservable(signal)`——订阅 signal 变化 push 到 Subject（注意初始值和去重）；`fromObservable(obs, initial)`——用 signal 保存流的最新值。注意背压与取消订阅（signal 无取消语义，Observable 有）。
- 追问钩子：面试官会问「能不能全用 Signal 替掉 RxJS」——答：复杂异步编排（竞态、重试、组合多个流）RxJS 仍更强；Signal 缺 `switchMap/debounce` 这类操作符，所以主流是组合而非替换。

```javascript
import { signal } from '@preact/signals-core';
import { Subject, interval, map, take } from 'rxjs';

// Signal → Observable：signal 变化时向 Subject 推送
function toObservable(s) {
  const subject = new Subject();
  s.subscribe(() => subject.next(s.value));
  return subject.asObservable();
}
// Observable → Signal：用 signal 保存流的最新值
function fromObservable(obs, initial) {
  const s = signal(initial);
  obs.subscribe(v => s.value = v);   // 生产中要在组件卸载时退订
  return s;
}
const ticks = fromObservable(interval(1000).pipe(map(i => i + 1), take(3)), 0);
const latest$ = toObservable(ticks);
latest$.subscribe(v => console.log('流中值:', v));
```
