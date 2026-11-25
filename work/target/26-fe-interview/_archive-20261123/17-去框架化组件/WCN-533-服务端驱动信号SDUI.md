---
title: [WCN-533] 服务端驱动 UI（SDUI）：服务端下发「信号定义 + 初始状态」，客户端如何安全恢复依赖图？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-533：服务端驱动 UI（SDUI）：服务端下发「信号定义 + 初始状态」，客户端如何安全恢复依赖图？

**答**：
- 结论：服务端只下发「声明式信号图 + 初值」（纯数据，不含函数），客户端按 schema 重建 signal/computed/effect。
- 函数型配置（如 equals）用字符串枚举映射到本地实现，杜绝反序列化任意代码。
- 恢复时先建信号、再建 computed 拓扑、最后激活 effect，顺序保证依赖可读。
- 追问：版本不一致（服务端新字段客户端不认识）怎么办？（答：schema 版本协商 + 忽略未知字段降级）

```javascript
// 服务端下发
const payload = { version: '1', signals: { price: 100, qty: 2 },
  computed: [{ name: 'total', deps: ['price','qty'], expr: 'multiply' }] };
// 客户端重建：expr 是枚举，映射到本地函数
const EXPR = { multiply: (p, q) => p * q, sum: (...xs) => xs.reduce((a,b)=>a+b,0) };
function restore(payload) {
  const store = {};
  for (const [k, v] of Object.entries(payload.signals)) store[k] = signal(v);
  for (const c of payload.computed) store[c.name] = computed(() => EXPR[c.expr](...c.deps.map(d => store[d].get())));
  return store;
}
```
