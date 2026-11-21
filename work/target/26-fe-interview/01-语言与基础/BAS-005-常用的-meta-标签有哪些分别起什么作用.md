---
title: [BAS-005] 常用的 meta 标签有哪些？分别起什么作用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-005：常用的 meta 标签有哪些？分别起什么作用？
**答**：
- `<meta charset="utf-8">`：声明字符编码，必须放在 head 最前面，防止乱码。
- `<meta name="viewport">`：控制移动端布局视口，`viewport-fit=cover` 兼容刘海屏。
- `<meta name="description">`：SEO 摘要，搜索结果里展示。
- `<meta http-equiv="Content-Security-Policy">`：无后端权限时用 meta 配置 CSP。

```html
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
<meta name="description" content="页面摘要，搜索引擎会展示这段文案" />
<meta name="format-detection" content="telephone=no" />
<!-- iOS 上禁止把长数字自动识别成电话拨号链接 -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'" />
```
