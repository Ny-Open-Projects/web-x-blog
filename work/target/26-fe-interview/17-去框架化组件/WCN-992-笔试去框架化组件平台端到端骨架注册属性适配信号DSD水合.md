---
title: [WCN-992] 手写去框架化组件平台端到端骨架：注册 + 属性适配 + 信号 + DSD SSR + 水合
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-992：手写去框架化组件平台端到端骨架：注册 + 属性适配 + 信号 + DSD SSR + 水合

**题目**：实现 `createMiniPlatform()`，返回 `{ define(name, ctor), adapt(el, props, spec), signal(init), renderDSD(el, html), hydrate(el, fn) }`。要求：① define 幂等注册（已定义则跳过）；② adapt 按 spec.kind（attr/prop）把 props 应用到元素；③ signal 返回 `{ get value(), set value(v), subscribe(f) }`，set 时值变化才通知（Object.is）；④ renderDSD 返回把 html 包进 `<template shadowrootmode="open">` 的字符串（服务端输出用）；⑤ hydrate 若 el.__hydrated 则跳过，否则执行 fn(el) 并打标，返回是否执行；⑥ 全部为纯逻辑，不依赖真实自定义元素注册。请自足实现并给出可运行示例。

**答**：

```javascript
function createMiniPlatform() {
  const defined = new Set();
  return {
    define(name, ctor) {
      if (defined.has(name)) return false;
      defined.add(name); return true;
    },
    adapt(el, props = {}, spec = {}) {
      for (const [k, v] of Object.entries(props)) {
        if ((spec[k] || {}).kind === 'prop') el[k] = v;
        else v == null ? el.removeAttribute(k) : el.setAttribute(k, String(v));
      }
    },
    signal(init) {
      let v = init; const subs = new Set();
      return { get value() { return v; },
        set value(n) { if (!Object.is(n, v)) { v = n; subs.forEach(f => f(v)); } },
        subscribe(f) { subs.add(f); return () => subs.delete(f); } };
    },
    renderDSD(el, html) {
      return `<${el}><template shadowrootmode="open">${html}</template></${el}>`;
    },
    hydrate(el, fn) {
      if (el.__hydrated) return false;
      fn(el); el.__hydrated = true; return true;
    },
  };
}
const p = createMiniPlatform();
const s = p.signal(0); s.subscribe(v => console.log('v=', v)); s.value = 1; // v=1
const el = {};
console.log(p.hydrate(el, x => x.ok = true), p.hydrate(el, () => {})); // true false
console.log(p.renderDSD('ds-card', '<b>hi</b>'));
```

**评分点**：
- define 幂等注册正确（重复返回 false）。
- adapt 按 kind 路由 attr/prop，null 移除属性。
- signal 值变化才通知（Object.is），subscribe 返回取消函数。
- renderDSD 正确包裹 template shadowrootmode。
- hydrate 幂等、示例可运行且输出正确。
