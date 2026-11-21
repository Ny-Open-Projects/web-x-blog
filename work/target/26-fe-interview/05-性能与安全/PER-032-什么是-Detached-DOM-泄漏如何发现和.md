---
title: [PER-032] 什么是 Detached DOM 泄漏？如何发现和修复？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-032：什么是 Detached DOM 泄漏？如何发现和修复？

**答**：
- 节点已从文档树移除，但 JS 变量、闭包或监听器仍引用它，导致整棵子树无法被 GC，这就是 Detached DOM 泄漏。
- 页面频繁切换视图/弹窗时最常见，泄漏随操作次数线性增长。
- 定位：Memory 面板拍堆快照，搜索 `Detached` 关键字（Chrome 中分离节点显示为 Detached HTMLDivElement），看 Retainers 找到持有它的变量。
- 修复：卸载时同步置空引用、移除监听器、清空定时器；框架下依托生命周期钩子统一清理。

```javascript
let detached = null;

function mount() {
  const panel = document.createElement('div');
  panel.innerHTML = '<h1>面板</h1>';
  document.body.appendChild(panel);
  detached = panel; // 全局变量持有 DOM 引用
  return panel;
}

// 反例：节点已移除，但 detached 仍引用它 -> Detached DOM 泄漏
function unmount() {
  document.querySelector('div')?.remove();
}

// 修复：卸载时同步断开引用，下次 GC 即可回收整个子树
function unmountFixed() {
  document.querySelector('div')?.remove();
  detached = null;
}

// 验证：Memory 面板拍快照，搜索 Detached 节点，看 Retainers 确认持有链
```

## 六、前端监控
