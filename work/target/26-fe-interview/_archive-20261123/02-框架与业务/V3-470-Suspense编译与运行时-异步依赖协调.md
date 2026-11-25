---
title: [V3-470] Suspense：异步依赖收集与协调机制
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-470：Suspense：异步依赖收集与协调机制

**答**：
- Suspense 是运行时协调器：default slot 内组件的 async setup()（或 onServerPrefetch）注册「异步依赖」到当前 Suspense——依赖全部 resolve 才挂载
- pending → fallback 切换：初次渲染显示 fallback；依赖就绪后一次性替换（真实内容原子出现，无中间态）——比 per-component loading 的一致性更强
- 嵌套 Suspense：内层独立 pending——「骨架部分先出」用嵌套；外层只等直接子组件的异步依赖（孙组件的依赖归内层）
- 老内容延迟切换（timeout）：数据更新触发 async setup 重新挂起时，Suspense 可保留旧内容（pending 超时后切 fallback）——`suspense.timeout` 语义
- 已知坑：Suspense 仍是实验性（API 可能变）、async setup 错误处理需 onErrorCaptured 就近捕获、与 Transition 配合的边界场景

```vue
<Suspense @resolve="onReady" @fallback="onFallback">
  <template #default><AsyncChart /></template>
  <template #fallback><ChartSkeleton /></template>
</Suspense>
<!-- AsyncChart 的 async setup() 完成前整体 pending -->
```
