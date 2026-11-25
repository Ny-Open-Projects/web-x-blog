---
title: [CSS-360] 打印与无障碍输出：CSS 的另两类媒体
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-360：打印与无障碍输出：CSS 的另两类媒体

**答**：
- 打印媒体：@media print 专属样式（隐藏导航/展开折叠内容/分页控制 page-break/白底黑字）——打印前浏览器重新布局为纸张尺寸，与屏幕布局互不影响
- 打印技术点：page-break-inside: avoid 防卡片截断、@page 边距与页眉页脚、打印时 fixed 变每页重复（页眉页脚实现）、颜色打印 forced-colors 约束
- 强制颜色模式（forced-colors: active）：Windows 高对比度模式——系统强改颜色，自定义样式要用系统色 token（CanvasText/ButtonText），确保文本可读
- reduced-motion/reduced-transparency：动画敏感用户降级为瞬时切换；prefers-contrast 提高对比——这些 media 特性是「用户偏好尊重」的义务项
- 无障碍输出清单：非文本信息有 aria 替代、焦点样式 :focus-visible 不被移除、内容顺序（DOM 顺序）与视觉顺序一致

```css
@media print {
  nav, .sidebar, .ads { display: none; }
  .article { color: #000; }
  .card { break-inside: avoid; }
  a::after { content: ' (' attr(href) ')'; }  /* 打印时展示链接 */
}
@media (forced-colors: active) {
  .btn { border: 1px solid ButtonText; background: ButtonFace; }
}
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; transition: none !important; }
}
```
