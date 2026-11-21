---
title: [PER-734] 手写一个 LQIP 渐进加载流水线：低质量占位图先行 + 主图到位淡入替换（blur-up）
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-734：手写一个 LQIP 渐进加载流水线：低质量占位图先行 + 主图到位淡入替换（blur-up）

**答**：
- 流水线：构建期生成每图的微缩 Base64（如 20px 宽 WebP，几百字节内联 HTML）；运行时先渲染 LQIP（blur 放大），主图 onload 后淡入替换并移除 blur。
- 要点：LQIP 内联在 HTML/首屏接口里（零额外请求）；blur 用 CSS filter（合成器），主图加载完 filter 过渡到 0；`img.decode()` 确保主图解码完成再淡入（避免淡入时才解码卡顿）。
- 边界：`content-visibility`/懒加载配合（离屏不加载主图）；动图/视频封面不做 blur（性能差）；低端机 blur 半径减小（光栅开销）。
- 评分点：decode 后再淡入与内联 LQIP。

```javascript

class LQIPImage {
  constructor(img, { blur = 12 } = {}) {
    this.img = img; this.blur = window.__deviceTier === 'low' ? 6 : blur;  // 低端减 blur
  }
  mount() {
    const lqip = this.img.dataset.lqip;                         // 构建期内联的微缩 Base64
    if (lqip) {
      this.img.src = lqip;
      this.img.style.filter = `blur(${this.blur}px)`;
      this.img.style.transform = 'scale(1.05)';                 // 放大遮住 blur 边缘
    }
    const full = this.img.dataset.src;
    if (full) this.loadFull(full);
  }
  async loadFull(src) {
    const io = new IntersectionObserver(async ([e]) => {
      if (!e.isIntersecting) return;
      io.disconnect();
      const url = this.img.dataset.src;
      const tmp = new Image();
      tmp.src = src;
      await tmp.decode().catch(() => {});                       // 解码完成再切换，防淡入卡顿
      this.img.src = src;
      this.img.style.filter = 'blur(0px)';                      // 过渡去 blur
      this.img.style.transform = 'scale(1)';
      this.img.style.transition = 'filter .4s, transform .4s';
    }, { rootMargin: '100%' });
    io.observe(this.img);
  }
}
// 构建期：sharp('./a.jpg').resize(20).webp({quality:30}).toBuffer() -> base64 -> data-lqip
```
