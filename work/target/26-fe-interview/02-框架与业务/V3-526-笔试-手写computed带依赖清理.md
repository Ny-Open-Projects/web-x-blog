---
title: [V3-526] 笔试：手写 computed（脏标记 + 分支依赖清理）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 语言特性]
type: 笔试题
---

## V3-526：笔试：手写 computed

**答**：实现 `computed(fn)`：① 懒计算：值被读时才求值，脏标记（dirty）控制重算；② 缓存：依赖未变直接返回旧值；③ 分支依赖清理：计算过程中走不同分支会收集不同依赖——重算时清掉上一轮不再读取的依赖（否则读到已被分支放弃的依赖变更也会触发失效）；④ 链式 computed：依赖 computed 的 computed 正确传播；⑤ stop（脱离响应式）。写出实现。

```javascript
let activeEffect = null;
const depMap = new WeakMap();

function computed(fn) {
  let value, dirty = true;
  const deps = new Set();          // 本 computed 收集的依赖
  const self = {
    [REF_FLAG]: true, __v_isReadonly: true,
    get value() {
      if (activeEffect) {           // 被外层 effect/computed 读取: 收集反向依赖
        deps.add(activeEffect);
        activeEffect.deps.add(self);
      }
      if (dirty) {
        const prev = activeEffect;
        activeEffect = self; self.deps = deps;
        const oldDeps = new Set(deps);
        deps.clear();
        value = fn();               // 计算过程中读到的依赖会 track 到 self
        // 分支清理: 上一轮有、这一轮没有的依赖解除订阅
        for (const d of oldDeps) if (!deps.has(d)) d.delete(self);
        dirty = false;
        activeEffect = prev;
      }
      return value;
    },
    deps,
  };
  return self;
}
// track(obj, key): dep = 获取依赖集; dep.add(activeEffect 或包含它的 computed 链)
// trigger(obj, key): 遍历 dep, 若是 computed → dirty = true 并递归 trigger 依赖它的 effect
//                    若是 effect → 重新调度
```

**评分点**：
- dirty 懒计算与缓存
- 依赖清理（分支切换后旧依赖解除）是核心考点
- computed 链传播（computed 依赖 computed 的递归 trigger）
- 反向依赖收集（value getter 中向 deps 注册 activeEffect）
