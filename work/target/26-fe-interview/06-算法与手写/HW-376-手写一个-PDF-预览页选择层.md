---
title: [HW-376] 手写一个 PDF 预览页选择层：文本层与渲染层坐标映射
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-376：手写一个 PDF 预览页选择层：文本层与渲染层坐标映射

**答**：
- 需求：实现 PdfSelect：渲染层（canvas 页面图）+ 文本层（透明 DOM 叠加，含每文本项位置）；文本选择（借用浏览器原生 selection，取选区跨的文本项）；选区 → 引用数据（页码 + 文本 + 归一化区间）；跳转高亮（给定引用定位滚动并高亮）。
- 边界：文本层坐标与 PDF 坐标系换算（PDF 原点左下 → DOM 左上，y 翻转）；跨页选择拆分；缩放时文本层同步缩放（同 transform）。
- 评分点：坐标系翻转；跨页拆分；缩放同步。

```javascript
class PdfSelect {
  constructor(pages) { this.pages = pages; }                 // pages: {num, canvasEl, textItems}
  buildTextLayer(page) {                                     // 文本层构建
    const layer = document.createElement('div');
    layer.className = 'pdf-text-layer';
    layer.style.cssText = 'position:absolute;inset:0;transform-origin:0 0;';
    for (const item of page.textItems) {
      const span = document.createElement('span');
      span.textContent = item.str;
      // PDF y 轴翻转：DOM y = pageH - pdfY - height
      Object.assign(span.style, {
        left: item.x + 'px', top: (page.height - item.y - item.height) + 'px',
        width: item.width + 'px', height: item.height + 'px',
        position: 'absolute', fontSize: item.height + 'px',
      });
      layer.appendChild(span);
    }
    page.canvasEl.parentElement.appendChild(layer);
    page.textLayer = layer;
    return layer;
  }
  getSelection() {                                           // 选区 → 引用数据
    const sel = getSelection();
    if (sel.isCollapsed) return null;
    const ranges = [];
    for (const page of this.pages) {                        // 跨页拆分
      const inPage = sel.rangeCount && page.textLayer?.contains(sel.anchorNode);
      if (!inPage) continue;
      ranges.push({ page: page.num, text: sel.toString(),
        norm: this.normalizeRange(sel, page) });            // 归一化区间
    }
    return ranges.length ? ranges : null;
  }
  normalizeRange(sel, page) { return { x: 0, y: 0, w: 1, h: 1 }; }   // 简化：实际按 rangeClientRects
  highlight(ref) {                                           // 跳转高亮
    const page = this.pages.find(p => p.num === ref.page);
    page.el.scrollIntoView({ block: 'center' });
    page.textLayer.querySelectorAll('.hl').forEach(e => e.classList.remove('hl'));
    // 按 norm 区间加高亮 overlay
    const overlay = document.createElement('div');
    overlay.className = 'hl';
    Object.assign(overlay.style, {
      left: ref.norm.x * 100 + '%', top: ref.norm.y * 100 + '%',
      width: ref.norm.w * 100 + '%', height: ref.norm.h * 100 + '%',
    });
    page.textLayer.appendChild(overlay);
  }
  syncScale(k) { for (const p of this.pages)
    if (p.textLayer) p.textLayer.style.transform = `scale(${k})`; }   // 缩放同步
}
```
