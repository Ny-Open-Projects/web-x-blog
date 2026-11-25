---
title: [V3-467] Teleport：编译透传与运行时目标容器
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-467：Teleport：编译透传与运行时目标容器

**答**：
- 编译层几乎零成本：Teleport 是普通组件标签（内置组件），编译器只做 helper 导入（_resolveComponent 不需要，TELEPORT flag 标记）——它的能力全在运行时 vnode 处理
- 运行时目标：teleport to 指定选择器/元素 → mount 时将 children DOM 移入目标容器；disabled 属性原地渲染（不 teleport）——动态 to 不支持（切换目标需要 key 强制重建）
- 与响应式的关系：Teleport 内的内容仍在父组件逻辑树中（provide/inject 正常穿透、父作用域插槽可用）——「DOM 在别处、逻辑在家里」的分离
- 更新机制：Teleport 内更新时 patch 正常进行，仅「挂载点」特殊——unmount 时把 DOM 从目标容器移除
- 深水点：SSR 下 Teleport 需要 teleport target 在服务端已存在（或标注 defer，3.5+ deferred teleport 解决「目标在内容之后渲染」的时序问题）

```vue
<Teleport to="#modal-root" :disabled="isServerRender">
  <Modal />
</Teleport>
<!-- disabled: 服务端渲染或测试环境原地渲染 -->
```
