---
title: [FRP-125] effect 作用域与手动 stop 如何实现组件卸载的清理链？（高频）
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-125：effect 作用域与手动 stop 如何实现组件卸载的清理链？（高频）

**答**：
- 每个副作用（render effect、watch、computed 的内部 effect）创建时自动注册到**当前激活的 EffectScope**；组件 setup 运行时会 push 一个组件专属 scope。
- `scope.stop()` 遍历自己收集的所有 effect，调用 `runner.stop()`：先执行依赖清理——从**每个依赖的 dep 集合里删掉自己**（靠 effect.deps 反向链表），再置 inactive。
- 清理后 trigger 永远找不到这个 effect——组件卸载后 store 里的数据变化不会白白触发它，这就是 Vue"响应式自动清理"的闭环（对比 React 需手写 useEffect cleanup）。
- scope 可嵌套成树：父 scope stop 会级联 stop 子 scope；脱离 scope 的独立 effect 要么放进 `effectScope().run()`，要么手动 stop，否则泄漏。

```javascript
// 简化实现，帮助理解 effectScope 与 stop 清理链
let activeEffect = null;
let activeScope = null;

class EffectScope {
  constructor(detached = false) {
    this.effects = [];
    this.scopes = [];   // 子 scope，形成树
    this.active = true;
    if (!detached && activeScope) {
      activeScope.scopes.push(this); // 挂到父 scope
    }
  }
  run(fn) {
    if (!this.active) throw new Error('scope 已停止');
    const prev = activeScope;
    activeScope = this;
    try { return fn(); } finally { activeScope = prev; }
  }
  stop() {
    if (!this.active) return;
    this.active = false;
    for (const e of this.effects) e.stop();       // 停自己的 effect
    for (const s of this.scopes) s.stop();        // 级联停子 scope
  }
}

function effect(fn) {
  const e = {
    deps: new Set(), // 反向记录：我依赖了哪些 dep
    stop() {
      for (const dep of e.deps) dep.delete(e); // 核心清理：从所有 dep 中剪除自己
      e.deps.clear();
      e.stopped = true;
    }
  };
  const run = () => {
    if (e.stopped) return;
    for (const dep of e.deps) dep.delete(e);
    e.deps.clear();
    activeEffect = e;
    try { fn(); } finally { activeEffect = null; }
  };
  e.run = run;
  if (activeScope) activeScope.effects.push(e); // 自动注册进当前 scope
  run();
  return e;
}

const targetMap = new Map();
function track(key) {
  if (!activeEffect) return;
  let dep = targetMap.get(key);
  if (!dep) targetMap.set(key, dep = new Set());
  dep.add(activeEffect); activeEffect.deps.add(dep);
}
function trigger(key) { (targetMap.get(key) || []).forEach(f => f()); }

// 模拟组件：setup 里创建 scope，卸载时 stop
const state = { msg: 'a' };   // 先有数据再建 effect（避免引用未初始化变量）
const scope = new EffectScope();
let updates = 0;
scope.run(() => {
  effect(() => { updates++; track('msg'); console.log('render, msg =', state.msg); });
});
trigger('msg');            // updates = 2
scope.stop();              // 组件卸载
trigger('msg');            // 不再执行！updates 仍是 2 —— 依赖已被剪除
console.log('updates =', updates); // 2
```
