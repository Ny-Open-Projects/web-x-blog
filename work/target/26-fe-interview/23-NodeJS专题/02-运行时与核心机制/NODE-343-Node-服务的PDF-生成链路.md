---
title: [NODE-343] Node 服务的 PDF 生成链路如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-343：Node 服务的 PDF 生成链路
**答**:
- 路线对比：程序化绘制（pdfkit：轻量、版式代码化）vs HTML 渲染（Puppeteer 打印 HTML → PDF：复杂版式/图表保真，但重）；主流用 Puppeteer + 共享 Web 模板（ARC-496 前端打印同源）。
- Puppeteer 生产化：浏览器实例池（复用 context，禁每请求起浏览器）、内存控制（页面上限、渲染完 destroy）、无头崩溃自动重启、镜像固定版本（依赖字体与渲染一致性）。
- 模板工程：HTML 模板与数据注入、内联 CSS 与字体（离线渲染禁外网资源）、分页规则（ARC-496 CSS）、图表用静态快照（ECharts SSR 渲染成图片嵌入）。
- 中文与字体：容器内置 Noto CJK；字体嵌入与文件体积权衡（子集化）。
- 安全与审计：敏感 PDF 水印（用户 ID）、下载签名 URL、生成任务异步化（大批量走队列）。
```javascript
// Puppeteer 池化渲染
const pool = new BrowserPool({ size: 4, launchOpts: ['--no-sandbox', '--disable-dev-shm-usage'] });
async function renderPdf(html) {
  const page = await pool.acquire();
  try {
    await page.setContent(html, { waitUntil: 'networkidle0' });
    return await page.pdf({ format: 'A4', printBackground: true,
      margin: { top: '15mm', bottom: '15mm' } });
  } finally { await pool.release(page); }
}
```
