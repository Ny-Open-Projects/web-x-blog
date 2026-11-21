---
title: [HW-020] 手写 EventEmitter
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-020：手写 EventEmitter

**答**：
- 评分点：内部用 `Map<事件名, Set/数组<回调>>` 维护订阅关系；on 注册、emit 触发（把注册顺序遍历并传参）、off 注销（注意遍历时的拷贝，避免回调内 off 造成索引错乱）；once 实现：包装函数执行一次后自注销，off 原始回调也要能匹配到包装函数（常考细节）；链式调用（on/off/emit 返回 this）是 Node.js 风格；事件中心单实例与命名空间（`user:login`）可顺带一提。

```javascript
// ===== 5 分钟速写版 =====
class EventEmitter {
  constructor() { this.events = new Map(); }
  on(type, cb) {
    if (!this.events.has(type)) this.events.set(type, new Set());
    this.events.get(type).add(cb);
    return this;
  }
  once(type, cb) {
    const wrap = (...args) => { this.off(type, wrap); cb(...args); };
    wrap._origin = cb;                 // 让 off 原始回调也能注销
    return this.on(type, wrap);
  }
  off(type, cb) {
    const set = this.events.get(type);
    if (set) {
      set.delete(cb);
      set.forEach(fn => fn._origin === cb && set.delete(fn)); // 兼容 once 包装
    }
    return this;
  }
  emit(type, ...args) {
    const set = this.events.get(type);
    if (!set) return false;
    [...set].forEach(cb => cb(...args)); // 拷贝后遍历，防止回调内 off 导致跳元素
    return true;
  }
}

// ===== 标准完整版（含边界处理）=====
class EventEmitterPro {
  constructor() { this.events = new Map(); this.maxListeners = 10; }
  setMaxListeners(n) { if (Number.isInteger(n) && n > 0) this.maxListeners = n; return this; }
  on(type, cb) {
    if (typeof type !== 'string' || typeof cb !== 'function') {
      throw new TypeError('type must be string and cb must be function');
    }
    if (!this.events.has(type)) this.events.set(type, new Set());
    const set = this.events.get(type);
    if (set.size >= this.maxListeners) {
      console.warn(`possible EventEmitter memory leak: ${set.size} listeners on "${type}"`);
    }
    set.add(cb);
    return this;
  }
  once(type, cb) {
    const wrap = (...args) => { this.off(type, cb); cb(...args); };
    wrap._origin = cb;
    return this.on(type, wrap);
  }
  off(type, cb) {
    if (cb === undefined) { this.events.delete(type); return this; } // 注销整类事件
    const set = this.events.get(type);
    if (set) {
      set.delete(cb);
      set.forEach(fn => fn._origin === cb && set.delete(fn));
      if (set.size === 0) this.events.delete(type); // 空集合清理
    }
    return this;
  }
  emit(type, ...args) {
    const set = this.events.get(type);
    if (!set || set.size === 0) return false;
    [...set].forEach(cb => {
      try { cb(...args); }
      catch (e) { console.error(`listener on "${type}" threw:`, e); } // 单个失败不影响其他订阅者
    });
    return true;
  }
  listenerCount(type) { return this.events.get(type)?.size ?? 0; }
}
```

---
## 三、数据结构必手写（HW-021 ~ HW-030）
