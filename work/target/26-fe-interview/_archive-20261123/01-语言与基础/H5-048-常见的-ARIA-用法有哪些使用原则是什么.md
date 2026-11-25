---
title: [H5-048] 常见的 ARIA 用法有哪些？使用原则是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-048：常见的 ARIA 用法有哪些？使用原则是什么？
**答**：
- 第一原则：优先用原生语义（button/nav/label），能用原生就不用 ARIA；"No ARIA is better than bad ARIA"。
- 角色（role）补齐语义：自定义下拉用 `role="listbox"` + `aria-expanded`；状态用 `aria-selected`、`aria-disabled`。
- 动态反馈：`aria-live="polite"` 播报 toast/加载结果；`aria-label` 给图标按钮命名。
- `alt` 是图片 a11y 的底线：信息图写描述，纯装饰写 `alt=""`（读屏跳过）。

```html
<!-- 图标按钮必须有可访问名称 -->
<button aria-label="关闭对话框">
  <svg aria-hidden="true" width="16" height="16"><use href="#icon-x" /></svg>
</button>

<!-- 自定义下拉：角色 + 状态 -->
<div class="select" role="combobox" aria-expanded="false" aria-haspopup="listbox">
  <span id="sel-label">排序方式</span>
  <ul role="listbox" aria-labelledby="sel-label" hidden>
    <li role="option" aria-selected="true">最新</li>
    <li role="option" aria-selected="false">最热</li>
  </ul>
</div>

<!-- 动态区域：内容变化时读屏自动播报 -->
<div aria-live="polite" class="toast">已保存</div>

<!-- 装饰性图片 alt 留空，读屏跳过；信息图写清楚 -->
<img src="divider.png" alt="" />
<img src="chart.png" alt="2026 年各季度营收柱状图，Q4 最高达 2.4 亿" />
```
