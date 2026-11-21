---
title: [MFW-116] Astro 的 View Transitions 是什么？内容站怎么做「应用级」过渡？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-116：Astro 的 View Transitions 是什么？内容站怎么做「应用级」过渡？
**答**：
- Astro 的 `<ClientRouter />`（原 ViewTransitions）：多页应用（MPA）导航时用浏览器 View Transitions API 做**跨文档动画**——列表页缩略图飞到详情页头图这类「SPA 质感」，纯静态站也能有。
- 核心指令：`transition:name` 给元素命名（同名元素跨页面 morph），`transition:animate` 选动画，`transition:persist` 让某元素跨导航不重建（视频播放器不断播）。
- 与 SPA 路由的本质区别：每次导航仍是**真实的文档切换**（完整 HTML 请求），浏览器负责新旧页面的过渡动画——SEO、进可退、无水合税，只是视觉上像 SPA。
- 兜底：不支持 VT API 的浏览器自动退化为普通 MPA 导航（渐进增强）。

```astro
---
// src/layouts/Base.astro —— 引入 Router
import { ClientRouter } from 'astro:transitions';
---
<html>
  <head><ClientRouter /></head>
  <body><slot /></body>
</html>
```

```astro
<!-- 列表页：命名元素，跨页 morph -->
<img src={post.cover} transition:name={`post-${post.id}`} />
<a href={`/blog/${post.id}`}>{post.title}</a>
```

```astro
<!-- 详情页：同名元素自动衔接动画 -->
<img src={post.cover} transition:name={`post-${post.id}`} />

<!-- 跨页持久的音频播放器 -->
<audio id="player" src="/bgm.mp3" transition:persist autoplay />
```
