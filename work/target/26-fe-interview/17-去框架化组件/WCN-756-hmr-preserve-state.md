---
title: [WCN-756] HMR 热替换时如何保留组件状态（preserveState）？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-756：HMR 热替换时如何保留组件状态（preserveState）？

**答**：
- 结论：热更新只替换渲染函数/样式，不卸载组件实例；把状态存在实例外的 store 中，新旧渲染函数共享同一状态对象；用 `__VUE_HMR_RUNTIME__` 风格的注册表按 id 更新 render。
- 对 hooks/effect 做清理与重建，避免重复注册；当状态结构发生不兼容变更时降级为整组件重载并提示。
- 追问钩子：修改了 props 定义导致状态含义变了还能保留吗？考察「状态兼容性检测」与「强制重载」策略。

```javascript
const registry = new Map();                       // id -> { instance, state }
function register(id, instance, state) {
  registry.set(id, { instance, state });           // 状态独立保存
}
function rerender(id, newRender) {
  const rec = registry.get(id);
  if (!rec) return;
  rec.instance.render = newRender;                 // 只换渲染函数
  rec.instance.update();                           // 复用 state
  console.log('状态已保留:', rec.state);
}
const inst = { render: () => 'old', update() {} };
register('CompA', inst, { count: 5 });
rerender('CompA', () => 'new');                    // count 仍为 5
```
