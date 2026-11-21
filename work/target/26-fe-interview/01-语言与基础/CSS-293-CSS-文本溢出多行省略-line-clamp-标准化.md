---
title: [CSS-293] CSS 文本溢出多行省略：line-clamp 标准化
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 排版]
type: 面试题
---

## CSS-293：多行省略：line-clamp 标准化

**答**：
- 单行省略：`white-space: nowrap; overflow: hidden; text-overflow: ellipsis;`
- 多行省略旧写法：-webkit-box + -webkit-line-clamp（非标准但 ubiquitous）；新标准：`line-clamp: 2`（Chrome 130+/Firefox 122+）
- 新标准附带能力：-webkit-line-clamp-box 与 clamp 后省略号样式定制（标准草案中），比 webkit 版更可控
- 兼容策略：双写——标准 line-clamp 优先，webkit 老写法兜底（级联覆盖）
- 细节：省略位置在行尾；需要「省略号自定义」仍要 JS 截断方案

```css
.clamp-2 {
  line-clamp: 2;                    /* 新标准 */
  display: -webkit-box;
  -webkit-line-clamp: 2;            /* 老写法兜底 */
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.single { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
```
