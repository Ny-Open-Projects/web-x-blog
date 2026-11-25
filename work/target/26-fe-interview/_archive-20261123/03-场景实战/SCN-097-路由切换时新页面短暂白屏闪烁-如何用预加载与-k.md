---
title: [SCN-097] 路由切换时新页面短暂白屏闪烁，如何用预加载与 keep-alive 消除？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-097：路由切换时新页面短暂白屏闪烁，如何用预加载与 keep-alive 消除？
**答**：
- 白屏来自"旧页卸载 → 新 chunk 请求 → 新数据请求 → 渲染"的串行空窗，要逐环压缩。
- chunk 层：常用路由组件 webpackPrefetch 空闲预取；数据层：导航确认前就发起请求（beforeEnter / React loader），组件挂载时数据已在途。
- 已访问页面用 keep-alive 缓存，来回切换零白屏；剩余空窗用过渡动画或骨架屏掩盖。

```javascript
// Vue Router：chunk 预取 + 数据预取 + keep-alive 三层消除白屏
const routes = [
  {
    path: '/detail/:id',
    // 空闲时预取 chunk，点击时大概率已在缓存
    component: () => import(/* webpackPrefetch: true */ './Detail.vue'),
    beforeEnter: async (to) => {
      // 导航确认前就发数据请求，组件挂载时数据已在途
      to.meta.prefetched = fetchDetail(to.params.id);
    },
  },
];

// Detail.vue 内直接消费预取结果，不二次等待
export default {
  async setup() {
    const data = await useRoute().meta.prefetched;
    return { data };
  },
};

// App.vue：缓存常用页面，来回切换不重建不白屏
// <router-view v-slot="{ Component }">
//   <keep-alive include="ListPage,DetailPage">
//     <component :is="Component" />
//   </keep-alive>
// </router-view>
```
