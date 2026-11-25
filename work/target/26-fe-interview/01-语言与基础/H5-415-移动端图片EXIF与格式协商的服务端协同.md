---
title: [H5-415] 移动端图片 EXIF 与格式协商：前后端协同
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 多媒体]
type: 面试题
---

## H5-415：移动端图片 EXIF 与格式协商：前后端协同

**答**：
- EXIF 方向问题链：拍照上传带 orientation 标记，显示端如果不统一处理会旋转错乱——约定「上传端归一化」：上传前 createImageBitmap from-image 重编码去掉 EXIF，服务端存「已归一化」图
- 格式协商服务端做：CDN 按 Accept 头自动出 AVIF/WebP（content negotiation），前端只写统一 URL，避免前端探测 WebP 支持的复杂度
- 质量与尺寸参数化：URL 约定（?w=750&q=80&fmt=webp）+ 防滥用签名（动态改参绕过计费）——CDN 层校验签名
- HEIC 特殊性：iPhone 原图 HEIC 浏览器解码有限，上传端优先转 JPEG/WebP 再传（H5-387 方案），服务端兜底转码
- 元信息沉淀：图片处理链路记录（原始尺寸/压缩参数/最终体积）入元数据服务，供体验优化与问题回溯

```javascript
// 上传端归一化: 去 EXIF + 统一格式
async function normalize(file) {
  const bmp = await createImageBitmap(file, { imageOrientation: 'from-image' });
  const off = new OffscreenCanvas(bmp.width, bmp.height);
  off.getContext('2d').drawImage(bmp, 0, 0);
  bmp.close();
  return off.convertToBlob({ type: 'image/webp', quality: 0.85 }); // 无EXIF污染的webp
}
// 展示端: 统一URL交给CDN协商
// <img src="https://img.example.com/p/abc.jpg?w=750&q=80"> → CDN按Accept出AVIF/WebP/JPEG
```
