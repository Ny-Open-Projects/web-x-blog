---
title: [FRP-166] 多标签页的状态一致性如何实现（BroadcastChannel + storage 事件）？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-166：多标签页的状态一致性如何实现（BroadcastChannel + storage 事件）？

**答**：
- 同源多 tab 同步的两条通道：**BroadcastChannel**（内存级广播，延迟低、可传结构化对象）与 **storage 事件**（基于 localStorage 写入，其他 tab 收到 storage 事件——本 tab 不触发；适合持久化兜底）。
- 通用模式：本地 store 更新 → 广播 action/payload → 其他 tab **重放**该 action 或直接替换快照；配版本号/时间戳解决并发冲突（last-write-wins 或合并）。
- 重放式（同步 action）保证多 tab 状态机一致；快照式（同步整个 state）实现简单但大状态时开销大。
- 注意 storage 事件只保证"同源"，且是无序投递——关键操作要带序号做幂等。

```javascript
// 简化实现，帮助理解跨 tab 状态同步
class CrossTabStore {
  constructor(name, initialState) {
    this.name = name;
    this.state = initialState;
    this.version = 0;
    this.listeners = new Set();

    // 通道 1：BroadcastChannel（首选：低延迟、可传对象）
    this.channel = new BroadcastChannel(`store:${name}`);
    this.channel.onmessage = (e) => this.applyRemote(e.data);

    // 通道 2：storage 事件（兜底：BroadcastChannel 不可用时）
    window.addEventListener('storage', (e) => {
      if (e.key === `store:${name}` && e.newValue) {
        this.applyRemote(JSON.parse(e.newValue));
      }
    });
  }

  dispatch(action) {
    // 1. 本地重放
    this.state = this.reducer(this.state, action);
    this.version++;
    // 2. 广播给其他 tab
    this.channel.postMessage({ type: 'action', action, version: this.version });
    localStorage.setItem(`store:${this.name}`, JSON.stringify({
      type: 'snapshot', state: this.state, version: this.version, // 兜底：持久化快照
    }));
    this.notify();
  }

  applyRemote(msg) {
    if (msg.type === 'action') {
      if (msg.version <= this.version) return;     // 序号防护：丢弃过期广播
      this.state = this.reducer(this.state, msg.action); // 重放 action
      this.version = msg.version;
    } else {
      if (msg.version <= this.version) return;
      this.state = msg.state;                      // 快照直接替换
      this.version = msg.version;
    }
    this.notify();
  }

  reducer(state, action) {
    switch (action.type) {
      case 'add': return { ...state, items: [...state.items, action.item] };
      default: return state;
    }
  }
  notify() { this.listeners.forEach(f => f(this.state)); }
}

// 验证：tab A dispatch 后 tab B 状态一致
// tabA.dispatch({ type: 'add', item: 'x' })
// tabB 收到广播 -> 重放 add -> items 同步 —— 全程无网络请求
```

## 二十五、框架与浏览器协同
