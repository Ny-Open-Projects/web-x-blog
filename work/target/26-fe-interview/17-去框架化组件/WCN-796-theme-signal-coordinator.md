---
title: [WCN-796] 笔试：手写主题切换时 signal 驱动的 WC 样式更新协调器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-796：笔试：手写主题切换时 signal 驱动的 WC 样式更新协调器

**答**：
- 需求：实现 `createThemeCoordinator(themeSignal, components)`，components 为 WC 元素数组。themeSignal 值形如 `{ brand, mode }`。每次主题变化：对每个 WC 调用 `el.setTheme?.(theme)`（若存在），否则回退设置 CSS 变量 `--brand/--mode` 到 el.style；用微任务批处理多次快速切换只应用最后一次；返回 `{ dispose }` 取消订阅。
- 要点：订阅 signal；批处理用 queueMicrotask + pending 标志；setTheme 优先、CSS 变量兜底；dispose 清理。

```javascript
function createThemeCoordinator(themeSignal, components) {
  let pending = false, latest = null;
  const unsub = themeSignal.subscribe((t) => {
    latest = t;
    if (pending) return;
    pending = true;
    queueMicrotask(() => {                          // 批处理：只应用最后一次
      pending = false;
      for (const el of components) {
        if (typeof el.setTheme === 'function') el.setTheme(latest);
        else { el.style.setProperty('--brand', latest.brand);
               el.style.setProperty('--mode', latest.mode); }
      }
    });
  });
  return { dispose() { unsub?.(); } };
}
function signal(v){ let val=v; const ss=new Set(); return {
  get value(){return val;}, set value(n){val=n;ss.forEach(f=>f(val));},
  subscribe(f){ss.add(f);return()=>ss.delete(f);} }; }
const theme = signal({ brand:'acme', mode:'light' });
const c = createThemeCoordinator(theme, [document.createElement('div')]);
theme.value = { brand:'x', mode:'dark' };
console.log(typeof c.dispose);
```

**评分点**：
- 订阅主题 signal，变化时更新所有 WC（含回退路径）。
- 微任务批处理：快速多次切换只应用最后一次。
- setTheme 优先、CSS 变量兜底，兼容不同 WC。
- dispose 取消订阅，无内存泄漏。
