---
title: [PER-681] 手写一个 touch 事件治理工具：自动检测页面里的非 passive 监听并生成修复清单
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-681：手写一个 touch 事件治理工具：自动检测页面里的非 passive 监听并生成修复清单

**答**：
- 检测原理：包装 `EventTarget.prototype.addEventListener`，对 touchstart/touchmove/wheel 记录 options.passive 缺省的注册点（堆栈归因到代码位置），输出修复清单。
- 要点：只针对可合成滚动的事件类型；区分需要 preventDefault 的合法非 passive"（通过后续调用标记）与漏配"；`passive: undefined` 与 `false` 都算缺省但 `false` 若真用了 preventDefault 则合法。
- 边界：第三方库的监听也要覆盖（prototype 包装天然全局）；开发环境开警告，生产只统计。
- 评分点：preventDefault 合法性判定。

```javascript

function auditPassiveListeners({ warn = true } = {}) {
  const findings = [];
  const orig = EventTarget.prototype.addEventListener;
  const SCROLLY = ['touchstart', 'touchmove', 'wheel'];
  EventTarget.prototype.addEventListener = function (type, fn, options) {
    if (SCROLLY.includes(type)) {
      const opt = typeof options === 'object' ? options : {};
      const passive = opt.passive ?? false;                    // 缺省 = 非被动
      const entry = { type, passive,
        target: this === window ? 'window' : this.tagName ?? 'node',
        stack: new Error().stack?.split('\n')[2] };
      if (!passive) {
        // 包装一次，检测是否真的调用 preventDefault
        const wrapped = function (e) {
          if (e.cancelable && !e.defaultPrevented && e.type !== 'touchstart') {
            entry.legit = true;                                // 合法非 passive
          }
          return fn.call(this, e);
        };
        findings.push(entry);
        return orig.call(this, type, wrapped, options);
      }
    }
    return orig.call(this, type, fn, options);
  };
  return { report: () => findings.filter(f => !f.legit) };     // 未用 preventDefault 的都是漏配
}
// 开发环境跑：console.table(audit.report()) 修复清单
```
