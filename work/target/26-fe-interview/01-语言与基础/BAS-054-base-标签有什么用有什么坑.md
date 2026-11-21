---
title: [BAS-054] base 标签有什么用？有什么坑？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-054：base 标签有什么用？有什么坑？
**答**：
- `<base href>` 为页面所有相对 URL 指定基准路径，`<base target>` 指定链接默认打开方式。
- 坑：锚点 `#xxx` 也会跳到 base 地址而不是当前页锚点；base 必须放在 head 中其他 URL 引用之前。
- SPA history 路由配置好 base 可避免资源 404，但多数框架已用绝对路径处理，base 用得越来越少。

```html
<head>
  <base href="/app/" target="_blank" />
  <!-- 下面的 a href="list.html" 实际请求 /app/list.html，且默认新窗口打开 -->
</head>
<body>
  <a href="list.html">列表页</a>
  <a href="#top">会跳到 /app/#top 而不是当前页锚点</a>
</body>
```
