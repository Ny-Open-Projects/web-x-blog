---
title: [HW-119] 手写 Proxy 表单代理——字段读写拦截、脏标记、嵌套路径与 reset/dirty 收集
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-119：手写 Proxy 表单代理——字段读写拦截、脏标记、嵌套路径与 reset/dirty 收集
**答**：用 Proxy 包装表单数据实现"脏检查表单"：get 拦截收集访问字段（渲染优化：只订阅被读过的字段）、set 拦截记录脏字段并触发通知；嵌套对象递归代理（路径化 dirty 集合）；reset 恢复初始快照并清脏。

```javascript
function reactiveForm(initial, { onChange } = {}) {
  const dirty = new Set();                              // 脏字段路径
  const visited = new Set();                            // 被读取字段（渲染订阅用）
  const snapshot = structuredClone(initial);

  function proxy(obj, path = '') {
    return new Proxy(obj, {
      get(target, key) {
        const p = path ? `${path}.${key}` : String(key);
        visited.add(p);
        const v = target[key];
        return (v && typeof v === 'object') ? proxy(v, p) : v;
      },
      set(target, key, value) {
        const p = path ? `${path}.${key}` : String(key);
        if (target[key] !== value) {
          target[key] = value;
          dirty.add(p);                                 // 脏字段收集
          onChange?.(p, value, [...dirty]);
        }
        return true;
      },
      deleteProperty(target, key) {
        dirty.add(path ? `${path}.${key}` : String(key));
        return delete target[key];
      },
    });
  }
  return {
    state: proxy(initial),
    get dirty() { return [...dirty]; },
    isDirty(field) { return dirty.has(field); },
    reset() {
      for (const k of Object.keys(initial)) initial[k] = structuredClone(snapshot)[k];
      dirty.clear();
      onChange?.('*', null, []);
    },
    get visited() { return [...visited]; },
  };
}
// 用法：state.user.name = 'x' → dirty: ['user.name']；reset 一键还原快照
// visited：React 订阅优化——组件只订阅它读过的字段（useSyncExternalStore 的 selector 依据）
```

**评分点**：
- Proxy get/set 双拦截：dirty 收集 + visited 收集（渲染订阅优化的依据）。
- 嵌套路径代理递归；路径化 dirty 集合。
- reset 用深快照还原并清脏；set 值相同不标脏。
- 能说出 Proxy vs 手动 onChange 的取舍（Proxy 侵入小但有性能开销，热路径注意）。
