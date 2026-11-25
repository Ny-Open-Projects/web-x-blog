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

**边界与易错**：

- `img.crossOrigin` 必须在给 `src` 赋值之前设置，赋值之后再设不会补发 CORS 请求，图片已按普通请求进缓存，画上去照样污染。
- 服务端只回 `Access-Control-Allow-Origin` 却没回 `Vary: Origin`，CDN 可能把无 CORS 头的响应缓存后发给带 crossOrigin 的请求，需要加 cache-busting 参数重取。
- 换成 `toBlob` 并不能绕过污染，因为污染判定发生在 `drawImage` 那一刻，导出方法只是把错误暴露出来。

**追问**：

1. `crossOrigin='anonymous'` 和 `'use-credentials'` 有什么区别？ → 前者不带 cookie，服务端可用 `*`；后者带凭证，响应必须是具体源且带 `Access-Control-Allow-Credentials: true`。
2. 之前没设 crossOrigin 加载过同一张图，现在补设还有救吗？ → 已经画进 canvas 的像素无法解污染，必须新建 Image 按正确顺序加载，并用新 URL 或参数破掉旧缓存。
3. 只有 Safari 报错、Chrome 正常，可能是什么原因？ → Safari 对 SVG 和缓存复用更严格，或某个 CDN 边缘节点漏配 CORS，要按 UA 分别抓响应头对比。
