---
title: [CSS-378] 媒体查询与视口计算：viewport meta 与动态视口单位
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 适配]
type: 面试题
---

## CSS-378：媒体查询与视口计算：viewport meta 与动态视口单位

**答**：
- 视口三层：layout viewport（meta width=device-width 定）、visual viewport（用户实际可见，缩放/键盘变化）、initial-scale——1px CSS ≠ 1px 物理的根由是 dpr 映射
- 动态视口单位体系：vh（布局视口，含被地址栏遮的区）→ svh（最小视口，地址栏展开时）→ lvh（最大视口）→ dvh（动态，跟随变化）——全屏 hero 用 dvh（注意 iOS 键盘期 dvh 抖动，用 svh 稳定布局）
- 媒体查询的失效成本：视口尺寸变化（旋转/缩放窗口）触发全部媒体查询重匹配 + 可能全局布局——断点别太多（3~4 档），容器查询分摊失效范围
- prefers-* 媒体族：color-scheme/reduced-motion/contrast/data 联网偏好——颜色主题用 `color-scheme: light dark` + light-dark() 函数简化声明
- 断点设计原则：内容优先断点（内容放不下才断）而非设备断点；断点变量与 token 一起管理

```css
:root { color-scheme: light dark; }
body { background: light-dark(#fff, #121212); }   /* 简化双主题 */
.hero { height: 100svh; }        /* 稳定全屏, 键盘不抖 */
.hero--expand { height: 100dvh; }
```

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```
