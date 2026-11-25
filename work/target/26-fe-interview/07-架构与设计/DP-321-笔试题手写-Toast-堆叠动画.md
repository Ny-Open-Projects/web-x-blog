---
title: [DP-321] 笔试题：手写 Toast 堆叠（上限/动画/退出时序）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-321：笔试题：手写 Toast 堆叠（上限/动画/退出时序）？
**答**：实现 Toast：1) 同屏上限 3 条，超限移除最旧（含退出动画）；2) 进入/退出动画（类名切换 + transitionend 兜底）；3) 手动关闭 API（返回 close 函数）；4) 位置支持 top/bottom。
**评分点**：
- 超限移除走退出动画（不是直接删 DOM）。
- transitionend + 超时兜底（动画事件丢失保护）。
- key 稳定（id 而非 index）。
- close 函数幂等（重复调用安全）。
```javascript
let seq = 0;
function toast(text, { position = 'top', duration = 3000 } = {}) {
  const host = getHost(position);                 // top/bottom 双容器
  const id = ++seq;
  const el = document.createElement('div');
  el.className = 'toast toast-enter';
  el.textContent = text;
  host.appendChild(el);
  const list = [...host.children];
  if (list.length > 3) remove(list[0]);           // 1) 超限移除最旧（走动画）
  requestAnimationFrame(() => el.classList.remove('toast-enter'));
  let closed = false;
  const timer = setTimeout(() => close(), duration);
  function close() {                              // 3) 幂等
    if (closed) return; closed = true;
    clearTimeout(timer);
    el.classList.add('toast-leave');
    let done = false;
    const finish = () => { if (done) return; done = true; el.remove(); };
    el.addEventListener('transitionend', finish, { once: true });
    setTimeout(finish, 250);                      // 2) 超时兜底
  }
  return close;
}
```
