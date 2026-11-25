---
title: [PER-280] 图片相关的内存问题：位图内存怎么算？objectURL 用完为什么要 revoke？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-280：图片相关的内存问题：位图内存怎么算？objectURL 用完为什么要 revoke？

**答**：
- 位图内存公式：宽 × 高 × 4 字节（RGBA）。一张 4000×3000 手机照片解码后约 48MB——与文件体积（几百 KB JPEG）无关，解码位图才是内存大头。缩略图按显示尺寸解码（`img decoding`、`createImageBitmap` 指定 resize）可省 90%+。
- objectURL（blob URL）生命周期：createObjectURL 让 Blob 进入"与文档关联"状态，revokeObjectURL 之前 Blob 数据与解码位图都留在内存；图片 onload 后 revoke 是标准动作，列表页几百张图不 revoke 就是持续堆积。
- 大图列表策略：IntersectionObserver 控制可视区渲染（虚拟列表）、离屏图片主动 `img.src = ''` 释放位图（或用 content-visibility 自动跳过渲染）、解码用 createImageBitmap 控制尺寸。
- 验证：Memory 面板看 Images 类别（或 Chrome 任务管理器的 Memory 列），滚动长列表内存应波动回落而非单调上涨。

```javascript
// 大图列表的标准释放流程
const url = URL.createObjectURL(blob);
img.src = url;
img.decode().finally(() => URL.revokeObjectURL(url));   // 解码完成后立刻释放 blob 引用
// 离屏释放：滚动出可视区时
io.observe(img);
ioCallback: if (!entry.isIntersecting && entry.boundingClientRect.top < 0) {
  img.dataset.src = img.src; img.src = '';              // 释放位图（保留可恢复的 src）
}
// 缩略图解码：
const bmp = await createImageBitmap(blob, { resizeWidth: 200, resizeQuality: 'medium' });
// 4000x3000 => 200x150 位图：48MB → 120KB
```
