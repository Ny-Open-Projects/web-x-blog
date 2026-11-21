---
title: [V3-203] Vue 3.5 的版本计数（version counting）如何判定 computed 脏状态？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-203：Vue 3.5 的版本计数如何判定 computed 脏状态？
**答**：
- 全局版本号：每次触发写操作，`globalVersion` 自增。
- 双重检查：computed 求值时先比对 `dep.version === globalVersion`，相等直接返回缓存值，连自身的 dirty 标记都不用碰。
- 逐级传播：若全局版本变了，再沿依赖链逐个属性检查其 `version`，任何一个依赖版本高于自己缓存版本才真正重算。
- 效果：**没被修改的 computed 即使在批量更新链路中被访问，也完全不执行 getter**，3.4 及以前需要靠 dirty flag + 重新跑一次比较。
- 追问钩子：为什么 computed 不能只在 set 时标脏？因为依赖可能来自嵌套 computed，版本号天然支持级联传递。

```javascript
// 版本计数核心思想
let globalVersion = 0;
function trigger(dep) {
  globalVersion++;
  dep.version = globalVersion; // 属性记录自己最后修改时的全局版本
  scheduleSubs(dep.subs);
}
function computedGetter(dep) {
  if (dep.version === globalVersion) return dep.value; // 快路径：0 开销
  for (let link = dep.deps; link; link = link.nextDep) {
    // 逐个检查上游依赖的版本是否更新过
    if (link.dep.version > dep.lastCheckedVersion) {
      dep.value = compute(dep); dep.version = globalVersion;
      break;
    }
  }
  return dep.value;
}
```
