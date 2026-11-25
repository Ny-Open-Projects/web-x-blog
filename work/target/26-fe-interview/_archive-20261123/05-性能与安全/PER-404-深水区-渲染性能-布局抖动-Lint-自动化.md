---
title: [PER-404] 布局抖动（Layout Thrashing）的自动化检测：lint 规则 + 运行时检测双管齐下？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-404：布局抖动的自动化检测：lint 规则 + 运行时检测双管齐下？

**答**：
- 布局抖动 = 循环里"读布局属性（offsetWidth/getBoundingClientRect）→ 写样式"交替，每轮强制同步布局。人工 review 容易漏（跨函数的读写交错更隐蔽），需要自动化两道防线。
- 静态检测（lint）：自定义 ESLint 规则扫描"同一函数/循环体内的布局读取 API + 样式写入调用"模式（可误报，标记 warn 由人复核）；限制名单 API：offsetTop/Left/Width/Height、clientWidth、getBoundingClientRect、getComputedStyle。
- 运行时检测（dev only）：monkey-patch 布局读取 API——读之前检查本帧内是否有"未 flush 的写"，有则 console.warn 并输出调用栈（定位交错点）；生产环境关闭零开销。也可用 PerformanceObserver 的 longtask + 帧内 layout 计数近似。
- 修复模式：读写分离（先批量读后批量写）、FastDOM 类批量调度器、rAF 合帧。检测到抖动的修复收益立即可见（同一场景 Layout 块从 N 个变 1 个）。

```javascript
// 开发期运行时检测：布局读写交错告警
if (import.meta.env.DEV) {
  const READS = ['offsetWidth', 'offsetHeight', 'offsetTop', 'clientWidth'];
  let wroteThisFrame = false;
  const original = {};
  for (const prop of READS) {
    original[prop] = Object.getOwnPropertyDescriptor(HTMLElement.prototype, prop);
    Object.defineProperty(HTMLElement.prototype, prop, {
      get() {
        if (wroteThisFrame) console.warn('布局抖动嫌疑：本帧已有写操作又读布局', new Error().stack);
        return original[prop].get.call(this);
      },
    });
  }
  const origSet = HTMLElement.prototype.__lookupSetter__ && undefined;   // 简化：写检测挂在 style setter
  const styleDesc = Object.getOwnPropertyDescriptor(CSSStyleDeclaration.prototype, 'cssText');
  // rAF 每帧重置写标记
  requestAnimationFrame(function reset() { wroteThisFrame = false; requestAnimationFrame(reset); });
}
// lint 规则（伪码）：no-layout-thrashing —— 同一函数作用域内
// 出现读取名单 API 且存在 el.style.xxx = 写入 ⇒ warn，人工确认是否真交错
```
