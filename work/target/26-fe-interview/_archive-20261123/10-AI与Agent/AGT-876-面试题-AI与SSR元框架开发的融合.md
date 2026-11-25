---
title: [AGT-876] RSC/SSR 项目里用 AI 编码，哪些点 AI 特别容易翻车（服务端/客户端边界）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-876：RSC/SSR 项目里用 AI 编码，哪些点 AI 特别容易翻车（服务端/客户端边界）

**答**：
- AI 翻车高发点：把浏览器 API 用进 Server Component（window/localStorage）、把服务端数据获取逻辑写进客户端、'use client' 边界乱标（整棵树客户端化）、流式 Suspense 边界与数据获取位置错配。
- 防御工程化：边界 lint（server-only/client-only 包强制导入边界）、AI rules 写明 RSC 约定（默认 Server Component、显式 use client、数据获取在服务端）、类型系统拦截（server-only 类型在客户端编译报错）。
- 评审焦点：AI 改动 SSR 代码时人工只看「边界变更」（数据获取位置/组件边界移动），实现细节免审。

```javascript
// AI rules 片段（RSC 项目）
const RSC_RULES = `
- 默认写 Server Component；需要交互才加 'use client'
- 数据获取在 Server Component / server actions，客户端只拿 props
- 禁止在 Server Component 引用 window/document/localStorage
- Suspense 边界与数据获取同级放置`;
// lint: server-only 包强制边界
import 'server-only';   // 客户端引入即编译报错
```

