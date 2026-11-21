---
title: [WCN-407] 笔试：实现 signal 的 equals 自定义比较选项。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-407：笔试：实现 signal 的 equals 自定义比较选项。
**题目**：`signal(v, {equals})`：写时用 equals(new, old) 判定是否传播；默认严格相等（NaN 处理：Object.is）。

```javascript
const defaultEq = Object.is;
export function createSignal(v, { equals = defaultEq } = {}) {
  const node = signal(v);
  const rawSet = node.set.bind(node);
  node.set = (nv) => { if (!equals(nv, node._v)) rawSet(nv); };
  return node;
}
export const shallowEq = (a, b) => {
  if (Object.is(a, b)) return true;
  if (typeof a !== 'object' || !a) return false;
  const ka = Object.keys(a);
  return ka.length === Object.keys(b).length && ka.every(k => Object.is(a[k], b[k]));
};

```

**评分点**：
- 默认 equals = Object.is（NaN 正确）。
- 自定义比较签名与语义（返回 true = 不传播）。
- shallow equals 内置实现（对象一层比较）。
- 性能说明：deep equal 大对象退回引用（阈值）。
