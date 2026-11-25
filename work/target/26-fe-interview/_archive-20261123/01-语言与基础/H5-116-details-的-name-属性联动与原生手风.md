---
title: [H5-116] details 的 name 属性联动与原生手风琴实践。
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-116：details 的 name 属性联动与原生手风琴实践。
**答**：
- `<details name="group">`：同名 details 组成**互斥手风琴**，展开一个自动收起其他，零 JS 实现 FAQ/侧栏菜单。
- 展开状态：`open` 属性（可 SSR 预置）；`toggle` 事件监听展开收起做埋点或联动。
- 动画方案：`::details-content` 伪元素（新）+ `interpolate-size: allow-keywords` 让 height: auto 可过渡；旧方案用 grid-template-rows 0fr/1fr 技巧包裹内容。
- 语义与无障碍：自带 `role="button"` + aria-expanded 映射，键盘可用；summary 内容决定可读名称。
- 边界：name 联动只在同文档同树生效；需要"可搜索展开"场景在 hash/锚点里控制 open。

```html
<style>
  /* 平滑展开：新特性组合（Chrome 129+），不支持则瞬时展开 */
  details {
    interpolate-size: allow-keywords;
  }
  details::details-content {
    block-size: 0;
    overflow: hidden;
    transition: block-size .3s, content-visibility .3s allow-discrete;
  }
  details[open]::details-content {
    block-size: auto;
  }
  summary {
    cursor: pointer;
    list-style: none;                       /* 去默认三角，自绘箭头 */
    display: flex; justify-content: space-between;
  }
  summary::after { content: '+'; transition: rotate .3s; }
  details[open] summary::after { rotate: 45deg; }
</style>

<!-- name 相同：天然互斥手风琴 -->
<details name="faq">
  <summary>支持哪些支付方式？</summary>
  <p>支持微信、支付宝与银行卡。</p>
</details>
<details name="faq">
  <summary>发货周期多久？</summary>
  <p>现货 48 小时内发货。</p>
</details>
<details name="faq" open>
  <summary>默认展开的一项</summary>
  <p>预置 open 属性即可。</p>
</details>

<script>
  // toggle 事件：只播报一次的展开埋点
  document.querySelectorAll('details[name=faq]').forEach((d) => {
    d.addEventListener('toggle', () => {
      if (d.open) track('faq-open', d.querySelector('summary').textContent);
    });
  });
</script>
```
