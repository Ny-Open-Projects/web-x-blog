---
title: [VIZ-204] WebGPU 纹理管线：大图纹理上传与 mipmap 自动生成
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-204：WebGPU 纹理管线：大图纹理上传与 mipmap 自动生成

**答**：
- 可视化大图（地图瓦片拼接/热力图底图）：纹理上传策略——copyExternalImageToTexture（支持 ImageBitmap）+ usage 标记。
- mipmap：commandEncoder 生成（WebGPU 无内建 genMipmap，需手写降采样 pass 链），避免远处纹理闪烁（摩尔纹）。
- 内存控制：纹理格式选 rgba8unorm（非 srgb 数据）与 bgra8unorm（展示），大图分块上传。

```javascript
async function uploadTexture(device, imgBitmap) {
  const texture = device.createTexture({
    size: [imgBitmap.width, imgBitmap.height],
    format: 'rgba8unorm',
    usage: GPUTextureUsage.TEXTURE_BINDING | GPUTextureUsage.COPY_DST
         | GPUTextureUsage.RENDER_ATTACHMENT,             // RENDER_ATTACHMENT 供 mip 生成
    mipLevelCount: Math.floor(Math.log2(Math.max(w, h))) + 1,   // mip 链
  });
  device.queue.copyExternalImageToTexture(
    { source: imgBitmap }, { texture }, [imgBitmap.width, imgBitmap.height]);
  // mip 生成：逐级 downscale pass（blit shader 采样上层），WebGPU 无内建需手写
  return texture;
}
```
