---
title: [WCN-409] 笔试：实现 selector 订阅（只订阅对象部分字段）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-409：笔试：实现 selector 订阅（只订阅对象部分字段）。
**题目**：`select(deepSig, s => s.user.name)` 返回子 signal：源对象对应属性变化才触发，其他属性变更不触发。

```javascript
function select(source, selector) {
  return computed(() => selector(source));   // 依赖 = selector 实际读取的属性节点
}
// deep-signal 属性级节点 → 天然窄订阅
const name = select(state, s => s.user.name);
effect(() => console.log(name.get()));      // age 变化不触发

```

**评分点**：
- selector 函数在源 deep-signal 上建立窄依赖（只收集实际读取的属性节点）。
- 子 signal 作为 computed（依赖 = selector 实际读取节点）。
- 变更传播自动窄化（deep-signal 属性级节点）。
- 验证：修改无关属性 → selector 订阅者不触发。
