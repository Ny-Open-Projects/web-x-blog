---
title: [H5-055] figure 和 figcaption 的正确用法是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-055：figure 和 figcaption 的正确用法是什么？
**答**：
- `figure` 表示"**被主体引用、但可移动到附录或其他位置而不影响正文**"的独立内容：图、代码块、图表、视频、公式。
- `figcaption` 必须是 figure 的**第一个或最后一个子元素**，为整个 figure 提供说明；一个 figure 至多一个 figcaption。
- img 的 alt 描述"图里是什么"，figcaption 解释"为什么放这张图/它说明什么"，两者互补不重复。
- 读屏会进入 figure 角色（figure/figcaption 映射为无障碍角色），figcaption 文本关联到图形，比裸 img + 下方 p 语义强。
- 不需要说明文字的图，直接用 `img + alt` 即可，不要为了"语义"硬包 figure。

```html
<!-- 图 + 说明：说明是第一个子元素 -->
<figure>
  <figcaption>图 1：各框架 2026 年满意度对比</figcaption>
  <img src="satisfaction.png" alt="柱状图，Solid 与 Svelte 满意度最高">
</figure>

<!-- 代码块也能用 figure：说明文字复用 figcaption -->
<figure>
  <figcaption>防抖函数的最小实现</figcaption>
  <pre><code>function debounce(fn, ms) { /* ... */ }</code></pre>
</figure>

<!-- 反例：无说明的装饰图不需要 figure -->
<img src="logo.png" alt="Example 公司 Logo">
```
