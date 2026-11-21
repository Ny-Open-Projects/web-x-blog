---
title: [JS-320] Proxy 与 Reflect 的配合：使用守则
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 对象]
type: 面试题
---

## JS-320：Proxy 与 Reflect 的配合守则

**答**：
- 为什么 trap 里要用 Reflect：`Reflect.get(target, key, receiver)` 保持默认行为的完整语义（getter 里的 this 正确指向 receiver）——手写 target[key] 会丢 receiver 上下文
- 13 个 trap 对照默认操作；get/set/has/deleteProperty/apply 最常用
- 不变式（invariant）约束：set trap 不能让「不可写属性」被改成功——违反抛 TypeError
- Vue3 响应式即 Proxy 实现：get 收集依赖、set 触发更新；Reflect 保证 getter 内嵌套访问也被追踪
- 守则：所有 trap 的默认分支用 Reflect.xxx(target, ...args, receiver)；不要在 trap 里做重活（性能）

```javascript
const reactive = new Proxy(obj, {
  get(target, key, receiver) {
    track(key);                              // 依赖收集
    return Reflect.get(target, key, receiver); // ✅ getter 内 this 正确
    // ❌ return target[key] —— 若属性是 getter，内部 this 指向 target，嵌套追踪丢失
  },
  set(target, key, value, receiver) {
    const ok = Reflect.set(target, key, value, receiver);
    trigger(key);
    return ok; // 必须返回布尔（不变式要求）
  },
});
```
