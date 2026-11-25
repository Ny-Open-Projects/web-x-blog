---
title: [VIZ-021] Canvas 如何做 DPR 与浏览器缩放适配？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-021：Canvas 如何做 DPR 与浏览器缩放适配？
**答**：canvas 的 CSS 尺寸与位图尺寸是两回事：位图 = CSS 尺寸 × devicePixelRatio，再通过 `ctx.scale(dpr, dpr)` 让绘制代码继续用 CSS 像素坐标系。只设 CSS 不设位图会得到模糊拉伸；设了位图不 scale 会得到小一半的图形。注意两点：超高 DPR 设备限到 2 节省内存；浏览器页面缩放会改变 effective DPR，需监听 `matchMedia('(resolution: 2dppx)')` 之类变化重建画布。

```javascript
function setupHiDPI(canvas, cssW, cssH) {
  const dpr = Math.min(window.devicePixelRatio || 1, 2); // 超高 DPR 限 2 省内存
  canvas.width = Math.round(cssW * dpr);   // 位图物理像素
  canvas.height = Math.round(cssH * dpr);
  canvas.style.width = cssW + 'px';        // CSS 尺寸保持布局大小
  canvas.style.height = cssH + 'px';
  const ctx = canvas.getContext('2d');
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);  // 后续逻辑坐标一律用 CSS 像素
  return ctx;
}
// 浏览器缩放会改变有效 DPR：监听变化后重建画布，否则变模糊
const mq = matchMedia(`(resolution: ${window.devicePixelRatio}dppx)`);
mq.addEventListener?.('change', () => location.reload()); // 简单场景；复杂场景重渲染不刷新
```

---

## 四、WebGL 基础（VIZ-022 ~ VIZ-029）
