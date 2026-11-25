---
title: [V3-363] 分层 Suspense 边界如何编排数据加载优先级？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-363：分层 Suspense 边界如何编排数据加载优先级？
**答**：
- 编排原则：关键内容（首屏主数据）放最内层第一个 resolve 的边界，次要内容（评论、推荐）用独立内层 Suspense 并行加载。
- 实现方式：主数据在页面组件 setup await（外层 Suspense 管），次数据在子组件 setup await（子组件自己的 Suspense 边界管），天然分层。
- 效果：外层 resolve 不等次数据 → 首屏更快；次数据完成时局部 fallback → 内容，更新不闪整页。
- 反模式：所有数据堆在一个 setup await 串行（Promise.all 也比串行好但会互相拖慢）。
- 与 SSR 流式渲染对齐：内层边界在服务端也会流式输出，与客户端编排一致——这是分层 Suspense 的核心收益。
```html
<Suspense>            <!-- 管主数据 -->
  <PageDetail/>        <!-- setup await 主数据 -->
  <template #fallback><PageSkeleton/></template>
</Suspense>
<!-- PageDetail 内部 -->
<Suspense><Comments/></Suspense> <!-- 次数据独立边界 -->
```
