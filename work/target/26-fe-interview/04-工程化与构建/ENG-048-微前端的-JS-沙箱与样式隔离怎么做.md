---
title: [ENG-048] 微前端的 JS 沙箱与样式隔离怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-048：微前端的 JS 沙箱与样式隔离怎么做？
**答**：
- JS 沙箱：qiankun 用 Proxy 代理 window，子应用的全局写入落在假 window 上，卸载时还原。
- 样式隔离：Shadow DOM 天然隔离但兼容性与弹窗挂载麻烦；常用方案是构建期加前缀 + 运行时 scoped。
- 还可以约定命名空间（class 前缀、CSS 变量前缀）做低成本隔离。
- 沙箱不是绝对安全：能逃逸的场景（document、localStorage、定时器）需要额外代理与清理。

```javascript
// 简化版 Proxy 沙箱
class ProxySandbox {
  constructor() {
    const fakeWindow = Object.create(null);
    this.proxy = new Proxy(fakeWindow, {
      get: (target, key) => (key in target ? target[key] : window[key]),
      set: (target, key, value) => {
        target[key] = value; // 写入假 window，不污染全局
        return true;
      },
    });
  }
}

// 样式隔离三选一：Shadow DOM / 构建期前缀 / 运行时 scoped css
```

---

## 第十一章 单元测试 Vitest（ENG-049 ~ ENG-050）
