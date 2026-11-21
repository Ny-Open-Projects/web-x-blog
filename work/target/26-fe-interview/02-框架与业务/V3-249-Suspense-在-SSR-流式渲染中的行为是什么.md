---
title: [V3-249] Suspense 在 SSR 流式渲染中的行为是什么？与客户端 Suspense 有何差异？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-249：Suspense 在 SSR 流式渲染中的行为是什么？与客户端 Suspense 有何差异？
**答**：
- SSR 行为：`renderToString` 等待所有 Suspense 依赖（同步流程）；`renderToNodeStream`/`experimental` 流式下，Suspense 边界外内容先输出，边界内异步完成后再**补发该片段 HTML**。
- 客户端补位：补发内容通过内联 `<script>` 通知运行时把 HTML 替换/水合到对应占位（fallback 位置）。
- 差异 1：客户端 Suspense 显示的是 fallback 组件；SSR 流式输出的是服务端预渲染的占位 HTML（可带真实骨架结构）。
- 差异 2：客户端可重试（key 重置）；SSR 片段失败会降级为客户端渲染（client-only 重挂）。
- Nuxt 对应：`<Suspense>` 与 Nuxt 的 `nuxt-loading-indicator`/页面级 Suspense 结合，流式开启需实验性配置或 RSC 类方案。

```javascript
// 服务端（伪流式示意）
import { renderToString } from 'vue/server-renderer';
// 全量等待模式：Suspense 依赖全部完成才返回完整 HTML（无流式收益）
const html = await renderToString(createApp(App));
// 流式模式（Nuxt/自研框架）：边界外壳先输出
// <div id="susp-1"><!--fallback 占位--></div> ...后续 chunk:
// <template data-susp="susp-1"><div class="comment">真实内容</div></template>
// <script>__VUE_SSR_SUSPENSE__.resolve('susp-1')</script> // 通知客户端替换并水合
```
