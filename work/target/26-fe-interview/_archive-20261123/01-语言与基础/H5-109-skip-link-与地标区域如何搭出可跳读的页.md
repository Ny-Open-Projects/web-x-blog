---
title: [H5-109] skip link 与地标区域如何搭出"可跳读"的页面骨架？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-109：skip link 与地标区域如何搭出"可跳读"的页面骨架？
**答**：
- skip link：页首"跳到主内容"的隐藏链接，获得焦点才显示，让键盘用户每次翻页**跳过几十个导航链接**；目标用 `href="#main"` 且 main 有 `tabindex="-1"`。
- 地标：`header/nav/main/aside/footer` 自动映射 landmark role；同类型地标多个时**必须加可区分名称**（`aria-label="主导航"`、"页脚导航"），否则读屏菜单里全是"navigation"。
- `main` 每页一个且不能嵌套在 header/nav/footer/article/aside 里；重复的页头页脚导航在模板层保持一致，读屏用户依赖记忆位置。
- 常见漏项：`main` 没有 skip link、导航没区分名、装饰区块滥用 aria-label 制造地标噪音（div 不是地标，别强加 role）。
- 走查法：用 VoiceOver 转子（VO+U）看地标列表，应能"header → 导航 → main → footer"一次读完主路径。

```html
<body>
  <!-- skip link：第一个可聚焦元素 -->
  <a class="skip-link" href="#main">跳到主内容</a>

  <header>
    <nav aria-label="主导航">
      <ul><li><a href="/">首页</a></li><li><a href="/products">产品</a></li></ul>
    </nav>
  </header>

  <!-- main：目标点，tabindex=-1 使其可被链接聚焦 -->
  <main id="main" tabindex="-1">
    <h1>产品列表</h1>
    <aside aria-label="筛选器">
      <!-- 筛选表单 -->
    </aside>
    <section aria-labelledby="list-title">
      <h2 id="list-title">全部商品</h2>
    </section>
  </main>

  <footer>
    <nav aria-label="页脚导航">         <!-- 与主导航区分名称 -->
      <ul><li><a href="/about">关于</a></li></ul>
    </nav>
  </footer>

  <style>
    .skip-link {
      position: absolute;
      left: -9999px;                    /* 隐藏但可聚焦 */
      background: #fff; color: #1677ff;
      padding: 8px 16px; z-index: 100;
    }
    .skip-link:focus {
      left: 8px; top: 8px;              /* 键盘 Tab 到达时出现 */
    }
    main:focus { outline: none; }       /* 跳转目标不画焦点框 */
  </style>
```
