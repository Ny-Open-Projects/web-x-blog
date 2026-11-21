---
title: [PER-612] 上传的 SVG/PDF 文件直接预览有什么风险？文件预览场景的安全基线怎么定？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-612：上传的 SVG/PDF 文件直接预览有什么风险？文件预览场景的安全基线怎么定？

**答**：
- SVG：同域打开即活动文档，内嵌脚本可执行 -> 存储型 XSS；PDF：浏览器内置 PDF 阅读器支持 JS（AcroForm/JS 动作），旧版本可触发、新版受限但仍有解析漏洞（CVE 常客）；HTML/XML 上传同理。
- 安全基线四条：**文件域名隔离**（专用文件域或对象存储直链，与业务域不共享 cookie 与 DOM 来源）、**强制下载头**（`Content-Disposition: attachment` + `X-Content-Type-Options: nosniff`，浏览器不渲染只下载）、**类型白名单 + 内容嗅探复核**（魔数与扩展名一致）、**预览走转换**（SVG/PDF 转 PNG/截图后展示，原图仅提供下载）。
- 前端职责：预览组件用 `<img>`/`<object>` 走转换后的安全格式，不提供在新标签打开原文件入口；下载入口确认响应头由服务端正确设置。
- 兜底：CSP 对文件域不可控（不在自己域），所以隔离是第一道防线，SRI/CSP 都救不了同域上传。

```javascript

const filePreviewBaseline = {
  isolate: { domain: 'files-cdn.example.com（独立域，无业务 cookie）' },
  headers: {
    'Content-Disposition': 'attachment; filename="safe.webp"',   // 强制下载不渲染
    'X-Content-Type-Options': 'nosniff',
    'Content-Security-Policy': "sandbox",                        // 文件域再加一层
  },
  allowTypes: [['webp', [0x52, 0x49, 0x46, 0x46]], ['png', [0x89, 0x50, 0x4e, 0x47]]],
  preview: 'SVG/PDF -> 服务端转 PNG -> <img> 展示；原始文件只提供下载',
  forbid: '禁止新标签打开原文件入口；禁止同域直接访问文件 URL',
};
console.log(filePreviewBaseline.preview);
```
