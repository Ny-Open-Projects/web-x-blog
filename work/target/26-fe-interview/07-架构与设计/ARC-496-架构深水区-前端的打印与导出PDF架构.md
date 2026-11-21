---
title: [ARC-496] 前端的打印与导出 PDF 架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-496：打印与导出 PDF 架构
**答**:
- 三条路线：浏览器打印（@media print + window.print，成本最低）、前端生成 PDF（pdfmake/jsPDF，模板固定场景）、服务端渲染（Puppeteer/wkhtmltopdf，保真度高、批量大）。决策按保真度与批量需求。
- 浏览器打印架构：打印样式层（独立 print stylesheet：隐藏交互件、分页控制 page-break、页眉页脚 @page margin）、打印预览页（独立路由渲染专用 DOM 而非复用页面 DOM）。
- 服务端 PDF 架构：模板化（HTML 模板 + 数据注入）、样式一致性（与 Web 共享 token）、字体与中文（服务端安装字体）、水印（用户 ID 隐写防泄露追责）、批量任务化（ARC-486）。
- 分页一致性：屏幕分页 ≠ 纸张分页——打印模板独立设计而非"屏幕页面直接打"，避免截断半行；表格分页重复表头（thead）。
- 保真验收：视觉回归（打印渲染快照对比），线上 PDF 抽样校验（乱码/截断检测）。
```css
@media print {
  .no-print, nav, aside { display: none; }
  main { margin: 0; }
  table { page-break-inside: auto; }
  tr { page-break-inside: avoid; }            /* 行不截断 */
  thead { display: table-header-group; }      /* 分页重复表头 */
}
@page { size: A4; margin: 15mm; @bottom-center { content: counter(page); } }
```
