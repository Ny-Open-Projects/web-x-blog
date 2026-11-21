---
title: [H5-203] Canvas 图片跨域污染是什么，toDataURL 报错怎么解
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Canvas]
type: 面试题
---

## H5-203：Canvas 图片跨域污染是什么，toDataURL 报错怎么解

**答**：
- 画了跨域图片的 canvas 会被标记为 tainted（污染），再调 toDataURL/getImageData 直接抛 SecurityError——防止读取他人站点像素数据
- 解法三件套：图片服务返回 CORS 头（Access-Control-Allow-Origin）、`img.crossOrigin = 'anonymous'`、缓存要重新请求（带 crossOrigin 的请求与普通请求缓存 key 不同，可能触发二次下载）
- 资源走 CDN 时确认 CDN 也透传 CORS 头，只配源站没用
- 降级方案：拿不到 CORS 时让服务端代理图片（同源拉取），或走服务端合成
- 调试技巧：报错时先 console.log(img.crossOrigin) 与 Network 面板响应头，三处对齐才能解封

```javascript
const img = new Image();
img.crossOrigin = 'anonymous';        // 必须在 src 赋值前设置
img.src = 'https://cdn.example.com/a.png';
img.onload = () => {
  ctx.drawImage(img, 0, 0);
  try {
    console.log(canvas.toDataURL());  // 需要 CORS 响应头配合
  } catch (e) {
    console.error('画布被污染，检查 Access-Control-Allow-Origin');
  }
};
```
