---
title: [V3-525] 笔试：手写 effectScope（副作用作用域）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 语言特性]
type: 笔试题
---

## V3-525：笔试：手写 effectScope

**答**：实现 `effectScope()`：① run(fn)：fn 内创建的 effect/watch/computed 自动注册到 scope；② stop()：停止 scope 内所有 effect（递归停子 scope）；③ 嵌套 scope：子 scope stop 时连带自身子作用域，父 scope stop 连带子；④ detached 选项：子 scope 脱离父（父 stop 不影响）；⑤ active 状态：stop 后 run 抛错。写出实现。

```javascript
let activeScope = null;

class EffectScope {
  #effects = []; #scopes = []; active = true;
  constructor(detached = false) {
    this.detached = detached;
    this.parent = activeScope;
    if (!detached && this.parent) this.parent.#scopes.push(this);
  }
  run(fn) {
    if (!this.active) throw new Error('scope stopped');
    const prev = activeScope;
    activeScope = this;
    try {
      return fn();
    } finally {
      activeScope = prev;
    }
  }
  #register(effect) {
    if (activeScope === this) this.#effects.push(effect);
    else if (activeScope) activeScope.#register(effect);   // 冒泡注册到当前 scope
  }
  stop() {
    if (!this.active) return;
    this.active = false;
    for (const e of this.#effects) e.stop();
    for (const s of this.#scopes) s.stop();               // 递归停子作用域
    this.#effects = []; this.#scopes = [];
  }
}
// 用法: 组件级统一清理
const scope = effectScope();
scope.run(() => {
  watch(src, cb);
  const c = computed(() => heavy());
});
scope.stop();    // watch 与 computed 一起停
```

**评分点**：
- activeScope 栈切换实现自动注册
- 嵌套递归 stop 与 detached 脱离
- 注册冒泡（子作用域内的 effect 归属正确）
- stop 后 run 抛错的状态防护
