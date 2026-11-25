---
title: [OPT-073] View Transitions API 怎么在 SPA 里落地？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-073：View Transitions API 怎么在 SPA 里落地？

**答**：
- 浏览器原生"新旧两帧过渡"：`document.startViewTransition(callback)` 自动截旧快照、更新 DOM、截新快照，然后对两者做插值动画，替代手写 FLIP。
- 默认是整页淡入淡出；给元素加 `view-transition-name` 后，同一元素在前后两个状态间**单独做位移动画**（列表到详情的共享元素转场）。
- 与路由结合：React/Vue Router 的导航回调包进 startViewTransition，注意异步数据要在回调内 await，否则过渡提前结束。
- 兼容处理：不支持的浏览器直接执行回调（渐进增强），不影响功能。

```html
<!-- 一一对应：SPA 路由切换接入 View Transitions（脚本 + 样式一套落地） -->
<style>
  /* 列表缩略图与详情头图之间建立共享元素：两边同名即可自动飞过去 */
  .list-thumb { view-transition-name: product-hero; }
  .detail-img { view-transition-name: product-hero; }

  /* 全页默认过渡改为横向推进 */
  ::view-transition-old(root) { animation: slide-out 0.25s ease; }
  ::view-transition-new(root) { animation: slide-in  0.25s ease; }
  @keyframes slide-out { to { transform: translateX(-30px); opacity: 0; } }
  @keyframes slide-in  { from { transform: translateX(30px); opacity: 0; } }
  /* 注意：view-transition-name 同一时刻必须全局唯一，
     列表 N 个缩略图不能同名——只给"即将点击"的那一个动态赋值 */
</style>
<script type="module">
  // 渐进增强封装：不支持的浏览器直接执行回调
  function withViewTransition(updateFn) {
    if (!document.startViewTransition) return updateFn();
    return document.startViewTransition(updateFn).updateCallbackDone;
  }

  // 路由切换：把状态更新包进过渡，数据获取留在回调内，新快照才是最终态
  async function navigateToDetail(id, setState, fetchDetail) {
    await withViewTransition(async () => {
      const detail = await fetchDetail(id);
      setState(detail); // 触发 DOM 更新
    });
  }

  // 共享元素动态赋值：点击时才给该缩略图命名，避免列表内同名冲突
  listEl.addEventListener('click', (e) => {
    const thumb = e.target.closest('.list-thumb');
    if (thumb) thumb.style.viewTransitionName = 'product-hero';
    navigateToDetail(thumb.dataset.id, setDetail, fetchDetail);
  });
</script>
```

## 十三、内存优化进阶
