---
title: [V3-008] shallowReactive 和 readonly 的应用场景是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-008：shallowReactive 和 readonly 的应用场景是什么？
**答**：
- shallowReactive 只转换第一层，适合大表格、大列表等"整体替换、局部不常改"的数据，省去深层递归开销。
- readonly 创建深层只读代理，任何修改在开发环境都会告警，适合共享的全局配置。
- shallowReadonly 只锁第一层，Vue3 的 props 本质上就是它。
- 这些 API 是性能与安全性之间的调节器，按数据访问模式选择。

```javascript
import { shallowReactive, readonly, shallowReadonly } from "vue";

// 浅层响应：只有第一层是响应式
const table = shallowReactive({ rows: [1, 2, 3], page: 1 });
table.page = 2; // 触发更新
table.rows.push(4); // 不触发更新（rows 是普通数组）

// 深层只读：适合全局配置
const frozen = readonly({ user: { name: "Tom" } });
// frozen.user.name = "Jerry"; // 开发环境运行时警告

// 浅层只读：props 的本质
const propsLike = shallowReadonly({ count: 1, nested: { value: 2 } });
// propsLike.nested.value = 3; // 深层不拦截
```

## 第二章 ref 与 reactive 家族
