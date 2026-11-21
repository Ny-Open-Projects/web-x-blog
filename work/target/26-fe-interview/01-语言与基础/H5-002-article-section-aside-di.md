---
title: [H5-002] article、section、aside、div 怎么区分使用？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-002：article、section、aside、div 怎么区分使用？
**答**：
- `article`：独立成篇、脱离页面也成立的内容（文章、评论、卡片商品）。
- `section`：按主题分组的内容块，必须有标题（h2~h6）；如果只是为样式包一层就用 div。
- `aside`：与主内容弱相关的外围内容（侧栏、广告、标签页脚注）。
- `div`：无语义容器，仅用于布局与样式；判断标准是"能不能给这个块起一个有意义的名字"。

```html
<!-- article 与 section 的嵌套判断 -->
<article>
  <h1>2026 前端趋势报告</h1>

  <section> <!-- 有标题的主题章节：用 section -->
    <h2>框架动态</h2>
    <p>...</p>
  </section>

  <section>
    <h2>工具链</h2>
    <p>...</p>
    <article> <!-- 每条评论独立可分发，嵌套 article 合法 -->
      <h3>读者评论：...</h3>
      <p>...</p>
    </article>
  </section>
</article>

<!-- 纯布局包裹：用 div，不用硬凑 section -->
<div class="grid">
  <div class="col">...</div>
</div>
```
