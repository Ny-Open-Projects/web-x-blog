---
title: [DP-201] 源码识别：Vue3 响应式源码中的观察者与代理模式？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-201：源码识别：Vue3 响应式源码中的观察者与代理模式？
**答**：
- 代理（Proxy 包装）：reactive() 用 Proxy 拦截 get/set/deleteProperty，是结构型**代理模式**的标准实现——控制访问（依赖收集、触发更新）而不改变被代理对象接口。
- 观察者（依赖追踪）：effect 是观察者，targetMap 存 target→key→Set<effect>，set 拦截时 trigger 通知——经典观察者，但通知链路是"订阅即收集、触发即遍历"，没有显式 Subject 类。
- 发布订阅变体：track/trigger 是去中心化的 pub-sub，事件名是 (target, key) 二元组；scheduler 是中间层（控制批处理/队列化），等价于"事件 + 中间人"。
- 识别要点：面试时要能指出"Vue3 是把三种模式融进一个函数式实现"，类图不存在但角色齐全。

```javascript
// Vue3 reactivity 简化源码
const targetMap = new WeakMap();                 // target → Map<key, Set<effect>>
let activeEffect = null;
function track(target, key) {                    // 观察者注册（订阅）
  if (!activeEffect) return;
  let depsMap = targetMap.get(target) ?? targetMap.set(target, new Map()).get(target);
  depsMap.set(key, (depsMap.get(key) ?? new Set()).add(activeEffect));
}
function trigger(target, key) {                  // 观察者通知
  (targetMap.get(target)?.get(key) ?? []).forEach(e => e.scheduler?.() ?? e.run());
}
function reactive(obj) {                         // 代理模式
  return new Proxy(obj, {
    get(t, k) { track(t, k); return Reflect.get(t, k); },
    set(t, k, v) { Reflect.set(t, k, v); trigger(t, k); return true; },
  });
}
function effect(fn) { activeEffect = { run: fn }; fn(); activeEffect = null; }  // 观察者
```
