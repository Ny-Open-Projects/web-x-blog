---
title: [WEB-628] WASM 与 Worker/OffscreenCanvas 的组合架构
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-628：WASM 与 Worker/OffscreenCanvas 的组合架构

**答**：
- 推荐架构：WASM 实例 + OffscreenCanvas 都放 Worker，主线程只做交互与轻渲染——计算与上屏都在 Worker 内完成，主线程零阻塞
- 数据通路：主线程 ImageBitmap → postMessage（transferable 零拷贝）→ Worker 内 wasm 处理 → OffscreenCanvas 渲染或结果 Uint8Array 转移回主线程
- 模块共享：每个 Worker 独立实例化 wasm（无法跨线程共享实例），多 Worker 场景内存翻倍要评估；或者单 Worker + 任务队列串行
- 主线程参与最少化的例外：需要 DOM 交互的实时预览，用 OffscreenCanvas 双向同步（Worker 画布 commit 到主线程显示）
- 注意事项：OffscreenCanvas 的 2D/WebGL 上下文在 Worker 内创建；ImageBitmap 用完 close() 释放；多 Worker 共享 wasm 线性内存必须走 SAB

```javascript
// 主线程: 转移 ImageBitmap 给 Worker, 不拷贝
const bmp = await createImageBitmap(file);
worker.postMessage({ bmp, w: bmp.width, h: bmp.height }, [bmp]);
// worker.js:
self.onmessage = ({ data: { bmp, w, h } }) => {
  const off = new OffscreenCanvas(w, h);
  const ctx = off.getContext('2d');
  ctx.drawImage(bmp, 0, 0);
  bmp.close();                                  // 立即释放
  const rgba = ctx.getImageData(0, 0, w, h).data;
  const out = wasmProcess(rgba);                // wasm 处理
  off.getContext('2d').putImageData(new ImageData(out, w, h), 0, 0);
  self.postMessage({ ready: true });            // 主线程显示 off.transferToImageBitmap()
};
```
