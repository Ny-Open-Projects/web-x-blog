---
title: [H5-052] heading 层级与 outline 算法是怎么回事？为什么不能滥用 h1？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-052：heading 层级与 outline 算法是怎么回事？为什么不能滥用 h1？
**答**：
- HTML4 时代的"文档大纲算法"（section 嵌套自动降级标题）在主流实现中已被搁置，实践中必须**手写正确的 h1~h6 层级**，不能依赖浏览器推算。
- 核心规则：每个 section/article/aside 建议有自己的标题；标题层级不跳级（h2 后直接 h4 是错误）；一个页面通常一个 h1。
- 读屏用户靠标题列表"满文跳读"，层级错了导航就废；SEO 同样按标题权重理解内容。
- section 无标题时 Chrome 会把它当"无标题分组"，对大纲没有贡献，反而产生噪音。
- 落地手段：CI 里跑 axe/lighthouse 检查 heading-order，或用浏览器 DevTools 的 Accessibility 面板查看标题树。

```html
<!-- 正确层级：逻辑树与视觉大小解耦，字号交给 CSS -->
<article>
  <h1>2026 前端趋势报告</h1>          <!-- 全文唯一 h1 -->
  <section>
    <h2>一、框架</h2>                  <!-- 不跳级 -->
    <section>
      <h3>1.1 编译时框架</h3>
      <h4>现状</h4>
    </section>
  </section>
  <section>
    <h2>二、构建工具</h2>
  </section>
</article>

<style>
  /* 错觉纠正：视觉大小不跟随层级，避免"为了显眼乱用 h1" */
  h1 { font-size: 28px; }
  h2 { font-size: 24px; }
  h3 { font-size: 20px; }
</style>
```
