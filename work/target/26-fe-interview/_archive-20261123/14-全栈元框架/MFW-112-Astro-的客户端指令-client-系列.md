---
title: [MFW-112] Astro 的 client:* 水合指令有哪几种，各适合什么场景？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-112：Astro 的 client:* 水合指令有哪几种，各适合什么场景？
**答**：
- 四档水合策略，从重到轻：`client:load`（页面加载即水合）、`client:idle`（requestIdleCallback 后）、`client:visible`（进入视口）、`client:media`（匹配媒体查询才水合）。全部是**部分水合**：不水合的岛不加载 JS。
- 选型口诀：首屏交互必须可用（搜索框）→ load；交互可稍等（评论区）→ idle；折叠区以下（购物车按钮、评论列表）→ visible；移动端专属/桌面专属组件 → media。
- 还有 `client:only`：完全跳过 SSR，纯客户端渲染（依赖 window 的库用）。
- 关键理解：指令只影响**运行时 JS 加载**，所有岛的 HTML 都在构建期渲染好了——未水合的岛也是可见可读的（渐进增强）。

```astro
---
import SearchBox from './SearchBox.jsx';
import Comments from './Comments.vue';
import CartButton from './CartButton.svelte';
import MobileNav from './MobileNav.svelte';
---
<SearchBox client:load />            <!-- 首屏核心交互：立即水合 -->

<article>…长文内容…</article>

<Comments client:idle />             <!-- 空闲时再激活 -->
<CartButton client:visible />        <!-- 滚到才激活，省首屏 JS -->
<MobileNav client:media="(max-width: 768px)" /> <!-- 小屏才水合 -->
<ConfettiWidget client:only="react" /> <!-- 纯客户端：依赖 window 的组件 -->
```
