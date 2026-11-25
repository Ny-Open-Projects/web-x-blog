---
title: [DP-095] 微前端的 JS 沙箱为什么是代理模式？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-095：微前端的 JS 沙箱为什么是代理模式？（高频）
**答**：
- 问题：多个子应用共享一个 `window`，全局变量/定时器/事件互相污染——沙箱要让每个子应用"以为自己独占 window"。
- legacy 方案（qiankun snapshotSandbox）：激活时拍 window 快照，卸载时还原——**备忘录**模式。
- 现代方案（ProxySandbox）：`new Proxy(fakeWindow)` 代理 get/set，写操作落在 fakeWindow，读不到再回落真 window——**代理 + 原型回落**。
- 另有 CSS 隔离（Shadow DOM = 封装）、样式前缀（策略），运行时容器 = 外观（loadMicroApp 一个入口）。

```javascript
// ProxySandbox：代理模式实现 window 隔离
class ProxySandbox {
  #fakeWindow = {};          // 子应用的私有窗口
  #isActive = false;
  #injectedKeys = new Set(); // 记录子应用写入的 key（卸载时清理）
  proxy;
  constructor(name) {
    const self = this;
    this.proxy = new Proxy(this.#fakeWindow, {
      get(target, key) {
        if (key in target) return target[key];               // 1. 先查子应用自己的
        const val = window[key];                             // 2. 回落真实 window（读共享）
        return typeof val === 'function' && !val.prototype ? val.bind(window) : val; // 保住 this
      },
      set(target, key, value) {
        self.#isActive = true;                               // 3. 写操作全部落在 fakeWindow
        if (!(key in window)) self.#injectedKeys.add(key);   // 记录新增的全局（污染治理）
        target[key] = value;
        return true;
      },
      has(target, key) { return key in target || key in window; },
      deleteProperty(target, key) { delete target[key]; return true; },
    });
    this.name = name;
  }
  activate() { this.#isActive = true; }
  deactivate() {                    // 卸载：清掉子应用注入的全局（快照法的替代）
    this.#injectedKeys.forEach((k) => { delete this.#fakeWindow[k]; });
    this.#injectedKeys.clear();
    this.#isActive = false;
  }
}
// 对照 snapshotSandbox（备忘录法，不支持多实例）
class SnapshotSandbox {
  #snapshot = {};
  activate() {
    this.#snapshot = {};                       // 1. 拍当前 window 快照（恢复上次子应用的全局）
    for (const k in window) this.#snapshot[k] = window[k];
    Object.keys(this.#modifyMap || {}).forEach((k) => { window[k] = this.#modifyMap[k]; });
  }
  deactivate() {
    this.#modifyMap = {};                      // 2. 卸载时记录改动并还原
    for (const k in window) {
      if (window[k] !== this.#snapshot[k]) {
        this.#modifyMap[k] = window[k];        // 记录子应用改了什么
        window[k] = this.#snapshot[k];         // 还原宿主
      }
    }
  }
}
const sb1 = new ProxySandbox('sub-app-1');
const subAppCode = function (windowProxy) {
  windowProxy.__POWERED_BY__ = 'sub-app-1';    // 写入被代理隔离，不污染真 window
  console.log('子应用读到', windowProxy.__POWERED_BY__);
};
subAppCode(sb1.proxy);
console.log(globalThis.__POWERED_BY__);        // undefined —— 宿主未被污染
sb1.deactivate();
```
