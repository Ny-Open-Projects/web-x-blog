---
title: [HW-038] 手写 Vue reactive 核心
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-038：手写 Vue reactive 核心

**答**：
- 评分点：`Object.defineProperty` 劫持 getter/setter（Vue2 方案）——get 时**收集依赖**（当前 Watcher 存入 Dep），set 时**派发更新**（通知所有 Watcher）；数据对象要**递归 observe**（深层属性也要响应式）；set 里新值若是对象同样要 observe；要用模块级变量 `activeWatcher`（Dep.target）做「正在求值的 Watcher」标记，Watcher 求值前后切换；能说出 Vue3 换成 Proxy 的原因——新增/删除属性、数组下标、length 无法被 defineProperty 拦截。

```javascript
// ===== 5 分钟速写版 =====
let activeWatcher = null;
class Dep {
  constructor() { this.subs = new Set(); }
  depend() { if (activeWatcher) this.subs.add(activeWatcher); }
  notify() { this.subs.forEach(w => w.update()); }
}
function defineReactive(obj, key, val) {
  const dep = new Dep();
  observe(val); // 新值/初值若为对象，递归劫持
  Object.defineProperty(obj, key, {
    get() { dep.depend(); return val; },          // 收集依赖
    set(nv) {
      if (nv === val) return;                     // 值未变不触发
      val = nv;
      observe(nv);
      dep.notify();                               // 派发更新
    }
  });
}
function observe(obj) {
  if (obj === null || typeof obj !== 'object') return;
  Object.keys(obj).forEach(k => defineReactive(obj, k, obj[k]));
}

// ===== 标准完整版（含边界处理）=====
// 复用上方 activeWatcher 模块级变量
class Dep2 {
  constructor() { this.subs = new Set(); }
  depend() {
    if (activeWatcher) {
      // 一个 Watcher 只收集一次（Set 去重），并建立双向关系便于清理
      this.subs.add(activeWatcher);
      activeWatcher.deps.add(this);
    }
  }
  notify() {
    [...this.subs].forEach(w => w.update()); // 拷贝遍历：更新中新增订阅不打乱循环
  }
}
class Watcher {
  constructor(getter, cb) {
    this.getter = getter;
    this.cb = cb;
    this.deps = new Set();
    this.value = this.get(); // 首次求值：过程中触发到的 getter 都会收集本 Watcher
  }
  get() {
    activeWatcher = this;    // 打开收集窗口
    let v;
    try { v = this.getter(); }
    finally { activeWatcher = null; } // 求值完必须关闭，防止污染其他读取
    return v;
  }
  update() {
    const old = this.value;
    this.value = this.get();
    if (old !== this.value) this.cb(this.value, old); // 值真正变化才回调
  }
}
function observe2(obj, seen = new WeakSet()) {
  if (obj === null || typeof obj !== 'object' || seen.has(obj)) return;
  seen.add(obj); // 循环引用保护
  Object.keys(obj).forEach(k => defineReactive2(obj, k, obj[k]));
}
function defineReactive2(obj, key, val) {
  const dep = new Dep2();
  observe2(val);
  Object.defineProperty(obj, key, {
    enumerable: true,
    configurable: true,
    get() { dep.depend(); return val; },
    set(nv) {
      if (nv === val || (nv !== nv && val !== val)) return; // NaN 也要能触发
      val = nv;
      observe2(nv);
      dep.notify();
    }
  });
}
// 局限说明（必答）：新增属性 / 删除属性 / 数组下标赋值不会触发，
// Vue2 用 $set/$delete 与重写七个数组方法弥补；Vue3 用 Proxy 根治。
```

---
