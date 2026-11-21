---
title: [H5-299] 笔试：手写 Canvas 像素级取色器
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Canvas]
type: 笔试题
---

## H5-299：笔试：手写 Canvas 像素级取色器

**题目**：实现取色器：鼠标移动实时预览像素色（悬停浮框），点击锁定颜色并输出 hex。要求处理 DPR 坐标与 willReadFrequently 优化，getImageData 只取 1px。

**答**：
```javascript
function createPicker(canvas) {
  const ctx = canvas.getContext('2d', { willReadFrequently: true }); // CPU 后备
  const dpr = devicePixelRatio;

  function colorAt(e) {
    const r = canvas.getBoundingClientRect();
    const x = Math.floor((e.clientX - r.left) * dpr); // 逻辑→物理像素
    const y = Math.floor((e.clientY - r.top) * dpr);
    const [rr, g, b, a] = ctx.getImageData(x, y, 1, 1).data;
    return a === 0 ? null : '#' + [rr, g, b].map(v => v.toString(16).padStart(2, '0')).join('');
  }

  const preview = document.createElement('div');
  preview.style.cssText = 'position:fixed;pointer-events:none;padding:4px 8px;background:#fff;border-radius:4px;font:12px monospace;z-index:99';
  document.body.appendChild(preview);

  canvas.addEventListener('pointermove', (e) => {
    const hex = colorAt(e);
    if (hex) {
      preview.textContent = hex;
      preview.style.background = hex;
      preview.style.left = e.clientX + 12 + 'px';
      preview.style.top = e.clientY + 12 + 'px';
    }
  });
  canvas.addEventListener('click', (e) => {
    const hex = colorAt(e);
    if (hex) onPick?.(hex);
  });
  let onPick;
  return { onPick: (fn) => (onPick = fn) };
}
```

**评分点**：
- willReadFrequently 开启（取色器是典型读密集场景）
- DPR 坐标换算：屏幕坐标 × dpr 得物理像素——漏掉必取错色
- getImageData(1,1) 而非整图读取
- hex 转换的 padStart 补零细节
