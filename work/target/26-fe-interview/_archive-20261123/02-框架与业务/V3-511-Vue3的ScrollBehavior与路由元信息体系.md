---
title: [V3-511] Vue3 的路由元信息体系：meta 驱动的横切能力
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 路由]
type: 面试题
---

## V3-511：Vue3 的路由元信息体系：meta 驱动的横切能力

**答**：
- meta 体系设计：路由 meta 承载横切语义（title/breadcrumb/perm/layout/keepAlive/scrollBehavior/transition 名）——全局守卫与布局组件消费 meta，避免各页面重复逻辑
- 滚动行为：scrollBehavior 按 meta 定制（返回列表恢复位置用 savedPosition，详情页回顶）——配合 KeepAlive 的滚动保留（Vue Router savedPosition 与 KeepAlive 的组合语义）
- 嵌套路由的 meta 合并：to.matched 合并 meta（Object.assign 链）——「模块级 meta + 页面级覆盖」的层级设计
- 类型安全：meta 类型扩展（RouteMeta 接口声明合并）——meta 字段有类型提示与约束，避免魔法字符串
- 动态 meta：页面内改 meta（document.title）用 afterEach 统一处理——SEO 元信息（title/description/canonical）集中在路由层

```typescript
declare module 'vue-router' {
  interface RouteMeta {
    title: string; perm?: string; layout?: 'default'|'blank';
    keepAlive?: boolean; breadcrumb?: string[];
  }
}
router.afterEach((to) => {
  document.title = to.meta.title ? `${to.meta.title} - 平台` : '平台';
});
```
