---
title: [OPT-176] 文档预览（PDF/Office）页面的性能方案怎么设计？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-176：文档预览（PDF/Office）页面的性能方案怎么设计？

**答**：
- PDF：pdf.js 分页渲染——只渲染视口附近页（虚拟滚动 + 按页 canvas 绘制），worker 解析（`pdfjs-dist/build/pdf.worker`）避免主线程卡顿；大 PDF 缩略图与正文双虚拟列表。
- Office：不在前端硬解 docx/xlsx 全文档（内存与 CPU 都爆炸）。方案优先级：服务端转 PDF/HTML 预览 > 只在线预览转好的静态文件 > 前端解析小文件（<5MB）。
- 体验细节：先出"第 1 页"再懒渲染其余；页与页之间的图片用缩略占位；下载按钮常驻，避免预览卡死时用户无路可走。
- 缓存：转换结果与分页数据按文件 hash 缓存（CDN + IndexedDB），二次打开秒开。

```javascript
// 一一对应：pdf.js 分页懒渲染（worker 解析 + 视口按页绘制）
import * as pdfjsLib from 'pdfjs-dist';
import PdfWorker from 'pdfjs-dist/build/pdf.worker.min.mjs?url';
pdfjsLib.GlobalWorkerOptions.workerSrc = PdfWorker;  // 解析全部进 worker

export async function setupPdfViewer(container, url) {
  const pdf = await pdfjsLib.getDocument({ url, rangeChunkSize: 65536 }).promise;
  const total = pdf.numPages;
  container.style.height = `${total * 1200}px`;   // 按平均页高撑起总高，滚动条稳定

  const rendered = new Map();   // page -> 渲染任务，防重复渲染
  const io = new IntersectionObserver(async entries => {
    for (const entry of entries) {
      const pageNum = +entry.target.dataset.page;
      if (!entry.isIntersecting || rendered.has(pageNum)) continue;
      const page = await pdf.getPage(pageNum);
      const viewport = page.getViewport({ scale: 1.5 });
      const canvas = document.createElement('canvas');
      canvas.width = viewport.width; canvas.height = viewport.height;
      canvas.style.aspectRatio = `${viewport.width}/${viewport.height}`;
      entry.target.replaceChildren(canvas);
      const task = page.render({ canvasContext: canvas.getContext('2d'), viewport });
      rendered.set(pageNum, task);
      task.promise.catch(() => rendered.delete(pageNum));   // 失败允许重试
      // 远离视口的页主动释放 canvas，长文档滚动内存恒定
      rendered.forEach((_, p) => {
        if (Math.abs(p - pageNum) > 6) {
          document.querySelector(`[data-page="${p}"]`)?.replaceChildren();
          rendered.delete(p);
        }
      });
    }
  }, { rootMargin: '1000px 0px' });

  for (let i = 1; i <= total; i++) {
    const placeholder = document.createElement('div');
    placeholder.dataset.page = i;
    placeholder.style.minHeight = '1200px';       // 页高占位防 CLS
    placeholder.textContent = `第 ${i} 页加载中…`;
    container.appendChild(placeholder);
    io.observe(placeholder);
  }
}
```

## 二十七、新特性与新平台
