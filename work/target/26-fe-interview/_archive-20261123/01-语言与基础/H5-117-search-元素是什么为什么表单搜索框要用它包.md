---
title: [H5-117] search 元素是什么？为什么表单搜索框要用它包起来？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-117：search 元素是什么？为什么表单搜索框要用它包起来？
**答**：
- `<search>` 是 HTML 5.4 后引入的分区元素，语义为"**搜索或过滤界面**"，映射 landmark role=search。
- 价值：读屏的地标菜单出现"搜索"入口，用户可直接跳转；之前普遍的 `<div role="search">` 写法被标准化替代。
- 用法：包住搜索表单/过滤控件区（type=search 的 input 只是控件，search 元素才是"区域"）。
- 每页可有多个 search 地标但需 aria-label 区分（全局搜索、表格过滤）。
- 注意别滥用：一次性的按钮触发动作不构成"搜索区域"，普通表单无需包裹。

```html
<!-- 站点全局搜索：landmark 化 -->
<search aria-label="全站搜索">
  <form action="/search">
    <label for="q">搜索</label>
    <input id="q" type="search" name="q"
           inputmode="search" enterkeyhint="search"
           placeholder="搜索文章、标签…">
    <button>搜索</button>
  </form>
</search>

<main>
  <!-- 表格过滤区：第二个 search 地标，命名区分 -->
  <search aria-label="订单过滤">
    <input type="search" name="order-no" placeholder="按订单号过滤">
    <select name="status"><option>全部状态</option></select>
  </search>

  <table id="orders"><!-- 过滤结果 --></table>
</main>

<script>
  // 过滤防抖：search 元素内部的事件委托
  const filterBox = document.querySelector('search[aria-label=订单过滤]');
  let timer;
  filterBox.addEventListener('input', (e) => {
    clearTimeout(timer);
    timer = setTimeout(() => reloadOrders(new FormData(e.target.closest('form'))), 300);
  });
</script>
```
