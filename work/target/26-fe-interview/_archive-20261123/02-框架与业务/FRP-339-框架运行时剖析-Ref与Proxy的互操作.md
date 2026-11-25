---
title: [FRP-339] 框架运行时剖析：Ref 与 Proxy 的互操作细节
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## FRP-339：框架运行时剖析：Ref 与 Proxy 的互操作细节

**答**：
- Vue 的 Proxy 成本面：深层 reactive 是「访问时惰性代理」——读一层包一层；toRaw 逃生口（大对象绕过代理的场景——但改动不触发更新）
- 互操作问题：外部库拿到 reactive 对象（Proxy）——库内部用 Map/Set 存引用时 Proxy 键不相等（identity 问题）——toRaw 或传原始引用
- signal 库的 identity：signal 是函数调用（Solid）或对象（Preact）——跨框架传 signal 对象安全（引用稳定）
- 深拷贝与 Proxy：structuredClone 对 Proxy 的处理（克隆展开后丢响应性）——「把 reactive 对象直接传给 Worker」必须 toRaw + 手动序列化
- 性能细节：Proxy 的 get 链在热路径（每帧读深层）有开销——热点数据用 shallowRef/原始对象 + 显式更新

```javascript
// Vue Proxy 互操作坑
const state = reactive({ meta: new Map() });
state.meta.set('a', 1);
// 外部库: new Map 同引用判定 → reactive(Map) 是新代理, identity 不同!
const raw = toRaw(state.meta);        // 逃生口: 原始 Map
// Worker 传输: toRaw + structuredClone(raw) — 否则 Proxy 无法克隆
```
