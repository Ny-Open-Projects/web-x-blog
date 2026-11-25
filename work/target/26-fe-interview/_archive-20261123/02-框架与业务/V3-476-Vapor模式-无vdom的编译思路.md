---
title: [V3-476] Vapor 模式：无 vdom 的编译思路
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-476：Vapor 模式：无 vdom 的编译思路

**答**：
- Vapor 的核心：编译期把「响应式 → DOM 操作」直接编译成指令（template ref + createIf/createFor 运行时原语），跳过 vnode 创建与 diff——更新路径从「重新 render + diff」变为「响应式直接驱动 DOM 节点引用」
- 与 block 模式的对比：block 模式仍要「重跑 render 函数 + 定向 patch」；Vapor 连 render 都没有——每个动态表达式编译成一个订阅该响应式依赖的 DOM 更新回调
- 编译产物形态：`t0 = createTemplate('<div>')` + `setText(t1, () => msg)`——setText 内部 effect 订阅 msg，变化时直接 node.textContent =
- 体积与性能收益：不需要 vdom runtime（约 -40% runtime 体积）；更新性能接近 SolidJS（细粒度）
- 与现有生态的兼容：Vapor 与 vdom 组件混用需桥接（transition/KeepAlive 等内置组件的适配层）；插件生态（devtools/指令）逐个适配——这是它渐进发布的理由

```javascript
// Vapor 编译产物(示意)
const t0 = _template('<div><span> </span></div>');
const t1 = _t(t0); // span 引用
_setText(t1, () => _ctx.msg);   // 细粒度订阅, 无 diff
// 更新: msg 变 → 直接 t1.textContent = v (无 render 无 patch)
```
