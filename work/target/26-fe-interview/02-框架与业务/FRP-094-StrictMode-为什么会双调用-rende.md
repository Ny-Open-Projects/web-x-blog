---
title: [FRP-094] StrictMode 为什么会双调用 render 与副作用？这对排查什么问题有帮助？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-094：StrictMode 为什么会双调用 render 与副作用？这对排查什么问题有帮助？

**答**：
- 仅开发环境生效：函数组件 render **双调用**（第二次丢弃结果）、`useState/useMemo/useReducer` 的初始化函数双调用、**effects 双挂载**（mount → destroy → 再 mount）。
- 目的 1——**暴露不纯的 render**：render 里改外部变量/依赖随机数/依赖 Date，两次调用结果不同即暴露；Concurrent 特性要求 render 可重放，纯函数是前提。
- 目的 2——**暴露缺失的 cleanup**：双挂载模拟"组件被挂载两次"，若 effect 里订阅了但没在 destroy 里取消，立即出现双份订阅/内存泄漏——为未来"组件可被挂载-卸载-重挂"的 Offscreen 等特性做准备。
- 生产构建零开销（不会双调用）；不应在代码里"适配"双调用，而应让它暴露的问题消失（render 纯化、effect 完整清理）。

```javascript
// 简化实现，帮助理解 StrictMode 双调用的检测原理
function strictDoubleInvoke(fn) {
  // 双调用：执行两次，第一次结果丢弃，只验证可重放性
  let firstResult, secondResult;
  try {
    firstResult = fn();
    secondResult = fn();
    if (firstResult !== secondResult) {
      console.warn('[StrictMode] render 结果不一致，检测到不纯函数！');
    }
  } catch (e) {
    console.warn('[StrictMode] 第二次调用抛错：', e.message);
  }
  return secondResult; // 以第二次结果为准（与真实 StrictMode 行为一致）
}

// 反例 1：render 里改外部变量 —— 双调用暴露
let callCount = 0;
const impureRender = () => { callCount++; return callCount; };
strictDoubleInvoke(impureRender); // warn：1 !== 2

// 反例 2：effect 订阅无 cleanup —— 双挂载暴露泄漏
const listeners = new Set();
const badEffect = () => {
  const handler = () => {};
  listeners.add(handler);
  // 缺少 return () => listeners.delete(handler)
  return undefined;
};
const goodEffect = () => {
  const handler = () => {};
  listeners.add(handler);
  return () => listeners.delete(handler); // 完整清理
};
const mountWithStrictMode = (effect) => {
  const destroy = strictDoubleInvoke(effect);
  destroy?.(); // StrictMode 双挂载：mount -> unmount -> mount
  effect();
};
mountWithStrictMode(badEffect);
console.log('坏 effect 残留监听器：', listeners.size); // 2：泄漏被暴露
mountWithStrictMode(goodEffect);
console.log('好 effect 残留监听器：', listeners.size); // 2：清理完整不增长
```

## 十四、React 状态管理原理
