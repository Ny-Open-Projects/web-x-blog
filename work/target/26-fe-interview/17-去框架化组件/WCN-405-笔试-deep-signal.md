---
title: [WCN-405] 笔试：实现 deep-signal（深层对象代理，属性级订阅）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-405：笔试：实现 deep-signal（深层对象代理，属性级订阅）。
**题目**：`deepSignal(obj)` 返回 Proxy：任意嵌套属性读取自动建子信号节点（懒建），写入只触发该属性订阅者。删除/新增属性也响应。

```javascript
function deepSignal(obj, path = '') {
  const nodes = new Map();
  const getNode = (p, init) => {
    if (!nodes.has(p)) nodes.set(p, signal(init));
    return nodes.get(p);
  };
  return new Proxy(obj, {
    get(t, k) {
      const p = path ? `${path}.${k}` : String(k);
      if (typeof t[k] === 'object' && t[k]) return deepSignal(t[k], p);
      return getNode(p, t[k]).get();
    },
    set(t, k, v) { getNode(path ? `${path}.${k}` : k, v).set(v); t[k] = v; return true; },
    deleteProperty(t, k) { getNode(`${path}.${k}`).set(undefined); delete t[k]; return true; },
  });
}
const s = deepSignal({ user: { name: 'x' } });
effect(() => console.log(s.user.name));   // 只订阅 name
s.user.name = 'y';                        // 只有 name 的 effect 触发

```

**评分点**：
- Proxy get：缓存路径 → 子 signal（懒建），递归代理。
- Proxy set：写入对应子 signal（触发订阅）。
- deleteProperty 与新属性（ownKeys）处理。
- 数组方法（push）语义：触发 length 与索引订阅。
