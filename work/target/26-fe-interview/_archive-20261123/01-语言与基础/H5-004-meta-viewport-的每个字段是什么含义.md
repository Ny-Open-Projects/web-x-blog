---
title: [H5-004] meta viewport 的每个字段是什么含义？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-004：meta viewport 的每个字段是什么含义？
**答**：
- 移动浏览器默认把页面渲染在约 980px 的虚拟视口上再缩小，导致字小；viewport meta 用来接管这个视口。
- `width=device-width` 视口宽度等于设备 CSS 像素宽度；`initial-scale=1` 初始缩放 1 倍。
- `maximum-scale` / `user-scalable=no` 禁缩放：对无障碍不友好（低视力用户无法放大），iOS 10 起强制忽略，不建议使用。
- `viewport-fit=cover` 配合 iPhone 刘海安全区使用；width 也可以写固定数字如 750（适配 rem 方案时）。

```html
<!-- 标准移动端配置 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<!-- 允许用户缩放是默认且推荐的，对可访问性友好 -->
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
```

```javascript
// 用 JS 读取当前视口信息，验证 viewport 配置生效
console.log('视口宽度:', window.innerWidth); // 配置后等于设备 CSS 宽度，如 390
console.log('屏幕宽度:', screen.width);
console.log('设备像素比:', window.devicePixelRatio); // iPhone 3x 屏为 3
// window.innerWidth = screen.width / devicePixelRatio 的关系可用于验证
```
