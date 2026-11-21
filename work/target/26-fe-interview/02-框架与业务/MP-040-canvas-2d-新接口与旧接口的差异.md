---
title: [MP-040] canvas 2d 新接口与旧接口的差异？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-040：canvas 2d 新接口与旧接口的差异？
**答**：
- 旧接口 `wx.createCanvasContext(canvasId)`：指令队列模式（ctx 操作被收集后 flush 到 native），API 与 Web Canvas 不一致，性能差、无法直接 getImageData、同层支持弱，官方已停止维护。
- 新接口：`<canvas type="2d">` → `SelectorQuery.select().fields({ node: true })` 拿 **Canvas 节点** → `node.getContext('2d')`，与 Web Canvas API 一致，支持离屏 `wx.createOffscreenCanvas`、逐帧绘制与导出临时文件。
- 高清适配：手动按 dpr 设置 `canvas.width = cssWidth * dpr` 再 `ctx.scale(dpr, dpr)`。

```javascript
Page({
  onReady() {
    wx.createSelectorQuery()
      .select('#myCanvas')
      .fields({ node: true, size: true })
      .exec((res) => {
        const { node: canvas, width, height } = res[0]
        const dpr = wx.getWindowInfo().pixelRatio
        canvas.width = width * dpr          // 物理像素
        canvas.height = height * dpr
        const ctx = canvas.getContext('2d') // 与 Web Canvas API 一致
        ctx.scale(dpr, dpr)
        ctx.fillStyle = '#07c160'
        ctx.fillRect(0, 0, 100, 100)
      })
  }
})
```
