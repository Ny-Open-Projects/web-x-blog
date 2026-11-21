---
title: [WEB-507] 笔试：手写内存泄漏检测 hook
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 排查SOP]
type: 笔试题
---

## WEB-507：笔试：手写内存泄漏检测 hook

**题目**：实现一个泄漏检测器：hook setTimeout/setInterval/addEventListener，登记每条「谁创建的」（调用栈）；组件注销时调 `cleanup(scope)` 一键清理并报告未释放项。

**答**：
```javascript
function createLeakDetector() {
  const timers = new Map();  // id -> { type, stack, scope }
  const listeners = new Map();

  const _setTimeout = window.setTimeout, _setInterval = window.setInterval,
        _add = EventTarget.prototype.addEventListener, _rm = EventTarget.prototype.removeEventListener;

  window.setTimeout = (fn, ms, ...rest) => {
    const id = _setTimeout(fn, ms, ...rest);
    timers.set(id, { type: 'timeout', stack: new Error().stack?.split('\n')[2] || '' });
    return id;
  };
  window.setInterval = (fn, ms, ...rest) => {
    const id = _setInterval(fn, ms, ...rest);
    timers.set(id, { type: 'interval', stack: new Error().stack?.split('\n')[2] || '' });
    return id;
  };
  const _clear = clearTimeout, _clearI = clearInterval;
  window.clearTimeout = (id) => { timers.delete(id); return _clear(id); };
  window.clearInterval = (id) => { timers.delete(id); return _clearI(id); };

  EventTarget.prototype.addEventListener = function (t, fn, opt) {
    _add.call(this, t, fn, opt);
    listeners.set(fn, { target: this, t, stack: new Error().stack?.split('\n')[2] || '' });
  };
  EventTarget.prototype.removeEventListener = function (t, fn, opt) {
    _rm.call(this, t, fn, opt);
    listeners.delete(fn);
  };

  return {
    report() {
      return {
        timers: [...timers.entries()].map(([id, v]) => ({ id, ...v })),
        listeners: [...listeners.values()],
      };
    },
    cleanupTimers() {
      timers.forEach((v, id) => v.type === 'interval' ? _clearI(id) : _clear(id));
      timers.clear();
    },
  };
}
const detector = createLeakDetector();
// 页面切换时 detector.report() 检查未清理项
```

**评分点**：
- hook 后必须保留原引用并在清理 hook 时可还原（防重复 hook 叠加）
- 登记与注销（clear* / removeEventListener）成对维护 Map，数量只增不减才算泄漏
- 调用栈截取创建者位置（split('\n') 偏移正确）
- 能主动说明：此工具只用于开发环境，生产禁用（性能开销）
