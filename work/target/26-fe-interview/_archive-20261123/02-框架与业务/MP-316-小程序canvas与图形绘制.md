---
title: [MP-316] 小程序 Canvas：2D 新接口与海报生成
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 多媒体]
type: 面试题
---

## MP-316：小程序 Canvas：2D 新接口与海报生成

**答**：
- 新旧接口：旧版 wx.createCanvasContext（已废弃方向）vs 新版 Canvas 2D 接口（type="2d" + SelectorQuery 拿 node——原生 canvas 上下文，性能与 API 对齐 Web）
- 海报生成链路：canvas 绘制（头像/二维码/文字排版）→ wx.canvasToTempFilePath 导出图片 → wx.saveImageToPhotosAlbum——「相册权限」处理（scope.writePhotosAlbum 拒绝后 openSetting 引导）
- DPR 处理：canvas 节点宽高 × dpr（wx.getSystemInfoSync().pixelRatio）+ ctx.scale——否则导出图模糊
- 字体与图文混排：ctx.measureText 换行计算（长文案手动断行）——小程序无富文本自动排版
- 深水点：二维码绘制进 canvas——后端生成图片（推荐，字体一致）vs 前端 weapp-qrcode 库；「draw 完成时机」用 node.requestAnimationFrame 或 canvas 的 onReady

```javascript
async function drawPoster() {
  const query = wx.createSelectorQuery();
  const { node, width, height } = await new Promise((r) =>
    query.select('#poster').fields({ node: true, size: true }).exec(r));
  const dpr = wx.getSystemInfoSync().pixelRatio;
  node.width = width * dpr; node.height = height * dpr;
  const ctx = node.getContext('2d');
  ctx.scale(dpr, dpr);
  drawLayout(ctx, width);                            // 绘制(含手动换行)
  const { tempFilePath } = await wx.canvasToTempFilePath({ canvas: node });
  await saveToAlbum(tempFilePath);                   // 权限引导闭环
}
```
