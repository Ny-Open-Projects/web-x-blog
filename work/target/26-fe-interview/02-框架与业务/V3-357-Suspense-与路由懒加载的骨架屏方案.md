---
title: [V3-357] Suspense 与路由懒加载怎么组合出骨架屏方案？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-357：Suspense 与路由懒加载怎么组合出骨架屏方案？
**答**：
- 路由组件 `() => import('./Detail.vue')` 本身是异步依赖：包在 Suspense 里，chunk 加载 + setup 内异步请求都归 Suspense 管辖，fallback 展示页面级骨架。
- 分层结构：外层 Suspense 管「页面 chunk + 首屏数据」，内层模块各自再包 Suspense 管「次屏数据」——外层不等待次屏，首屏更快。
- 与 router-view 结合：`<RouterView v-slot="{ Component }"><Suspense><component :is="Component"/><template #fallback>…</template></Suspense></RouterView>`。
- 注意路由切换时 Suspense 的 pending/resolve 会重放，骨架屏天然复用；keep-alive 缓存的页面第二次进入不再触发 pending。
- 陷阱：路由内导航中断（用户快速点击）会导致 resolve 后又 pending，骨架屏要做成可复入组件，不要在 setup 里一次性创建大对象。
