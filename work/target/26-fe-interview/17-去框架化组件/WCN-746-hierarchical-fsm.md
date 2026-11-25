---
title: [WCN-746] 笔试：手写 signal 驱动的分层状态机核心（hierarchical FSM）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-746：笔试：手写 signal 驱动的分层状态机核心（hierarchical FSM）

**答**：
- 需求：实现 `createMachine(config, signalImpl)`，config 形如 `{ initial, states: { A: { on: { NEXT:'B' }, initial:'a1', states:{ a1:{}, a2:{} } }, B:{} } }`。支持嵌套状态、事件派发 `send(event)`，当前状态用 signal 暴露路径数组 `['A','a1']`。
- 要点：send 时从最深活动状态向上找匹配的 on 转移；进入新状态时若是复合状态则进入其 initial 子状态；边界：无匹配事件忽略，外部自转移。

```javascript
function signal(v) { let val = v; const subs = new Set(); return {
  get value(){return val;}, set value(n){val=n;subs.forEach(f=>f(n));}, subscribe(f){subs.add(f);} }; }
function createMachine(config) {
  const state = signal(resolve(config, config.initial));
  function resolve(cfg, name) {
    const s = cfg.states[name];
    return s.states ? [name, ...resolve(s, s.initial)] : [name];
  }
  function send(event) {
    const path = state.value;
    for (let i = path.length - 1; i >= 0; i--) {
      const node = getNode(config, path.slice(0, i + 1));
      const target = node?.on?.[event];
      if (target) { state.value = resolve(config, target); return; }
    }
  }
  function getNode(cfg, path) {
    let n = cfg.states[path[0]];
    for (const p of path.slice(1)) n = n.states[p];
    return n;
  }
  return { state, send };
}
const m = createMachine({ initial:'A', states:{
  A:{ initial:'a1', on:{ NEXT:'B' }, states:{ a1:{}, a2:{} } }, B:{} } });
m.send('NEXT');
console.log(m.state.value);   // ['B']
```

**评分点**：
- 事件派发从最深状态向上查找转移（分层语义）。
- 进入复合状态时自动进入其 initial 子状态。
- 当前状态用 signal 暴露路径，响应式可订阅。
- 无匹配事件安全忽略，具备边界防御。
