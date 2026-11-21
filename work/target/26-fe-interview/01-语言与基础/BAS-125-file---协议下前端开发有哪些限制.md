---
title: [BAS-125] file:// 协议下前端开发有哪些限制？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-125：file:// 协议下前端开发有哪些限制？
**答**：
- 每个 file 页面被视为不透明源：fetch/XHR 一律视为跨域被拦，无法请求本地其他文件。
- ES 模块受 CORS 限制，`type="module"` 在 file:// 下直接报错；Cookie、部分存储行为异常。
- 所以本地调试必须走 HTTP 服务（vite dev server、npx serve 等），不要直接双击 html 文件。

```bash
npx serve .                        # 快速起本地静态服务
# 浏览器访问 http://localhost:8000
# 而不是 file:///Users/xx/project/index.html
```

## 十五、深入 JS 语义
