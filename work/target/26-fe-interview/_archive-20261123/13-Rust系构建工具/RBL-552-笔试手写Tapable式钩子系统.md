---
title: [RBL-552] 笔试：手写 Tapable 式钩子系统（Sync/Async/Waterfall 三类）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-552：手写 Tapable 式钩子系统（Sync/Async/Waterfall 三类）
**需求**：实现 `createHooks()`：1) `syncHook(name)`：顺序执行，返回值忽略；2) `asyncSeriesHook(name)`：异步串行（前一完成才下一）；3) `waterfallHook(name)`：瀑布（上一返回值传给下一）；4) `tap(name, fn)` / `call(...args)`；5) 插件错误传播（携带插件名）；6) 附用例：三类钩子执行与错误携带。

```javascript
function createHooks() {
  const hooks = new Map()

  function get(name, kind) {
    if (!hooks.has(name)) hooks.set(name, { kind, taps: [] })
    const h = hooks.get(name)
    if (h.kind !== kind) throw new Error(`钩子 ${name} 类型冲突: ${h.kind} vs ${kind}`)
    return h
  }

  function tap(name, kind, pluginName, fn) {
    get(name, kind).taps.push({ pluginName, fn })
    return () => {                                     // 退订
      const h = get(name, kind)
      h.taps = h.taps.filter((t) => t.pluginName !== pluginName)
    }
  }

  function callSync(name, ...args) {
    const h = hooks.get(name)
    for (const { pluginName, fn } of h.taps) {
      try { fn(...args) }
      catch (e) { throw new Error(`[hook:${name}][plugin:${pluginName}] ${e.message}`) }   // 错误携带
    }
  }

  async function callAsyncSeries(name, ...args) {
    const h = hooks.get(name)
    for (const { pluginName, fn } of h.taps) {
      try { await fn(...args) }
      catch (e) { throw new Error(`[hook:${name}][plugin:${pluginName}] ${e.message}`) }
    }
  }

  async function callWaterfall(name, value) {
    const h = hooks.get(name)
    let acc = value
    for (const { pluginName, fn } of h.taps) {
      try { acc = await fn(acc) ?? acc }               // 瀑布：返回 undefined 保持
      catch (e) { throw new Error(`[hook:${name}][plugin:${pluginName}] ${e.message}`) }
    }
    return acc
  }

  return {
    tap,
    callSync,
    callAsyncSeries,
    callWaterfall,
    taps: (name) => hooks.get(name)?.taps.map((t) => t.pluginName) ?? [],
  }
}

// 用例
const hooks = createHooks()

// SyncHook
hooks.tap('buildStart', 'sync', 'PluginA', () => console.log('A start'))
hooks.tap('buildStart', 'sync', 'PluginB', () => console.log('B start'))
hooks.callSync('buildStart')
// A start / B start

// Waterfall：配置瀑布
hooks.tap('config', 'waterfall', 'PluginA', (cfg) => ({ ...cfg, a: true }))
hooks.tap('config', 'waterfall', 'PluginB', (cfg) => ({ ...cfg, b: cfg.a }))
console.log(await hooks.callWaterfall('config', {}))    // { a: true, b: true }

// 错误携带
hooks.tap('transform', 'async', 'BadPlugin', () => { throw new Error('oops') })
try { await hooks.callAsyncSeries('transform', {}) } catch (e) {
  console.log(e.message)     // [hook:transform][plugin:BadPlugin] oops
}
```
**评分点**：
- 三类钩子语义（sync 顺序/async 串行/waterfall 传递）
- 错误传播携带插件名与钩子名（可定位）
- tap 退订函数
- 类型冲突防护（同名钩子不同 kind 报错）
