---
title: [H5-054] address 元素是干什么的？和 footer 里的联系信息怎么配合？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-054：address 元素是干什么的？和 footer 里的联系信息怎么配合？
**答**：
- `<address>` 专指"**当前 article 或 body 的作者/维护者**联系信息"，不是任意地址（快递收货地址、景点地址都不该用）。
- 作用域跟随最近的 `article`：文章内的 address 表示文章作者联系方式；body 直属的 address 表示全站联系信息。
- 典型位置是 `footer` 内部；内容通常是邮箱、社交链接、电话，排版无默认特殊样式（多为斜体，可重置）。
- 里面放 `<a href="mailto:">` / `tel:` 链接，对读屏和无障碍最友好。
- 反例：门店地址列表用 address 是误用，应使用带 itemporp（schema.org 微数据）或普通标记。

```html
<article>
  <h1>容器查询实战</h1>
  <p>正文……</p>
  <footer>
    <!-- 文章作者联系方式：作用于本 article -->
    <address>
      作者：<a href="mailto:lin@example.com">lin@example.com</a> ·
      <a href="https://twitter.com/lin">Twitter</a>
    </address>
  </footer>
</article>

<footer>
  <!-- 全站维护者信息：作用于 body -->
  <address>
    有问题请联系 <a href="mailto:support@example.com">支持团队</a>，
    电话 <a href="tel:+861012345678">010-12345678</a>。
  </address>
  <p><small>© 2026 Example Inc.</small></p>
</footer>
```
