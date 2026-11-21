---
title: [WCN-112] 笔试：手写跨框架共享的消息中心（Signals store 三端联动）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 跨框架复用]
type: 笔试题
---

## WCN-112：笔试：手写跨框架共享的消息中心

**题目**：React 子应用、Vue 子应用与一个 WC 角标组件共享未读消息数：① 模块级 store：`messages` signal 数组 + `unread` computed（未读 = 已加载且未 read）；② `markAllRead()`；③ React 端用 `useSyncExternalStore` 订阅 store 快照；④ Vue 端 `watchEffect` 订阅；⑤ WC 角标 effect 直改文本；⑥ 三端写同一 store，验证一方 markAllRead 三方同步更新。

**答**：

```javascript
// store.js（框架无关）
import { createSignal, computed, effect } from './mini.js';
export const messages = createSignal([]);
export const unread = computed(() =>
  messages().filter((m) => !m.read).length);
export const markAllRead = () =>
  messages(messages().map((m) => ({ ...m, read: true })));
export const subscribe = (fn) => effect(fn);   // 统一订阅入口
export const getSnapshot = () => unread();
```

```jsx
// React 端
import { useSyncExternalStore } from 'react';
import * as store from './store.js';
function ReactBadge() {
  const n = useSyncExternalStore(
    (cb) => store.subscribe(cb),   // 订阅（effect 每次执行时回调）
    store.getSnapshot);
  return <span className="badge">{n}</span>;
}
```

```vue
<!-- Vue 端 -->
<script setup>
import { ref, watchEffect, onUnmounted } from 'vue';
import * as store from './store.js';
const n = ref(0);
const stop = watchEffect(() => { n.value = store.getSnapshot(); });
onUnmounted(stop);
</script>
<template><span class="badge">{{ n }}</span></template>
```

```javascript
// WC 角标
class MsgDot extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = '<b id="n">0</b>';
    this.#stop = store.subscribe(() => {
      this.shadowRoot.getElementById('n').textContent = String(store.getSnapshot());
    });
  }
  #stop;
  disconnectedCallback() { this.#stop(); }
}
customElements.define('msg-dot', MsgDot);
```

**评分点**：
- store 单一事实源：三端读同一 signals 模块（无桥接通信）。
- React 用 useSyncExternalStore 语义正确（subscribe + snapshot）；Vue watchEffect + onUnmounted 停止；WC 生命周期配对。
- computed unread 保持派生一致；markAllRead 不可变更新。
