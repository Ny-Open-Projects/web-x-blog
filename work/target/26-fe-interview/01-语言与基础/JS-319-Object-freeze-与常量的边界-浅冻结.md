---
title: [JS-319] Object.freeze 与常量的边界：浅冻结
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 对象]
type: 面试题
---

## JS-319：Object.freeze 的边界：浅冻结

**答**：
- freeze 是浅冻结：顶层属性不可增删改；嵌套对象内部照常可变——「冻结后还能改」的经典事故
- 深冻结需递归（注意循环引用用 WeakSet 防死循环）
- 与 const 的区分：const 锁绑定（不能重新赋值），freeze 锁内容（对象内部）；两者独立
- 运行时代价：冻结对象访问属性略慢（引擎优化差异）；「防呆」用途为主——真正的不可变性靠不可变数据结构
- 检测：Object.isFrozen；strict 模式下修改冻结对象抛 TypeError

```javascript
const cfg = Object.freeze({ api: { url: '/v1' } });
cfg.api.url = '/v2';       // ⚠️ 静默成功（非严格）——浅冻结失效！

function deepFreeze(o, seen = new WeakSet()) {
  if (o && typeof o === 'object' && !seen.has(o)) {
    seen.add(o);
    Object.freeze(o);
    Object.values(o).forEach(v => deepFreeze(v, seen));
  }
  return o;
}
deepFreeze(cfg);
cfg.api.url = '/v3';       // strict 下 TypeError
```
