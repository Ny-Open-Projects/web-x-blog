---
title: [WCN-414] 笔试：实现信号图的内存审计工具。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-414：笔试：实现信号图的内存审计工具。
**题目**：注册表记录全部 effect（创建栈/宿主/disposed）。`audit()` 返回：存活但无宿主的 effect（泄漏嫌疑）清单与依赖图规模。

```javascript
const registry = new Set();
function effect(fn, { owner = null, name = 'anon' } = {}) {
  const node = { name, owner, disposed: false,
    stack: new Error().stack.split('\n').slice(2, 5) };
  registry.add(node);
  const dispose = realEffect(fn, node);
  return () => { node.disposed = true; registry.delete(node); dispose(); };
}
function audit() {
  const leaked = [...registry].filter(e => !e.disposed && !e.owner);
  return { leaked: leaked.map(e => ({ name: e.name, stack: e.stack })),
           graphSize: registry.size };
}

```

**评分点**：
- 注册 + dispose 状态追踪。
- 宿主标记（owner 标签）。
- 审计条件：!disposed && !owner。
- 创建栈采样（定位泄漏源）。
