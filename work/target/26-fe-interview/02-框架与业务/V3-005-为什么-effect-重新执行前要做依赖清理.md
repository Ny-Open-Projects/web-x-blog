---
title: [V3-005] 为什么 effect 重新执行前要做依赖清理？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-005：为什么 effect 重新执行前要做依赖清理？
**答**：
- 依赖关系是动态的：分支条件变化后，effect 可能不再读取某些属性。
- 不清理会产生"多余依赖"，改一个无关属性也会触发 effect 重跑。
- Vue 在每次 effect 运行前，把它上次收集的依赖全部删除，再重新收集。
- 简化模型：effect 身上记一个 deps 数组，指向它所在的所有依赖集合。

```javascript
let activeEffect = null;
const depsMap = new Map();

function track(target, key) {
  if (!activeEffect) return;
  if (!depsMap.has(key)) depsMap.set(key, new Set());
  const depSet = depsMap.get(key);
  depSet.add(activeEffect);
  // 记录当前 effect 收集过的依赖集合，便于之后清理
  activeEffect.deps.push(depSet);
}

function cleanup(effect) {
  effect.deps.forEach((depSet) => depSet.delete(effect));
  effect.deps.length = 0;
}

function run(effect, fn) {
  cleanup(effect); // 先清掉旧依赖，再重新收集
  activeEffect = effect;
  fn();
  activeEffect = null;
}
```
