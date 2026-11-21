---
title: [H5-077] Canvas 的 DPR 高清适配如何做成工程化工具？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-077：Canvas 的 DPR 高清适配如何做成工程化工具？
**答**：
- 模糊根因：canvas 物理像素尺寸 = CSS 尺寸时，在 2x/3x 屏上一逻辑像素被拉伸到多物理像素。
- 工程化三步：`width = cssW * dpr` → `ctx.scale(dpr, dpr)` 让绘制代码继续用逻辑坐标 → CSS 限定 `width: cssWpx`。
- dpr 要**钳制上限**（常见 2~3）：0.5x 屏没关系，但 4K 3x 屏按 3 渲染内存翻倍，收益边际递减。
- 尺寸变化用 `ResizeObserver` 重建画布，注意 `ctx.setTransform` 重置后再 scale；状态（填充色等）也要重设。
- DPR 变化场景：浏览器缩放、拖去外接屏——`matchMedia(`(resolution: ${dpr}dppx)`)` 变更监听可感知（注意每次要重挂监听）。

```html
<canvas id="hd"></canvas>
<script>
  function setupHiDPI(canvas, cssW, cssH) {
    const dpr = Math.min(window.devicePixelRatio || 1, 2); // 钳制上限
    canvas.width = Math.round(cssW * dpr);
    canvas.height = Math.round(cssH * dpr);
    canvas.style.width = cssW + 'px';
    canvas.style.height = cssH + 'px';
    const ctx = canvas.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);   // 逻辑坐标系
    return { ctx, dpr };
  }

  const cv = document.getElementById('hd');
  const draw = () => {
    const cssW = cv.parentElement.clientWidth;
    const cssH = 300;
    const { ctx } = setupHiDPI(cv, cssW, cssH);
    // 之后所有绘制按 CSS 像素写，无需关心 DPR
    ctx.clearRect(0, 0, cssW, cssH);
    ctx.beginPath();
    ctx.arc(cssW / 2, 150, 80, 0, Math.PI * 2);
    ctx.fillStyle = 'steelblue';
    ctx.fill();
    ctx.font = '24px sans-serif';              // 字体同样受益于 scale
    ctx.fillStyle = '#fff';
    ctx.textAlign = 'center';
    ctx.fillText('HiDPI 清晰', cssW / 2, 158);
  };

  draw();

  // 尺寸自适应：容器变化时重设（会重置画布内容）
  new ResizeObserver(() => draw()).observe(cv.parentElement);
</script>
```
