---
title: [WEB-635] 笔试：手写 WASM trap 分类包装层
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, WebAssembly]
type: 笔试题
---

## WEB-635：笔试：手写 WASM trap 分类包装层

**答**：实现 `WasmWrapper`：① 包装全部导出函数，捕获异常并分类：`WebAssembly.RuntimeError` → Fatal（实例不可用，标记 poisoned 并回调重建）；`RangeError` → OOM（可恢复，回调 onOom 由业务决定重试/拒绝）；其余 → Unknown；② 分类结果上抛自定义错误类型（带 method 名与耗时）；③ 调用耗时统计：每次调用记录 duration，超阈值（100ms）慢调用计数；④ 上报钩子 `onEvent({ kind, method, durationMs })`。写出核心实现。

```javascript
class WasmWrapper {
  constructor(instance, { onPoisoned, onEvent } = {}) {
    this.poisoned = false; this.slowCount = 0;
    this.exports = new Proxy(instance.exports, {
      get: (t, name) => {
        const fn = t[name];
        if (typeof fn !== 'function') return fn;
        return (...args) => {
          if (this.poisoned) throw new WasmFatalError(name, 'instance poisoned');
          const t0 = performance.now();
          try {
            const r = fn(...args);
            this._track(name, performance.now() - t0);
            return r;
          } catch (e) {
            const dur = performance.now() - t0;
            this._track(name, dur, true);
            if (e instanceof WebAssembly.RuntimeError) {
              this.poisoned = true;                 // trap 后内存状态不可信
              onPoisoned?.(name, e);
              throw new WasmFatalError(name, e);
            }
            if (e instanceof RangeError) throw new WasmOOMError(name, e);
            throw new WasmUnknownError(name, e);
          }
        };
      },
    });
    this.onEvent = onEvent;
  }
  _track(name, dur, failed = false) {
    if (dur > 100 && !failed) this.slowCount++;
    this.onEvent?.({ kind: failed ? 'error' : 'call', method: name, durationMs: +dur.toFixed(1) });
  }
}
class WasmFatalError extends Error {} class WasmOOMError extends Error {} class WasmUnknownError extends Error {}
```

**评分点**：
- 三类异常分类正确（RuntimeError=trap 致命 / RangeError=OOM 可恢复 / 其他）
- trap 后 poisoned 语义正确（实例状态不可信必须重建）
- 耗时统计与慢调用计数，onEvent 上报钩子
- Proxy 包装对全部导出统一生效，业务零侵入
