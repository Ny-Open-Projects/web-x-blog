---
title: [H5-110] lang 与 dir 如何支撑多语言与 RTL 布局？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-110：lang 与 dir 如何支撑多语言与 RTL 布局？
**答**：
- `lang` 影响三件事：读屏**发音引擎选择**、断行/连字符规则（`hyphens: auto` 依赖 lang）、字体与标点渲染选择；缺失 lang 的中文页 VoiceOver 常用英文音素硬读。
- `dir="rtl"` 是布局方向开关：块级流向、flex/grid 主轴起点、text-align 默认值全部镜像；**逻辑属性**（margin-inline-start、padding-block、inset-inline、text-align: start）自动适配，物理属性（left/right）不会。
- 局部覆盖：段落内混排外语 `<span lang="en">`、数字与代码块强制 `dir="ltr"`，避免标点与阅读顺序错乱。
- `:dir()` 伪类与 `dir` 属性选择器 `[dir=rtl]` 用于少量无法用逻辑属性表达的特例样式。
- 测试要点：翻转后箭头/进度条/关闭按钮方向、emoji 与变量插值的拼接顺序（用 CSS logical 而非字符串翻转）。

```html
<html lang="zh-CN" dir="ltr">
<head>
  <style>
    /* 全部使用逻辑属性：RTL 下自动镜像 */
    .card {
      padding-inline: 16px;
      margin-block: 8px;
      border-inline-start: 4px solid #1677ff;
      text-align: start;
    }
    .breadcrumb li::after {
      content: '/';                       /* 分隔符位置随方向自动变化 */
      margin-inline: 8px;
    }
    /* 极少数需要方向特判的样式 */
    .back-icon { transform: scaleX(1); }
    [dir="rtl"] .back-icon { transform: scaleX(-1); }  /* 返回箭头镜像 */
  </style>
</head>
<body dir="rtl" lang="ar">
  <!-- RTL 示例：阿拉伯语页面 -->
  <article lang="ar" dir="rtl">
    <h1>مرحبا</h1>
    <!-- 混排：内嵌英文术语局部还原 LTR -->
    <p>استخدم <span lang="en" dir="ltr">position: sticky</span> في الشبكة.</p>
    <!-- 代码块/公式：强制 LTR，避免标点错乱 -->
    <pre dir="ltr" lang="en">const x = a < b ? 1 : 0;</pre>
  </article>
</body>
</html>

<script>
  // 动态切换语言方向（i18n 框架的底层动作）
  function setLocale(locale) {
    const rtl = ['ar', 'he', 'fa', 'ur'].some(l => locale.startsWith(l));
    document.documentElement.lang = locale;
    document.documentElement.dir = rtl ? 'rtl' : 'ltr';
  }
  setLocale('ar');   // 整站布局自动镜像
</script>
```
