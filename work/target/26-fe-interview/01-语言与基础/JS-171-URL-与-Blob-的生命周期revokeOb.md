---
title: [JS-171] URL 与 Blob 的生命周期？revokeObjectURL 不调用会怎样？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-171：URL 与 Blob 的生命周期？revokeObjectURL 不调用会怎样？

**答**：
- `URL.createObjectURL(blob)` 返回的 URL 生命周期挂靠在 document 上：不 revoke 就一直持有 Blob，直到页面卸载。
- SPA 中反复预览大文件（图片/视频）不 revoke = 每次都泄漏一份完整 Blob 内存。
- 规则：换图前 revoke 旧 URL；组件卸载 revoke；列表复用 img 的场景尤其要管理。
- dataURL（base64）无需 revoke 但体积 +33% 且解析慢，大文件一律用 objectURL。
- 手动 revoke 后再访问该 URL 报错，且已加载完成的 img 不受影响——加载完成即可安全释放。

```javascript
let currentUrl = null;

function previewFile(file) {
  const img = document.getElementById('preview');
  if (currentUrl) URL.revokeObjectURL(currentUrl);  // 换图前先释放旧 Blob
  currentUrl = URL.createObjectURL(file);           // 此刻 Blob 被页面引用
  img.src = currentUrl;
  img.onload = () => {
    // 可选优化：一次性预览且无需重载时，加载完成即可释放
    // URL.revokeObjectURL(currentUrl); currentUrl = null;
  };
}

function destroyPreview() {                          // 组件卸载/页面隐藏时兜底
  if (currentUrl) {
    URL.revokeObjectURL(currentUrl);
    currentUrl = null;                               // 置空防止误用已释放的 URL
  }
}
window.addEventListener('pagehide', destroyPreview);

// 列表场景：生成缩略图 URL 必须随元素销毁一起回收
const cache = new Map();                             // fileId -> objectURL
function getThumb(fileId, blob) {
  if (!cache.has(fileId)) {
    const url = URL.createObjectURL(blob);
    cache.set(fileId, url);
    return url;
  }
  return cache.get(fileId);
}
function disposeThumb(fileId) {
  const url = cache.get(fileId);
  if (url) { URL.revokeObjectURL(url); cache.delete(fileId); }
}
// 对比：dataURL 无需管理但内存翻倍；objectURL 引用传递 + 手动回收，大文件首选
```

## 二十五、工程与规范
