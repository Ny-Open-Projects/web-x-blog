---
title: [SCN-044] 十年老项目是 jQuery + JSP，如何渐进式迁移到 Vue？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-044：十年老项目是 jQuery + JSP，如何渐进式迁移到 Vue？
**答**：
- 原则：不停服、按页面/模块逐步替换；先做工程化改造——引入 Vite 构建 Vue 产物，以 module 脚本方式挂到旧页面。
- 局部接管：Vue 应用只 mount 到旧页面的某个容器，与 jQuery 共存；两边通信用 window 自定义事件或桥接对象，禁止直接操作对方 DOM。
- 演进节奏：新功能一律 Vue 并沉淀公共组件，旧模块按迭代节奏逐个迁移，最后统一路由与全局状态、下线 jQuery。

```html
<!-- 旧 JSP 页面：Vue 只接管一个容器，jQuery 区块保持不动 -->
<div id="old-panel"><!-- 原 jQuery 区块 --></div>
<div id="new-order-panel"></div>

<script src="/legacy/jquery.min.js"></script>

<script type="module">
  // src/pages/order-panel/main.js（Vite 构建后以 module 方式引入旧页面）
  import { createApp } from 'vue';
  import OrderPanel from './OrderPanel.vue';

  createApp(OrderPanel).mount('#new-order-panel');

  // 与 jQuery 侧通信走自定义事件，互不触碰对方 DOM
  window.addEventListener('vue:order:refresh', () => bus.emit('refresh'));
</script>

<script>
  // 旧 jQuery 代码触发 Vue 更新：只广播事件
  $('#refresh-btn').on('click', function () {
    window.dispatchEvent(new CustomEvent('vue:order:refresh'));
  });
</script>
```
