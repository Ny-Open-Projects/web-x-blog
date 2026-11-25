---
title: [H5-051] article、section、aside 在真实页面里如何判定？给一个可执行的判定流程。
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-051：article、section、aside 在真实页面里如何判定？给一个可执行的判定流程。
**答**：
- 先问"这段内容脱离页面还能独立成篇吗"，能就是 `article`（博客正文、评论、商品卡、一条消息）。
- 再问"它是不是围绕同一主题的分组且有自己的标题"，是就用 `section`；没有标题的纯样式分组退回 `div`。
- 与主内容"相关但可剥离"（侧栏推荐、广告、术语表）用 `aside`；注意 aside 不等于视觉侧栏，正文里的补充说明也可以是 aside。
- `section` 可以嵌在 `article` 里当章节，`article` 也可以嵌在 `article` 里表示"被引用的独立内容"（如评论）。
- 判定顺序：独立分发？→ article；主题分组有标题？→ section；可剥离的辅助内容？→ aside；都不是 → div。

```html
<!-- 一篇文章页：三种标签各就各位 -->
<main>
  <article>                      <!-- 正文可独立分发（RSS 抓走也完整） -->
    <h1>CSS 容器查询实战</h1>
    <section aria-labelledby="s1">
      <h2 id="s1">背景</h2>
      <p>容器查询改变了组件写响应式的思路……</p>
    </section>
    <section aria-labelledby="s2">
      <h2 id="s2">示例</h2>
      <p>下面的代码演示……</p>
    </section>
    <aside>                      <!-- 与正文相关但可剥离：术语解释 -->
      <p>注：容器查询即 @container 规则，区别于媒体查询。</p>
    </aside>
  </article>

  <section aria-labelledby="comments">
    <h2 id="comments">评论</h2>
    <article class="comment">    <!-- 每条评论本身也是独立内容 -->
      <p>写得很清楚，受益了。</p>
    </article>
  </section>

  <aside class="related">        <!-- 页面级侧栏：相关推荐，可整体剥离 -->
    <h2>相关文章</h2>
    <ul><li><a href="/a">逻辑属性</a></li></ul>
  </aside>
</main>
```
