---
title: [FRP-093] Offscreen（现 Activity）组件的概念是什么？"隐藏但保活"是如何实现的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-093：Offscreen（现 Activity）组件的概念是什么？"隐藏但保活"是如何实现的？

**答**：
- Offscreen（React 18 实验特性，19 更名 Activity）允许把子树**隐藏但保留状态**：UI 不显示，组件树、state、DOM 全部保留——介于"v-if 卸载"与"v-show 样式隐藏"之间的第三种状态。
- 实现机制：Offscreen fiber 的子树以 `mode: 'hidden'` 渲染，HostComponent 走隐藏分支（`style.display = 'none'` 语义，实际通过 OffscreenDetached 标记），**状态与 fiber 完全不销毁**，恢复时从缓存树直接复用。
- 副作用契约：隐藏时**effect 卸载**（useEffect/layoutEffect 的 destroy 执行），显示时重新 mount——保证隐藏组件不发心跳轮询、不占监听，但 useState/useRef 数据全在；这是与 CSS display:none 的关键区别。
- 典型应用：Tab 缓存（切走再切回无重新请求）、预渲染下一屏（hidden 提前挂载，切换时秒开）。

```javascript
// 简化实现，帮助理解 Offscreen 的隐藏保活与 effect 生命周期
let effectLog = [];
function mountActivity(isVisible, subtree) {
  // mode: 'visible' | 'hidden'
  const mode = isVisible ? 'visible' : 'hidden';
  const el = subtree.stateNode || document.createElement('div');
  subtree.stateNode = el;
  if (mode === 'hidden') {
    // 1. DOM 保留，仅标记 detached（真实实现通过 style 与 OffscreenDetached fiber 标记）
    el.style.display = 'none';
    el.__detached = true;
    // 2. 关键差异：隐藏触发 effect 卸载（不是不执行，而是 destroy）
    if (!el.__effectsUnmounted) {
      effectLog.push('effects destroyed (polling stopped, listeners off)');
      el.__effectsUnmounted = true;
    }
    // 3. state 保留：subtree 的 Hook 链/实例完全不动
  } else {
    el.style.display = '';
    el.__detached = false;
    if (el.__effectsUnmounted) {
      effectLog.push('effects re-mounted (with preserved state)');
      el.__effectsUnmounted = false;
    }
  }
  return el;
}

// 模拟 Tab 缓存场景
const tabA = { stateNode: null }; // fiber 代表
const el = mountActivity(true, tabA);
document.body.appendChild(el);
effectLog.push('mounted (state initialized, polling on)');

mountActivity(false, tabA); // 切走
mountActivity(true, tabA);  // 切回：DOM/state 仍在，只是 effect 重挂
console.log(tabA.stateNode.style.display);           // ''：DOM 一直存在
console.log(effectLog.join('\n'));
// mounted -> effects destroyed -> effects re-mounted
// 对比 v-show：CSS display 切换不触发任何 effect；对比 v-if：卸载连 state 一起丢
```
