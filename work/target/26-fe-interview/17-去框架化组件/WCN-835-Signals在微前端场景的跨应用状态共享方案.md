---
title: [WCN-835] Signals 在微前端场景如何做跨应用状态共享？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-835：Signals 在微前端场景如何做跨应用状态共享？

**答**：
- 结论先行：微前端里跨应用共享状态要「共享一个 signal 实例 + 统一版本 + 明确所有权」——把信号 store 提升为共享依赖（模块联邦/importmap），各微应用通过同一引用读写，避免多份实例导致状态分裂。
- 一致性前提：所有微应用必须引用同一个 signal 运行时（通过 module federation 的 shared singleton 或全局注入），否则 A 应用写的值 B 应用看不到——这是最常见的坑。
- 共享方式：① 全局 store（挂在 window/共享模块）适合简单场景；② 事件总线 + signal（各应用订阅宿主的变更事件更新本地 signal）；③ 宿主提供 context provider，子应用注入消费。
- 隔离与边界：只共享「真正需要跨应用的少量全局态」（登录态、主题、语言），业务状态各自私有，避免形成「分布式单体」；共享 signal 的 schema 与所有权要写清楚（谁写、哪些应用读）。
- 追问钩子：面试官会问「不同微应用用了不同版本的 signal 库怎么办」——答：必须统一到同一大版本并用 shared singleton 锁定，否则连 get/set 语义都可能不一致；这是微前端依赖治理的一部分。

```javascript
// 宿主注入共享 signal 单例，子应用从全局取，保证同一引用
const KEY = '__SHARED_SIGNALS__';
function ensureShared() {
  if (!globalThis[KEY]) {
    globalThis[KEY] = { auth: { user: null }, theme: 'light', listeners: new Set() };
  }
  return globalThis[KEY];
}
const shared = ensureShared();
function setTheme(next) {
  shared.theme = next;
  shared.listeners.forEach(fn => fn('theme', next)); // 通知各微应用
}
function onSharedChange(fn) { shared.listeners.add(fn); return () => shared.listeners.delete(fn); }

// 每个微应用：const shared = ensureShared(); onSharedChange((k,v) => localSignal[k].value = v);
onSharedChange((key, val) => console.log('子应用收到:', key, val));
setTheme('dark');
```
