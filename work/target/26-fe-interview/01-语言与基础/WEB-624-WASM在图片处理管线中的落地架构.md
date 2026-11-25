---
title: [WEB-624] WASM 在图片处理管线中的落地架构
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-624：WASM 在图片处理管线中的落地架构

**答**：
- 标准管线：用户选图 → Worker 里解码（wasm 解码器/builtin decode）→ OffscreenCanvas 或 wasm 处理（裁剪/滤镜/压缩）→ 编码（wasm mozjpeg/webp）→ 上传
- Worker + OffscreenCanvas 是关键架构：图片处理全程不占主线程，主线程 UI 不卡；WASM 实例在 Worker 内创建（冷启动成本一次摊销）
- 内存管理：解码后的 RGBA buffer 直接复用（wasm alloc + JS TypedArray 共享），处理链多步时传指针不拷贝；任务结束 free，防止线性内存只涨不缩
- 降级链：WASM 编码器失败/不支持 → Canvas.toBlob 原生编码兜底（质量略差但保证可用）
- 质量验证：同一图片 wasm mozjpeg vs canvas 原生 jpeg 输出对比体积/清晰度，用 SSIM 或人工抽样，作为技术汇报证据

```javascript
// worker.js: 图片压缩管线
let mod;
self.onmessage = async ({ data: { bitmap, quality }, }) => {
  mod ||= await loadWasm('/wasm/mozjpeg.wasm');          // 模块级单例
  const rgba = new Uint8ClampedArray(bitmap.width * bitmap.height * 4);
  bitmap.data ? rgba.set(bitmap.data) : null;
  const ptr = mod.alloc(rgba.length);
  mod.HEAPU8.set(rgba, ptr);                              // 共享线性内存
  const jpegPtr = mod.encode_jpeg(ptr, bitmap.width, bitmap.height, quality);
  const size = mod.encoded_size();
  const jpeg = new Uint8Array(mod.memory.buffer, jpegPtr, size).slice(); // 拷出结果
  mod.free(ptr);
  self.postMessage({ jpeg }, [jpeg.buffer]);              // 零拷贝回主线程
};
```
