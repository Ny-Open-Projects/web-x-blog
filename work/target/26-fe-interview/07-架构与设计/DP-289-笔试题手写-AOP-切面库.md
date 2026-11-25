---
title: [DP-289] 笔试题：手写 AOP 切面库（before/after/around）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-289：笔试题：手写 AOP 切面库（before/after/around）？
**答**：实现 aspect 库：1) `before(obj, method, hook)`（hook 返回 false 阻断原方法）；2) `after`（拿到返回值可改写）；3) `around`（完全接管，可调用 target 转发）；4) 支持异步方法；5) 移除切面（返回 unweave）。
**评分点**：
- 三类切面语义正确（before 短路/after 改写/around 转发）。
- 异步兼容（await 原方法与 hook）。
- this 绑定保持（Reflect.apply）。
- unweave 恢复原方法。
```javascript
function before(obj, method, hook) {
  const orig = obj[method];
  obj[method] = function (...args) {
    if (hook.apply(this, args) === false) return;           // 1) 阻断
    return orig.apply(this, args);
  };
  return () => { obj[method] = orig; };                     // 5) unweave
}
function after(obj, method, hook) {
  const orig = obj[method];
  obj[method] = async function (...args) {
    const result = await orig.apply(this, args);            // 4) 异步
    return hook.call(this, result, args) ?? result;         // 2) hook 可改写返回值
  };
  return () => { obj[method] = orig; };
}
function around(obj, method, hook) {
  const orig = obj[method];
  obj[method] = function (...args) {
    return hook.call(this, () => orig.apply(this, args), ...args);   // 3) target 转发
  };
  return () => { obj[method] = orig; };
}
// 用：around(tracker, 'send', async (target, payload) => {
//   if (sampled()) return target();      // 采样后才真正上报
// }); 
```
